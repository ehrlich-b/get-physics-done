---
phase: 55-s4-facial-structure-lemma
plan: 01
depth: full
one-liner: "Classified 10 §S4-region A-S invocations (1 iii / 3 ii / 6 i), closed Prop 7.43 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE, resolved line-68 Thm 9.37 as PRE-S4 scope for Plan 55-02 fix; notes extended with 7 append-only rows."
subsystem: [literature, formalism, validation]
tags: [alfsen-shultz, citation-audit, peirce-preservation, s4-axiom, jordan-circularity, paper5-revision-prep]

requires:
  - phase: 54-3-3-peirce-preservation-from-ous-primitives
    provides: [S0 axiom, Peirce-Preservation Lemma, A-S Prop 7.23/Def 7.1/Prop 7.50 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE, alfsen-shultz-notes.md baseline]
provides:
  - 55-01-CLASSIFICATION.md frozen blueprint for Plan 55-02 (10 §S4-region invocations tagged + consumption pointers)
  - Prop 7.43 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE verdict (Ch. 7)
  - Line 68 (S2 proof Thm 9.37) classified PRE-S4 SCOPE → include in Plan 55-02 edit scope
  - alfsen-shultz-notes.md Section 8 extension (7 new rows; append-only; dated change-log entry)
  - secondary-source-verification.md Prop 7.43 appendix entry
affects: [55-02 (revision text), 55-03 (close + adversarial review), 57 (phi-audit — may want line-39/180 VERIFIED-AS-IS rows), 58 (Lean axiom audit — Prop 7.43 now VERIFIED per same pattern as Phase 54 rows)]

methods:
  added: [S4-region A-S citation classification rubric, S0-termwise derivation pattern for unnamed facial-orthogonality theorems]
  patterns: [append-only shared-artifact extension (alfsen-shultz-notes.md), secondary-source-verification appendix pattern, Phase 54 → Phase 55 internal-cross-reference salvage]

key-files:
  created:
    - .gpd/phases/55-s4-facial-structure-lemma/55-01-CLASSIFICATION.md
    - .gpd/phases/55-s4-facial-structure-lemma/55-01-SUMMARY.md
  modified:
    - derivations/paper5-peirce-preservation/alfsen-shultz-notes.md (+145 lines, 0 deletions; append-only)
    - derivations/paper5-peirce-preservation/secondary-source-verification.md (+ Prop 7.43 Phase 55-01 appendix entry)

plan_contract_ref:
  contract_sha: null
  path: .gpd/phases/55-s4-facial-structure-lemma/55-01-PLAN.md
  schema_version: 1

contract_results:
  claims:
    - id: claim-s4-classification
      status: established
      evidence:
        - 55-01-CLASSIFICATION.md Section 2 rows 1-19 (10 invocations in §S4 region tagged, 8 outside-§S4 for completeness)
        - 55-01-CLASSIFICATION.md Section 1 summary (one-line tag per invocation)
        - Every row has classification tag (i/ii/iii) + citation proposal; acceptance test test-classification-every-cite-tagged PASS
      notes: "§S4-strict tags: 1 (iii) REPLACE-WITH-S0 at line 125 + 1 (iii) REPLACE at line 68 (pre-S4 contiguous); 5 (ii) with RESOLVE-VIA-S0-TERMWISE or REPLACE-WITH-LEMMA; 4 (i) with TIGHTEN-CITE or VERIFIED-AS-IS."
    - id: claim-as-citation-resolution
      status: established
      evidence:
        - Section 3 Prop 7.43 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE → A-S 2003 Ch. 7, Prop 7.43 via derivations/04-axiom-S4.md line 65
        - secondary-source-verification.md Phase 55-01 appendix entry with Route 1 grep evidence
        - Zero A-S 2001 hits in §S4 region (grep verification; fp-volume-collapse REJECTED)
      notes: "Every A-S 2003 invocation has volume (190) + chapter (1/7/8/9) + prop/thm populated. Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE rows (Prop 7.23, Def 7.1, Prop 7.49, Prop 7.50) carried forward; Prop 7.43 newly added at same level."
    - id: claim-notes-extension-with-changelog
      status: established
      evidence:
        - alfsen-shultz-notes.md Section 8 with 7 new rows (55-01-A1 through 55-01-A6 and 55-01-B1, 55-01-B2)
        - git diff shows 145 insertions, 0 deletions (append-only verified)
        - Dated Phase 55-01 change-log addendum at end of file
      notes: "Minimum 4 required rows exceeded (7 added); all Phase 54 rows untouched."
    - id: claim-line68-scope-decision
      status: established
      evidence:
        - 55-01-CLASSIFICATION.md Section 4 records PRE-S4 SCOPE verdict with 3+ sentence justification (enclosing S2 subsection evidence, semantic content analysis, Flag 4.1 applicability)
        - alfsen-shultz-notes.md row 55-01-A2 records matching PRE-S4 verdict
      notes: "Line 68 Thm 9.37 is inside the S2 (Continuity) proof; pre-S4 scope; MANDATORY Plan 55-02 fix. Substitute: A-S 2003 Ch. 8 Spectral Theory or textbook citation (Bhatia/Conway)."
  deliverables:
    - id: deliv-classification-md
      status: produced
      path: .gpd/phases/55-s4-facial-structure-lemma/55-01-CLASSIFICATION.md
      notes: "Sections 1-7 all populated (Plan 55-01 asked for 1-6; added Section 7 Plan 55-02 consumption pointers as bonus per Task 5 closing section); forbidden-token exception log in Section 6; Plan 55-02 substitution-site list in Section 7."
    - id: deliv-notes-extension
      status: produced
      path: derivations/paper5-peirce-preservation/alfsen-shultz-notes.md
      notes: "+145 lines, 0 deletions; 7 new rows; dated Phase 55-01 change-log addendum; append-only discipline verified via git diff."
    - id: deliv-secondary-source-update
      status: produced
      path: derivations/paper5-peirce-preservation/secondary-source-verification.md
      notes: "Prop 7.43 Verification (Phase 55-01, 2026-04-16) section appended with Route 1 internal cross-reference PASS; Routes 2/3 documented but not executed per stop-at-first-PASS rule."
  acceptance_tests:
    - id: test-classification-every-cite-tagged
      status: passed
      evidence: 55-01-CLASSIFICATION.md Section 2 — every row has non-empty tag ∈ {(i),(ii),(iii)} and citation-proposal field
      notes: "Required minimum invocation set confirmed: line 125 → (iii) REPLACE-WITH-S0; line 154 → (ii) RESOLVE-VIA-S0-TERMWISE; line 155-157 → (ii) REPLACE-WITH-LEMMA (Part iii); appendix:79 → (i) TIGHTEN-CITE; appendix:108 → (ii) RESOLVE-VIA-S0-TERMWISE; appendix:109-113 → (ii) REPLACE-WITH-LEMMA (Part iii)."
    - id: test-classification-line68-resolved
      status: passed
      evidence: 55-01-CLASSIFICATION.md Section 4 (PRE-S4 SCOPE verdict + 3-sentence justification + downstream implication for Plan 55-02 edit scope)
      notes: "Enclosing environment identified as §S2 (Continuity) subsection; justification draws on three independent arguments."
    - id: test-classification-evidence-line-numbers
      status: passed
      evidence: Section 2 rows cite verbatim quotes from axiom-verification.tex:39,68,83,125,136-137,143-147,154,155-157,180,182,228,232,321 and appendix-proofs.tex:37-49,78-79,85-89,106-108,109-113,204
      notes: "All quotes match source files verbatim (modulo LaTeX escape notation)."
    - id: test-every-cite-has-ch-prop
      status: passed
      evidence: Section 2 A-S 2003 rows — Ch. 7, Ch. 8, Ch. 9 disambiguated; Prop 7.23, Def 7.1, Prop 7.43, Prop 7.49, Prop 7.50, Thm 9.37, Thm 1.23 all specified
      notes: "Row 5/15 Prop 7.43 carries VERIFIED-VIA-INTERNAL-CROSS-REFERENCE status (not VERIFICATION-DEFERRED); fallback pointer unused."
    - id: test-no-as-2001-for-compressions
      status: passed
      evidence: "grep -nE 'AlfsenShultz2001' sections/axiom-verification.tex sections/appendix-proofs.tex → zero hits"
      notes: No fp-volume-collapse bug in §S4 region.
    - id: test-prop-743-status-declared
      status: passed
      evidence: 55-01-CLASSIFICATION.md Section 3 + secondary-source-verification.md Phase 55-01 appendix entry — both declare VERIFIED-VIA-INTERNAL-CROSS-REFERENCE with cross-pointers
      notes: Route 1 PASS via derivations/04-axiom-S4.md line 65; Routes 2/3 unexecuted per stop-at-first-PASS rule.
    - id: test-notes-row-count
      status: passed
      evidence: alfsen-shultz-notes.md Section 8 has 7 rows (55-01-A1..A6, B1, B2); minimum 4 required; all 4 required categories covered (line 125, line 68, Prop 7.43, facial orthogonality)
    - id: test-notes-append-only
      status: passed
      evidence: "git diff derivations/paper5-peirce-preservation/alfsen-shultz-notes.md → 145 insertions, 0 deletions"
    - id: test-notes-changelog-present
      status: passed
      evidence: "grep -c '2026-04-16 (Phase 55-01)' alfsen-shultz-notes.md → 1"
    - id: test-line68-context-determined
      status: passed
      evidence: Section 4 identifies enclosing \subsection*{S2 (Continuity)} at line 47, blockquote at 48-52, proof body at 54-70, and the S3 boundary at line 71
      notes: alfsen-shultz-notes.md row 55-01-A2 matches Section 4 verdict (PRE-S4, INCLUDE in Plan 55-02 scope).
  forbidden_proxies_rejected:
    - id: fp-bare-cite
      status: rejected
      evidence: Every A-S 2003 invocation in Section 2 has volume + chapter + prop/thm (or VERIFICATION-DEFERRED with dated TODO); zero bare "\cite{AlfsenShultz2003}" citations in the §S4 classification rows without chapter + prop pinning.
    - id: fp-volume-collapse
      status: rejected
      evidence: grep for AlfsenShultz2001 in §S4 region returns zero hits; no 2001 ↔ 2003 confusion.
    - id: fp-hos-invocation
      status: rejected
      evidence: Zero classification rows propose Hanche-Olsen-Størmer as a pre-S4 substitute; Approach 2 Foulis-Holland documented but not invoked; H-O discussed only in forbidden-anchor context.
    - id: fp-mock-prop-743-verification
      status: rejected
      evidence: secondary-source-verification.md Phase 55-01 appendix cites derivations/04-axiom-S4.md:65 with verbatim-matching statement; not a "looks right" claim.
    - id: fp-line68-handwave
      status: rejected
      evidence: Section 4 reads axiom-verification.tex lines 46-71 (enclosing environment), identifies S2 subsection explicitly, and gives 3 independent arguments for PRE-S4 classification.
    - id: fp-notes-overwrite
      status: rejected
      evidence: git diff shows 145 insertions, 0 deletions; Section 8 is a new append-only block below all existing sections; Phase 54 change-log entries preserved verbatim.
    - id: fp-jordan-token-leak
      status: rejected
      evidence: Section 6 Forbidden-Token Exception Log enumerates every Jordan/9.37/Hanche-Olsen hit; all are inside fenced code blocks, `% BEGIN TRANSCRIBED ... % END` markers, or prose-as-flag-label use (authorized by Phase 55-01 `forbidden_tokens_exception_scope`).
  comparison_verdicts:
    - id: approach-1-vs-approach-2-gate
      subject: Approach 1 (S0 + Prop 7.43) vs Approach 2 (Foulis-Holland)
      verdict: "Approach 1 confirmed"
      evidence:
        - Prop 7.43 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (fallback trigger FALSE)
        - Approach 2 fallback criterion (Prop 7.43 FAILS) AND (no internal-cross-reference salvage) has both conjuncts FALSE
      consequence: Plan 55-02 proceeds with S0 + Peirce-Preservation Lemma + tightened Prop 7.43 citations; Foulis-Holland route remains documented fallback only.
  references:
    - id: ref-axiom-verification
      status: read
      actions_taken: [read, used for inventory, cited in Section 2 rows]
    - id: ref-appendix-proofs
      status: read
      actions_taken: [read, used for inventory, cited in Section 2 rows]
    - id: ref-main-jmp-submitted
      status: unchanged
      actions_taken: [verified frozen — git status landing/papers/qm-from-self-modeling/ shows zero changes]
    - id: ref-phase54-notes
      status: extended
      actions_taken: [read, used for schema pattern, extended Section 8 with 7 append-only rows]
    - id: ref-phase54-s0
      status: cited
      actions_taken: [read, cited as REPLACE-WITH-S0 target in Section 2 rows 2, 4]
    - id: ref-phase54-secondary-source
      status: extended
      actions_taken: [read, used as template, extended with Phase 55-01 Prop 7.43 appendix entry]
    - id: ref-phase54-result
      status: carried_forward
      actions_taken:
        - "cited as authorizing the {S0, S1, S3, linearity, A-S compressions} toolkit for all Phase 55 revisions"
    - id: ref-as-2003
      status: cited
      actions_taken: [Ch. 1, Ch. 7, Ch. 8, Ch. 9 disambiguated; Prop 7.23, Def 7.1, Prop 7.43, Prop 7.49, Prop 7.50, Thm 9.37, Thm 1.23 cross-referenced]
    - id: ref-as-2001
      status: verified_absent
      actions_taken: [grep verification — zero hits in §S4 region]
    - id: ref-vdw-2019
      status: cited
      actions_taken: [referenced as S4 statement source; not directly cited in classification rows but noted in research]
    - id: ref-hos-1984
      status: flagged_forbidden
      actions_taken: [noted as post-Jordan-circular; zero substitutions propose H-O as pre-S4 fix]
    - id: ref-niestegge
      status: not_required
      actions_taken: [Route 2 unexecuted per stop-at-first-PASS rule; Route 1 internal-cross-reference PASSED]
    - id: ref-jencova-pulmannova
      status: not_required
      actions_taken: [not consulted — Route 1 closed the verification]
    - id: ref-claim-md
      status: cited
      actions_taken: [Peirce-Preservation Lemma referenced as REPLACE-WITH-LEMMA target]
---

## Outcome

**CLASSIFICATION-COMPLETE** — Phase 55-01 produced a frozen classification blueprint for Plan 55-02 with the following decisive results:

1. **Primary bug identified and staged for fix:** axiom-verification.tex:125 (Thm 9.37 in S4 Case A) → REPLACE-WITH-S0 + REPLACE-WITH-LEMMA. This was the motivating primary bug of Phase 55.

2. **Secondary pre-S4 bug identified:** axiom-verification.tex:68 (Thm 9.37 in S2 Continuity proof) → PRE-S4 SCOPE → include in Plan 55-02 edit scope. Substitute: A-S 2003 Ch. 8 Spectral Theory (pre-Jordan-legal for continuous spectral functional calculus) or textbook citation.

3. **Prop 7.43 verification succeeded:** VERIFIED-VIA-INTERNAL-CROSS-REFERENCE → A-S 2003 Ch. 7, Prop 7.43 via `derivations/04-axiom-S4.md` line 65. Exact statement `b ≥ 0 ∧ C_p(b) = 0 ⟹ b ∈ face(p^⊥)` matches Paper 5 blockquote verbatim. Approach 2 Foulis-Holland fallback NOT triggered.

4. **Unnamed facial appeals resolved:** The "facial orthogonality theorem" (axiom-verification.tex:154, appendix-proofs.tex:108) is replaced by an explicit S0-termwise derivation; the "facial structure" handwave for Q_{jk}(a) vanishing (lines 155-157 + 109-113) is replaced by the Peirce-Preservation Lemma Part (iii) with an explicit role-swap note.

5. **Approach 1 (S0 + Prop 7.43) gate:** CONFIRMED. Plan 55-02 proceeds with S0 axiom + Peirce-Preservation Lemma + tightened Prop 7.43 citations.

6. **No A-S 2001 in §S4 region:** grep confirms zero hits — no volume-collapse bug to correct.

7. **frozen baseline unchanged:** main-jmp-submitted.tex carries zero diff; Plan 55-01 is strictly read-only against paper files.

## Key Results

| # | Result | Status | Confidence |
|---|--------|--------|------------|
| 1 | S4-region inventory: 10 invocations in §S4 + 1 pre-S4 contiguous (line 68) + 8 outside-§S4 for completeness (19 total rows) | Complete | HIGH |
| 2 | Tag distribution in §S4 strict: 1 (iii), 3 (ii), 6 (i); pre-S4 contiguous: 1 (iii); outside-§S4: 7 (i), 1 FLAG-OUT-OF-SCOPE | Complete | HIGH |
| 3 | Prop 7.43: VERIFIED-VIA-INTERNAL-CROSS-REFERENCE → A-S 2003 Ch. 7 | Verified (Route 1) | MEDIUM-HIGH (internal cross-ref; direct book access still a TODO) |
| 4 | Line 68 scope: PRE-S4 (S2 Continuity proof) → INCLUDE in Plan 55-02 | Determined | HIGH |
| 5 | Approach-1 vs Approach-2 gate: Approach 1 CONFIRMED | Decided | HIGH |
| 6 | alfsen-shultz-notes.md extension: 7 new rows, 0 deletions, dated change-log entry | Complete | HIGH |
| 7 | Plan 55-02 substitution-site count: 12 sites (2 MANDATORY/PRIMARY, 8 HIGH, 2 LOW) indexed by classification row | Complete | HIGH |

## Derivation / Verification Details

**Prop 7.43 verification (Route 1 — internal cross-reference):**

- **Evidence source:** `derivations/04-axiom-S4.md` line 65 produced under convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY` (GPD v2.0 Phase 04).
- **Statement match:** Internal `b >= 0 and C_p(b) = 0 => b in face(p^perp)` vs Paper 5 blockquote `If C_p(b) = 0 and b ≥ 0, then b ∈ face(p^⊥)` — identical modulo notation.
- **Confidence basis:** The convention-locked derivation explicitly uses A-S Prop/Thm numbers; no paraphrasing risk.

**Line 68 scope argument (Section 4, three independent threads):**

1. **Textual:** S2 subsection (line 47-72) precedes S4 (line 95); all S1-S7 proofs feed into vdW Thm 1 EJA promotion; Jordan structure is the CONCLUSION not a premise.
2. **Semantic:** The continuity claim "continuous function of the eigenvalues alone" is a spectral functional calculus property, properly homed in A-S 2003 Ch. 8 "Spectral Theory" (p. 251, pre-Jordan-legal), not Ch. 9 Jordan characterization.
3. **Boundary discipline:** Thm 9.37 is marked PRE-JORDAN-ILLEGAL per Flag 4.1 regardless of usage context; R6 circularity applies at any pre-S4 scope.

## Task Commits

| Task | Purpose | Commit SHA |
|------|---------|------------|
| 1 + 2 | Create 55-01-CLASSIFICATION.md with Sections 1-7 (inventory, tags, Section 3 Prop 7.43 verdict, Section 4 line 68 decision, Section 5 Approach gate, Section 6 forbidden-token log, Section 7 Plan 55-02 pointers) | `4e298d8b` |
| 3 | Append Prop 7.43 verification entry to secondary-source-verification.md | `4f334f19` |
| 4 | Append 7 rows + Phase 55-01 change-log to alfsen-shultz-notes.md | `0fb8d983` |
| 5 | Finalize + SUMMARY.md | (this commit) |

## Hand-off to Plan 55-02

**Plan 55-02 (revision text + integration) consumes this phase as follows:**

### Substitution sites (from 55-01-CLASSIFICATION.md Section 7, priority-ordered)

**MANDATORY + PRIMARY:**
1. `sections/axiom-verification.tex:68` — `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37)` → `(Alfsen--Shultz~\cite[Ch.~8]{AlfsenShultz2003})` OR `(Bhatia, *Matrix Analysis* §VI)` [Option 1 preferred; finite-dim spectral functional calculus continuity].
2. `sections/axiom-verification.tex:125` — `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~9.37)` → `(by axiom~\ref{ax:S0} and Lemma~\ref{lem:peirce-preservation})`.

**HIGH:**
3. `sections/axiom-verification.tex:136-137` — tighten `(Proposition~7.43 of~\cite{AlfsenShultz2003})` → `(Alfsen--Shultz~\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003})`.
4. `sections/axiom-verification.tex:143-147` — replace "By the facial structure..." with `by Lemma~\ref{lem:peirce-preservation} Part (iii) (R3 cross-term case, role-swap $a \leftrightarrow b$)`.
5. `sections/axiom-verification.tex:154` — replace "the facial orthogonality theorem gives" with explicit S0-termwise derivation (see CLASSIFICATION.md Section 7 row 7 for the exact LaTeX snippet).
6. `sections/axiom-verification.tex:155-157` — replace "vanish by facial structure" with `vanish by Lemma~\ref{lem:peirce-preservation} Part (iii) (role-swap)`.
7. `sections/appendix-proofs.tex:78-79` — tighten to `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`.
8. `sections/appendix-proofs.tex:106-108` — same S0-termwise derivation as site 5.
9. `sections/appendix-proofs.tex:109-113` — same Lemma Part (iii) cite as site 6.

**MEDIUM:**
10. `sections/appendix-proofs.tex:85-89` — add `\ref{ax:S0}` or `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` citation to "act independently on their respective faces".

**LOW (optional):**
11. `sections/axiom-verification.tex:39` — tighten bare `Ch.~7` to `Ch.~7, Prop.~7.23, Def.~7.1`.
12. `sections/appendix-proofs.tex:37-49` — add parenthetical `(axiom~\ref{ax:S0} + Lemma~\ref{lem:peirce-preservation})` alongside `\eqref{eq:peirce-proj}`.

### Approach decision for Plan 55-02

- **Approach 1 (S0 + Prop 7.43)** — CONFIRMED per Section 5 gate decision. Proceed.
- **Approach 2 (Foulis-Holland)** — documented but NOT triggered.

### Verification targets for Plan 55-02 exit

- Zero `Theorem~9.37` or `Thm~9.37` or `9\.37` hits in §S4 region AND pre-S4 scope (including line 68).
- At least 4 `\ref{ax:S0}` or `\ref{lem:peirce-preservation}` citations in sections/axiom-verification.tex + sections/appendix-proofs.tex.
- Zero bare `\cite{AlfsenShultz2003}` (every cite has `[Ch.~X, Prop.~Y.Z]`).
- LaTeX compile succeeds; all cross-references resolve.
- main-jmp-submitted.tex still carries zero diff.

### Prop 7.43 status reminder

Prop 7.43 is VERIFIED-VIA-INTERNAL-CROSS-REFERENCE, NOT VERIFIED-AGAINST-BOOK-TEXT. The Plan 55-02 revision text can cite it with confidence, but the upgrade to VERIFIED-AGAINST-BOOK-TEXT remains a Phase 55/56 or later TODO (requires direct A-S 2003 vol. 190 book access).

## Deviations

None. All tasks completed inside the approved contract; no deviation rules (1-6) triggered. Task 2 was merged into Task 1 (Sections 1, 5, 6 populated in the same write as Sections 2, 4) as an efficiency — this is not a deviation because the acceptance tests at the plan level apply to the final state of the document, not to the task sequence.

## Conventions

| Choice | Value | Source |
|--------|-------|--------|
| Sequential product | a ∘ b | Paper 5 Def 3.2 / vdW 2019 Def 2 |
| Compression | C_p | Paper 5 §2 / A-S 2003 Ch. 7 Def 7.1 |
| A-S 2003 | Birkhäuser PM 190 | Phase 54 convention lock |
| A-S 2001 | Birkhäuser PM 179 (disambiguation anchor) | Phase 54 convention lock |
| Pre-Jordan boundary | A-S 2003 Ch. 1-8 legal; Ch. 9 illegal | Flag 4.1 / ADDENDUM Finding 1 |
| Forbidden tokens (pre-S4 revision text) | Jordan, EJA, Lüders, pxp, √a b √a, Hanche-Olsen, 9.37 | Phase 54 R7 |
| Classification tags | {(i), (ii), (iii)} + {REPLACE-WITH-S0, REPLACE-WITH-LEMMA, TIGHTEN-CITE, VERIFIED-AS-IS, FLAG-OUT-OF-SCOPE, RESOLVE-VIA-S0-TERMWISE, RESOLVE-VIA-PROP-743} | Phase 55-01 plan |

## Surprises / Notes

- **Line 68 is a second Thm 9.37 bug, not just "adjacent scope."** The plan anticipated this but flagged it as "classification pending"; the evidence clearly places it PRE-S4 in §S2, making it another MANDATORY fix for Plan 55-02. This expands the Plan 55-02 edit scope by one substitution site, not a scope change (still inside §S2-§S4 axiom-verification, still inside the Phase 55 contract).

- **Prop 7.43 was easier to verify than anticipated.** Route 1 (internal cross-reference) closed the verification in under 2 minutes via `derivations/04-axiom-S4.md:65`. Routes 2 (Niestegge) and 3 (H-O) were not required. The "direct book access" fallback tier was never reached.

- **appendix-proofs.tex:204 is out-of-scope.** Grep caught a Thm 1.23 citation inside `thm:lt-full` (Local Tomography). Ch. 1 is pre-Jordan-legal; no bug. Recorded in Section 2.3 for audit-trail completeness only.

- **Row consolidation:** Plan 55-02 will see that rows 55-01-A4, 55-01-A5, 55-01-A6 each cover TWO Paper 5 invocations (one in axiom-verification.tex and a parallel one in appendix-proofs.tex). The classification schema consolidates parallel invocations into a single row when the substitution is identical; 12 substitution sites, 7 new notes rows.

## Self-Check

**PASSED.** Verification:

- [x] 55-01-CLASSIFICATION.md exists with Sections 1-7 populated (Section 7 is a bonus Plan 55-02 consumption-pointer section; Plan contract required Sections 1-6).
- [x] alfsen-shultz-notes.md shows 145 additions, 0 deletions (append-only).
- [x] secondary-source-verification.md has Phase 55-01 appendix entry with VERIFIED-VIA-INTERNAL-CROSS-REFERENCE verdict.
- [x] Prop 7.43 status declared in BOTH classification doc Section 3 AND secondary-source-verification.md with cross-pointers.
- [x] Line 68 PRE-S4 scope decision recorded in classification doc Section 4 with 3-sentence justification and in alfsen-shultz-notes.md row 55-01-A2.
- [x] Zero A-S 2001 hits in §S4 region (grep verified).
- [x] Zero deletions in alfsen-shultz-notes.md (git diff verified).
- [x] Dated Phase 55-01 change-log entry present (grep returns 1).
- [x] main-jmp-submitted.tex unchanged (git status on blog repo: zero diff).
- [x] sections/axiom-verification.tex + sections/appendix-proofs.tex unchanged (read-only discipline).
- [x] Every forbidden-token hit in 55-01-CLASSIFICATION.md is inside fenced code block, TRANSCRIBED demarcation, or prose-as-flag-label (Section 6 exception log documents all modes).
- [x] All 10 plan-level acceptance tests PASS.
- [x] All 7 forbidden proxies REJECTED with evidence.
- [x] Approach gate decision records Approach 1 CONFIRMED with disconfirming-observation counterfactuals checked.

Next action: `gpd commit` this SUMMARY plus final consistency pass, then signal Phase 55-01 close.
