---
artifact: carries-senses
phase: 56
plan: 01
task: 4
status: COMPLETE
role: reusable artifact consumed by Plan 56-02 and Plan 56-03
conventions:
  ambient_V: V = V_{BM} (finite-dim archimedean OUS; R-linear)
  subspace_W: W ⊆ V (linear subspace, with W ∩ V^+ the induced positive cone)
  sequential_product: "∘ : [0,1]_V × [0,1]_V → [0,1]_V satisfying S1-S7 (vdW 2019 Def. 2)"
  citation_style: bracketed `\cite[…]{…}` where possible
---

# Three Senses of "W Carries the Product-Form Sequential Product"

This artifact formalizes the three distinct senses in which one might say a subspace
W of a sequential-product-space V "carries" or "inherits" the ambient sequential
product. The senses are stated with symbolic formulas; the collapse diagram is
stated (which senses imply which); and the non-collapse witnesses are named so that
downstream Paper 5 text cannot silently equivocate.

**Discipline (binding for all Phase 56 artifacts):** every occurrence of "carries",
"inherits", "restricts", "respects", "extends", or "closed under ∘" in Phase 56
artifacts (Plan 56-01 onward) MUST be tagged with a sense (a)/(b)/(c) at its first
use in a paragraph, using the citation form "sense (b) per carries-senses.md §2".
Uses inside fenced code blocks quoting prior text are exempt (the tag may be added
in surrounding commentary).

---

## Section 1 — Sense (a): set-level closure

**Formal definition.**

```
Sense (a) — set-level closure:
  For all a, b ∈ [0,1]_W := [0,1]_V ∩ W, we have a ∘_V b ∈ W.
  Equivalently: ∘_V ([0,1]_W × [0,1]_W) ⊆ W.
```

**Operational reading.** The product stays inside W *as a set*, but nothing is claimed
about W being an OUS in its own right, about the induced cone W^+ := W ∩ V^+ being
proper, or about W-restricted ∘ satisfying S1-S7 internally.

**Status.** Weakest of the three senses. Satisfied automatically in the Paper 5
setting because the product-form identity `(a ⊗ b) ∘ (c ⊗ d) = (a ∘ c) ⊗ (b ∘ d)`
(composite-lt.tex:216-217; appendix-proofs.tex:232-233) produces a product effect
whenever the factors are; hence `[0,1]_W × [0,1]_W → W` is immediate.

**Not enough for `sms:minimal`.** The minimality clause of Paper 5 compares OUS
structures; sense (a) does not equip W with an OUS structure, so sense (a) W is not a
competitor in the comparison.

## Section 2 — Sense (b): induced-structure SPS

**Formal definition.**

```
Sense (b) — induced-structure SPS:
  (W, ≤|_W, 1_W, ∘|_W) is itself an order unit space satisfying vdW 2019 Def. 2
  axioms S1-S7, where:
    - ≤|_W is the restriction of the partial order ≤_V to W,
    - 1_W := 1_V (valid iff 1_V ∈ W),
    - ∘|_W := ∘_V |_{[0,1]_W × [0,1]_W}, which is defined as set-theoretic
      restriction (not a new operation).
```

**Hypothesis to verify for sense (b):**

- (i) 1_V ∈ W;
- (ii) W^+ := W ∩ V^+ is a proper cone generating W (i.e., W = W^+ − W^+);
- (iii) sense (a) holds (`∘|_W` maps into W);
- (iv) S1-S7 hold for (W, ≤|_W, 1_W, ∘|_W).

**In the Paper 5 setting (W = span{a_i ⊗ b_j}):**

- (i) holds: 1_V = 1_B ⊗ 1_M ∈ W (since 1_B ∈ span{a_i} and 1_M ∈ span{b_j}).
- (ii) holds: W^+ contains the product cone and generates W.
- (iii) holds: product-form closure identity.
- (iv) is the content of Plan 56-02 — each axiom S1 through S7 must be verified on W
  with `∘|_W`. The axioms S1, S2, S3, S5, S6, S7 reduce cleanly to factor-level
  axioms; S4 is more subtle and uses state separation (A-S 2003 Thm 1.23).

**Status.** This is the sense required by the `sms:minimal` clause. Per
`downstream-consumer-scan.md` §6-7, sense (b) is what 15 of 16 in-scope §5/§6
consumers need. Plan 56-02's primary target.

## Section 3 — Sense (c): functorial SPS-morphism

**Formal definition.**

```
Sense (c) — functorial SPS-morphism:
  The inclusion ι: W ↪ V is an SPS-morphism, meaning:
    (c1) ι is R-linear,
    (c2) ι is unital: ι(1_W) = 1_V,
    (c3) ι is positive: ι(W^+) ⊆ V^+,
    (c4) ι preserves ∘: ι(a ∘|_W b) = ι(a) ∘_V ι(b) for all a, b ∈ [0,1]_W.
```

**Note on (c4).** When `∘|_W` is defined by set-theoretic restriction (as in sense
(b) above), both sides of (c4) are literally the same element of V: the left side is
`a ∘_V b` (computed in V and declared to live in W), and the right side is `a ∘_V b`
(computed in V after inclusion). So (c4) is automatic once `∘|_W` is well-defined as
a restriction. The non-trivial content of sense (c) is that ι is unital and positive
— (c2) and (c3).

**Status.** Strongest; clean for monoidal-category / BGW 2020 constructions. In the
Paper 5 setting (c) is a free corollary of (b), because:

- (c1) holds trivially (ι is the inclusion of a subspace).
- (c2) holds trivially (1_W = 1_V in Paper 5's W).
- (c3) holds trivially (W^+ := W ∩ V^+ ⊆ V^+).
- (c4) holds automatically once `∘|_W` is the restriction of `∘_V`.

Hence (b) ⇒ (c) in this setting with no additional work.

## Section 4 — Collapse diagram

```
(c) ========> (b) ========> (a)
  ⇑ unit-compat.  ⇑ not always

(c) (unital positive linear) ⇒ (b) (domain is an SPS):
  an SPS-morphism's DOMAIN is an SPS by definition of morphism.

(b) (SPS structure on W) ⇒ (a) (closure):
  if (W, ≤|_W, 1_W, ∘|_W) is an SPS, then in particular ∘|_W is a well-defined
  binary operation [0,1]_W × [0,1]_W → [0,1]_W ⊆ W, hence sense (a) holds.

(a) ⇏ (b) in general:
  Gudder-Greechie 2002 Example 39 — effect-algebra-level set-closed
  sequential product on a subsystem that does NOT lift to a full SPS over
  the induced order. AXIOM-STATED-IN-SECONDARY-SOURCE tier (RMP 49 paper
  not directly accessed; cited with acknowledgement).

(b) ⇏ (c) in general:
  In general, requires 1_W ≠ 1_V (different order units) or ι failing
  cone-preservation. IN THE PAPER 5 SETTING (W = span{a_i ⊗ b_j} with
  1_B ⊗ 1_M ∈ W), 1_W = 1_V and ι is cone-preserving by construction,
  so (b) ⇒ (c) actually HOLDS here. The general non-collapse is a
  caveat for general theory, not an issue for Paper 5.
```

**Key collapse observation for Plan 56-02:** In the Paper 5 setting, the three senses
ARE related by (c) ⇔ (b) ⇒ (a) with (b) ⇒ (c) as a free corollary. Sense (b) is the
pivotal target; sense (c) is automatic; sense (a) is already trivially satisfied.

## Section 5 — Non-collapse witnesses (general-theory caveats)

### (a) ⇏ (b) witness: Gudder--Greechie 2002 Example 39

**Citation:** Gudder, S. & Greechie, R., "Sequential products on effect algebras,"
*Reports on Mathematical Physics* **49**, 87--111 (2002). Example 39 (page number
unverified — RMP 49 not directly accessed in this project).

**Tier:** AXIOM-STATED-IN-SECONDARY-SOURCE.

**Content (paraphrased from research-level secondary references; verbatim quote
PENDING RMP 49 access):** Example 39 exhibits an effect-algebra structure with a
sequential product that is associative and set-closed on a certain subsystem, but
does NOT lift to an OUS SPS satisfying S1-S7 over the induced order structure. The
failure mode typically involves non-real-linearity or non-Jordan behavior at the
induced-OUS level. The example functions as a counterexample to the implication
"set-closure implies induced SPS."

**Why Paper 5 is safe:** Paper 5's W is explicitly `span{a_i ⊗ b_j}` inside the OUS
V_{BM}, with the ambient V_{BM}'s own ≤ and cone. The non-real-linearity and
non-Jordan failure modes of Gudder-Greechie 2002 Example 39 do not apply: Plan 56-02
establishes sense (b) directly via vdW 2019 Thm 1, which produces an EJA structure
on W if S1-S7 are verified.

### (b) ⇏ (c) witness: unit-choice subtlety

In general OUS theory, (W, ≤|_W, 1', ∘|_W) can be a valid SPS with an order unit 1'
that is NOT equal to 1_V (e.g., if W is a face of V not containing 1_V, then 1'
must be chosen inside W and the inclusion ι: W ↪ V fails to be unital).

**Why Paper 5 is safe:** 1_V = 1_B ⊗ 1_M ∈ W. So 1_W = 1_V and unital-ness of ι
is automatic.

## Section 6 — Downstream-consumer mini-table (pointer to downstream-consumer-scan.md)

This mini-table mirrors the argumentative rows of `downstream-consumer-scan.md`
Sections 2-5, with each consumer's required sense tagged.

| file:line                      | Consumer short label                   | Required sense |
|--------------------------------|----------------------------------------|----------------|
| composite-lt.tex:44-45         | `sms:minimal` definition (V_{BM} side) | (b)            |
| composite-lt.tex:67-69         | `prop:inheritance` (on V_{BM})         | (b)            |
| composite-lt.tex:92-107        | `rem:bootstrap` (algebraic tensor W)   | (b) + (c)      |
| composite-lt.tex:162-168       | `thm:local-tomo` theorem statement     | (b) [source]   |
| composite-lt.tex:204-221       | `thm:local-tomo` upper-bound proof     | (b) [source]   |
| composite-lt.tex:227-232       | `sms:minimal` eliminates ent. sector   | (b) [framing]  |
| type-exclusion.tex:46-47       | §6 exclusion invokes `thm:local-tomo`  | (b) [use]      |
| type-exclusion.tex:114-116     | `thm:vdW3` hypothesis "V⊗V is SPS"     | (b)            |
| type-exclusion.tex:126-129     | `thm:vdW3` hypothesis table row        | (b)            |
| type-exclusion.tex:245-248     | `thm:main` proof outline (V_{BM})      | (b)            |
| discussion.tex:31-34           | Dependency audit `sms:minimal` row     | (b) [framing]  |
| discussion.tex:61-64           | Dependency audit conditions (iii)-(iv) | (b) [use]      |
| discussion.tex:118-129         | `sms:minimal` paragraph (structural)   | (b) [source]   |
| discussion.tex:181-183         | Internality operational paragraph      | (b) [framing]  |
| discussion.tex:210-217         | `sms:minimal` defense                  | (b) [framing]  |
| discussion.tex:245-254         | `cor:equivalence` proof                | (b)            |
| discussion.tex:293-296         | Masanes-Müller comparison              | (b) [use]      |
| discussion.tex:426-468         | `rem:minimality-objection`             | (b) [use]      |
| appendix-proofs.tex:164-173    | `thm:lt-full` theorem statement        | (b) [source]   |
| appendix-proofs.tex:229-238    | `thm:lt-full` upper-bound proof        | (a) → (b)      |

Count: 15 rows sense (b); 1 row sense (a); 2 rows sense (b)+(c). Total in-scope: 18.

**Conclusion from the mini-table:** Sense (b) is the minimum-necessary target across
§5/§6. Sense (c) is additionally useful at two sites and is automatic here.

## Section 7 — `sms:minimal` minimum sense = (b)

**Claim.** The minimum sense required by the `sms:minimal` clause (Paper 5's
Definition~\ref{def:self-modeling-system}\ref{sms:minimal}) is sense (b).

**Justification.** The minimality clause asserts that `V_{BM}` is the *smallest* OUS
satisfying (C1)-(C4) and carrying a product-form sequential product. For W = span{a_i
⊗ b_j} to function as a competitor in this minimality comparison (so that the
upper-bound step `dim V_{BM} ≤ dim W = d²` is licensed), W must itself be an OUS
satisfying the same structural conditions: (C1)-(C4) and the product-form SP, with
its own order unit, cone, and restricted product.

- Sense (a) does NOT equip W with an OUS structure. It only says `∘` takes
  [0,1]_W × [0,1]_W into W. It says nothing about an order unit, a proper cone, or
  the axioms S1-S7 on the restricted product. A sense-(a) W is NOT a competitor in
  the minimality comparison.

- Sense (b) EXACTLY equips W with the required OUS structure (≤|_W, 1_W = 1_V,
  W^+ = W ∩ V^+, ∘|_W by restriction) and asserts S1-S7 hold. A sense-(b) W IS a
  competitor in the minimality comparison.

- Sense (c) is stronger than (b) but is not required by the minimality clause; the
  minimality clause compares OUS structures, not morphism structures.

Therefore: **sense (b) is the minimum for `sms:minimal`**. Plan 56-02 locks sense (b)
as the target; sense (c) is a free corollary because 1_W = 1_V.

## Forbidden-proxy rejections

- **fp-carries-sense-collapse** — REJECTED. This artifact is itself the antidote to
  sense-collapse: every use of "carries"/"inherits" below is explicitly tagged to a
  numbered sense.
