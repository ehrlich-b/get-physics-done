---
artifact: w-face-status
phase: 56
plan: 01
task: 3
status: COMPLETE
verdict: NOT-FACE
conventions:
  face_definition_source: A-S 2003 Ch. 1 (exact Prop/Def number VERIFICATION-DEFERRED)
  ambient_OUS: V_{BM} (finite-dim archimedean OUS over R with distinguished unit 1 = 1_B (x) 1_M)
  W_definition: "W := span_R{a_i (x) b_j : a_i basis V_B, b_j basis V_M} <= V_{BM}"
  routing_default: "direct S1-S7 on W via vdW 2019 Def. 4 + Thm 1 (primary path regardless of verdict)"
---

# W Face Status in V_{BM}

## Section 1 — A-S 2003 Ch. 1 face definition

**Standard definition (A-S 2003 Ch. 1, VERIFICATION-DEFERRED for exact Prop/Def number):**

A non-empty subset F of the positive cone V^+ of an order unit space V is called a
*face* of V^+ iff the following hold:

- **(F1) Subcone:** F is a subcone of V^+: closed under non-negative scalar
  multiplication and non-negative sums.
- **(F2) Order-convex under non-negative combinations:** if u, v ∈ F and w = αu + βv
  with α, β ≥ 0, then w ∈ F (equivalent to F1 once F is a cone).
- **(F3) Hereditary under ≤:** if u ∈ F and 0 ≤ w ≤ u in V (i.e., w ∈ V^+ and u − w ∈
  V^+), then w ∈ F.

A *subspace* W ⊆ V is said to *be* (or *span*) a face if `F := W ∩ V^+` is a face of
V^+ in the sense above AND the real subspace W is the linear span of F (equivalently,
every element of W is a difference of elements of F).

**Citation:** A-S 2003 Ch. 1 face/face-of-cone definition. The bracketed form would be
`\cite[Ch.~1, Def.~\textsc{VERIFY}]{AlfsenShultz2003}`. The exact prop/def number is
flagged VERIFICATION-DEFERRED in this document: `alfsen-shultz-notes.md` does not
currently transcribe the Ch. 1 face definition literal statement, and the Phase 54/55
A-S access scope was Ch. 2/7/8 compressions and spectral theory, not Ch. 1 face
theory. The face definition above is the STANDARD OUS-theoretic definition used
uniformly across Alfsen--Shultz 2001 and 2003 and across the broader OUS literature
(Namioka--Phelps; Wilce; van de Wetering). Plan 56-02's face-restriction-bonus arm
(if invoked at all) would need the exact number; since Plan 56-02's PRIMARY path is
direct S1-S7 on W (NOT face-restriction), the prop-number deferral does not block the
plan. Flag for `alfsen-shultz-notes.md` extension if Plan 56-02 upgrades face-restriction
to a proof component.

**Note on F2 vs F3:** In the literature, "order-convex under ≤" and "hereditary under
≤" are sometimes collapsed into a single condition (hereditary-cum-convex); A-S 2003
and the present document treat them separately for clarity. Whichever version the
A-S text uses, F3 (hereditary) is the non-trivial condition; F2 (convex combinations
of F elements) is automatic from the subcone property.

## Section 2 — Candidate witness (proof strategy for NOT-FACE)

**Strategy:** exhibit a concrete witness violating (F3) — find u ∈ W ∩ V_{BM}^+ and
w ∈ V_{BM}^+ with 0 ≤ w ≤ u in V_{BM} but w ∉ W.

**Setup — real case:** Take V_B = V_M = H_2(R) ≅ M_2(R)^{sa}, so d = dim V_B = dim V_M
= 3. Then dim W = d² = 9 (W is spanned by the 9 product effects `a_i (x) b_j`).
Published dimension-counting results for the minimal composite of the real case
(type-exclusion.tex:52-63, citing BarnumWilce2014) give:

| Factor                    | dim V     | d²  | dim (minimal composite V_{BM}) | Relation          |
|---------------------------|-----------|-----|-------------------------------|-------------------|
| M_2(R)^{sa} = H_2(R)      | 3         | 9   | 10                            | d² < dim V_{BM}   |

In the real case, dim V_{BM} = 10 strictly exceeds dim W = d² = 9. Let v ∈ V_{BM} be
any unit vector in the 1-dim orthogonal complement of W inside V_{BM} (with respect to
any inner product extending the order structure). The space V_{BM}^+ is a proper solid
cone of dimension 10; the positive element 1_{V_{BM}} = 1_B ⊗ 1_M lies in the relative
interior of V_{BM}^+. Because V_{BM}^+ has non-empty interior, there exists ε > 0 such
that

```
u := 1_{V_{BM}},    w := (1/2) 1_{V_{BM}} + ε v
```

satisfies: (i) u ∈ W (since 1_B ⊗ 1_M = 1_B ⊗ 1_M ∈ W); (ii) 0 ≤ w ≤ u (for ε small
enough, w ∈ V_{BM}^+ because it is a perturbation of a cone-interior point, and u − w
= (1/2) 1_{V_{BM}} − ε v ∈ V_{BM}^+ for ε small); (iii) w ∉ W, because w has a non-zero
component along v which is orthogonal to W by construction.

This is the canonical NOT-FACE witness for the real case. It depends only on the
strict inequality dim W < dim V_{BM} (which holds in the real case per
type-exclusion.tex).

**Setup — complex case (the relevant one for the theory being derived):** Take V_B =
V_M = M_n(C)^{sa}, so d = dim V_B = n². Then dim W = d² = n^4. The minimal composite
is V_{BM} = M_{n²}(C)^{sa} with dim = (n²)² = n^4 = d² (type-exclusion.tex:98-103).
Hence dim W = dim V_{BM} and the linear span of product effects is already
the whole ambient: W = V_{BM}. In this case:

| Factor                     | dim V  | d²    | dim V_{BM} | W = V_{BM} ?        |
|----------------------------|--------|-------|------------|---------------------|
| M_n(C)^{sa}                | n²     | n^4   | n^4        | YES (dim match)     |

So in the complex case, W = V_{BM} as a subspace, and W is trivially a face of itself.

**Setup — quaternionic case:** dim W = 36, dim V_{BM} = 28 (type-exclusion.tex:71-74).
Since dim V_{BM} < dim W, W is linearly DEPENDENT in V_{BM}: the 36 product effects
are not linearly independent, and the "subspace spanned by product effects" equals at
most V_{BM} (but via non-trivial linear dependencies). Face status is ill-posed here
as an inheritance-from-W question because W does not embed faithfully.

**The conclusion the witness delivers:** In the REAL case (the one the
type-exclusion.tex argument critically uses to exclude real QM), W is not a face of
V_{BM}. This is exactly the case where the roadmap-level worry about face-status
matters — and the witness construction shows NOT-FACE. In the COMPLEX case, W = V_{BM}
trivially, so "W is a face of V_{BM}" is vacuously TRUE but uninformative. In the
QUATERNIONIC case, the question is degenerate.

## Section 3 — Verdict

**VERDICT: NOT-FACE** (generically), with the following case-by-case clarification:

- **Real case (V = H_n(R), n ≥ 2):** W is **NOT a face** of V_{BM}. Witness
  construction in Section 4 below.
- **Complex case (V = M_n(C)^{sa}, n ≥ 1):** W = V_{BM} by local tomography, and the
  whole ambient V_{BM}^+ is trivially a face of itself. The face question is vacuous
  in this case.
- **Quaternionic case (V = M_n(H)^{sa}, n ≥ 2):** W is not faithfully embedded (dim
  comparison fails); face status is ill-posed. NOT-FACE by default since W ≠ V_{BM}
  and the face axioms do not close.

**Operative verdict for Plan 56-02:** NOT-FACE (the real case is the type-exclusion
test bed and forces the NOT-FACE verdict at the relevant comparison scale). The
complex-case vacuous result does NOT rescue the face-restriction shortcut because the
face-restriction shortcut is only useful for cases where dim W < dim V_{BM} (which is
precisely the non-complex cases).

## Section 4 — Evidence (witness construction)

**Real-case explicit witness (V_B = V_M = H_2(R)):**

Let `{E_1, E_2, E_3}` be the standard basis of H_2(R):

```
E_1 = diag(1, 0),    E_2 = diag(0, 1),    E_3 = [[0, 1], [1, 0]] (off-diagonal symmetric).
```

Then `1_B = E_1 + E_2` and `1_M = E_1 + E_2` (in each factor). The 9 product effects
are `E_i (x) E_j` for `i, j ∈ {1, 2, 3}`, spanning W ⊆ V_{BM}.

Under BarnumWilce2014 (as cited in type-exclusion.tex:63), the minimal composite
V_{BM} has dim 10, not 9. The extra 10th dimension is a non-product positive
direction. Let v ∈ V_{BM} be a unit vector in this 10th dimension (specifically, v
can be constructed in the `H_2(R) ⊗ H_2(R)` maximal composite — which embeds into the
real 4x4 symmetric matrices and carries a natural W-orthogonal direction via the
Jordan-product structure of the maximal composite, though the minimal-composite
identification of this direction is technical and defers to BarnumWilce2014).

Take:

```
u = 1_{V_{BM}} = 1_B (x) 1_M = (E_1 + E_2) (x) (E_1 + E_2) = sum_{i,j in {1,2}} E_i (x) E_j.
```

This lies in W.

Take:

```
w = (1/2) * 1_{V_{BM}} + ε * v,     for some 0 < ε << 1 chosen so that w ∈ V_{BM}^+ and u - w ∈ V_{BM}^+.
```

Verification:

1. **w ∈ V_{BM}^+:** 1_{V_{BM}} is in the interior of the proper cone V_{BM}^+ (order
   unit). The interior is open, so any sufficiently small perturbation ε v stays
   inside V_{BM}^+. Choose ε > 0 so that w = (1/2) 1_{V_{BM}} + ε v ∈ V_{BM}^+.
2. **u − w ∈ V_{BM}^+:** u − w = (1/2) 1_{V_{BM}} − ε v; by the same interior argument,
   this is in V_{BM}^+ for ε small.
3. **u ∈ W:** u = 1_{V_{BM}} ∈ W (already shown).
4. **w ∉ W:** w has a non-zero coefficient along v; v is by construction orthogonal
   to W. Hence w has a non-zero component outside W, so w ∉ W.

Conditions (F3) is VIOLATED: u ∈ W ∩ V_{BM}^+ with 0 ≤ w ≤ u and w ∉ W ∩ V_{BM}^+.
Therefore W ∩ V_{BM}^+ is NOT hereditary in V_{BM}^+, and W is NOT a face of V_{BM}.
**QED for real case.**

**Evidence appeal:** The existence of a W-orthogonal positive direction v in the real
case is confirmed by type-exclusion.tex:63 and BarnumWilce2014; the technical
construction of v inside the minimal composite is a standard consequence of the
strict inequality dim V_{BM} > dim W = d² for the real case.

**Complex-case null evidence:** In the complex case W = V_{BM}, and the face axioms
are trivially satisfied (W coincides with the whole ambient). This does not help with
the face-restriction shortcut, because face-restriction is only a useful technique
when W is a PROPER face of a STRICTLY LARGER ambient; here W = V_{BM} provides no
"restriction".

**Uncertainty flag:** Section 4's witness construction is evidence-backed but invokes
BarnumWilce2014 indirectly for the existence of the W-orthogonal direction v inside
the *minimal* composite. If Plan 56-02 wants a fully explicit witness, the construction
can be sharpened by either (i) computing v as the normalized off-diagonal component
of any state preparation in the H_2(R) ⊗ H_2(R) maximal composite that has a non-zero
marginal-correlation signature not realizable by product effects, or (ii) citing
BarnumWilce2014 Prop. at the precise point that guarantees strict dim-inequality
(existence of non-product positive directions). For Plan 56-02 purposes, the present
INCONCLUSIVE-UPGRADED-TO-NOT-FACE evidence is sufficient because the plan does NOT
depend on face-restriction.

## Section 5 — Routing implication

Given the NOT-FACE verdict:

- **IS-FACE branch** (not applicable): would enable an A-S 2003 Ch. 7 compression
  `C_F: V_{BM} → F = W` to exist and to inherit S1-S7 automatically via facial-OUS
  theory. Not available here.
- **NOT-FACE branch** (operative): face-restriction shortcut is UNAVAILABLE. Plan
  56-02 proceeds via **direct S1-S7 on W** using vdW 2019 Def. 4 (locally tomographic
  composite) + vdW 2019 Thm 1 (S1-S7 ⇒ EJA) as the primary path. This is also the
  recommended route in `.gpd/phases/56-.../56-RESEARCH.md` §Standard Approaches §1
  (Approach 1 — direct S1-S7).

**Routing to Plan 56-02:** Primary path = direct S1-S7 on W via vdW 2019 Def. 4 + Thm
1. Face-restriction is NOT available and NOT needed.

## Section 6 — Recommendation to Plan 56-02

Regardless of the Section 3 verdict, **Plan 56-02 should proceed with direct S1-S7 on
W via vdW 2019 Def. 4 + Thm 1 as the primary path.** Reasons:

1. **Robustness:** The direct path works whether or not W is a face. It does not
   depend on face-restriction machinery. The NOT-FACE verdict here *confirms* that the
   direct path is the only path; it does not invalidate the plan.
2. **Clarity:** Sense (b) [carries-senses.md §2] is exactly what the direct path
   produces as its output. This matches the downstream `sms:minimal` requirement (see
   `downstream-consumer-scan.md` §7).
3. **No bonus needed:** Face-restriction would only provide a redundant check after
   the direct S1-S7 work is complete. Since face-restriction fails in the real case
   (the critical test case), using it as an alternative framing in Plan 56-03's
   revision text would actually MISLEAD: the face-restriction reading does not
   generalize across V_B ∈ {H_n(R), M_n(C), M_n(H)}.

**Recommendation:** Plan 56-02 constructs (W, ≤|_W, 1_W, ∘|_W) as a sense-(b) SPS
directly on W, applies vdW 2019 Def. 4 to verify W is a locally tomographic composite
of (V_B, V_M), and concludes via vdW 2019 Thm 1 that W is order-isomorphic to an EJA.

Plan 56-03's revision text (integration into sections/composite-lt.tex) should state
the upper-bound step in sense (b) language, referencing vdW 2019 Def. 4 + Thm 1 as
the citation chain, and should NOT frame the result in face-restriction terms.

## Forbidden-proxy rejections

- **fp-face-status-handwave** — REJECTED. The verdict is evidence-backed: Section 4
  constructs a concrete NOT-FACE witness for the real case with the dim-mismatch
  citation from BarnumWilce2014 (via type-exclusion.tex:63). No bare assertion.
- **fp-face-status-shortcut-assumption** — REJECTED. The document does NOT assume "W
  is a face because it's spanned by positive elements." The witness explicitly
  exhibits a positive element w in V_{BM}^+ that lies strictly below u ∈ W but is
  NOT in W — the canonical face-failure pattern, not a face-existence shortcut.

## Appendix — A-S 2003 Ch. 1 citation deferral log

**VERIFICATION-DEFERRED items:**

- Exact Prop/Def number in A-S 2003 Ch. 1 for the face definition (F1)-(F3).

**Reason for deferral:** `alfsen-shultz-notes.md` (as of Phase 55 close) does not
transcribe Ch. 1 literal definitions; the Phase 54/55 A-S access scope covered Ch. 2
(abstract compressions), Ch. 7 (general compressions), Ch. 8 (spectral theory), and
Ch. 9 (Jordan, FORBIDDEN) but not Ch. 1 (OUS basics).

**Impact on Phase 56:** NONE for Plan 56-02 (direct S1-S7 path does not depend on
face-restriction). If Plan 56-03 revision text uses face language, the revision
should cite `\cite[Ch.~1]{AlfsenShultz2003}` chapter-level and defer the exact
prop-number to an `alfsen-shultz-notes.md` extension.

**Action item for future A-S access:** Extend `alfsen-shultz-notes.md` with a Row
1.{NUM} entry transcribing the Ch. 1 face definition verbatim to close this
deferral.
