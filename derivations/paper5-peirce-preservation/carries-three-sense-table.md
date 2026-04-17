---
artifact: carries-three-sense-table
phase: 56
plan: 02
task: 4
status: COMPLETE
role: R7-mitigation artifact; input to Plan 56-03 revision text
conventions:
  senses: "(a) set-closure ⊂ (b) induced-structure SPS ⊂ (c) functorial SPS-morphism"
  senses_source: carries-senses.md §§1-5 (Phase 56-01 Task 4)
  consumer_source: downstream-consumer-scan.md §§2-5 (Phase 56-01 Task 2)
  phase_56_establishes_all_rows: sense (c) (strongest) — sense (c) ⇒ (b) ⇒ (a) by collapse
  w_sps_proof_artifact: w-sps-proof.md (Phase 56-02 Task 2) — sense (b) source
  ci_sps_morphism_artifact: ci-sps-morphism.md (Phase 56-02 Task 3) — sense (c) source
  sympy_certificate: w-closeout-sympy.py + w-closeout-sympy.log (Phase 56-02 Task 1)
  revision_text_target: composite-lt.tex L203-221 + appendix-proofs.tex L228-238 (Plan 56-03 integration)
---

# Three "Carries" Senses × Downstream-Consumer Matrix

Phase 56-02 Plan 56-02 Task 4 — R7 mitigation artifact. This table maps each
§5/§6 downstream consumer (from `downstream-consumer-scan.md` §§2-5) to (i) the
sense of "carries" it requires (a/b/c), (ii) what Phase 56 establishes for that
consumer, and (iii) the proof artifact that supplies the evidence. Plan 56-03
revision text is built by selecting consumer rows and the matching language
phrases from Section 4.

**R7 mitigation.** R7 = "`sms:minimal` and `prop:inheritance` might be reading
'carries' in different senses; §5/§6 consumers might depend on a sense we
don't deliver". This artifact explicitly closes R7 by enumerating every
consumer, its required sense, and showing that **Phase 56 establishes sense
(c) — the maximum — for every row**. No consumer is under-served.

---

## Section 1 — Formal three-sense definitions (compressed)

Reproduced from `carries-senses.md §§1-5`; see that artifact for full
derivations and non-collapse witnesses.

### Sense (a): set-level closure

```
Sense (a) — set-level closure:
  For all a, b ∈ [0,1]_W := [0,1]_V ∩ W,  a ∘_V b ∈ W.
  Equivalently: ∘_V([0,1]_W × [0,1]_W) ⊆ W.
```

**Operational reading.** The product stays inside W *as a set*. Does NOT
equip W with an OUS structure or verify S1-S7.

### Sense (b): induced-structure SPS

```
Sense (b) — induced-structure SPS:
  (W, ≤|_W, 1_W, ∘|_W) satisfies vdW 2019 Def. 2 (S1-S7), where:
    ≤|_W  := restriction of ≤_V to W,
    1_W   := 1_V (valid iff 1_V ∈ W, true in Paper 5 setting),
    ∘|_W  := set-theoretic restriction of ∘_V to [0,1]_W × [0,1]_W.
```

**Operational reading.** W is itself an SPS under the induced structure.
This is the minimum for `sms:minimal` (per `carries-senses.md §7`).

### Sense (c): functorial SPS-morphism

```
Sense (c) — functorial SPS-morphism:
  The inclusion ι: W ↪ V is an SPS-morphism (BGW 2020 §2):
    (c1) R-linear,
    (c2) unital: ι(1_W) = 1_V,
    (c3) positive: ι(W^+) ⊆ V^+,
    (c4) ∘-preserving: ι(a ∘|_W b) = ι(a) ∘_V ι(b).
```

**Operational reading.** Strongest; clean for monoidal-category composition
(BGW 2020). Requires (c2) — i.e., `1_W = 1_V` — which holds in Paper 5.

### Collapse diagram

```
  (c) ==========> (b) ==========> (a)
  │               │              
  ⇕ unit-compat   ⇗ (a)⇏(b) in general (Gudder-Greechie 2002 Ex. 39)
  │                  but in Paper 5 setting (b) ⇒ (c) is free
  │                  since 1_W = 1_V.
  ↓
  In Paper 5 setting: (a) ⇔ (b) ⇔ (c).
```

Witness non-collapse cases (only relevant for general theory):

- **(a) ⇏ (b) in general:** Gudder-Greechie 2002 *Rep. Math. Phys.* **49**
  Ex. 39 (AXIOM-STATED-IN-SECONDARY-SOURCE tier; RMP 49 not directly
  accessed per `carries-senses.md §5`). In Paper 5, (a) ⇒ (b) holds via
  `w-sps-proof.md` because the set-closure is produced by the product-form
  identity, which induces full SPS structure on W.
- **(b) ⇏ (c) in general:** unit-choice subtlety — W might be a face of V
  not containing 1_V, forcing 1_W ≠ 1_V. In Paper 5, `1_W = 1_B ⊗ 1_M =
  1_V`, so this non-collapse does not apply.

---

## Section 2 — Downstream-consumer × required-sense matrix

Rows correspond to argumentative consumer sites identified in
`downstream-consumer-scan.md` §§2-5 (18 argumentative rows total; 3
out-of-scope rows omitted per §6 of that artifact).

Columns:

- **Consumer (file:line)** — Living Paper 5 source location (frozen
  `main-jmp-submitted.tex` is not listed; living section files are
  authoritative per Plan 56-01 convention).
- **Consumer summary** — 1-line description of what the consumer argues.
- **Required sense** — minimum carries-sense the consumer needs.
- **What Phase 56 establishes** — sense that Phase 56 supplies (always (c)
  in Paper 5 setting; see §3).
- **Proof artifact** — which Phase 56 deliverable supplies the evidence.

| # | Consumer (file:line) | Consumer summary | Required sense | Phase 56 establishes | Proof artifact |
|---|---|---|---|---|---|
| 1 | composite-lt.tex:44-45 | `sms:minimal` definition (V_{BM} side) — minimality clause restated locally | (b) [source] | (c) | w-sps-proof.md §4 + ci-sps-morphism.md §6 |
| 2 | composite-lt.tex:67-69 | `prop:inheritance` statement — S1-S7 on V_{BM} inheritance lemma | (b) | (c) | w-sps-proof.md §2-3 (reused structure) + ci-sps-morphism.md §6 |
| 3 | composite-lt.tex:92-107 | `rem:bootstrap` — explicit S1-S7 on algebraic tensor W | (b)+(c) | (c) | w-sps-proof.md §2 (primary route) + ci-sps-morphism.md §6 |
| 4 | composite-lt.tex:162-168 | `thm:local-tomo` theorem statement | (b) [source] | (c) | w-sps-proof.md §4 (Consequences) + w-closeout-sympy.log (certificate) |
| 5 | composite-lt.tex:204-221 | `thm:local-tomo` upper-bound proof — W satisfies (C1)-(C4) + product-form SP | (b) [source] | (c) | **CENTRAL** — w-sps-proof.md §1-4 + ci-sps-morphism.md §6 |
| 6 | composite-lt.tex:227-232 | `sms:minimal` eliminates entangled sector (framing) | (b) [framing] | (c) | w-sps-proof.md §4 Downstream use paragraph |
| 7 | type-exclusion.tex:46-47 | §6 exclusion invokes `thm:local-tomo` (dim identity) | (b) [use] | (c) | w-sps-proof.md §4 |
| 8 | type-exclusion.tex:114-116 | `thm:vdW3` hypothesis: `V⊗V` is an SPS | (b) | (c) | w-sps-proof.md §2 + ci-sps-morphism.md (functorial) |
| 9 | type-exclusion.tex:126-129 | `thm:vdW3` hypothesis table row: `V⊗V` + product-form SP satisfies S1-S7 | (b) | (c) | w-sps-proof.md §3 (fallback per-axiom table) |
| 10 | type-exclusion.tex:245-248 | `thm:main` proof outline: V_{BM} inherits S1-S7 from factors | (b) | (c) | w-sps-proof.md §2-3 |
| 11 | discussion.tex:31-34 | Dependency audit `sms:minimal` row | (b) [framing] | (c) | w-sps-proof.md §4 + carries-senses.md §7 |
| 12 | discussion.tex:61-64 | Dependency audit conditions (iii)-(iv) | (b) [use] | (c) | w-sps-proof.md §4 |
| 13 | discussion.tex:118-129 | `sms:minimal` structural paragraph: V_{BM} = minimal OUS carrying product states + SP | (b) [source] | (c) | w-sps-proof.md §4 Downstream use paragraph |
| 14 | discussion.tex:181-183 | Internality operational paragraph | (b) [framing] | (c) | w-sps-proof.md §4 |
| 15 | discussion.tex:210-217 | `sms:minimal` defense: internality as formal content | (b) [framing] | (c) | w-sps-proof.md §4 + ci-sps-morphism.md §6 |
| 16 | discussion.tex:245-254 | `cor:equivalence` proof: product-form SP inherits S1-S7 from factors | (b) | (c) | **USE SENSE (c)** — ci-sps-morphism.md §6 (cleaner for monoidal-category corollary) |
| 17 | discussion.tex:293-296 | Masanes-Müller comparison — cites `thm:local-tomo` | (b) [use] | (c) | w-sps-proof.md §4 |
| 18 | discussion.tex:426-468 | `rem:minimality-objection` — extended defense; explicit W construction | (b) [use] | (c) | w-sps-proof.md §1-4 + ci-sps-morphism.md §6 |
| 19 | appendix-proofs.tex:164-173 | `thm:lt-full` theorem statement | (b) [source] | (c) | w-sps-proof.md §4 |
| 20 | appendix-proofs.tex:229-238 | `thm:lt-full` upper-bound proof — preserves-this-subspace + again-product-effect | (a) → (b) | (c) | **CENTRAL** — w-sps-proof.md §1-4 + w-closeout-sympy.log |

**Row count:** 20 rows.

**Cross-check against downstream-consumer-scan.md §6 consumer summary:**
the scan reports 15 sense-(b), 1 sense-(a), 2 sense-(b)+(c) rows = 18
argumentative rows (out-of-scope excluded). The 20 rows above include:
- 15 sense-(b) in-scope rows (2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20 with row 20 having (a)→(b) notation — counted as the sense-(a) row per the scan's §5);
- 1 sense-(a) row (row 20, appendix-proofs.tex:229-238, upgraded to (b) by `prop:inheritance` in the next paragraph);
- 2 sense-(b)+(c) rows (rows 3 and 16 — both benefit from (c));
- row 1 (`sms:minimal` definition at composite-lt.tex:44-45) and row 5 (`thm:local-tomo` upper-bound proof) appear as additional argumentative-use rows beyond the 18-count but are the authoritative source / consumer sites for the identity itself. The count discrepancy (20 rows here vs 18 in the scan) is explained by splitting each `thm:local-tomo` site into its statement row and its proof row — both of which are consumer sites in the sense that downstream §6 text invokes them. Every `downstream-consumer-scan.md` §§2-5 row is represented.

**Every row's Phase-56-establishes entry is sense (c).** By the collapse
diagram (Section 1: (c) ⇒ (b) ⇒ (a) with equivalence in Paper 5 setting),
establishing (c) serves every consumer at or above its required sense.

---

## Section 3 — Phase 56 establishes sense (c) for all consumers

**Claim.** For every argumentative §5/§6 consumer identified in
`downstream-consumer-scan.md §§2-5` (Phase 56-01 Task 2) and enumerated in
Section 2 above, **Phase 56 establishes sense (c) of "carries"**.

**Justification.**

1. `w-sps-proof.md` (Plan 56-02 Task 2) proves sense (b) for W: `(W, ∘|_W)`
   satisfies vdW 2019 Def. 2 (S1-S7), via vdW 2019 Def. 4 + Thm 1 (primary
   route) with a fallback per-axiom table (S1-S7).
2. `ci-sps-morphism.md` (Plan 56-02 Task 3) proves sense (c) for W: the
   inclusion `ι : W ↪ V_{BM}` is an SPS-morphism in the BGW 2020 sense,
   with all four conditions (c1)-(c4) verified — the upgrade from (b) to
   (c) is free because `1_W = 1_{V_{BM}}` and `∘|_W` is a set-theoretic
   restriction (no alternative W-internal operation introduced).
3. `w-closeout-sympy.py` + `w-closeout-sympy.log` (Plan 56-02 Task 1)
   provide the symbolic-exact certificate on H_3(ℝ) ⊗ H_3(ℝ): 5/5 tests
   PASS in 0.006 s, exit 0. The certificate validates sense (a) closure,
   factor-level S1 + bilinearity, S3 unitality, S4 orthogonality
   symmetry, and negative-test (no counterexample on W_full; W_wedge
   annihilation via Phase 54 Test (ii)). This is the small-case
   certificate grounding the general-case proof in Section 2 of
   `w-sps-proof.md`.

Since sense (c) ⇒ sense (b) ⇒ sense (a) by the collapse diagram (and,
in the Paper 5 setting, all three senses are equivalent — see Section 1
last line), **every consumer is served at or above its required sense**.
This is the R7 mitigation artifact referenced in Plan 56-03's revision
text.

**Statement for Plan 56-03 to quote (maximum sense established):**

> Phase 56 establishes sense (c) of carries (per `carries-senses.md §3`)
> for every §5/§6 downstream consumer identified in Phase 56-01
> `downstream-consumer-scan.md §§2-5`. Sense (c) implies sense (b)
> implies sense (a) by the collapse diagram of `carries-senses.md §4`;
> in the Paper 5 setting (1_W = 1_{V_{BM}}), the three senses are
> equivalent. No consumer is under-served.

---

## Section 4 — Revision-text language inventory

Plan 56-03 will integrate revised proof text into:

- **Primary target:** `composite-lt.tex` lines 203-221 (living) — upper-bound step of `thm:local-tomo`.
- **Companion target:** `appendix-proofs.tex` lines 228-238 (living) — upper-bound step of `thm:lt-full`.
- **Frozen file:** `main-jmp-submitted.tex` — NOT TOUCHED (git tag `paper5-jmp-submitted`).

The following phrases are available for use in the revised proof text, in
increasing order of strength (sense (a) → (c)):

**L1. Sense (a) closure statement (factual, lowest sense).**
> "The product-form sequential product preserves W:
> $\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes (\seqp{b}{d})$
> is again a product effect in W."

(Already used at appendix-proofs.tex:232-233 and composite-lt.tex:215-217.)

**L2. Sense (b) induced-structure statement.**
> "W equipped with the restricted order, the order unit $1_W = 1_B \otimes 1_M$,
> the induced cone $W^+ := W \cap V_{BM}^+$, and the restricted sequential
> product $\seqp{}{}|_W$, is a sequential product space in the sense of
> \cite[Definition 2]{vandeWetering2019}."

**L3. Sense (b) via vdW 2019 Def. 4 + Thm 1 (primary route, ≤ 2 pages).**
> "Since $V_B$ and $V_M$ are each sequential product spaces (Proposition~\ref{prop:inheritance}),
> $W = V_B \otimes_\mathbb{R} V_M$ equipped with the product-form sequential product
> is a locally tomographic composite in the sense of
> \cite[Definition 4]{vandeWetering2019}, hence itself a sequential product space.
> By \cite[Theorem 1]{vandeWetering2019}, $W$ is order-isomorphic to a Euclidean
> Jordan algebra."

**L4. Sense (c) functorial SPS-morphism statement.**
> "The inclusion $\iota : W \hookrightarrow V_{BM}$ is a sequential-product-space
> morphism: linear, unital ($\iota(1_W) = 1_{V_{BM}}$), positive
> ($\iota(W^+) \subseteq V_{BM}^+$), and preserving $\seqp{}{}$ by construction
> (since $\seqp{}{}|_W$ is the set-theoretic restriction of $\seqp{}{}$)."

**L5. Sense (b) + (c) combined, compact (recommended for composite-lt.tex:204-221 integration).**
> "$W$ carries the product-form sequential product in sense (b)
> [induced-structure SPS satisfying S1-S7 per \cite[Definition 2]{vandeWetering2019}];
> since $1_W = 1_{V_{BM}}$ and $\seqp{}{}|_W$ is the restriction of $\seqp{}{}$,
> the inclusion $\iota : W \hookrightarrow V_{BM}$ is moreover an SPS-morphism
> (sense (c), \cite[§2]{BarnumGraydonWilce2020}), so sense (c) holds as a free
> corollary."

**L6. `sms:minimal` restatement with explicit sense tag.**
> "By minimality (Definition~\ref{def:self-modeling-system}\ref{sms:minimal}),
> $V_{BM}$ is the smallest order unit space satisfying the composite axioms
> (C1)-(C4) and carrying a product-form sequential product in sense (b) per
> \ref{carries-senses.md §2}. Since $W$ carries the product-form sequential
> product in sense (b) and has dimension $d^2$, we have $\dim(V_{BM}) \le d^2$."

**L7. Appendix upgrade (for appendix-proofs.tex:228-238 integration).**
> "The product-form sequential product preserves this subspace
> [$\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes (\seqp{b}{d})$,
> again a product effect — sense (a)]; moreover, by
> \cite[Definition 4 + Theorem 1]{vandeWetering2019}, $(W, \seqp{}{}|_W)$ is
> itself a sequential product space (sense (b)), and the inclusion is an
> SPS-morphism (sense (c)) since $1_W = 1_{V_{BM}}$."

**Plan 56-03 selection policy.** The recommended integration is:

- **composite-lt.tex:204-221** → use **L5** (compact sense-(b)+(c) statement)
  replacing the existing "inherits OUS structure" language at L208-210,
  then continue with L6 for the minimality-argument paragraph.
- **appendix-proofs.tex:228-238** → use **L7** (appendix upgrade) to
  replace the existing "preserves this subspace" language at L232-233,
  then continue to the minimality conclusion at L235-237.

Plan 56-03 contract will pin the exact line substitutions; this section is
the source-of-truth **phrase inventory** for those substitutions.

---

## Forbidden-proxy rejections

- **fp-three-sense-table-single-sense-default** — REJECTED. Section 3
  explicitly claims sense (c) for all rows (strongest established), not
  merely sense (b) default. Section 2's "Phase 56 establishes" column is
  (c) in every row.
- **fp-carries-sense-collapse** — REJECTED. Every consumer row in Section 2
  has an explicit sense tag in the "Required sense" column and a distinct
  tag in "Phase 56 establishes". No bare "carries" usage without sense
  designation appears in this artifact; every "carries" / "inherits" token
  is sense-tagged per `carries-senses.md` discipline.
- **fp-frozen-file-edit** — REJECTED. This artifact is a markdown file;
  no paper LaTeX file is modified. The revision-text phrases in Section 4
  are STRINGS to be integrated by Plan 56-03, not commits against any
  frozen file.

## Forbidden-token scan (outside demarcated/declaration scope)

- `Thm 9.37` — zero hits. ✓
- `Hanche-Olsen` — zero hits. ✓
- `Lüders` / `Luders` — zero hits. ✓
- `M_n(ℂ)^{sa}` — zero hits. ✓
- `AlfsenShultz.*Ch.~9` — zero hits. ✓
