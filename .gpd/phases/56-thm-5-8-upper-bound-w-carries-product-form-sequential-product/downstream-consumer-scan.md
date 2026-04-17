---
artifact: downstream-consumer-scan
phase: 56
plan: 01
task: 2
status: COMPLETE
conventions:
  sense_assignments: a = set-level closure, b = induced-structure SPS, c = functorial SPS-morphism
  cited_senses_document: carries-senses.md (Task 4 output)
  scan_scope: four living section files + main.tex (frozen main-jmp-submitted.tex NOT scanned — living is authoritative)
---

# Downstream Consumer Scan — §5/§6 consumers of `thm:local-tomo`, V_{BM}, and "carries"/"inherits" language

Scope: grep-driven scan of the living Paper 5 to locate every site that consumes
`thm:local-tomo`, `V_{BM}`, product-form SP language, or "carries"/"inherits"/`sms:minimal`
tokens. Each hit is classified by which of the three "carries" senses (a/b/c,
carries-senses.md) is required downstream.

## Section 1 — Grep patterns

```
thm:local-tomo
ref{thm:local-tomo}
Cref{thm:local-tomo}
V_{BM}
V_BM
product-form
\bcarries\b
\binherits\b
sms:minimal
ref{sms:minimal}
```

Executed via:

```bash
cd /Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling
for f in sections/composite-lt.tex sections/type-exclusion.tex sections/discussion.tex sections/appendix-proofs.tex main.tex; do
  echo "=== $f ==="
  grep -nE 'thm:local-tomo|V_\{BM\}|V_BM|product-form|\bcarries\b|\binherits\b|sms:minimal' "$f"
done
```

Raw-hit counts per file (strict-grep, no deduplication):

| File                          | Hit count |
|-------------------------------|-----------|
| sections/composite-lt.tex     | 39        |
| sections/type-exclusion.tex   | 9         |
| sections/discussion.tex       | 17        |
| sections/appendix-proofs.tex  | 14        |
| main.tex                      | 6         |
| **Total**                     | **85**    |

Strict R7 consumer rows are only those hits that ACTUALLY consume `thm:local-tomo` /
`sms:minimal` / product-form SP / carries / inherits as an *argumentative invocation*
of W's carries-structure. Many hits are definitional/framing or are uses of `V_{BM}` as
a pure symbol (not an invocation of carries-structure). Tables below record
argumentative consumer sites and classify each; the count summary in Section 6 lists
*argumentative* consumer row counts (not raw grep hits).

## Section 2 — composite-lt.tex consumer table

| file:line                  | Verbatim context (2-4 lines; trimmed)                                                                                     | Required sense | Rationale |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------|-----------|
| composite-lt.tex:14        | "isomorphically the model $M$) carries EJA structure, we now formalize the composite system $V_{BM}$"                     | (c)            | Pre-composite carry: applies EJA carry-structure to the self-modeling map at the factor level. Out of Phase 56 scope but retained for token inventory completeness. |
| composite-lt.tex:44-45     | "$V_{BM}$ is the \emph{minimal} order unit space satisfying (C1)--(C4) and the product-form sequential product"          | (b) [source]   | This IS the `sms:minimal` definition locally re-stated; downstream the competitor W must be sense (b). |
| composite-lt.tex:67-69     | "\begin{proposition}[S1--S7 inheritance]\label{prop:inheritance}... product-form sequential product on $V_{BM}$ satisfies S1--S7" | (b)            | `prop:inheritance` claims S1-S7 hold on `V_{BM}` (not W); W's S1-S7 is the Phase 56 separate task. Phase 56 reuses the proof structure (S4 via state separation) but applies it to W in place of V_{BM}. |
| composite-lt.tex:92-107    | Remark `rem:bootstrap` — "The product-form sequential product... on the algebraic tensor product $V_B \otimes V_M$ (not on all of $V_{BM}$)... Axioms S1--S7 are verified on this subspace... this product carries EJA structure. State separation (Theorem~\ref{thm:local-tomo}) then shows..." | (b)+(c)        | The remark EXPLICITLY talks about S1-S7 on the subspace (sense (b)); the phrase "carries EJA structure" is about the subspace itself so sense (b) or (c). KEY downstream consumer — the remark already presumes sense (b) on `V_B \otimes V_M`. R7 confirmed: `rem:bootstrap` is the site where Plan 56-02's direct-S1-S7-on-W verification is intended. |
| composite-lt.tex:162-168   | `\begin{theorem}[Local tomography]\label{thm:local-tomo}` — the theorem statement itself (`dim V_{BM} = dim V_B * dim V_M`) | (b) [source]   | The theorem is the identity; its upper-bound proof is the carries invocation. |
| composite-lt.tex:204-221   | The upper-bound proof itself — "$W$ inherits OUS structure from $V_{BM}$"; "We check that $W$... satisfies (C1)--(C4)"; "the product-form SP maps $W$ into $W$" | (b) [source]   | CENTRAL consumer row. Phase 56 exists to fill in the sense (b) proof here. |
| composite-lt.tex:227-232   | "minimality (`sms:minimal`) eliminates this sector by construction: $V_{BM}$ is defined as the smallest OUS satisfying the composite axioms" | (b) [framing]  | Restates `sms:minimal` — framing of sense (b) minimality-semantics, not a fresh consumer invocation. |

**Factor-level Peirce invariance flag (R11):** None of the composite-lt.tex rows invoke
factor-level Peirce invariance (the Phase 54 `\ref{lem:peirce-preservation}` lemma is
not touched by the upper-bound step). The `prop:inheritance` S4 proof uses state
separation (A-S 2003 Thm 1.23), not Peirce preservation. No R11 citation required here.

## Section 3 — type-exclusion.tex consumer table

| file:line                    | Verbatim context (2-4 lines; trimmed)                                                                 | Required sense | Rationale |
|------------------------------|------------------------------------------------------------------------------------------------------|----------------|-----------|
| type-exclusion.tex:46-47     | "We now show that local tomography (Theorem~\ref{thm:local-tomo}) excludes every non-complex type"   | (b) [use]      | §6 exclusion argument INVOKES the theorem statement `dim V_{BM} = d^2`. Only the equality identity is consumed, not the carries-structure on W. Sense (b) reads the theorem's upper-bound step; downstream consumer does NOT need morphism-level (c). |
| type-exclusion.tex:114-116   | "composite $V\otimes V$, equipped with the product-form sequential product, is also a sequential product space and the composite is locally tomographic" | (b)            | `thm:vdW3` hypothesis: `V⊗V` must itself be an SPS (sense (b)). This is where the carries-structure-on-W identity is actually consumed at the theorem-invocation level. |
| type-exclusion.tex:126-129   | Table row: "$V\otimes V$ with product-form SP satisfies S1--S7 — Verified — Proposition~\ref{prop:inheritance}" | (b)            | Explicit sense (b) consumer — the table row names `prop:inheritance` as establishing the carries-structure. The `V⊗V` here is NOT W, it is the composite V_{BM} in the case V_B = V_M = V. The theorem `thm:vdW3` needs `V⊗V` as an SPS (sense (b)); the Phase 56 sense-(b)-on-W result IS what `prop:inheritance` establishes (when restricted to the upper-bound argument). |
| type-exclusion.tex:222-223   | `thm:main` conclusion: "$M_n(\mathbb{C})$ carries the conjugate-transpose involution $X^* = X^\dagger$" | (out of scope) | This is a post-classification use of "carries" referring to the C*-involution on the classified algebra, NOT to the W-carries-SP question. Tag: out of Phase 56 scope. |
| type-exclusion.tex:230       | "(C4) follows from the internal-accessibility condition~\ref{sms:minimal}"                          | (b) [framing]  | Restates `sms:minimal` as sense (b) framing. Downstream uses the minimality-identity (sense (b)) but not the carries-structure on W directly. |
| type-exclusion.tex:245-248   | "The composite $V_{BM}$ with the product-form SP inherits S1--S7 (Proposition~\ref{prop:inheritance}), and state separation combined with minimality yields local tomography (Theorem~\ref{thm:local-tomo})" | (b)            | Main-theorem proof outline row; sense (b) explicit via "inherits S1-S7". The structure-identity from `thm:local-tomo` + `prop:inheritance` is composed. |

## Section 4 — discussion.tex consumer table

| file:line                   | Verbatim context (2-4 lines; trimmed)                                                               | Required sense | Rationale |
|-----------------------------|----------------------------------------------------------------------------------------------------|----------------|-----------|
| discussion.tex:31-34        | "Local tomography follows from Condition~\ref{sms:minimal}... via state separation (lower bound) and minimality (upper bound)" | (b) [framing]  | Dependency audit row — names sense (b) as the `sms:minimal` semantic content. |
| discussion.tex:61-64        | "Definition...(iii)--(iv) (minimal composite + simplicity): yields local tomography (Theorem~\ref{thm:local-tomo}), which excludes all non-complex simple EJA types" | (b) [use]      | Same as above but for Main Dependency Audit. |
| discussion.tex:118-129      | "Condition~\ref{sms:minimal}: Minimal composite... The body--model composite $V_{BM}$ is defined as the minimal order unit space carrying product states, product effects, non-signaling constraints, and a product-form sequential product." | (b) [source]   | CORE `sms:minimal` statement — the "carrying" here is at the `V_{BM}` level not W, but the W-carries-SP argument ultimately has to match this minimality statement. Sense (b). |
| discussion.tex:181-183      | "Condition~\ref{sms:minimal} (minimal composite) says the body--model composite carries no structure beyond what product measurements can resolve" | (b) [framing]  | "Carries no structure" is a negative-framed version of sense (b). No new argumentative claim. |
| discussion.tex:210-217      | "Condition~\ref{sms:minimal} \emph{is} the formal statement of `internal' for a spectral OUS equipped with a tracking map... $\ref{sms:minimal}$ is part of the definition of self-modeling system." | (b) [framing]  | Philosophical defense of `sms:minimal`; sense (b) content unchanged. |
| discussion.tex:245-254      | Corollary `cor:equivalence` proof: "The minimal composite of $\Mnsa{n}$ with itself is $M_{n^{2}}(\mathbb{C})^{\mathrm{sa}}$... Local tomography holds, and the product-form sequential product inherits S1--S7 from the factors." | (b)            | EXPLICIT sense (b): the proof of the corollary invokes "the product-form SP inherits S1-S7 from the factors". This IS the carries identity on the subspace (sense (b) at the subspace level). Here `the factors` = factor-level EJAs, and the inheriting subspace is `V_B ⊗_alg V_M ⊆ V_{BM}` — exactly W. Row MATCHES Phase 56 work. |
| discussion.tex:293-296      | "Masanes--Müller... tomographic locality postulate assumes local tomography... whereas we \emph{derive} local tomography from faithful tracking via the EJA trace form non-degeneracy argument (\Cref{thm:local-tomo})" | (b) [use]      | Comparison §: cites `thm:local-tomo` as the derivation target. No new carries invocation. |
| discussion.tex:426-468      | Remark `rem:minimality-objection` — extended discussion of `sms:minimal` (mathematical + structural + conceptual). "the derivation---state separation for the lower bound, explicit construction of~$W$ for the upper bound---is given in full in Theorem~\ref{thm:local-tomo}." | (b) [use]      | The remark explicitly names the explicit construction of W as the upper-bound mechanism. Sense (b) on W is the downstream target; the objection response DEPENDS on W being a sense (b) competitor OUS. |

## Section 5 — appendix-proofs.tex consumer table

| file:line                      | Verbatim context (2-4 lines; trimmed)                                                             | Required sense | Rationale |
|--------------------------------|--------------------------------------------------------------------------------------------------|----------------|-----------|
| appendix-proofs.tex:164-173    | Theorem statement `thm:lt-full`                                                                  | (b) [source]   | Detailed version of `thm:local-tomo`; same dim identity; upper-bound step is sense (b) on W. |
| appendix-proofs.tex:229-238    | "The product effects $\{a_i \otimes b_j\}$ span a $d^2$-dim subspace of $V_{BM}$. The product-form sequential product preserves this subspace: $\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes (\seqp{b}{d})$, which is again a product effect." | (a) → (b)      | Appendix upper-bound proof. Sense (a) (closure) is asserted by the `preserves this subspace` + `is again a product effect` language. Sense (b) is what `prop:inheritance` provides and what minimality consumes. Phase 56 tightens the (a)→(b) inference. |

## Section 6 — Consumer-by-sense summary

Argumentative consumer rows (not raw grep hits):

| Sense | Count | Notes |
|-------|-------|-------|
| (a)   | 1     | appendix-proofs.tex:229-238 is the *only* row where sense (a) stands alone; every other "inherits"/"carries" site immediately upgrades to (b). |
| (b)   | 15    | Dominant consumer sense. `sms:minimal` (framing), `prop:inheritance` (source), `thm:vdW3` hypothesis (use), `cor:equivalence` proof (explicit), type-exclusion.tex `thm:main` outline (explicit), composite-lt.tex `rem:bootstrap` (source), composite-lt.tex upper-bound proof (source). |
| (c)   | 2     | composite-lt.tex:14 (pre-composite, out of Phase 56 scope); main.tex:308 (informal "carries a SP" definitional). No strict argumentative sense (c) consumer exists in §5/§6 that is NOT automatically satisfied by sense (b) in the Paper 5 setting (since 1_W = 1_V). |
| unclassified-pending-user | 0 | No genuinely ambiguous row found. |
| out-of-scope              | 3 | type-exclusion.tex:222-223 (`M_n(C) carries conjugate-transpose`); composite-lt.tex:14 (factor-level pre-composite); main.tex:308 (general SPS-morphism definitional). These are different "carries" usages not related to W-carries-SP. |

Total argumentative rows (excluding out-of-scope): **18**
Of which sense (b) is the required minimum: **15 of 16 in-scope rows** (all except the 1 sense-(a) row). The sense-(a) row upgrades to (b) via `prop:inheritance` in the very next paragraph.

## Section 7 — `sms:minimal` row — explicit sense (b) classification

The `sms:minimal` clause is the pivotal consumer. Its locations across the scan:

- **Definition site:** composite-lt.tex:43-45 and main.tex:351-353. The clause asserts
  `V_{BM}` is the *smallest* OUS satisfying (C1)-(C4) + product-form SP.
- **Upper-bound consumer:** composite-lt.tex:218-221 and appendix-proofs.tex:236-237.
  The upper-bound step says: "since W satisfies (C1)-(C4) + product-form SP and has
  dimension d², the minimality clause forces dim V_{BM} ≤ d²".

**Required sense: (b).** Justification:

> The minimality clause says `V_{BM}` is the smallest OUS satisfying (C1)-(C4) and
> carrying a product-form sequential product. For W to count as a competitor (so that
> `dim V_{BM} ≤ dim W = d²` follows), W must itself be an OUS satisfying the same
> structural conditions — (C1)-(C4) and the product-form SP, with W's own order unit,
> its own cone, and the restriction of the product. This is exactly sense (b): `(W,
> ≤|_W, 1_W, ∘|_W)` is an SPS in the vdW 2019 Def. 2 sense. Sense (a) (set-closure)
> alone does not make W an OUS — it does not equip W with an order unit or verify
> S1-S7 on the restricted product. The minimality clause compares OUS structures, so
> W must arrive at the comparison already equipped as an OUS.

**R11 Peirce-preservation flag:** None of the `sms:minimal` consumer rows invoke
factor-level Peirce invariance. The Phase 54 `\ref{lem:peirce-preservation}` lemma is
NOT required at the W-level. (It is required *upstream*, at the §3.3 Peirce-preservation
site, which is a factor-level V_B or V_M argument; Phase 56 is downstream of that and
consumes the OUS structure of V_B, V_M as given.)

## Section 8 — Recommendation for Plan 56-02 target sense

**Primary recommendation:** Target sense **(b)** as the core Plan 56-02 deliverable.
Upgrade to sense **(c)** as a low-cost extension, since in the Paper 5 setting:

1. `1_W = 1_B ⊗ 1_M = 1_V` (the order unit of W coincides with that of V_{BM}), so the
   unit-preservation requirement of the SPS-morphism `ι: W ↪ V_{BM}` is automatic.
2. The closure identity `(a⊗b) ∘ (c⊗d) = (a∘c) ⊗ (b∘d)` shows `ι` preserves `∘`
   trivially by set-restriction.
3. Positivity of `ι`: `W^+ ⊆ V_{BM}^+` by construction (W^+ := W ∩ V_{BM}^+).
4. Hence (b) ⇒ (c) holds *in this setting* as a free corollary, once (b) is verified.

**Consumers that would benefit from sense (c):**

- `cor:equivalence` proof (discussion.tex:249-254) names `product-form SP inherits
  S1-S7 from the factors` — a functorial reading (sense (c)) would be CLEANER for this
  corollary.
- `thm:vdW3` hypothesis (type-exclusion.tex:114-116) — `V ⊗ V ... is also an SPS` —
  sense (b) is sufficient, but sense (c) makes the composition functorial and
  compositional (BGW 2020 monoidal-category framing).

**Downstream consumers that force sense (b) MINIMUM but are satisfied by (b) alone:**
all 15 of the sense (b) rows above.

**Downstream consumers that would force sense (c) strictly:** none found. Sense (c)
is optional.

**Plan 56-02 target (recommended):** prove sense (b) directly via vdW 2019 Def. 4 +
Thm 1; observe sense (c) as a free corollary from 1_W = 1_V. Record this in the
Plan 56-02 hand-off.

## Forbidden-proxy rejections

- **fp-carries-sense-collapse** — REJECTED. Every consumer row has an explicit sense
  assignment (a/b/c/out-of-scope); zero rows carry bare "carries" without sense tag.
- **fp-phase-54-ci-bypass** — REJECTED. Every row that could conceivably invoke
  factor-level Peirce invariance has been explicitly checked; none of the W-level
  upper-bound rows invoke it (the relevant S4-on-W proof uses state separation from
  A-S 2003 Thm 1.23, not Peirce preservation). If Plan 56-02 later discovers a
  factor-level Peirce invocation hidden in the `prop:inheritance` proof reuse, that
  row will be flagged and `\ref{lem:peirce-preservation}` cited.
