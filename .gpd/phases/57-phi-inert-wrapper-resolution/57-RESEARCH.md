# Phase 57: Phi Inert-Wrapper Resolution — Research

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; tracking_macro=\varphi (single existing macro — NOT \phi, NOT \Phi, NOT \widehat{\Phi}); phi_independent_results={S4 (Cor cor:S4-phi-indep), Peirce-Preservation Lemma, prop:inheritance factor-level S5/S6/S7 chain}; phi_dependent_results={mixing-function selection f=√(λμ) from faithfulness, \seqp{\varphi^{-1}(b)}{} trace-form non-degeneracy in §5 local-tomo}; frozen_submission=~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex @ tag paper5-jmp-submitted; living_copy=~/repos/blog/landing/papers/qm-from-self-modeling/main.tex (v14.0 edits applied through Phase 56)

**Researched:** 2026-04-17
**Domain:** Paper 5 (Quantum from Self-Modeling) notation audit / revision methodology / operational-QM reconstruction terminology
**Confidence:** HIGH for grep methodology, macro scope, phi-independence inheritance from Phases 54–56, taxonomy derivation, and the split-vs-standing-definition recommendation; MEDIUM for exact equivocation count and author-facing aesthetics of each draft; LOW only for whether referees will re-open already-closed sections on notation grounds (out of this phase's control).

---

## Summary

Phase 57 is a **notation-audit revision** of Paper 5 (`qm-from-self-modeling/main.tex` + 6 section files, 931 + 1883 lines total). The roadmap frames the scope as "enumerate every Φ occurrence and decide split vs standing-definition," but direct inspection of the living manuscript reveals a sharper picture: **there is exactly one phi-family macro in the source — `\varphi` — and zero occurrences of `\phi`, `\Phi`, `\widehat{\Phi}`, or `\hat{\Phi}`.** The preamble (`preamble.sty`) defines no custom phi macros. Paper 5 uses `\varphi` for the single named object "tracking isomorphism `\varphi: V_B → V_M`" (Def. `def:self-modeling-system`, clause `sms:faithful`). The "split notation Φ / φ / Φ̂" in the roadmap description is therefore a **hypothetical intervention** — an option the author is weighing — not a set of existing macros that need disambiguating.

The real phi-audit problem is **role shift of the single `\varphi` symbol across sections**, not macro proliferation. Phases 54 (Cor `cor:S4-phi-indep`), 55 (S4 phi-independence SymPy-verified symbolically in both mixing functions), and 56 (CLOSE note lines 500–511 of `alfsen-shultz-notes.md`) have all proved or affirmed that paper-surface claims are phi-independent at their respective scopes. The Phase 56 CLOSE entry explicitly names **`prop:inheritance` (factor-level S5/S6/S7 chain, `composite-lt.tex:66`) as "the primary phi-audit target"** still outstanding. Phase 57's first load-bearing task is not "find all Φ" (single-macro grep with 100 raw matches — 16 in main.tex, 2+7+2+7+13+1 across six section files — all `\varphi`), it is **classify each `\varphi` occurrence by role and detect sections where the role shifts silently**.

**Primary recommendation:** Execute a three-step audit → classify → revise pipeline:

1. **Enumerate:** run a single `ripgrep` pass `rg -nH --no-heading -e '\\varphi' -e '\\phi' -e '\\Phi' -e '\\widehat\{.*[Pp]hi.*\}' -e '\\hat\{.*[Pp]hi.*\}' main.tex sections/*.tex preamble.sty` across the paper5 directory; also scan `\newcommand` / `\DeclareMathOperator` for any hidden phi-macros. Expected raw count: ~48 `\varphi` lines; zero matches on the other patterns (per preflight). Commit the raw grep output verbatim into `phi-audit.md` §2 as the evidentiary baseline.
2. **Classify** every occurrence into the four operational roles (a)/(b)/(c)/(d) defined in §Classification Taxonomy below, using a 5-column table per occurrence: (file:line, local text, role, minimal property of `\varphi` used at this site, inherited constraint from Phase 54/55/56). Flag any row where the "minimal property" column contains more than faithfulness — those are the R8 equivocation sites.
3. **Decide revision strategy** using the diff-cost pivot rule in §Split-vs-Standing-Definition: count distinct sections with role-shift edits needed. If > 5 sections require edits, recommend **standing definition + per-section role qualifier**; else recommend **split notation with new `\varphitrack` / `\varphiinert` / `\varphianc` macros** in `preamble.sty`. Produce **both** drafts as `phi-audit.md` §5 and §6 per DERV-57-03 (author-choice deliverable).

**Predicted outcome:** Based on Phase 54 (C-i: §3.3 phi-independent via S0/Peirce-Preservation Lemma), Phase 55 (C-i: §S4 phi-independent via `cor:S4-phi-indep`), and Phase 56 (B: paper-surface phi-independent but factor-level `prop:inheritance` flagged as the primary phi-audit target), outcome **(B)** is most likely: the paper's claims survive, but the text needs 3–6 localized role-qualifier insertions + one standing definition in §2 (or its Def. `def:self-modeling-system` block). **Outcome (C) — backtracking "Φ is inert" globally — is triggered only if grep reveals a `\varphi`-dependent step** not already classified as phi-dependent by Phases 54/55/56; audit both §5 (`composite-lt.tex` lines 131–157, which uses `\varphi^{-1}` in the trace-form non-degeneracy argument) and the mixing-function selection `f = √(λμ)` (§3.4 / §`sec:sp` "Determining the Mixing Function", main.tex line 696) carefully — these are the two known phi-dependent anchors.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| **Paper 5 living `main.tex`** (`~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`, 931 lines) | Prior artifact; EDIT TARGET | The grep source per DERV-57-01 and the integration target for revision text per DERV-57-04. | Grep; quote-with-line-numbers into `phi-audit.md` §2; stage revision text for §3.4 and §5 role qualifiers if outcome (B). | Plan 57-XX grep task; revision-text tasks; RESULT.md §2/§5. |
| **Paper 5 `sections/*.tex`** (6 files: `axiom-verification.tex`, `appendix-proofs.tex`, `composite-lt.tex`, `discussion.tex`, `type-exclusion.tex`, `appendix-numerical.tex`) | Prior artifact; EDIT TARGETS (all except appendix-numerical.tex which is a table only) | Per-section files where `\varphi` appears: appendix-proofs.tex:137–200 (Cor S4-phi-indep + local-tomo trace form), composite-lt.tex:131–157 (trace form non-degeneracy), discussion.tex:471–487 (`rem:phi-inert-objection`), type-exclusion.tex:216 (def reminder), axiom-verification.tex:179–182 (`rem:S4-phi-independent`). | Grep each; table-entry per occurrence with role; stage revision text only for equivocation sites. | Plan 57-XX grep task, per-occurrence classification table, revision-text tasks. |
| **Paper 5 `preamble.sty`** | Prior artifact; EDIT TARGET only if split-notation chosen | Preamble currently defines ZERO phi macros. Split-notation draft must add `\newcommand{\varphitrack}`, `\newcommand{\varphiinert}`, `\newcommand{\varphianc}`. | Verify no hidden phi macros; stage new macros in split-notation draft only. | Plan 57-XX preamble-scan task (1 grep); split-notation revision draft in `phi-audit.md` §5. |
| **Paper 5 frozen `main-jmp-submitted.tex`** @ git tag `paper5-jmp-submitted` | Prior artifact; READ-ONLY BASELINE (MUST NOT EDIT) | The pre-revision reference for latexdiff at Phase 59. Phase 57 never touches this file. | Cite as baseline; verify zero-diff with `git -C ~/repos/blog diff --stat paper5-jmp-submitted -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` → must remain 0 changes. | Plan 57-XX frozen-file verification task (last task before RESULT.md, mirroring Phase 54/55/56 discipline). |
| **Phase 54 RESULT.md, Cor `cor:S4-phi-indep`** (C-i outcome, sealed 2026-04-16) | Hard constraint (R11 cross-phase) | Establishes that §3.3 Peirce preservation + Axiom S4 hold for any mixing function with `f(0,x)=0`, i.e., paper-surface §3.3/§S4 is phi-independent. Phase 57 must cite this corollary, not re-derive. | Read §2/§5 of `54-RESULT.md`; cite `\ref{cor:S4-phi-indep}` wherever a §3.3 or §S4 occurrence is classified as role (d) exposition shorthand. | `phi-audit.md` §4 (classification table) role-(d) justification column; revision-text cross-references. |
| **Phase 55 RESULT.md, `rem:S4-phi-independent` + SymPy Test 3** (C-i outcome, sealed 2026-04-17) | Hard constraint (R11 cross-phase) | Symbolically verified φ-independence of S4 both directions under alternative mixing `f = λ·μ` (runtime 0.3s exact). Confirms the Cor `cor:S4-phi-indep` claim in SymPy. | Cite as the SymPy-level confirmation; no new SymPy needed in Phase 57. | `phi-audit.md` §4 role-(d) justification; Phase 57 R7-absence argument (no new SymPy needed for phi-audit). |
| **Phase 56 CLOSE entry in `alfsen-shultz-notes.md`** (lines 500–511 "Phase 57 inheritance note (φ-audit)") | SHARED ARTIFACT; must NOT modify, MUST cite | Explicitly names **`prop:inheritance` factor-level S5/S6/S7 chain (`composite-lt.tex:66`) as "the primary phi-audit target"**. Phase 57 deliverable MUST audit this proposition's dependency chain specifically, not just surface occurrences. | Quote-with-line-numbers; append Phase 57 CLOSE entry at end of `alfsen-shultz-notes.md` (append-only discipline from Phase 54/55/56). | `phi-audit.md` §3 (prop:inheritance deep-dive subsection — mandatory); Phase 57 CLOSE append entry in shared artifact. |
| **`rem:phi-inert-objection`** (`discussion.tex:471–487`) | Paper 5 self-declared thesis | The paper itself claims `\varphi` is "mathematically inert in the derivation of the main theorem" and appeals to `\ref{cor:S4-phi-indep}`. Phase 57 tests whether this claim is globally sound. | Read verbatim; every role-(b)-classified occurrence must be consistent with this remark's claim, else role-(b) is wrong and the remark must be revised. | `phi-audit.md` §3 (consistency check of `rem:phi-inert-objection`); revision-text if inconsistency found. |
| **`prop:inheritance`** (`composite-lt.tex:66` + 3 consumer sites: `appendix-proofs.tex:235`, `composite-lt.tex:217`, `type-exclusion.tex:127, 246`) | Named proposition; phi-audit target per Phase 56 CLOSE | Factor-level S1–S7 inheritance of W from V_B, V_M. This is where `\varphi`'s role must be audited most carefully. | Read verbatim; classify every `\varphi` in its proof as (a)/(b)/(c)/(d); verify R8 absence. | `phi-audit.md` §3 primary audit site; possibly a role-qualifier insertion in revision text. |
| **Mixing-function selection `f=√(λμ)`** (`main.tex:~696` "Determining the Mixing Function") | Phi-dependent anchor | The ONE surface-level §3.4 result that genuinely depends on `\varphi` being a specific order isomorphism (not just any positive unital map). | Classify every `\varphi` in this §3.4 block as role (a); confirm no role (b)/(d) misclassification here. | `phi-audit.md` §4 phi-dependent roster; no revision needed if classification clean. |
| **Trace-form non-degeneracy** (`composite-lt.tex:131–157`, `appendix-proofs.tex:186–200`) | Phi-dependent anchor | The §5 local-tomography proof uses `\varphi^{-1}` explicitly in `B(a,b) = τ(a ∘ \varphi^{-1}(b))`. This is role (a). | Classify as role (a); confirm no role (d) shorthand misclassification. | `phi-audit.md` §4 phi-dependent roster. |
| **PITFALLS.md §R8** (`.gpd/research/PITFALLS.md:245–273`) | Project-level pitfall registry | Defines the exact equivocation pattern Phase 57 must avoid + prescribes phi-audit methodology. Already identifies that "phi overloading late-detected" recovery cost is 1–2 hours with symbol-rename pass. | Inherit the four-section role description (§2 map, §3 tracking, §4 inert wrapper, §5–6 reinterpreted) as Phase 57 prior hypothesis; test against actual grep output. | `phi-audit.md` §1 methodology; revision-text scope estimate. |
| **vdW 2019 Def. 2** (S1–S7 axioms, arXiv:1803.11139) | Axiom source (inherited from Phase 56) | Paper 5's axioms; S4 is where phi-independence lives (via Cor `cor:S4-phi-indep`). | Cite by Def. 2 when describing which axioms are verified phi-independently. | `phi-audit.md` §4 axiom-level phi-independence column. |
| **Hardy 2001 ancilla elimination pattern** (arXiv:quant-ph/0101012) | Precedent; critique anchor | Hardy's permutability/ancilla argument was heavily critiqued for ancilla-elimination subtleties. Phase 57 should verify Paper 5 does NOT replicate this pitfall (no ancilla hidden behind `\varphi`). | Read §6/§7 of Hardy 2001 briefly; confirm Paper 5 `\varphi` is NOT an ancilla (it is an order iso V_B→V_M, not a purifying extension). | `phi-audit.md` §1 anti-pattern section; `rem:phi-inert-objection` consistency check. |

**Missing or weak anchors:**

- **Exact role count per occurrence (48 tracked):** The raw `\varphi` count per file is established (main.tex:16; appendix-proofs.tex:7; composite-lt.tex:7; discussion.tex:13; type-exclusion.tex:1; axiom-verification.tex:2; appendix-numerical.tex:2 — total 48). Which of these are load-bearing (a/c) vs exposition (d) is **UNKNOWN until the classification task runs**. Pre-research status: weak anchor — the classification task itself produces the evidence.
- **Whether any "ancilla" usage exists in Paper 5:** Preflight grep for `ancilla|wrapper` returned **zero matches** in all 7 tex files. Role (b) "inert auxiliary wrapper / ancilla" as a roadmap category may therefore be EMPTY in Paper 5 — a potentially important finding. The `discussion.tex:471` remark uses "mathematically inert" not "ancilla." Confirm in Plan.
- **Split-notation Φ̂ macro need:** If role (b)/(c) sets are empty post-classification, the split-notation draft degenerates to `\varphi` (tracking) + optional `\varphiinert` (if any role-(b) sites exist). The roadmap's `Φ̂` (ancilla) macro is **likely unneeded**.
- **Referee-level risk of re-opening closed §3.3/§S4 on notation grounds:** OUT OF PHASE 57 CONTROL. Documented as open question §Open Questions Q3.

---

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Single phi macro in Paper 5 | `\varphi` (NO `\phi`, NO `\Phi`, NO `\widehat`) | Hypothetical: `\varphitrack`, `\varphiinert`, `\varphianc` (split-notation draft only) | `preamble.sty` inspection; `grep -c '\\phi\\|\\Phi' main.tex sections/*.tex` → 48 matches, all `\varphi` |
| Tracking map signature | `\varphi: V_B → V_M` order isomorphism | `V_M = V_B` with `\varphi = id` (shorthand specialization) | `main.tex:330, 343, 349`; clause `sms:faithful` in Def. `def:self-modeling-system` |
| Phi-independence citation | `\ref{cor:S4-phi-indep}` + `\ref{lem:peirce-preservation}` | bare `\ref{thm:S4}` (does NOT encode phi-independence; avoid) | Phase 54 RESULT §2; Phase 55 RESULT §5; `appendix-proofs.tex:137` |
| Revision target file | `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` + `sections/*.tex` (living) | `main-jmp-submitted.tex` FORBIDDEN edit target | Phase 54 RESULT §5 convention; Phase 55/56 reconfirmed |
| Bracketed A-S citations | `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` | bare `\cite{AlfsenShultz2003}` FORBIDDEN (inherited from Phase 55 R5) | Phase 55 `55-03-ADVERSARIAL-REVIEW.md` R5 |
| A-S 2003 Ch. 9 | FORBIDDEN (post-Jordan) | Ch. 1–8 pre-Jordan-legal | Phase 55 Flag 4.1 |
| Append-only shared-artifact discipline | `alfsen-shultz-notes.md` mutations = append new rows only; dated change-log entry required for any existing-row edit | silent edits FORBIDDEN | Phase 54/55/56 CLOSE entries; file footer notice |
| Sequential product notation | `a ∘ b` (Paper 5 v14.0) | `a & b` (vdW 2019 Def. 2) | inherited from Phase 54–56 |
| Compression | `C_p` (macro `\comp{p}` in preamble) | — | `preamble.sty:53` |

**CRITICAL:** Every revision-text draft must use `\varphi` (not `\phi` or `\Phi`), unless the split-notation draft is chosen, in which case the three new macros `\varphitrack` / `\varphiinert` / `\varphianc` are defined in `preamble.sty` and `\varphi` is retired from the paper entirely (the macro remains in the amssymb namespace but is no longer invoked in Paper 5 source).

Convention loading: see `.gpd/research/agent-infrastructure.md` Convention Loading Protocol (CUSTOM_CONVENTION front-matter in RESULT.md; this research file inherits from Phase 54/55/56 convention headers).

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation / Object | Name / Description | Source | Role in This Phase |
| ----------------- | ------------------ | ------ | ------------------ |
| `\varphi: V_B → V_M` order isomorphism | Tracking map, clause `sms:faithful` | `main.tex:330, 343, 349` (Def. `def:self-modeling-system`) | The ONE primitive object whose occurrences must be classified. |
| `a ∘ b = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} f(λ_i, λ_j) P_{ij}(b)` with `f(λ,μ) = √(λμ)` | General sequential product with mixing function; faithful choice | `main.tex:~696` (§3.4 "Determining the Mixing Function"); `eq:general-product` | The PHI-DEPENDENT surface result: `f = √(λμ)` is selected specifically by faithfulness of `\varphi`. Role (a) site. |
| `\ref{cor:S4-phi-indep}`: S4 holds for any `f` with `f(0,x) = 0` | Phase-54-established phi-independence of S4 | `appendix-proofs.tex:137–153` | Every §3.3 / §S4 `\varphi` occurrence classified as role (d) must cite this corollary. |
| `B(a, b) = τ(a ∘ \varphi^{-1}(b))` | Correlation bilinear form (non-degenerate iff `\varphi` is iso) | `composite-lt.tex:131`; `appendix-proofs.tex:186` | PHI-DEPENDENT §5 local-tomo result. Role (a) site; `\varphi^{-1}` is unavoidably explicit. |
| `\ref{prop:inheritance}`: S1–S7 inherited from V_B, V_M to W | Factor-level SPS inheritance (Phase 56 primary phi-audit target) | `composite-lt.tex:66`; consumers at `appendix-proofs.tex:235`, `composite-lt.tex:217`, `type-exclusion.tex:127, 246` | Phase 56 CLOSE explicitly names this as "the primary phi-audit target." EVERY `\varphi` in its proof must be classified and verified R8-absent. |
| `\varphi = id` specialization | "Without loss of generality, take `V_M = V_B` with `\varphi = id`" | `main.tex:92, 407, 410`; `discussion.tex:249` | Role (d) exposition shorthand IF and ONLY IF the specialization is justified by `\ref{cor:S4-phi-indep}`. Each occurrence must cite it or be flagged as R8 risk. |
| `rem:phi-inert-objection` | "`\varphi` does not appear as a free variable" | `discussion.tex:471–487` | Paper 5's own self-declared thesis about `\varphi`'s role. Phase 57 tests global soundness. |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Ripgrep with multiple-pattern alternation | Enumerate every `\phi`, `\Phi`, `\varphi`, `\widehat{Φ}`, `\hat{Φ}` occurrence across multi-file LaTeX document | Task 1 (grep methodology) | GNU ripgrep(1); `rg --no-heading -nH -e PAT1 -e PAT2 ...` |
| LaTeX macro-expansion audit | Scan `preamble.sty` + `\newcommand` / `\DeclareMathOperator` / `\def` for any custom phi-macro that grep on `\varphi` alone would miss | Task 1 preflight | LaTeX Companion Ch. 2 (macros); `grep -nE '\\newcommand.*[Pp]hi\|\\def.*[Pp]hi' preamble.sty` |
| Role-classification rubric (see Taxonomy below) | Assign (a)/(b)/(c)/(d) to every occurrence using textual cues + minimal-property column | Task 2 (classification) | Strunk-White rule 17 (stable referents); PITFALLS.md §R8 |
| R8 equivocation detection heuristic | Flag sections where same `\varphi` macro is used with two or more incompatible minimal properties without explicit reintroduction | Task 2b (equivocation detection) | PITFALLS.md §R8; Phase 56 CLOSE note |
| LaTeX diff-cost estimation | Count (sections-affected, lines-added, lines-deleted, `\ref` / `\eqref` churn) per revision strategy | Task 3a (diff-cost pivot) | `latexdiff` preview semantics; git `--stat` |
| Append-only shared-artifact update | Add Phase 57 CLOSE entry to `alfsen-shultz-notes.md` without modifying prior rows | Task 7 (shared-artifact append) | Phase 54 RESULT §5 convention; Phase 55/56 CLOSE precedents |
| Forbidden-proxy rejection | Reject Chiribella purification / R8-partial-fix / global-identity-assumption / rename-without-role-check patterns | All revision tasks | ROADMAP.md Phase 57 "Forbidden proxies" list |

### Approximation Schemes

| "Approximation" | When Applied | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --------------- | ------------ | ------------------ | -------------- | ----------------------- |
| Treat every `\varphi = id` occurrence as role (d) shorthand | Sections that explicitly cite `\ref{cor:S4-phi-indep}` or descend from it | Whenever `\varphi`'s specific form is unused in the surrounding argument | Zero error IF cite is in the same paragraph; LOW risk IF cite is in an adjacent paragraph; HIGH risk otherwise | Promote to role (a) and add a role qualifier |
| Treat `\varphi^{-1}` in `B(a, b) = τ(a ∘ \varphi^{-1}(b))` as role (a) | §5 local-tomography proof | Always — the inverse is explicitly needed | N/A (exact) | None needed |
| Single-macro source = single-object classification | If every occurrence resolves to the same order-iso V_B→V_M | Confirmed via classification table "minimal property" column | Risk if any occurrence requires MORE than faithfulness (e.g., specific form) | Rename that occurrence with split notation; re-audit |

---

## Standard Approaches

### Approach 1: Standing Definition + Per-Section Role Qualifier (RECOMMENDED if > 5 sections affected)

**What:** Add a single boxed definition in §2 (or within Def. `def:self-modeling-system` as a new clarifying Remark immediately after clause `sms:faithful`), stating: "Throughout this paper, `\varphi` denotes the tracking isomorphism `V_B → V_M` of Def. `def:self-modeling-system` exclusively. Occurrences appearing within proofs of φ-independent results (Cor `cor:S4-phi-indep`, Lemma `lem:peirce-preservation`) are exposition-shorthand under the faithful choice; load-bearing uses of `\varphi` are restricted to §3.4 (mixing-function selection) and §5 (trace-form non-degeneracy via `\varphi^{-1}`)." Then add a **one-sentence role qualifier** (e.g., "(φ-independent: see Cor `cor:S4-phi-indep`)" or "(φ-dependent: selects mixing function)") at the first `\varphi` in each new section/subsection that uses it.

**Why standard:** This is the minimum-diff approach. It matches Strunk-White rule 17 (stable referent) and the standard JMP/Foundations-of-Physics revision style for single-symbol papers. It preserves the `\varphi` macro throughout (zero preamble edits) and restricts source churn to (i) one boxed def/remark and (ii) one role qualifier per affected subsection.

**Track record:**
- vdW 2019 (arXiv:1803.11139) uses exactly this pattern: "the sequential product `&`" is introduced once in Def. 2, and role qualifiers ("compatible effects," "orthogonal effects") are inserted per section.
- Alfsen-Shultz 2003 uses a similar pattern for compression `c_p` — defined once in Ch. 7, role-qualified ("compression determined by p") per chapter.

**Key steps:**
1. Run grep pass per Technique §1 → raw occurrence list (expected 48).
2. Classify (a)/(b)/(c)/(d) per Taxonomy + "minimal property" column.
3. Identify sections/subsections where same `\varphi` shifts role silently → equivocation sites.
4. Author **one** boxed definition or clarifying Remark in §2 / Def. `def:self-modeling-system`.
5. Author **one role qualifier** per equivocation site (target ≤ 6 insertions based on §Summary prediction).
6. Verify every `\varphi = id` specialization cites `\ref{cor:S4-phi-indep}` in the same paragraph.
7. Generate `phi-audit.md` with full classification table + revision diff.

**Known difficulties at each step:**
- Step 2: "minimal property" column requires careful reading — what property of `\varphi` is actually used at this line? If "order iso" is used but only "positive unital map" is needed, that is NOT R8 equivocation (it is over-qualification); if "faithful specifically" is used but the argument would go through for any positive unital map, it IS R8 equivocation (understatement of the claim).
- Step 3: Silent role shift often appears at subsection boundaries; read §3.3 → §3.4 → §3.5 transitions carefully.
- Step 5: Role qualifier language must avoid implying more than the corollary proves.

### Approach 2: Split Notation `\varphitrack` / `\varphiinert` / `\varphianc` (FALLBACK if ≤ 5 sections affected AND author prefers macro-level clarity)

**What:** Define three new macros in `preamble.sty`:
```latex
\newcommand{\varphitrack}{\varphi_{\text{track}}}  % role (a): faithful tracking iso, load-bearing
\newcommand{\varphiinert}{\varphi_{\text{inert}}}  % role (b): inert wrapper (likely empty set)
\newcommand{\varphianc}{\varphi_{\text{anc}}}       % role (c): state-preparation / ancilla (likely empty)
```
Retire `\varphi` from the paper source entirely (search-and-replace every existing `\varphi` to the appropriate role-macro). Role (d) exposition shorthand gets `\varphitrack` plus the same boxed-def/remark as Approach 1.

**When to switch:** ≤ 5 sections affected AND all roles (b)/(c) have ≥ 1 occurrence (non-empty) AND author explicitly prefers macro-level clarity over minimum-diff.

**Tradeoffs vs Approach 1:**
- **Diff cost:** ~48 `\varphi` → `\varphitrack` search-and-replace lines + preamble edit. Approach 1 costs ~6 role-qualifier insertions + 1 remark. Approach 2 is ~8× larger diff.
- **`\ref` churn:** Zero (only `\varphi` itself changes; no label renames).
- **Reader cognitive load:** Approach 2 is more explicit per-occurrence; Approach 1 relies on reader remembering the standing definition. JMP referees historically prefer minimum-diff.
- **Referee-review risk:** Approach 2's large diff may re-open §3.3/§S4 (already-closed Phase 54/55) on notation grounds — a non-zero risk given the JMP revision timeline. Approach 1 minimizes this surface.

**Predicted preference:** Approach 1, UNLESS the role-(b) or role-(c) set has ≥ 3 occurrences (currently preflight = 0 for both).

### Anti-Patterns to Avoid

- **R8: Fixing one `\varphi` occurrence without checking all (forbidden proxy).** Every Phase 57 revision must be accompanied by a full classification table showing all 48 occurrences classified; revising a single occurrence without the table is the explicit R8 failure mode.
  - _Example:_ revising `discussion.tex:473` ("`\varphi` does not appear as a free variable") to "`\varphi` appears only in §3.4 mixing-function selection and §5 trace-form non-degeneracy" WITHOUT first verifying that every other `\varphi` occurrence is role (d) or cites `\ref{cor:S4-phi-indep}`.
- **Chiribella purification slippage (forbidden proxy).** Do NOT invoke Chiribella-D'Ariano-Perinotti 2011 purification postulate to argue `\varphi` is an ancilla; Paper 5 uses a strictly weaker assumption (faithful self-modeling ≠ purification). Any role-(c) "ancilla" classification must be verified to NOT import CDP's heavier structure.
  - _Example:_ arguing "`\varphi` is an ancilla preparation in §2" and citing CDP 2011 as justification — this introduces a forbidden assumption chain.
- **Global-identity assumption.** `\varphi = id` is a WLOG SPECIALIZATION (justified by `\ref{cor:S4-phi-indep}` for phi-independent results) — NOT a global claim. Revising the paper to say "`\varphi` is the identity" is a category error: `\varphi` is a generic order iso; its specialization to `id` is proof-technique, not definition.
  - _Example:_ replacing `\varphi: V_B → V_M` in Def. `def:self-modeling-system` clause `sms:faithful` with `V_B = V_M, \varphi = id` — this trivializes the definition and breaks §3.4 and §5.
- **Renaming without role-classification (forbidden proxy).** Do NOT execute the split-notation search-and-replace BEFORE the classification table is complete. The classification column IS the rename rule; without it, renaming is guesswork.
- **Re-deriving `cor:S4-phi-indep` (wasted work).** Phase 54 proved this corollary; Phase 55 SymPy-verified it. Phase 57 cites, never re-derives.
- **Editing `main-jmp-submitted.tex`.** Frozen baseline per Phase 54/55/56 discipline; every Phase 57 edit goes to the living `main.tex` and living `sections/*.tex` only.
- **Post-Jordan A-S 2003 Ch. 9 material.** Inherited from Phase 55 Flag 4.1.

---

## Classification Taxonomy (Operational Criteria for (a)/(b)/(c)/(d))

This is the core deliverable. Every `\varphi` occurrence in the paper must be classified into exactly one of four roles using the operational criteria below.

### Role (a): Self-Modeling Tracking Map B → M (LOAD-BEARING)

**Operational criterion:** The occurrence sits in a step that **would not go through** if `\varphi` were replaced by an arbitrary positive unital map without the order-isomorphism property. Specifically: the proof uses `\varphi^{-1}`, or the argument selects a specific property of `\varphi` (e.g., faithful selects `f = √(λμ)` via `f(\varphi(p)) = \varphi(f(p))`), or the conclusion changes if faithfulness is weakened.

**Textual cues:**
- "the tracking isomorphism `\varphi`" (main.tex:330; composite-lt.tex:144)
- "`\varphi^{-1}: V_M → V_B`" (appendix-proofs.tex:190; composite-lt.tex:133)
- "faithful self-modeling" in the same sentence as `\varphi`
- "`\varphi` provides [property]" where [property] is used in the next step (main.tex:400, 792; discussion.tex:109)

**Pre-audit predicted count:** ~8–12 occurrences, concentrated in:
- Def. `def:self-modeling-system` (main.tex:330, 343, 349, 400) — 4 occurrences
- §3.4 mixing-function selection (main.tex:~700) — 2–4 occurrences (pending grep)
- §5 trace-form non-degeneracy (composite-lt.tex:131–157; appendix-proofs.tex:186–200) — 6–8 occurrences

**Revision action:** Keep as `\varphi`; no role qualifier needed (role (a) is the default).

### Role (b): Inert Auxiliary Wrapper / Ancilla (LIKELY EMPTY)

**Operational criterion:** The occurrence is used in a role equivalent to an ancilla preparation (Hardy 2001 style) — a system adjoined for computational convenience whose state does not affect the outcome. A wrapper that could be removed without changing the conclusion.

**Textual cues:**
- "ancilla" (preflight grep: **zero matches**)
- "wrapper" (preflight grep: **zero matches**)
- "adjoined system"
- "auxiliary system"

**Pre-audit predicted count:** **ZERO.** Paper 5 does not use ancilla formalism. The "inert" language in `rem:phi-inert-objection` refers to role (d) (exposition shorthand in a phi-independent proof), not role (b).

**Revision action:** If the audit confirms zero occurrences, explicitly document "role (b) is empty in Paper 5" in `phi-audit.md` §4 and recommend the split-notation draft (Approach 2) OMIT the `\varphianc` macro.

**Important distinction:** "Inert" as a descriptor in `rem:phi-inert-objection` ≠ role (b). The remark's "inert" means "not a free variable in the main theorem," which is role (d) per Phase 54/55. Classifying it as role (b) would be a category error.

### Role (c): State-Preparation Notation (LIKELY EMPTY)

**Operational criterion:** The occurrence denotes a specific state (not a map) or a preparation procedure. E.g., `\varphi \in V_M^+` as a density.

**Textual cues:**
- "`\varphi` is a state"
- "the state `\varphi`"
- "prepare `\varphi`"
- `\varphi \in V^+` or `\varphi(p) \geq 0` used as a state-positivity condition

**Pre-audit predicted count:** **ZERO.** Paper 5 uses `\varphi` exclusively as a MAP (V_B → V_M), never as a state. Preflight inspection of all 48 occurrences confirms map-typing throughout.

**Revision action:** If the audit confirms zero occurrences, explicitly document "role (c) is empty in Paper 5" in `phi-audit.md` §4.

### Role (d): Exposition Shorthand — Phi-Independent Context (EXPECTED DOMINANT)

**Operational criterion:** The occurrence sits in a step that would go through for ANY positive unital map `\varphi` satisfying minimal conditions (typically `\varphi(0) = 0` plus some regularity). The phi-independence is already proved elsewhere (Cor `cor:S4-phi-indep`, Lemma `lem:peirce-preservation`, etc.); `\varphi` appears only because the surrounding context is "a self-modeling system" and the proof-writing convention is to carry the triple `(V, \varphi, V_{BM})` even when the specific `\varphi` is unused.

**Textual cues:**
- "`\varphi = id`" specialization (main.tex:92, 407, 410; discussion.tex:249) — role (d) IF `\ref{cor:S4-phi-indep}` or equivalent is cited in the same paragraph
- `\varphi` appears in a theorem statement whose proof does NOT reference `\varphi` beyond the definition
- `\varphi`-independence is proved at the cited result (e.g., axiom-verification.tex:179 `rem:S4-phi-independent`)

**Pre-audit predicted count:** ~30–40 occurrences (majority of the 48 total).

**Revision action (Approach 1):** At the FIRST role-(d) occurrence in each affected section/subsection, insert a **one-sentence role qualifier** citing the phi-independence result. E.g.:
> "Here `\varphi` plays a role that is ultimately exposition-only: the argument below is `\varphi`-independent by Corollary `cor:S4-phi-indep`."

Subsequent role-(d) occurrences in the same subsection do NOT need individual qualifiers.

### R8 Equivocation Detection Heuristic

**Heuristic:** Build a table with columns [file:line, role (a/b/c/d), minimal property of `\varphi` used here, cite of phi-independence result if role (d)]. An R8 equivocation is **any pair of rows** within the same subsection where:
1. Both rows are role (d), BUT
2. The "minimal property" columns are incompatible (e.g., row 1 needs only "positive unital"; row 2 silently needs "order iso"), AND
3. No explicit reintroduction of `\varphi` occurs between them.

OR:

1. Row N is role (a) (load-bearing) and row N+1 is role (d) (shorthand),
2. No subsection boundary or cite of phi-independence result occurs between them.

OR:

1. A role-(d) occurrence's phi-independence cite is MISSING or STALE (cites `\ref{thm:S4}` instead of `\ref{cor:S4-phi-indep}`).

**Expected equivocation sites (pre-audit hypotheses):**
- **`discussion.tex:471–487` `rem:phi-inert-objection`** — the remark's "`\varphi` does not appear as a free variable" claim must be tested globally. If it is FALSE globally (e.g., §5 trace-form non-degeneracy uses `\varphi^{-1}` as a non-trivial free variable), the remark's claim is over-stated and needs revision to "`\varphi` does not appear as a free variable in the proofs of §3.3 / §S4 / §Axiom verification."
- **§3.4 "Determining the Mixing Function"** (main.tex:~696–792) — this is the phi-dependent section; every `\varphi` here is role (a). Any role (d) classification here would be a category error.
- **§5 local-tomography** (composite-lt.tex:131–157) — `\varphi^{-1}` is role (a); surrounding `\varphi` mentions must be consistent.
- **`prop:inheritance`** (composite-lt.tex:66) — Phase 56 CLOSE explicitly flags as primary phi-audit target; audit its proof's `\varphi` usage carefully.

**Expected non-equivocation sites (pre-audit hypotheses):**
- Def. `def:self-modeling-system` (main.tex:330, 343, 349) — clean role (a) definition.
- `cor:S4-phi-indep` (appendix-proofs.tex:137) — definitionally phi-independent.
- `rem:S4-phi-independent` (axiom-verification.tex:179) — paraphrase of the corollary; clean role (d).

---

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| **Cor `cor:S4-phi-indep`**: S4 holds for any `f` with `f(0,x) = 0` | "Axiom S4 holds for the sequential product `eq:general-product` with any mixing function `f` satisfying `f(0, x) = 0` for all `x ∈ [0,1]`, not only the faithful choice `f = √(λ_i λ_j)`." | `appendix-proofs.tex:137–153`; Phase 54 RESULT §2 | Cite in every role-(d) justification for a §3.3 or §S4 occurrence. |
| **Lemma `lem:peirce-preservation`** (Phase 54 C-i) | Three-part propositions 3.1, 3.2, 3.3 with R3 cross-term case | Phase 54 RESULT §2; `main.tex:~540` (post-Phase-54 integration) | Cite for Peirce-invariance of `L_a`; phi-independent. |
| **`rem:S4-phi-independent`** | "Axiom S4 is `\varphi`-independent: it holds for \emph{any} mixing..." | `axiom-verification.tex:179–182` (added in Phase 55 integration) | Reader-facing paraphrase of `cor:S4-phi-indep`; cite alongside the corollary. |
| **Phase 55 SymPy Test 3** | Forward+reverse S4 verified with alternative mixing `f = λ·μ`, both directions symbolically zero | Phase 55 RESULT §6; `derivations/paper5-peirce-preservation/s4-sympy-spot-check.py` | Cite as existing computational verification; Phase 57 needs NO new SymPy. |
| **`rem:phi-inert-objection`** | "In the derivation of the main theorem, the tracking map `\varphi` does not appear as a free variable..." | `discussion.tex:471–487` | Paper 5's own self-declared thesis. Audit its truth globally; revise if scope is overclaimed. |
| **vdW 2019 Def. 2** (S1–S7 verbatim) | See Phase 56 RESEARCH §"vdW 2019 Definition 2 — S1–S7 axioms" | arXiv:1803.11139 p. 3 | S4 is where phi-independence lives; cite Def. 2 when describing axioms. |

**Key insight:** Phase 57 is entirely a NOTATION and REVISION-TEXT audit. Every mathematical claim about phi-dependence or phi-independence is already decided by Phases 54/55/56. Phase 57 must never re-prove — only cite and classify. Attempting to re-derive even one of these is wasted context budget and risks introducing notation conflicts.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `\varphi = id` WLOG reduction | Safe specialization in any phi-independent proof | `main.tex:92, 407, 410; discussion.tex:249` | Must cite `\ref{cor:S4-phi-indep}` in same paragraph for role (d) classification |
| Phase 56 CLOSE "Phase 57 inheritance note" | Explicit roadmap of what Phase 57 must audit | `alfsen-shultz-notes.md:500–511` | Names `prop:inheritance` as primary target |
| Phase 55 F3 non-blocking caveat (`55-RESULT §7`) | Phase 57 inherits the same S0 + Peirce-Preservation Lemma pattern | Phase 55 RESULT Section 7, row F3 | R11 cascade tracker |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| Hardy 2001 "Quantum Theory from Five Reasonable Axioms" | L. Hardy | 2001 | Ancilla elimination pattern; role-(b) precedent in QM reconstruction | Verify Paper 5 does NOT replicate Hardy's permutability-ancilla argument; `\varphi` is NOT an ancilla |
| Chiribella-D'Ariano-Perinotti 2011 purification | G. Chiribella, G.M. D'Ariano, P. Perinotti | 2011 | FORBIDDEN PROXY — purification is strictly heavier than Paper 5's faithful self-modeling | Do NOT invoke; reject CDP-style purification as justification for any role-(c) classification |
| Barnum-Wilce 2014 "Local Tomography and the Jordan Structure of Quantum Theory" | H. Barnum, A. Wilce | 2014 | Qubit-subsystem approach; phi-like map handling | Contrast with Paper 5's `\varphi`; BW use subsystem inclusion, not tracking iso |
| Masanes-Müller 2011 "A derivation of quantum theory from physical requirements" | L. Masanes, M.P. Müller | 2011 | Composite-assumption treatment; phi-less reconstruction | Benchmark: how to write reconstruction without introducing a `\varphi` at all |
| Masanes-Galley-Müller 2019 "The measurement postulates of quantum mechanics are operationally redundant" | L. Masanes, T.D. Galley, M.P. Müller | 2019 | Standing-definition methodology example | Cite as Approach 1 precedent (standing def + per-section qualifier) |
| van de Wetering 2019 "An effect-theoretic reconstruction of quantum theory" | J. van de Wetering | 2019 | Paper 5 primary anchor; sequential product formalism | `&` introduced once in Def. 2 + role qualifiers per section → Approach 1 precedent |
| Alfsen-Shultz 2001 vol. 179 / 2003 vol. 190 | E.M. Alfsen, F.W. Shultz | 2001/2003 | Compression `c_p` — single-symbol-with-role-qualifier style | Approach 1 precedent; Paper 5 inherits citation discipline from Phase 55 |
| Gudder-Greechie 2002 "Sequential products on effect algebras" | S. Gudder, R. Greechie | 2002 | Counterexample source; Example 39 non-EJA associative SP | Not directly relevant to Phase 57, but inherited from Phase 56 context |

---

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| `ripgrep` (`rg`) | ≥ 13.0 (shipped macOS Homebrew) | Multi-pattern `\phi` / `\Phi` / `\varphi` / `\widehat` / `\hat` / `\newcommand` enumeration across main.tex + sections/*.tex + preamble.sty | Faster than GNU grep; ships with PCRE2; supports `-e PAT1 -e PAT2` alternation; `-nH --no-heading` for table-ready output |
| `grep -nE` (POSIX extended regex) | macOS/BSD grep or GNU grep | Fallback for CI or environments without `rg`; identical output shape with `-n -E` | Ubiquitous; requirements pin `grep -n "\\\\phi\\|\\\\Phi"` literally in DERV-57-01 |
| `git diff` | system git | LaTeX diff size estimation per revision draft; verify `main-jmp-submitted.tex` zero-diff discipline (inherited from Phase 54/55/56) | Standard CI/review tool |
| `git log -p` | system git | Cross-reference prior `\varphi` edits (Phase 54/55 integration commits) to check for patterns | Standard |
| Python 3 (for optional line-number reconciliation) | 3.10+ | If classification table exceeds ~50 rows, a small `py-parse.py` helper can reconcile `rg` output → CSV → markdown table | Standard scripting; no new deps |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| `wc -l` | Count lines per .tex file for scope estimation | Plan-time scope check; RESULT §2 line-count column |
| `texcount` (optional) | LaTeX word/equation counts per section — sanity-check revision-text size | Phase 57 final task; verify revision text is "substantive" (inherit Phase 54 R4 floor-20-lines discipline) |
| `latexdiff` (NOT REQUIRED for Phase 57) | PRE-FLIGHT for Phase 59 only | **Do NOT install in Phase 57.** `latexdiff` is a Phase 59 prerequisite per ROADMAP Wave 4 scope. Phase 57 recommends the user `brew install latexdiff` at Phase 59 start, not at Phase 57. |
| `tectonic` or `pdflatex` | Post-revision compile check | Inherited Phase 55 F5 discipline — static verification in Phase 57 plan tasks; full compile is user-side action |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| `ripgrep` | GNU `grep -rn` | `rg` handles multi-pattern alternation cleanly with `-e`; POSIX grep needs awkward `\|` escaping. Both acceptable. |
| Manual classification table | LLM-assisted classification (self-draft) | LLM risks hallucinating minimal-property column; **manual classification is the recommended approach** for this audit. Phase 57 is small enough (48 rows) that manual is feasible and more rigorous. |
| Three new split-notation macros in preamble | Inline `\varphi_{\text{track}}` / `\varphi_{\text{inert}}` strings | Macros reduce search-and-replace churn and let the author flip between drafts by changing one macro body. Preamble macros RECOMMENDED for Approach 2. |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| `rg -e '\\varphi' -e '\\phi' -e '\\Phi' main.tex sections/*.tex preamble.sty` | < 50 ms | None | — |
| Manual classification of 48 rows | 30–60 min | Reading minimal-property context | Use classification rubric in §Taxonomy; process by file in sequence |
| Author both revision drafts (Approach 1 + Approach 2) | 1–2 hours | Writing per-section role qualifiers and preamble macros | Use Approach 1 template; Approach 2 is mostly mechanical sed |
| `main-jmp-submitted.tex` zero-diff verify | < 1 s | — | `git -C ~/repos/blog diff --stat paper5-jmp-submitted -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` → 0 |
| `phi-audit.md` produce (~400 lines projected) | 30 min | Writing section-by-section review + revision-text staging | Follow `phi-audit.md` structure in §Validation Strategies below |
| Append Phase 57 CLOSE to `alfsen-shultz-notes.md` | < 10 min | Append-only discipline | Mirror Phase 55 / Phase 56 CLOSE entry format (see `alfsen-shultz-notes.md:397–533`) |

**Installation / Setup:**
```bash
# Phase 57 needs no new packages. ripgrep ships with most dev setups.
# If ripgrep is not installed:
brew install ripgrep    # macOS (user-side; agent does NOT silently install)

# Phase 59 pre-flight (NOT PHASE 57):
# brew install latexdiff    # Phase 59 ONLY; mention in phi-audit.md §7 for user-side action
```

---

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| **Grep-count reconciliation** | Classification table covers every raw grep occurrence | `rg -cnH '\\varphi\|\\phi\|\\Phi' main.tex sections/*.tex` → must equal sum of rows in `phi-audit.md` classification table | 48 total = 16 + 2 + 7 + 2 + 7 + 13 + 1 per file (preflight) |
| **Role-coverage exhaustiveness** | Every row classified (a)/(b)/(c)/(d) with zero NULLs | Table column "role" has no blanks | 100% coverage; ≤ 2 rows flagged as "author-judgment needed" per DERV-57-01 |
| **R8 equivocation absence** | No within-subsection silent role shifts | Apply R8 heuristic per §Taxonomy; flag all candidate sites | ≤ 6 flagged sites (predicted; may be fewer) |
| **`rem:phi-inert-objection` global soundness** | Remark's claim "`\varphi` does not appear as a free variable in the main theorem" matches role-(a) roster | Audit role-(a) rows; confirm all are inside §3.4 (mixing-function) or §5 (trace-form), NOT inside the main-theorem statement itself | Claim SURVIVES (main theorem is defined via `\ref{thm:main}` at `main.tex:~84–101`; its statement and proof cite `\varphi` only in the definition-reference sense, role (d)) |
| **Phase 54/55/56 inheritance** | Phase 57 cites, never re-derives | Every role-(d) cite resolves to `\ref{cor:S4-phi-indep}` or `\ref{lem:peirce-preservation}` | Zero re-derivations of phi-independence results |
| **Frozen-file zero-diff** | `main-jmp-submitted.tex` untouched | `git -C ~/repos/blog diff --stat paper5-jmp-submitted` | 0 changes |
| **Append-only shared artifact** | `alfsen-shultz-notes.md` Phase 57 CLOSE is append, not modification | `git diff alfsen-shultz-notes.md` shows only `+` lines in Phase 57 region | Every diff line is `+` in the Phase 57 entry |
| **Forbidden-proxy rejection** | Neither Chiribella purification nor R8-partial-fix nor global-identity-assumption invoked | Text-search `phi-audit.md` + revision drafts for keywords: `purification`, `Chiribella`, `\varphi = id` without `\ref{cor:S4-phi-indep}` adjacent | Zero forbidden-proxy hits |
| **Split-notation macro coverage** (Approach 2 only) | Every `\varphi` in the source replaced with role-macro | After search-and-replace, `grep -c '\\varphi[^a-z]' main.tex sections/*.tex` → 0 | 100% replacement |
| **Axiom scope check** | No Ch. 9 A-S material or post-Jordan argument introduced | `grep -nE 'Ch\.~?9\|Theorem~?9\.' phi-audit.md revision-drafts` → 0 | 0 Ch. 9 references (Phase 55 Flag 4.1 inherited) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| Phi-independent proof length | §3.3 Peirce-Preservation Lemma, §S4 full, Cor `cor:S4-phi-indep` | Established and SymPy-verified symbolically | Phase 54 RESULT §2, §4; Phase 55 RESULT §6 |
| Phi-dependent proof length | §3.4 mixing-function selection + §5 local-tomography trace-form | Known surface-level phi-dependence | `main.tex:~696–829`, `composite-lt.tex:131–157` |
| Maximum equivocation sites | Per PITFALLS.md §R8 recovery | "Symbol-rename pass; ~1–2 hours" cost if late-detected | PITFALLS.md §R8 recovery row |
| Outcome decision pivot | Split vs standing-def threshold | > 5 sections ⟹ standing-def; ≤ 5 ⟹ split OK | Backtracking rule in Phase 57 description |

### Red Flags During Computation

- **Preflight grep returned zero `\Phi` or `\phi` matches but classification table row count ≠ 48.** Counts mismatch ⟹ either hidden macro not enumerated OR miscounted; stop and re-grep with broadened patterns.
- **Any classification row's "minimal property" column says "ancilla" or "purification."** Forbidden-proxy hit; re-examine the line — Paper 5 does not use ancilla formalism.
- **Any `\varphi = id` specialization occurs without `\ref{cor:S4-phi-indep}` or equivalent citation in the same paragraph.** R8 equivocation risk; this is the highest-probability bug-site.
- **`rem:phi-inert-objection` classification says "true globally" but role-(a) roster includes `\varphi^{-1}` in §5.** `rem:phi-inert-objection` scope is narrower than claimed; remark needs revision to restrict to main-theorem-statement scope.
- **Revision draft introduces a new role not in {(a), (b), (c), (d)}.** Taxonomy is over-specified or new semantic role needed; if so, ESCALATE to `gpd:discuss-phase` — do NOT silently add a role.
- **`prop:inheritance` audit finds a load-bearing `\varphi` step not yet classified as role (a) by Phase 56.** Phase 56 CLOSE scope is tighter than thought; escalate — Phase 56 RESULT may need reopening.
- **Phase 57 CLOSE append to `alfsen-shultz-notes.md` modifies a prior row.** Append-only discipline violation; revert and re-append.

### `phi-audit.md` Structure (DERV-57-01 DELIVERABLE)

This is the mandatory output structure the planner must enforce for `phi-audit.md`:

```markdown
# Phi Audit — Paper 5 `\varphi` Occurrence Classification

**Consumed by:** Phases 54, 58, 59 (per DERV-57-01)
**Produced in:** Phase 57 (sealed 2026-04-XX)
**Frozen reference:** `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` @ tag paper5-jmp-submitted
**Living editable copy:** `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` + sections/*.tex

## §1. Methodology

[Grep command used; preamble.sty scan result; 4-role taxonomy summary; R8 heuristic]

## §2. Raw Grep Output (Evidentiary Baseline)

[Commit the full `rg -nH` output verbatim; ~48 lines]

## §3. `prop:inheritance` Deep-Dive (Phase 56 CLOSE primary target)

[Per-step audit of composite-lt.tex:66 proposition and its 3 consumer sites]

## §4. Per-Occurrence Classification Table

| # | File:line | Local Text (excerpt) | Role (a/b/c/d) | Minimal property used | Phi-indep cite | R8 equivocation? |
|---|-----------|----------------------|-----------------|-------------------------|------------------|-------------------|
| 1 | main.tex:92 | "take $\varphi = \mathrm{id}$..." | d | f(0,x)=0 | cor:S4-phi-indep | NO |
| 2 | main.tex:330 | "positive unital map $\varphi: V_B \to V_M$ (the tracking isomorphism)" | a | full definition | — | NO |
| ... | ... | ... | ... | ... | ... | ... |
| 48 | appendix-numerical.tex:52 | "multiple $\varphi$ choices" | d | f(0,x)=0 | cor:S4-phi-indep | NO |

## §5. Approach 1 Draft — Standing Definition + Per-Section Role Qualifier

[Verbatim LaTeX revision text for each affected section]

## §6. Approach 2 Draft — Split Notation (\varphitrack / \varphiinert / \varphianc)

[Verbatim preamble.sty edit + per-file search-and-replace rule]

## §7. Author Decision Pivot

[If > 5 sections affected ⟹ recommend Approach 1; else recommend Approach 2]

## §8. Consistency Check

[Grep-count reconciliation; R8 equivocation absence; frozen-file zero-diff; forbidden-proxy rejection]

## §9. Downstream Consumer Hand-Off

[Phase 54 status; Phase 58 inheritance note; Phase 59 latexdiff preparation note]
```

---

## Common Pitfalls

### Pitfall R8: Fixing One `\varphi` Occurrence Without Checking All

**What goes wrong:** Paper 5's `\varphi` appears 48 times across 7 files. A revision that fixes one occurrence (e.g., edits `rem:phi-inert-objection`) without first producing the full classification table is the R8 failure mode. Consequence: inconsistent role assignments silently persist; referee correctly identifies at line Y that "the inert wrapper claim conflicts with the `\varphi^{-1}` usage at line X."

**Why it happens:** Temptation to jump directly to revision text before the classification table is complete. The roadmap's "revision text for each affected Paper 5 section" (DERV-57-04) can be misread as "start editing" instead of "start editing AFTER the table."

**How to avoid:** Plan 57 TASK ORDER MUST BE: (1) grep → (2) classify → (3) audit `prop:inheritance` → (4) detect R8 equivocations → (5) decide pivot → (6) author BOTH drafts → (7) revision-text integration → (8) shared-artifact append. Steps 6–7 MUST NOT start until step 4 is complete. Enforce via plan-checker.

**Warning signs:** A plan task that edits `sections/*.tex` before `phi-audit.md` classification table is populated.

**Recovery:** Revert the premature edit; regenerate the classification table; re-plan.

### Pitfall R8b: Chiribella Purification Slippage

**What goes wrong:** Classifying a `\varphi` occurrence as role (c) "ancilla" and citing CDP 2011 purification as justification. This imports a structurally heavier assumption (purification) than Paper 5 uses (faithful self-modeling ≠ purification).

**Why it happens:** "Ancilla" is a familiar QM-reconstruction term; the easiest way to justify an ancilla formalism is via CDP purification.

**How to avoid:** Preflight confirmation that Paper 5 has ZERO "ancilla" / "wrapper" / "auxiliary system" language (verified). Reject any Phase 57 classification that attempts to introduce these terms.

**Warning signs:** Revision draft or `phi-audit.md` contains the string `purification`, `Chiribella`, `CDP`, or `ancilla` (beyond "is NOT an ancilla" rejections).

**Recovery:** Reclassify the flagged occurrence as role (d) if phi-independent, or role (a) if phi-dependent; remove all CDP citations.

### Pitfall R8c: Global-Identity Assumption

**What goes wrong:** Revising Def. `def:self-modeling-system` to state "`V_M = V_B`, `\varphi = id`" globally. This trivializes the definition — the tracking isomorphism is generic; its specialization is a proof technique, not a definition.

**Why it happens:** The WLOG `\varphi = id` specialization is used in `main.tex:92, 407, 410; discussion.tex:249`. Misreading these as global claims rather than local specializations.

**How to avoid:** Every `\varphi = id` occurrence must remain a LOCAL specialization with a citation to `\ref{cor:S4-phi-indep}` (or equivalent) in the same paragraph. No global identification in Def. `def:self-modeling-system`.

**Warning signs:** Revision draft modifies Def. `def:self-modeling-system` clause `sms:faithful` to collapse V_B and V_M.

**Recovery:** Restore original definition; move the WLOG reduction to the proof (or remark) where it is actually used.

### Pitfall R8d: Renaming Without Role-Classification Exhaustiveness

**What goes wrong:** Executing the split-notation search-and-replace (Approach 2) before the classification table is complete. Result: some occurrences mapped to wrong macro; role-(b) / role-(c) sets may be empty but macros defined anyway.

**Why it happens:** sed/rg text replacement is faster than careful classification; shortcut tempting.

**How to avoid:** Plan task order enforces classification-before-rename. Approach 2 draft requires the classification table as its INPUT (not output).

**Warning signs:** Approach 2 preamble edit committed before `phi-audit.md` §4 table is populated.

**Recovery:** Revert preamble edit; regenerate table; re-author Approach 2 from the table.

### Pitfall R8e: Re-Deriving `cor:S4-phi-indep`

**What goes wrong:** Phase 57 plan includes a task to re-prove or re-verify phi-independence of S4. Wasted context budget; risks introducing a second proof that conflicts with the Phase 54 original.

**Why it happens:** Temptation to "double-check" Phase 54's result.

**How to avoid:** Phase 57 is a PURE NOTATION AUDIT — cite Phase 54 RESULT and Phase 55 SymPy verification; do not re-derive anything.

**Warning signs:** Plan task includes a SymPy or proof-writing step that attempts to re-verify `cor:S4-phi-indep`.

**Recovery:** Replace the re-derivation task with a cite-only task.

### Pitfall R8f: Editing `main-jmp-submitted.tex`

**What goes wrong:** The frozen baseline is modified, breaking the Phase 59 latexdiff.

**Why it happens:** Editor default to most-recently-opened file; inheritance from Phase 54/55/56 R1 discipline.

**How to avoid:** Every Phase 57 task specifies edit target as living `main.tex` + `sections/*.tex`; final consistency check verifies `git diff --stat paper5-jmp-submitted -- main-jmp-submitted.tex` → 0.

**Warning signs:** `git status` shows changes in `main-jmp-submitted.tex`.

**Recovery:** `git checkout paper5-jmp-submitted -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex`; re-verify zero-diff.

### Pitfall: Post-Jordan A-S 2003 Ch. 9 Citation

Inherited from Phase 55 Flag 4.1. Any Phase 57 revision text citing Ch. 9 is forbidden. Use Ch. 1–8 only.

---

## Level of Rigor

**Required for this phase:** Audit-level with explicit exhaustiveness. Every one of ~48 `\varphi` occurrences must be classified; equivocation detection must cover every within-subsection role-shift pattern; forbidden proxies must be explicitly rejected with text evidence.

**Justification:** Phase 57 is the LAST notation-level phase before the Lean axiom audit (Phase 58) and the final latexdiff (Phase 59). A missed equivocation here cascades: Phase 58's axiom-to-citation cross-check will re-surface it (at higher cost), Phase 59's latexdiff will expose it to the referee (at highest cost). Exhaustiveness here is cheaper than late-detection.

**What this means concretely:**
- Every row in the classification table has all 6 columns filled (no NULLs).
- Every role-(d) classification has a `\ref{cor:S4-phi-indep}` (or equivalent) citation in the "phi-indep cite" column.
- Every forbidden-proxy is explicitly rejected in `phi-audit.md` §8 (zero keyword hits confirms absence).
- `prop:inheritance` factor-level chain audited line-by-line (Phase 56 CLOSE primary target).
- `main-jmp-submitted.tex` zero-diff verified at Phase 57 close.
- Both revision drafts (Approach 1 + Approach 2) are complete — no "author choice" means skip one.
- Shared-artifact `alfsen-shultz-notes.md` appends Phase 57 CLOSE entry mirroring Phase 55/56 format.

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Submitted-era §3.3 Peirce-invariance hand-wave (`main.tex` pre-Phase-54 lines 524–544) | Phase 54 C-i: S0 axiom + Peirce-Preservation Lemma | 2026-04-16 (Phase 54 close) | Paper-surface §3.3 is phi-independent via Cor `cor:S4-phi-indep` |
| Submitted-era §S4 Theorem 9.37 invocation (axiom-verification.tex:125, post-Jordan-illegal) | Phase 55 C-i: `\ref{ax:S0}` + `\ref{lem:peirce-preservation}` + `\cite[Ch.~7]{AlfsenShultz2003}` | 2026-04-17 (Phase 55 close) | §S4 phi-independence symbolically verified under alternative mixing |
| Submitted-era §5 upper-bound hand-wave ("W carries the product-form SP") | Phase 56 B: structural vdW 2019 Def. 4 + Thm 1 + `\ref{prop:inheritance}` | 2026-04-17 (Phase 56 close) | §5 paper-surface is phi-independent; factor-level `prop:inheritance` flagged as Phase 57 target |
| Single `\varphi` macro playing all roles implicitly | Phase 57 (this phase): explicit role classification + either standing-def+qualifier OR split-notation | 2026-04-XX (Phase 57 pending) | Reader/referee can immediately verify which `\varphi` is load-bearing vs exposition |
| `\varphi = id` WLOG specialization scattered without explicit cite | Phase 57: every specialization paragraph cites `\ref{cor:S4-phi-indep}` or equivalent | 2026-04-XX (Phase 57 pending) | R8 equivocation risk eliminated |

**Superseded approaches to avoid:**
- **Hardy 2001 permutability/ancilla pattern:** Do NOT classify any `\varphi` as "ancilla" in role (c). Paper 5 does not use ancilla formalism; Hardy's ancilla-elimination subtleties do not apply.
- **Pre-Phase-54 §3.3 Peirce-invariance argument:** Cite Phase 54 RESULT + Lemma `lem:peirce-preservation`; do NOT invoke the submitted-era hand-wave.
- **Pre-Phase-55 §S4 Theorem 9.37 invocation:** Post-Jordan-illegal; use Prop 7.43 + S0 + Prop 7.50 chain.

---

## Open Questions

1. **Q1: What is the exact equivocation count after classification?**
   - What we know: Preflight predicts 3–6 sites based on `rem:phi-inert-objection` scope claim vs §5 `\varphi^{-1}` usage, plus the `\varphi = id` specializations (main.tex:92, 407, 410; discussion.tex:249), plus `prop:inheritance` factor-level chain.
   - What's unclear: Whether each specialization cites `\ref{cor:S4-phi-indep}` adjacently (if not, it is R8 equivocation).
   - Impact on this phase: Determines split-vs-standing-def pivot. > 5 ⟹ standing-def; ≤ 5 ⟹ either.
   - Recommendation: Plan the grep+classify tasks as a single block BEFORE the decision task; do not attempt to pre-commit to an approach.

2. **Q2: Does `prop:inheritance` (composite-lt.tex:66) actually have a `\varphi`-dependent step in its proof?**
   - What we know: Phase 56 CLOSE names it "the primary phi-audit target" but does not pre-classify its internal `\varphi` usages.
   - What's unclear: If the proof uses `\varphi` only through Peirce-Preservation Lemma (phi-independent), then `prop:inheritance` is fully phi-independent and needs only a role-qualifier. If it uses a `\varphi`-specific property, it becomes a role-(a) site and may require structural revision.
   - Impact: May shift phase outcome from (B) to (C-i) or (C-ii) if structural revision needed.
   - Recommendation: Plan a dedicated task for the `prop:inheritance` deep-dive BEFORE the classification table. This is the highest-uncertainty node.

3. **Q3: Will the referee re-open Phases 54/55/56 on notation grounds?**
   - What we know: JMP referee has seen submitted-era `main-jmp-submitted.tex`; Phase 57 revisions are outside their initial scope.
   - What's unclear: Whether notation-only revisions reset the review clock on affected sections.
   - Impact: OUT OF PHASE 57 CONTROL. But it does favor Approach 1 (minimum-diff) over Approach 2 (48 search-and-replace lines).
   - Recommendation: Document as open question; recommend Approach 1 for minimum referee-surface.

4. **Q4: Is the `\varphi = id` WLOG reduction ever used INSIDE a proof whose conclusion depends on it?**
   - What we know: Two distinct usage patterns: (i) for illustration ("take `\varphi = id` for concreteness"); (ii) for WLOG simplification ("WLOG `\varphi = id` by Cor `cor:S4-phi-indep`").
   - What's unclear: If any occurrence is (ii) but the cite is absent, that is R8.
   - Impact: Determines role-(d) vs R8-equivocation classification per occurrence.
   - Recommendation: Classification table "minimal property" column must distinguish (i) from (ii); R8 flag applies to (ii)-without-cite.

5. **Q5: Does `rem:phi-inert-objection` overclaim its scope?**
   - What we know: The remark claims `\varphi` "does not appear as a free variable" in the derivation of the main theorem. The main theorem is `\ref{thm:main}` at main.tex ~84.
   - What's unclear: Does the main theorem's proof (via `\ref{sec:sp}` + `\ref{sec:self-modeling}`) hit §5 local-tomo? If yes, `\varphi^{-1}` appears as a free variable, and the remark's scope is overclaimed.
   - Impact: May require revision of `rem:phi-inert-objection` text to narrow its scope to "main-theorem-statement-level" rather than "main-theorem-proof-level."
   - Recommendation: Plan task to trace the main theorem proof chain and determine which sections it enters.

---

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Approach 1 (standing def + qualifier) | Equivocation count exceeds 5 sections | Approach 2 (split notation) | ~48 search-and-replace lines + preamble edit; 1–2 hours |
| Approach 2 (split notation) | Author prefers minimum-diff for JMP referee | Approach 1 | One boxed def + ≤ 6 qualifiers; 30 min |
| Both drafts | `prop:inheritance` audit reveals `\varphi`-dependent step not pre-classified | (C-i): structural revision of `prop:inheritance` proof itself, following Phase 54 C-i precedent | 1–2 days (similar to Phase 54 close scope); escalate via `gpd:discuss-phase 57` |
| Outcome (B) | Grep reveals `\varphi` is genuinely state-dependent (not inert) somewhere new | Outcome (C): "Φ is inert" claim false globally; revision becomes structural | Days; requires `gpd:discuss-phase 57` escalation and potentially reopening `rem:phi-inert-objection` with much narrower scope language |

**Decision criteria:**
- Switch from Approach 1 to Approach 2: IF equivocation sites ≤ 5 AND author explicitly requests macro-level clarity.
- Switch from (B) to (C-i): IF `prop:inheritance` factor-level proof has a `\varphi`-specific step that cannot be re-routed through Peirce-Preservation Lemma.
- Switch from (B) to (C): IF role-(a) count > ~20 (i.e., `\varphi` is actually load-bearing in many more places than pre-audit predicted).

---

## Caveats and Alternatives (Pre-Submission Self-Critique)

**Q: What assumption am I making that might be wrong?**
A: I am assuming the single-macro `\varphi` source is canonical. If the author has been editing `main.tex` locally with their preferred symbol `\Phi` in draft comments, a broader scan (including comments and non-math-mode text) might reveal occurrences. Mitigation: Plan task 1 grep includes `-e '\\Phi' -e '\\phi' -e '\\widehat' -e '\\hat'` patterns to catch drift.

**Q: What alternative approach did I dismiss too quickly?**
A: I dismissed "do nothing" (keep the paper as-is; rely on `rem:phi-inert-objection`'s claim). This is arguably the true minimum-diff approach. Why I dismissed it: DERV-57-01 through DERV-57-04 are contract-required; the milestone v14.0 explicitly includes Phase 57 as a gap-closing phase. The author/contract has already decided an audit is needed.

**Q: What limitation of my recommended method am I understating?**
A: Manual classification of 48 rows is feasible but tedious, and the "minimal property" column is subjective in a few rows (e.g., is `\varphi` in Def. `def:self-modeling-system` clause `sms:faithful` "full definition" or "order iso"? Both are true; which is minimal?). Mitigation: provide 2–3 example rows in the plan template so the executor has a reference for ambiguous cases; flag ≤ 2 rows as "author-judgment needed."

**Q: Is there a simpler method I overlooked because the complex one is more impressive?**
A: Possibly: a **one-line addition to Def. `def:self-modeling-system`** stating "Throughout this paper, `\varphi` denotes this tracking isomorphism; subsequent mentions refer to this object, unless explicitly re-introduced" might suffice as a minimum-viable audit response if classification reveals zero R8 equivocations. Mitigation: keep this as the ultra-minimum-diff fallback in the plan, triggered only IF classification table shows every role-(d) already has an adjacent `\ref{cor:S4-phi-indep}` cite.

**Q: Would a physicist specializing in this subfield disagree with my recommendation? Why?**
A: A subfield specialist (e.g., vdW, Masanes, Wilce) might prefer **Approach 1 with a stronger boxed statement** — not just "standing def" but a full "Notation conventions" paragraph at the top of §2 explicitly listing phi-independent vs phi-dependent results with cross-references. This is closer to MathSciNet/review-style, heavier than minimum-diff. Mitigation: Mention this as an Approach-1-variant in `phi-audit.md` §5; author can choose variant after seeing both drafts.

---

## Sources

### Primary (HIGH confidence)

- **Paper 5 living `main.tex` + `sections/*.tex` + `preamble.sty`** (`~/repos/blog/landing/papers/qm-from-self-modeling/`) — Direct inspection of all phi-family occurrences and macro definitions; 931 + 1883 lines total.
- **Phase 54 RESULT.md** (`.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-RESULT.md`, outcome C-i, sealed 2026-04-16) — Cor `cor:S4-phi-indep` established.
- **Phase 55 RESULT.md** (`.gpd/phases/55-s4-facial-structure-lemma/55-RESULT.md`, outcome C-i, sealed 2026-04-17) — SymPy Test 3 φ-independence verified; F3 non-blocking caveat naming Phase 57 inheritance.
- **Phase 56 RESULT.md** + **CLOSE entry in `alfsen-shultz-notes.md`** (`derivations/paper5-peirce-preservation/alfsen-shultz-notes.md:426–533`) — Explicit "Phase 57 inheritance note" naming `prop:inheritance` as primary phi-audit target.
- **`.gpd/research/PITFALLS.md` §R8** (lines 245–273) — Phi equivocation pitfall definition + recovery strategy.
- **`.gpd/ROADMAP.md` Phase 57 entry** (lines 762–777) — DERV-57-01 through DERV-57-04 requirements + forbidden proxies.
- **`.gpd/REQUIREMENTS.md`** (lines 49–79) — Phase 57 requirements table + DERV-00-01 success-criteria row.

### Secondary (MEDIUM confidence)

- **van de Wetering 2019** (arXiv:1803.11139) — Def. 2 sequential product axioms; inherited from Phase 54–56; standing-definition precedent.
- **Alfsen-Shultz 2003** (Birkhäuser PM 190, Ch. 1–8 pre-Jordan-legal) — Compression `c_p` single-symbol precedent.
- **`.gpd/research/METHODS.md`** — Inherits method list from project-level research; no Phase-57-specific methods directly listed, but R8 methodology is in PITFALLS.md.
- **`.gpd/STATE.md`** (lines 15–23, 254) — Phase 57 current-phase context; Phase 56 close confirmation.

### Tertiary (LOW confidence)

- **Hardy 2001** (arXiv:quant-ph/0101012) — Referenced as anti-pattern anchor for role (b)/(c) classification (do not replicate).
- **Chiribella-D'Ariano-Perinotti 2011** (arXiv:1011.6451) — Referenced as forbidden proxy (do not invoke).
- **Masanes-Müller 2011 / Masanes-Galley-Müller 2019 / Barnum-Wilce 2014** — Standing-definition-style reconstruction precedents; not directly consulted during this research (would require WebFetch; relying on Phase 54/55/56 already-established citation chain).
- **Strunk-White rule 17 (stable referent)** — Referenced as standard revision methodology; inherited from PITFALLS.md §R8.

---

## Metadata

**Confidence breakdown:**

- Grep methodology + macro scope: **HIGH** — Direct inspection of `preamble.sty` and all 7 .tex files; patterns verified with preflight grep (48 total matches, zero `\Phi` / `\phi` / `\widehat`).
- Classification taxonomy with operational criteria: **HIGH** — (a)/(b)/(c)/(d) derived from PITFALLS.md §R8 four-section prior hypothesis + role-(b)/(c) preflight (zero ancilla/wrapper matches confirms both likely empty).
- Equivocation detection heuristic: **HIGH** — Based on R8 pattern in PITFALLS.md + specific pre-identified sites (`rem:phi-inert-objection` scope, `\varphi = id` specializations, `prop:inheritance` factor-level).
- Split-vs-standing-definition tradeoff analysis: **HIGH** — Diff-cost pivot derived from backtracking rule in ROADMAP Phase 57 (> 5 sections ⟹ standing-def); precedents in vdW 2019 and A-S 2003.
- Prior-phase anchor inheritance: **HIGH** — Phase 54/55/56 RESULT.md files and `alfsen-shultz-notes.md` CLOSE entries read directly.
- Forbidden-proxy handling: **HIGH** — ROADMAP Phase 57 list is explicit; preflight confirms zero matches for purification/ancilla keywords.
- Tool recommendations: **HIGH** — ripgrep, git, standard POSIX tools; no new installations beyond what's already available.
- Validation strategies: **HIGH** — Inherited from Phase 54/55/56 consistency-check discipline; applied to notation-audit scope.
- Computational tools: **HIGH** — Phase 57 requires no numerical work; all tools are text-processing.
- Open questions (Q1–Q5): **MEDIUM** — Grounded in specific sites; will resolve during plan execution.

**Research date:** 2026-04-17
**Valid until:** Phase 57 completion (≤ 1 week). Longer-term stable (notation audit results do not decay).
