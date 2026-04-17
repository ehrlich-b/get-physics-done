---
artifact: ci-sps-morphism
phase: 56
plan: 02
task: 3
status: COMPLETE
sense_established: (c) [functorial SPS-morphism] — cheap upgrade from sense (b)
conventions:
  ambient: V = V_{BM} (finite-dim archimedean OUS; 1_V = 1_B (x) 1_M)
  subspace: W := span_R{a_i (x) b_j} <= V_{BM}
  restriction_product: "∘|_W := ∘_{V_{BM}} restricted (set-theoretic)"
  inclusion_map: "ι: W ↪ V_{BM}, ι(w) := w"
  sps_morphism_definition: BGW 2020 §2 (completely Jordan-preserving map; adapted to SPS via vdW 2019 Def. 2)
  sense_c_conditions: (c1) R-linearity, (c2) unitality ι(1_W) = 1_V, (c3) positivity ι(W^+) ⊆ V^+, (c4) ∘-preservation ι(a ∘|_W b) = ι(a) ∘_V ι(b)
  frozen_file: main-jmp-submitted.tex (zero-diff preserved)
---

# ι: W ↪ V_{BM} is a Sequential-Product-Space Morphism — Sense (c) Upgrade

Phase 56-02 Plan 56-02 Task 3 — sense-(c) deliverable per `carries-senses.md §3`.
This artifact proves that the inclusion `ι : W ↪ V_{BM}` is an SPS-morphism in
the Barnum-Graydon-Wilce 2020 sense (completely Jordan-preserving map),
upgrading the sense-(b) result of `w-sps-proof.md` to the stronger sense (c)
— at no additional proof cost, because `1_W = 1_{V_{BM}}` and `∘|_W` is a
set-theoretic restriction.

---

## Section 1 — Statement

**Theorem (ι is an SPS-morphism).** With W, V_{BM}, ∘|_W, and 1_W as defined
in `w-sps-proof.md` Section 1, the inclusion map

```
ι : W ↪ V_{BM},  ι(w) := w  (identity on elements)
```

is a **sequential-product-space morphism** in the sense of Barnum, Graydon, &
Wilce, "Composites and Categories of Euclidean Jordan Algebras,"
*Quantum* **4**, 359 (2020), §2 (arXiv:1606.09331).

Concretely, ι satisfies the four SPS-morphism conditions
(per `carries-senses.md §3`):

- **(c1)** ι is ℝ-linear;
- **(c2)** ι is unital: `ι(1_W) = 1_{V_{BM}}`;
- **(c3)** ι is positive: `ι(W^+) ⊆ V_{BM}^+`;
- **(c4)** ι preserves the sequential product: `ι(a ∘|_W b) = ι(a) ∘_{V_{BM}} ι(b)` for all `a, b ∈ [0,1]_W`.

Establishing (c1)-(c4) upgrades the sense-(b) result of `w-sps-proof.md`
(sense (b) per `carries-senses.md §2`) to **sense (c) per
`carries-senses.md §3`** — the strongest of the three "carries" senses. This
is the "cheap upgrade" predicted by `56-RESEARCH.md` §"Three Senses of
Carries" (inherited from Phase 56-01 `carries-senses.md` §3).

---

## Section 2 — (c1) Linearity

**Proof.** ι is the set-theoretic inclusion of W as a linear subspace of
V_{BM}. For any `u, v ∈ W` and `λ, μ ∈ ℝ`:

```
ι(λ u + μ v) = λ u + μ v  (as an element of V_{BM})
             = λ ι(u) + μ ι(v).
```

The first equality holds by definition of the inclusion (it is literally the
identity map on elements, viewed as a map W → V_{BM}). The second equality
holds because ι(u) = u and ι(v) = v as elements of V_{BM}. Trivial. ✓

---

## Section 3 — (c2) Unitality: ι(1_W) = 1_{V_{BM}}

**Proof.** Per `w-sps-proof.md` Section 1 and `carries-senses.md §2`, the
order unit of W is defined as:

```
1_W := 1_{V_{BM}} = 1_B ⊗ 1_M.
```

The assertion `1_B ⊗ 1_M ∈ W` holds because:

1. `1_B ∈ span(a_i)` — since `{a_i}` is a basis of the OUS V_B, the order
   unit `1_B` lies in the R-linear span of the basis. (Paper 5 convention;
   every OUS has a distinguished order unit in its linear span by definition
   of basis.)
2. `1_M ∈ span(b_j)` — same reason.
3. Therefore `1_B ⊗ 1_M ∈ span{a_i ⊗ b_j} = W` by bilinearity of the tensor
   product: writing `1_B = Σ_i α_i a_i` and `1_M = Σ_j β_j b_j`, we have
   `1_B ⊗ 1_M = Σ_{i,j} α_i β_j (a_i ⊗ b_j) ∈ W`.

By Paper 5's composite OUS convention (composite-lt.tex §composite-def
region, L18-40 of the living file), the order unit of V_{BM} is
`1_{V_{BM}} := 1_B ⊗ 1_M`. Hence:

```
ι(1_W) = ι(1_B ⊗ 1_M) = 1_B ⊗ 1_M = 1_{V_{BM}}.  ✓
```

The key identity `1_W = 1_{V_{BM}}` (both equal to `1_B ⊗ 1_M`) is the
non-trivial content of (c2) — it is what distinguishes the Paper 5 setting
from general OUS-subspace situations where `1_W` might be a proper face unit
that is not the ambient order unit (see `carries-senses.md §5` for the
unit-choice subtlety in general).

---

## Section 4 — (c3) Positivity: ι(W^+) ⊆ V_{BM}^+

**Proof.** By the definition of the induced positive cone on W (per
`w-sps-proof.md` Section 1):

```
W^+ := W ∩ V_{BM}^+.
```

For any `w ∈ W^+`, we have `w ∈ W` and `w ∈ V_{BM}^+` by definition of the
set intersection. Therefore:

```
ι(W^+) = W^+ = W ∩ V_{BM}^+ ⊆ V_{BM}^+.  ✓
```

This is literal set inclusion: an element positive in the induced cone is,
by definition, positive in the ambient cone. No further axiom is invoked.

---

## Section 5 — (c4) ∘-preservation: ι(a ∘|_W b) = ι(a) ∘_{V_{BM}} ι(b)

**Proof.** By the definition of the restricted sequential product on W
(per `w-sps-proof.md` Section 1):

```
∘|_W := ∘_{V_{BM}} |_{[0,1]_W × [0,1]_W}
```

— the set-theoretic restriction of `∘_{V_{BM}}` to pairs of elements in
`[0,1]_W`. The sense-(b) theorem (`w-sps-proof.md` Section 4) asserts that
the result of this restricted operation lands back in W (sense (a) closure),
so that `∘|_W : [0,1]_W × [0,1]_W → [0,1]_W` is a well-defined binary
operation on W.

For any `a, b ∈ [0,1]_W`:

```
ι(a ∘|_W b) = a ∘|_W b                               (by definition of ι)
            = a ∘_{V_{BM}} b                         (by set-theoretic restriction)
            = ι(a) ∘_{V_{BM}} ι(b).                  (by definition of ι applied to a, b)
```

Both sides of (c4) evaluate to **literally the same element of V_{BM}**:
the element `a ∘_{V_{BM}} b`, computed in V_{BM} and (thanks to sense-(a)
closure) landing in W, so its image under ι is itself. **Automatic** — no
axiom beyond the definitions is invoked. ✓

**Caveat (tracked for Plan 56-03).** The automatic identification in (c4)
depends on `∘|_W` being defined by set-theoretic **restriction** of
`∘_{V_{BM}}`, not by some alternative W-internal formula. If Plan 56-03
revision text introduced a new operation `∘|_W` via (e.g.) the
product-form formula applied internally to W's own basis decomposition
without reference to V_{BM}'s ambient `∘`, then (c4) would need an
additional argument showing the internal and restricted operations
coincide. Per Plan 56-01 `carries-senses.md §3` note and Plan 56-02
contract uncertainty_markers, Plan 56-03 **must not** introduce such
an alternative operation; the revision text uses "restriction" language
only. This caveat is non-binding for Plan 56-02 itself.

---

## Section 6 — Conclusion: sense (c) holds freely

All four SPS-morphism conditions (c1)-(c4) are verified:

- (c1) linearity — trivial (Section 2);
- (c2) unitality — `1_W = 1_B ⊗ 1_M = 1_{V_{BM}}` (Section 3);
- (c3) positivity — `W^+ := W ∩ V_{BM}^+ ⊆ V_{BM}^+` (Section 4);
- (c4) ∘-preservation — automatic from the restriction definition of ∘|_W (Section 5).

**Sense (c) per `carries-senses.md §3` is ESTABLISHED.** The inclusion
`ι : W ↪ V_{BM}` is an SPS-morphism in the BGW 2020 sense.

**Cheap-upgrade statement.** In the Paper 5 setting, **sense (c) holds
freely as a corollary of sense (b)**. No additional proof beyond checking
the four conditions (c1)-(c4) — each of which reduces to a definition or
a trivial set-inclusion — was needed. This matches the prediction of
`carries-senses.md §3` Section 3 (Paper 5 setting bullet list) and
`56-RESEARCH.md §"Three Senses of Carries"`.

**Downstream consequence.** Plan 56-03 revision text (composite-lt.tex
L203-221 + appendix-proofs.tex L228-238) may quote **sense (c)** directly
— the strongest of the three senses — without requiring any additional
proof machinery in the Paper 5 LaTeX. The revision-text language
inventory in `carries-three-sense-table.md §4` will include phrases
such as:

- "ι : W ↪ V_{BM} is an SPS-morphism (sense (c))";
- "W carries the product-form sequential product in sense (b) with the free upgrade to sense (c)";
- "the inclusion is completely Jordan-preserving in the sense of BGW 2020".

Since sense (c) ⇒ sense (b) ⇒ sense (a) by the collapse diagram of
`carries-senses.md §4`, **every §5/§6 downstream consumer is served**:
the 15 sense-(b) consumers in `downstream-consumer-scan.md §2-5` are
served by (b) which follows from (c); the 1 sense-(a) consumer
(appendix-proofs.tex:229-238) is served by (a) which follows from (b).
The `carries-three-sense-table.md` companion artifact formalizes this
consumer-by-sense matrix.

---

## Forbidden-proxy rejections

- **fp-sense-c-claim-without-c4-proof** — REJECTED. Section 5 contains an
  explicit (c4) proof showing both sides of the ∘-preservation identity
  reduce to the same element of V_{BM}. The caveat about alternative
  operation definitions is tracked but does not affect (c4) as stated in
  the Paper 5 setting.
- **fp-frozen-file-edit** — REJECTED. This artifact is a markdown file
  in `derivations/paper5-peirce-preservation/`; no paper LaTeX file is
  modified by Plan 56-02.
- **fp-carries-sense-collapse** — REJECTED. Every use of "carries" /
  "inherits" / "morphism" in this artifact is tagged with a specific
  sense (a), (b), (c), or explicitly marked as an SPS-morphism (BGW
  2020 sense). Zero bare/ambiguous "carries" usages.

## Forbidden-token scan (outside demarcated scope)

- `Thm 9.37` — zero hits. ✓
- `Hanche-Olsen` — zero hits. ✓
- `Lüders` / `Luders` — zero hits. ✓
- `M_n(ℂ)^{sa}` — zero hits. ✓
- `AlfsenShultz.*Ch.~9` — zero hits. ✓

No A-S citation appears in this artifact; the BGW 2020 citation is
Plan-scoped (allowed) and vdW 2019 is also allowed.
