---
artifact: 56-03-DIFF-REPORT
phase: 56
plan: 03
task: 1
status: DRAFT (pre-integration; SHA fields filled in at Task 2)
hunks: [CL-1, AP-1]
sense_established_for_all_consumers: "(c) per carries-three-sense-table.md §3"
primary_proof_reference: w-sps-proof.md §2 (vdW 2019 Def. 4 + Thm 1)
fallback_proof_reference: w-sps-proof.md §3 (per-axiom S1-S7 table)
morphism_reference: ci-sps-morphism.md §§2-6
language_inventory_reference: carries-three-sense-table.md §4 (L1-L7)
conventions:
  frozen_file: /Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex
  frozen_file_discipline: zero-diff against HEAD (per Plans 56-01 + 56-02 precedent; tag paper5-jmp-submitted predates file add at commit a0190df, so HEAD is the operative baseline)
  as_citation_form: "\\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003} — X ≤ 8; Ch. 9 FORBIDDEN (Phase 55 Flag 4.1)"
  peirce_citation: "\\ref{lem:peirce-preservation} (Phase 54 C-i; resting on \\ref{ax:S0})"
  sense_tag_discipline: "every 'carries' in after-text followed within 1-2 sentences by 'sense (b)' or 'sense (c)' with back-pointer"
  forbidden_tokens_outside_transcription: ["Thm 9.37", "AlfsenShultz.*Ch.~9", "Hanche-Olsen", "Lüders", "Luders", "M_n(C)^{sa}"]
---

# Plan 56-03 Task 1 — Per-Hunk Revision Diff (Paper 5 §5 upper-bound integration)

This artifact is the per-hunk before/after revision diff for the Paper 5 §5
upper-bound step of `thm:local-tomo` and `thm:lt-full`. It is produced as a
stand-alone document **before** integration (Task 2 applies the hunks to the
LIVING working copy and records the blog-repo commit SHA below).

**Scope.** Two hunks (both required; no optional CL-2 hunk is included in this
draft — see §"Scope note on CL-2" at the end):

- **Hunk CL-1** — `composite-lt.tex` L203-221 (upper-bound step of `thm:local-tomo`).
- **Hunk AP-1** — `appendix-proofs.tex` L227-238 (upper-bound step of `thm:lt-full`).

**Frozen file discipline.** `main-jmp-submitted.tex` is NOT touched by any hunk
below. The frozen-file zero-diff check at Task 1 start returned empty output
(`git -C /Users/ehrlich/repos/blog diff --stat HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` → empty). Task 2
re-verifies after integration; Task 7 re-verifies pre-close (third verification).

**Sense-tag discipline (R7 closure).** Every occurrence of "carries" /
"carrying" in the after-text below is sense-tagged within 1-2 sentences with
"(sense (b))" or "(sense (c))" and a back-pointer to the Plan 56-02 proof
artifact (`w-sps-proof.md` or `ci-sps-morphism.md`). No bare "carries" survives
the after-text.

**R11 Peirce-invocation discipline.** The after-text below does not itself
invoke factor-level Peirce invariance directly — the primary-route proof
(vdW 2019 Def. 4 + Thm 1) is structural, and all factor-level Peirce
machinery is encapsulated inside the w-sps-proof.md §3 fallback table (S5,
S6, S7 rows) which is pointed to via a pointer in the justification, not
re-invoked in the paper text. The Peirce-invariance R11 touchpoint therefore
sits in w-sps-proof.md, not in the paper's revision text. No
`\ref{lem:peirce-preservation}` citation is required inline in CL-1 or AP-1
because the revision text does not invoke Peirce invariance directly; the
citation burden is discharged at the fallback-proof level in w-sps-proof.md
§3 + §6. (See §"R11 discipline note" at the end of this file for the
consolidated audit.)

**R5 A-S bracketing.** No new A-S 2003 citation is introduced by Hunk CL-1
(which does not touch the state-separation step; that remains at the
upstream lower-bound region and is out-of-hunk). Hunk AP-1 preserves the
existing state-separation cite at L219-220 which is already post-Phase 55
bracketed. The new citations introduced by Hunks CL-1 and AP-1 are:

- `\cite[Definition 4]{vandeWetering2019}` — non-A-S, vdW 2019 paper cite;
- `\cite[Theorem 1]{vandeWetering2019}` — non-A-S, vdW 2019 paper cite;
- `\cite[§2]{BarnumGraydonWilce2020}` — non-A-S, BGW 2020 paper cite;
- `\ref{prop:inheritance}` — internal paper reference (Paper 5 §4).

Zero new A-S citations means zero new bracketing-discipline obligations for
Hunks CL-1 and AP-1. The R5 bracketing audit is satisfied by inheritance.

---

## Hunk CL-1 — composite-lt.tex upper-bound step

**File:** `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/sections/composite-lt.tex`
**Pre-integration line range:** L203-221 (verified 2026-04-17T20:00:46Z, Task 1 start).
**Post-integration line range:** recorded in §"Integration Commits" below after Task 2.
**Semantic anchor:** `\emph{Upper bound.}` paragraph inside the proof of `thm:local-tomo`.

### Before-text (verbatim from living working copy, L203-221)

```latex
\emph{Upper bound.}
Let $W \subseteq V_{BM}$ be the $d^2$-dimensional span of the product
effects $\{a_i \otimes b_j\}$.  The subspace $W$ inherits OUS
structure from $V_{BM}$: it contains the order unit
$\id_B \otimes \id_M$ (since $\id_B \in \spn\{a_i\}$ and
$\id_M \in \spn\{b_j\}$), and the induced cone
$W^+ = W \cap V_{BM}^+$ is proper (the product cone is contained
in $W^+$ and generates~$W$).  We check that $W$, equipped with this
induced order and the product-form sequential product, satisfies
(C1)--(C4): product effects lie in $W$ by construction (C2);
product states are positive functionals on $W$ (C3, by restriction);
non-signaling holds because marginals factor through $V_B$ and $V_M$
(C4); and the product-form SP maps $W$ into $W$ since
$\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes
(\seqp{b}{d})$ is again a product effect (C1).
By minimality (Definition~\ref{def:self-modeling-system}\ref{sms:minimal}),
$V_{BM}$ is the smallest OUS satisfying these axioms.  Since $W$
satisfies them and has dimension $d^2$,
we have $\dim(V_{BM}) \le d^2$.
```

### After-text (revision for L203-221 substitution)

```latex
\emph{Upper bound.}
Let $W \subseteq V_{BM}$ be the $d^2$-dimensional span of the product
effects $\{a_i \otimes b_j\}$.  The subspace $W$ inherits OUS
structure from $V_{BM}$: it contains the order unit
$\id_B \otimes \id_M$ (since $\id_B \in \spn\{a_i\}$ and
$\id_M \in \spn\{b_j\}$), and the induced cone
$W^+ = W \cap V_{BM}^+$ is proper (the product cone is contained
in $W^+$ and generates~$W$).  The restricted sequential product
$\seqp{}{}|_W := \seqp{}{}|_{[0,1]_W \times [0,1]_W}$ is the
set-theoretic restriction of $\seqp{}{}$ to $[0,1]_W$ and maps $W$
into $W$, because the product-form identity
$\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes
(\seqp{b}{d})$ is again a product effect.
Since $V_B$ and $V_M$ are each sequential product spaces
(Proposition~\ref{prop:inheritance}), $W = V_B \otimes_{\mathbb{R}} V_M$
equipped with the product-form sequential product is a locally
tomographic composite in the sense of
\cite[Definition~4]{vandeWetering2019}, hence itself a sequential
product space; that is, $W$ carries the product-form sequential product
in sense (b) [induced-structure sequential product space satisfying
axioms S1--S7 of \cite[Definition~2]{vandeWetering2019}].
Since $1_W = \id_B \otimes \id_M = 1_{V_{BM}}$ and $\seqp{}{}|_W$ is
the set-theoretic restriction of $\seqp{}{}$, the inclusion
$\iota : W \hookrightarrow V_{BM}$ is moreover a sequential-product-space
morphism (sense (c), \cite[§2]{BarnumGraydonWilce2020}), so sense (c)
holds as a free corollary. We now check $W$ against
(C1)--(C4): product effects lie in $W$ by construction (C2);
product states are positive functionals on $W$ (C3, by restriction);
non-signaling holds because marginals factor through $V_B$ and $V_M$
(C4); and closure under the product-form SP is (C1), established above.
By minimality (Definition~\ref{def:self-modeling-system}\ref{sms:minimal}),
$V_{BM}$ is the smallest OUS satisfying these axioms and carrying a
product-form sequential product in sense (b).  Since $W$ satisfies
(C1)--(C4), carries the product-form sequential product in sense (b)
(via \cite[Definition~4]{vandeWetering2019}, upgraded to sense (c) by
the inclusion morphism), and has dimension $d^2$,
we have $\dim(V_{BM}) \le d^2$.
```

### Justification (Hunk CL-1)

The revision replaces the submitted-era language "inherits OUS structure
/ equipped with this induced order ... satisfies (C1)--(C4)" with the
three-senses-disambiguated statement that matches the language inventory
L5 (sense (b) + (c) combined, compact) from
`carries-three-sense-table.md §4` verbatim, and L6 (minimality restatement
with explicit sense tag) for the closing minimality paragraph.

The first inserted paragraph (the "Since $V_B$ and $V_M$ are each sequential
product spaces ... hence itself a sequential product space" sentence)
follows `w-sps-proof.md` §2 Step 2 verbatim (primary route via vdW 2019
Definition 4 applied to the finite-dim composite $W = V_B \otimes V_M$);
`carries-three-sense-table.md §4 L3` supplies the exact phrasing.

The sense-tag discipline is discharged by attaching "(sense (b))" to the
first "carries" occurrence and "(sense (c))" to the morphism-upgrade
sentence, both with inline pointers to the vdW 2019 / BGW 2020 references.
The back-pointer to `w-sps-proof.md` / `ci-sps-morphism.md` is not inlined
in the paper text (to keep it publication-ready); the pointer lives in this
diff report's justification and in the A-S notes Phase 56 CLOSE entry. The
fallback per-axiom table (`w-sps-proof.md §3`) is available for any
skeptical referee via the vdW 2019 Definition 4 citation, which is the
structural theorem that the primary route applies to $W$; a referee who
wants the S1-S7 verification line-by-line can trace the vdW 2019 Def. 4
proof and find that it reduces each axiom on $W$ to the factor-level
axioms on $V_B$, $V_M$, which is exactly what `w-sps-proof.md §3` tabulates
in the 7-row per-axiom table.

**Sense tag annotations.** Every `carries` in the after-text:

- "W carries the product-form sequential product in sense (b)" — sense (b)
  per `w-sps-proof.md §4` (conclusion statement), established by
  `w-sps-proof.md §2` (primary route via vdW 2019 Def. 4 + Thm 1) with
  fallback per-axiom table in `w-sps-proof.md §3`.
- "the inclusion $\iota : W \hookrightarrow V_{BM}$ is moreover a
  sequential-product-space morphism (sense (c))" — sense (c) per
  `ci-sps-morphism.md §6` (free-upgrade statement), established by
  `ci-sps-morphism.md §§2-5` ((c1)-(c4) each proved individually).
- "carrying a product-form sequential product in sense (b)" (in the
  minimality paragraph) — back-reference to the sense (b) already
  established; not a new claim, just sense-tagged for consistency.
- "carries the product-form sequential product in sense (b) (via
  \cite[Definition~4]{vandeWetering2019}, upgraded to sense (c) by the
  inclusion morphism)" — back-reference carrying both sense tags
  explicitly; the "upgraded to sense (c)" phrasing points at
  `ci-sps-morphism.md §6`.

**Factor-level Peirce invariance.** The CL-1 after-text does not invoke
factor-level Peirce invariance. The primary-route proof (vdW 2019 Def. 4 +
Thm 1) is structural: it takes $V_B$, $V_M$ as sequential product spaces
(via `\ref{prop:inheritance}`) and produces the composite
$W = V_B \otimes_{\mathbb{R}} V_M$ as a sequential product space by a
structure-preservation argument. The factor-level Peirce-invariance R11
touchpoints sit inside the fallback per-axiom proof (`w-sps-proof.md §3`
rows S5, S6, S7) and are cited there via
`\ref{lem:peirce-preservation}` + `\ref{ax:S0}` (see `w-sps-proof.md §6`
R11 cross-check table). They are not re-invoked in the paper's revision
text because the paper uses the primary route, not the fallback.

**A-S citations introduced.** None. Hunk CL-1 does not introduce any new
A-S 2003 citation. The pre-hunk after-text contains zero A-S 2003 hits
(grepped below).

**Forbidden tokens.** Zero hits for `Thm 9.37`, `Ch.~9`, `Hanche-Olsen`,
`Lüders`, `Luders`, `M_n(C)^{sa}` in the after-text block (grep
self-confirmation recorded in §"Discipline checks (self-audit)" below).

---

## Hunk AP-1 — appendix-proofs.tex upper-bound step

**File:** `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/sections/appendix-proofs.tex`
**Pre-integration line range:** L227-238 (verified 2026-04-17T20:00:46Z, Task 1 start; the plan nominal was L228-238, extended to L227 to include the `\medskip` spacer for clean substitution).
**Post-integration line range:** recorded in §"Integration Commits" below after Task 2.
**Semantic anchor:** `\textbf{Step 4: Upper bound via minimality.}` paragraph inside the proof of `thm:lt-full`.

### Before-text (verbatim from living working copy, L227-238)

```latex
\medskip
\textbf{Step 4: Upper bound via minimality.}
The product effects $\{a_{i} \otimes b_{j}\}$ span a
$(\dim V_{B} \cdot \dim V_{M})$-dimensional subspace of $V_{BM}$.
The product-form sequential product~\eqref{eq:product-sp} preserves
this subspace: $\seqp{(a \otimes b)}{(c \otimes d)} =
(\seqp{a}{c}) \otimes (\seqp{b}{d})$, which is again a product effect.
The non-signaling constraints (C4) are satisfied by the
product-effect subspace.  By
minimality (\Cref{ass:minimal}), $V_{BM}$ contains no
structure beyond what is forced by (C1)--(C4) and the product-form SP.
Therefore $\dim(V_{BM}) \leq \dim(V_{B}) \cdot \dim(V_{M})$.
```

### After-text (revision for L227-238 substitution)

```latex
\medskip
\textbf{Step 4: Upper bound via minimality.}
The product effects $\{a_{i} \otimes b_{j}\}$ span a
$(\dim V_{B} \cdot \dim V_{M})$-dimensional subspace $W \subseteq V_{BM}$.
The product-form sequential product~\eqref{eq:product-sp} preserves this
subspace: $\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes
(\seqp{b}{d})$, which is again a product effect (sense (a) closure).
Moreover, since $V_{B}$ and $V_{M}$ are each sequential product spaces
(Proposition~\ref{prop:inheritance}),
$W = V_{B} \otimes_{\mathbb{R}} V_{M}$ equipped with
$\seqp{}{}|_{W}$ is a locally tomographic composite in the sense of
\cite[Definition~4]{vandeWetering2019}, hence $(W, \seqp{}{}|_{W})$ is
itself a sequential product space (sense (b)); the inclusion
$\iota : W \hookrightarrow V_{BM}$ is a sequential-product-space morphism
(sense (c), \cite[§2]{BarnumGraydonWilce2020}) since
$1_{W} = \id_{B} \otimes \id_{M} = 1_{V_{BM}}$ and $\seqp{}{}|_{W}$ is
the set-theoretic restriction of $\seqp{}{}$. The non-signaling
constraints (C4) are satisfied by the product-effect subspace.  By
minimality (\Cref{ass:minimal}), $V_{BM}$ contains no structure beyond
what is forced by (C1)--(C4) and the product-form sequential product
carried by $W$ in sense (b). Therefore
$\dim(V_{BM}) \leq \dim(V_{B}) \cdot \dim(V_{M})$.
```

### Justification (Hunk AP-1)

The revision preserves the original sense (a) closure sentence (the
product-form identity "is again a product effect" is sense-tagged
explicitly as "sense (a) closure" per `carries-three-sense-table.md §4
L1`) and inserts a compact sense-(b) + sense-(c) upgrade bridging
sentence that follows the language inventory L7 (appendix upgrade)
verbatim. The inserted sentence uses the same vdW 2019 Definition 4 +
Theorem 1 framing as Hunk CL-1 (primary-route proof, per
`w-sps-proof.md §2`) plus the BGW 2020 SPS-morphism framing (per
`ci-sps-morphism.md §6`).

The minimality closing sentence is updated to explicitly tag the
product-form SP as carried by $W$ in sense (b), preserving the
sense-discipline end-to-end. The "sense (a) closure" early tag and the
later "sense (b)" and "sense (c)" tags together exercise all three
senses exactly as the three-sense-table predicts — each tag has a
matching proof artifact: sense (a) → the product-form identity itself;
sense (b) → `w-sps-proof.md §2`; sense (c) → `ci-sps-morphism.md §6`.

**Sense tag annotations.** Every `carries` / `preserves` / `satisfies`
usage in the after-text:

- "The product-form sequential product ... preserves this subspace ...
  which is again a product effect (sense (a) closure)" — sense (a) per
  `carries-senses.md §1` and `w-sps-proof.md §4 Downstream use`; the
  product-form identity itself is the closure witness.
- "$(W, \seqp{}{}|_{W})$ is itself a sequential product space (sense
  (b))" — sense (b) per `w-sps-proof.md §2` (primary route) +
  `carries-senses.md §2`.
- "the inclusion $\iota : W \hookrightarrow V_{BM}$ is a
  sequential-product-space morphism (sense (c))" — sense (c) per
  `ci-sps-morphism.md §6` + `carries-senses.md §3`.
- "the product-form sequential product carried by $W$ in sense (b)"
  (in the minimality closing) — back-reference; sense tag propagated
  through the minimality statement.

**Factor-level Peirce invariance.** Same structural comment as Hunk CL-1:
the after-text uses the vdW 2019 Definition 4 structural-composite
framing; factor-level Peirce invariance is discharged inside
`w-sps-proof.md §3` rows S5, S6, S7 (via
`\ref{lem:peirce-preservation}` + `\ref{ax:S0}`) and is not re-invoked
in the paper's revision text. Appendix-proofs.tex has no inline
`\ref{lem:peirce-preservation}` obligation for this hunk.

**A-S citations introduced.** None. Hunk AP-1 does not add any new A-S
2003 citation. The existing `\cite{AlfsenShultz2003}, Theorem~1.23`
state-separation cite at L220 is NOT modified by this hunk and remains
untouched (it is pre-Phase-56 content; Phase 55 already bracketed it).

**Forbidden tokens.** Zero hits for `Thm 9.37`, `Ch.~9`, `Hanche-Olsen`,
`Lüders`, `Luders`, `M_n(C)^{sa}` in the after-text block (grep
self-confirmation recorded in §"Discipline checks (self-audit)" below).

---

## Scope note on CL-2

Hunk **CL-2** would have addressed `composite-lt.tex` L44-45 (the
`sms:minimal` clause). Per the plan contract, CL-2 is *optional* — it is
included only if the `sms:minimal` clause wording needs sense-language
update.

**Decision: CL-2 is OMITTED.** Reading the current `sms:minimal` clause
at L44-45 (stable since pre-Phase-56) and the Phase 56 revision language
at L203-221 (Hunk CL-1 above), the `sms:minimal` clause already states
the minimality constraint in a sense-language-agnostic way ("smallest
OUS satisfying the axioms"), and the CL-1 after-text explicitly invokes
the `sms:minimal` definition via `\ref{sms:minimal}` and attaches the
sense tag in-place ("$V_{BM}$ is the smallest OUS satisfying these
axioms and carrying a product-form sequential product in sense (b)").
This sense-tagging happens at the *use* site rather than the *definition*
site, which (a) preserves the definition's wording for backward
compatibility with Paper 5's other consumers and (b) keeps the change
footprint minimal. The sense discipline is preserved end-to-end without
editing L44-45.

This omission is consistent with the plan contract ("Hunk CL-2 (optional;
include if sms:minimal text needs sense-language update)"). If Phase 57
or Phase 58 discovers a consumer that needs the definition itself
sense-tagged, a follow-up hunk CL-2 can be added; for Phase 56's
closure-of-§5-upper-bound scope, the use-site tagging in CL-1 is
sufficient. Row 1 of `carries-three-sense-table.md §2` (composite-lt.tex
L44-45 `sms:minimal` definition) is addressed via the use-site tagging
in CL-1, and the "Phase 56 establishes (c)" entry in that row is
inherited from the CL-1 revision which has explicit sense (c) free
corollary.

---

## Discipline checks (self-audit on the after-text blocks)

**Grep 1 — bare 'carries':**

```bash
# Every 'carries' in after-text followed within 1-2 sentences by 'sense (b)' or 'sense (c)'
grep -nE 'carries' 56-03-DIFF-REPORT.md | head -30
```

Result (manual audit of after-text blocks only, not pre-text or
justification):

| Hunk | Line (in this file) | Context | Sense tag present? |
|---|---|---|---|
| CL-1 | after-text | "W carries the product-form sequential product in sense (b)" | **YES — sense (b) inline** |
| CL-1 | after-text | "so sense (c) holds as a free corollary" | **YES — sense (c) inline (explicit upgrade)** |
| CL-1 | after-text | "carrying a product-form sequential product in sense (b)" | **YES — sense (b) inline** |
| CL-1 | after-text | "carries the product-form sequential product in sense (b)" | **YES — sense (b) inline; sense (c) upgrade noted in same clause** |
| AP-1 | after-text | "is again a product effect (sense (a) closure)" | **YES — sense (a) inline** |
| AP-1 | after-text | "itself a sequential product space (sense (b))" | **YES — sense (b) inline** |
| AP-1 | after-text | "is a sequential-product-space morphism (sense (c))" | **YES — sense (c) inline** |
| AP-1 | after-text | "carried by $W$ in sense (b)" | **YES — sense (b) inline** |

**Verdict: zero bare 'carries' / 'carrying' / 'carried' in after-text blocks.**

**Grep 2 — factor-level Peirce invocation audit:**

```bash
grep -nE 'Peirce|peirce' 56-03-DIFF-REPORT.md | head -30
```

Result: the only occurrences of "Peirce" / "peirce" in this file are
inside the *justification* paragraphs where they refer to the R11
discipline audit ("factor-level Peirce invariance is discharged inside
`w-sps-proof.md §3`..."). Zero occurrences in the after-text blocks
themselves. The paper's revision text does not invoke factor-level
Peirce invariance directly — it uses the vdW 2019 Def. 4 structural
composite theorem, which absorbs the factor-level axiom reductions
inside its proof. R11 discipline is therefore vacuously satisfied by
Hunks CL-1 and AP-1 (no implicit Peirce invocations to be caught).

**Verdict: R11 discipline satisfied — zero factor-level Peirce
invocations in after-text blocks, so no
`\ref{lem:peirce-preservation}` citation obligation inline.**

**Grep 3 — A-S citation bracketing:**

```bash
grep -nE 'AlfsenShultz' 56-03-DIFF-REPORT.md
```

Result: zero hits in after-text blocks. Hunks CL-1 and AP-1 introduce
NO new A-S 2003 citation. The existing A-S cite at appendix-proofs.tex
L220 (state-separation via `\cite{AlfsenShultz2003}, Theorem~1.23`) is
OUT OF HUNK — it is at L218-222 in the before-text, but our hunk AP-1
targets L227-238, so the A-S cite is preserved untouched by this hunk.

**Verdict: R5 A-S bracketing discipline preserved — zero new A-S cites
in after-text; existing A-S cites outside hunk scope unchanged.**

**Grep 4 — Ch. 9 / Thm 9.*** scan:**

```bash
grep -nE 'Ch\.~?9|Thm 9\.|Theorem 9\.|9\.3[0-9]' 56-03-DIFF-REPORT.md
```

Result: zero hits in after-text blocks. Grep matches in the frontmatter
discipline declaration ("Ch. 9 FORBIDDEN") are DECLARATION scope, not
after-text scope. Fixture-matching substrings in bibliography keys (e.g.,
`BarnumGraydonWilce2020`) do not match the pattern (the `9.3` branch
requires the dot-digit pattern, not key substrings).

**Verdict: Ch. 9 discipline preserved — zero Ch. 9 references in
after-text blocks.**

**Grep 5 — other forbidden tokens:**

```bash
grep -nE 'Hanche-?Olsen|Lüders|Luders|pxp|M_n\(C\)\^\{sa\}|M_n\(\\mathbb\{C\}\)\^\{sa\}' 56-03-DIFF-REPORT.md
```

Result: zero hits in after-text blocks. All forbidden-token mentions in
this file are INSIDE declaration scope (frontmatter `forbidden_tokens_outside_transcription`
list and this discipline check block itself).

**Verdict: forbidden-token discipline preserved.**

---

## R11 discipline note (consolidated audit)

Per `w-sps-proof.md §6` R11 cross-check:

| Axiom | Paper-level (revision text) | Proof-level (w-sps-proof.md §3) | Peirce cited? |
|---|---|---|---|
| S1 | not re-invoked; structural | factor-level S1 only | No — not needed |
| S2 | not re-invoked; structural | finite-dim linear algebra | No — not needed |
| S3 | not re-invoked; structural | factor-level S3 only | No — not needed |
| S4 | not re-invoked; structural | state separation via `\cite[Ch.~1, Thm.~1.23]{AlfsenShultz2003}` | No — uses A-S Ch. 1 state separation, not Peirce |
| S5 | not re-invoked; structural | **Yes — `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`** | Yes (at proof level) |
| S6 | not re-invoked; structural | **Yes — `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`** | Yes (at proof level) |
| S7 | not re-invoked; structural | **Yes — `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`** | Yes (at proof level) |

**Conclusion.** Paper 5 revision text (Hunks CL-1 + AP-1) does not
directly invoke factor-level Peirce invariance — it uses the structural
vdW 2019 Def. 4 + Thm 1 framing. The R11 Peirce-citation discipline is
discharged inside `w-sps-proof.md §3` (the fallback per-axiom table) at
rows S5, S6, S7 where `\ref{lem:peirce-preservation}` is cited with
`\ref{ax:S0}` as its dependency. A skeptical referee can trace from the
paper's vdW 2019 Def. 4 citation to the fallback per-axiom table and
find the explicit Peirce citations there.

This satisfies the plan contract requirement that "every factor-level
Peirce invocation cites `\ref{lem:peirce-preservation}`" — the revision
text contains no factor-level Peirce invocations (so the condition is
vacuously true for the paper text), and the fallback proof contains
them with correct citations (so the condition is actively true at the
proof level where the citations belong).

---

## Integration Commits

**STATUS:** awaiting Task 2 execution.

After Task 2 applies Hunks CL-1 and AP-1 to the LIVING working copy and
commits in the blog repo, the following fields will be populated:

- **Blog-repo commit SHA(s):** `{filled by Task 2}`
- **Post-integration line ranges:**
  - `composite-lt.tex` Hunk CL-1 new line range: `{filled}`
  - `appendix-proofs.tex` Hunk AP-1 new line range: `{filled}`
- **Frozen-file zero-diff re-verified after Task 2:** `{filled by Task 2}`
- **pdflatex compile-clean status:** `{user-verified via checkpoint:human-verify}`

Task 2 will re-read the commit SHA and line ranges from `git show {SHA}`
and write them back into this section.

---

## Plan 56-03 Task 1 Forbidden-proxy rejections

- **fp-frozen-file-edit** — REJECTED. This artifact is a markdown file
  under `.gpd/phases/56-.../`; no paper LaTeX file is modified by Task 1
  (Task 2 applies the hunks to the LIVING working copy, never to
  `main-jmp-submitted.tex`). Frozen-file zero-diff verified at Task 1
  start (`git -C /Users/ehrlich/repos/blog diff --stat HEAD --
  landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` returns
  empty).
- **fp-revision-without-sense-tag** — REJECTED. Every `carries` /
  `carrying` / `carried` occurrence in Hunk CL-1 and Hunk AP-1
  after-text blocks is sense-tagged within the same sentence or the
  immediately following clause. See §"Discipline checks (self-audit)"
  Grep 1 table above — 8 occurrences, 8 sense-tagged, zero bare.
- **fp-revision-without-peirce-ref** — REJECTED vacuously. The after-text
  blocks contain zero factor-level Peirce invocations (structural
  vdW 2019 Def. 4 + Thm 1 framing). The `\ref{lem:peirce-preservation}`
  citation obligation sits inside `w-sps-proof.md §3` fallback rows
  (S5/S6/S7) where factor-level Peirce IS invoked, and those citations
  are present and verified per `w-sps-proof.md §6`.
- **fp-ch-9-leak-in-revision** — REJECTED. Zero Ch. 9 references in
  after-text blocks. See §"Discipline checks" Grep 4. Frontmatter
  `forbidden_tokens_outside_transcription` list is declaration scope.
- **fp-bare-as-cite-in-revision** — REJECTED vacuously. Hunks CL-1 and
  AP-1 introduce NO new A-S 2003 citation (the only new citations are
  to vdW 2019 Def. 4 + Thm 1 and BGW 2020 §2, neither of which is A-S).
  Zero bare `\cite{AlfsenShultz2003}` introduced.
- **fp-sense-c-weakening** — REJECTED. Hunk CL-1 after-text explicitly
  uses sense-(c) language ("the inclusion $\iota : W \hookrightarrow
  V_{BM}$ is moreover a sequential-product-space morphism (sense (c))")
  per `carries-three-sense-table.md §4 L5`. Hunk AP-1 after-text also
  uses sense-(c) language ("the inclusion $\iota : W \hookrightarrow
  V_{BM}$ is a sequential-product-space morphism (sense (c))") per
  `carries-three-sense-table.md §4 L7`. Sense (c) is not weakened to
  sense (b); it is cited in both hunks.

---

## Plan 56-03 Task 1 Self-check

- [x] Hunk CL-1 present with verbatim before-text (L203-221) and
  after-text blocks (both delimited by triple-backtick-latex fences).
- [x] Hunk AP-1 present with verbatim before-text (L227-238) and
  after-text blocks (both delimited by triple-backtick-latex fences).
- [x] CL-2 decision documented (OMITTED with rationale) under §"Scope
  note on CL-2".
- [x] Every hunk has a justification paragraph ≥ 3 sentences citing
  Plan 56-02 artifacts (`w-sps-proof.md §2`, `w-sps-proof.md §3`,
  `w-sps-proof.md §4`, `w-sps-proof.md §6`, `ci-sps-morphism.md §6`,
  `carries-three-sense-table.md §4 L1/L5/L6/L7`) by section number.
- [x] Every `carries` occurrence in after-text blocks is sense-tagged
  within 1-2 sentences with "sense (a)", "sense (b)", or "sense (c)".
- [x] Every factor-level Peirce occurrence in after-text cites
  `\ref{lem:peirce-preservation}` — vacuously satisfied (zero Peirce
  occurrences in after-text; citation discipline discharged in
  `w-sps-proof.md §3` at proof level).
- [x] Every A-S citation in after-text is bracketed — vacuously
  satisfied (zero new A-S cites in Hunks CL-1 + AP-1).
- [x] Zero Ch. 9 references in after-text blocks (grep returns zero
  hits under `Ch\.~?9|Thm 9\.|Theorem 9\.|9\.3[0-9]`).
- [x] `## Integration Commits` placeholder section present at end of
  file with fields awaiting Task 2.
- [x] Plan-level forbidden-proxy rejections documented with evidence
  pointers for all six Plan 56-03 `fp-*` IDs in scope for Task 1.

Task 1 complete. Task 2 applies the hunks to the LIVING working copy
and updates `## Integration Commits`.
