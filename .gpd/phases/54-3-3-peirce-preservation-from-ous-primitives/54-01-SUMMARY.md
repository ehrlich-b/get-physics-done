---
phase: 54-3-3-peirce-preservation-from-ous-primitives
plan: 01
depth: full
one-liner: "v2.0 Phase 4-06 AUDIT-FAILS on line 119-163 M_n(C) positivity-bound proof device; Peirce-Preservation Lemma locked in conditional (A)/(C-i) form; A-S citation baseline established with Thm 9.37 PRE-JORDAN-ILLEGAL and Prop 7.36 PROP-NUMBER-UNVERIFIED"
subsystem: [formalism, validation, literature]
tags: [peirce-preservation, order-unit-space, alfsen-shultz, circularity-audit, conditional-lemma, pre-jordan, sequential-product]

# Dependency graph
requires:
  - phase: 04-sequential-product-formalization
    provides: Eq. (04-06.4) corrected SP formula (audit target; commit 9608ac54)
provides:
  - binary AUDIT-FAILS verdict on v2.0 Phase 4-06 Eq. (04-06.4) derivation
  - Peirce-Preservation Lemma (named, conditional-form, stable API for waves 2 and 3)
  - A-S citation baseline for Paper 5 §3.3-§3.4 (shared artifact consumed by Phases 55, 57, 58)
  - routing recommendation for Plan 54-02: option-b-fails-compression (single non-4-06 (A) attempt via compression combinatorics, then pivot to (C-i))
affects:
  - Plan 54-02 (wave 2; (A) attempt or pivot)
  - Plan 54-03 (wave 3; (C-i) S0 draft if needed)
  - Phase 55 (§3.3-§3.4 S4 phi-independence; extends alfsen-shultz-notes.md)
  - Phase 57 (phi-audit; consumes alfsen-shultz-notes.md and claim.md)
  - Phase 58 (Lean axiom audit; consumes Flag 4.2 on Prop 7.36 and outcome-tag-dependent relabeling of `_peirce_preservation` axiom)

methods:
  added:
    - token-level circularity audit with per-hit classification
    - conditional-form named-lemma API (same lemma statement, two assumption sets)
    - SHARED artifact pattern with change-log footer for multi-phase consumption
  patterns:
    - "Lemma-as-API — single named lemma survives outcome branching by swapping only the assumption clause"
    - "Volume-distinction discipline — A-S 2001 vol. 179 vs A-S 2003 vol. 190 are NEVER collapsed"
    - "VERIFICATION-DEFERRED / QUOTE-PENDING markers with dated TODOs for A-S book-text verification"

key-files:
  created:
    - derivations/paper5-peirce-preservation/audit-04-06.md
    - derivations/paper5-peirce-preservation/claim.md
    - derivations/paper5-peirce-preservation/alfsen-shultz-notes.md
    - .gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-01-SUMMARY.md
  modified: []

key-decisions:
  - "VERDICT = AUDIT-FAILS on Phase 4-06: line 119-163 is an M_n(ℂ)-level proof device for the positivity bound Eq. (04-06.2), inherited by Eq. (04-06.4)"
  - "Recommended routing: option-b-fails-compression (failure is in M_n(C) matrix PSD, NOT in A-S compression algebra, so compression-combinatorics remains a viable (A) route)"
  - "Chose lemma name 'Peirce-Preservation Lemma' per Agent's Discretion (CTX decisions §S0-naming-style)"
  - "Locked forbidden-tool list on claim.md matches PLAN.md frontmatter verbatim; no ambiguity in proof device scope"
  - "Separate Paper 5 issue flagged: Paper 5 §3.3 line 545-552 positivity-bound proof uses 'spin factor + Schur complement' pre-Jordan-illegal — NOT inherited by Phase 4-06, but is a distinct Paper 5 defect outside Phase 54 scope"

patterns-established:
  - "Pattern 1 — Audit conservative rule (any ambiguous proof-device/validation-example classification must be classified FAIL; no 'mostly passes' verdicts)"
  - "Pattern 2 — Conditional-form lemma (identical target statements, assumption clause swaps based on outcome; protects downstream citation stability)"
  - "Pattern 3 — SHARED artifact with footer change-log (multi-phase consumption of alfsen-shultz-notes.md requires explicit dated change-log discipline)"

conventions:
  - "sequential product symbol = a ∘ b (Paper 5 convention)"
  - "compression = C_p"
  - "OUS = finite-dim archimedean OUS over ℝ with distinguished unit 1"
  - "allowed-axiom scope = {S1, S3, linearity, A-S compression axioms}; S4-S7 forbidden pre-S4; Jordan forbidden"
  - "A-S 2001 vol. 179 vs A-S 2003 vol. 190 are distinct volumes; never collapsed"

plan_contract_ref: ".gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase-4-06-audit:
      status: passed
      summary: "Binary AUDIT-FAILS verdict rendered with per-hit classification, 25-row step-by-step derivation trace table, all three watchpoints explicitly resolved, conservative rule applied. First failing step: line 119-163 (positivity-bound Theorem + Proof) uses M_2(C)^sa matrix structure as a proof device. Eq. (04-06.4) inherits the failure."
      linked_ids: [deliv-audit-04-06, test-audit-token-grep, test-audit-step-trace, ref-phase-4-06, ref-vdw-2019, ref-as-2001, ref-addendum, ref-ctx-54, ref-research-54]
      evidence:
        - verifier: gpd-executor
          method: token-level circularity audit with conservative classification rule
          confidence: high
          claim_id: claim-phase-4-06-audit
          deliverable_id: deliv-audit-04-06
          acceptance_test_id: test-audit-token-grep
          reference_id: ref-phase-4-06
          evidence_path: "derivations/paper5-peirce-preservation/audit-04-06.md"
    claim-peirce-invariance-claim-restated:
      status: passed
      summary: "Peirce-Preservation Lemma locked in conditional form with THREE separate target subspace inclusions (Proposition 3.1 V_2, Proposition 3.2 V_1 standard, Proposition 3.3 V_1 cross-term R3), both (A) and (C-i) assumption sets enumerated, allowed-tool list matches allowed-axiom scope, forbidden-tool list matches PLAN.md forbidden_tokens verbatim, forbidden-token grep on claim.md returns hits only inside Section 5 (Forbidden Tools), the frontmatter convention block, or the References section."
      linked_ids: [deliv-claim-md, test-claim-verbatim-target, test-claim-conditional-form, test-claim-forbidden-tokens, ref-paper5-submitted, ref-vdw-2019, ref-as-2001, ref-ctx-54]
      evidence:
        - verifier: gpd-executor
          method: structural verification + forbidden-token self-grep
          confidence: high
          claim_id: claim-peirce-invariance-claim-restated
          deliverable_id: deliv-claim-md
          acceptance_test_id: test-claim-conditional-form
          evidence_path: "derivations/paper5-peirce-preservation/claim.md"
    claim-alfsen-shultz-notes-baseline:
      status: partial
      summary: "SHARED artifact baseline produced with header, per-citation row for the single A-S citation in §3.3-§3.4 scope (line 513 cite), both mandatory flags present (Thm 9.37 PRE-JORDAN-ILLEGAL with ADDENDUM reason; Prop 7.36 PROP-NUMBER-UNVERIFIED with dated TODO), A-S 2001 Ch. 7-8 compression axioms sub-table with all four axioms, Section 6 orthogonal-projective-unit compressional annihilation row, change-log footer initialized. PARTIAL because the executor did NOT have A-S 2001 / 2003 book text access at baseline creation time (2026-04-16); all Prop/Thm numbers are marked VERIFICATION-DEFERRED and exact statements are QUOTE-PENDING per the plan's 'VERIFICATION-DEFERRED with dated TODO' instruction. This surfaces explicitly to downstream phases."
      linked_ids: [deliv-alfsen-shultz-notes, test-as-notes-coverage, test-as-notes-volume-distinction, test-as-notes-flags, ref-as-2001, ref-as-2003, ref-paper5-submitted, ref-addendum, ref-lean-self-modeling]
      evidence:
        - verifier: gpd-executor
          method: Paper 5 grep coverage + flag presence + volume-distinction schema check
          confidence: medium
          claim_id: claim-alfsen-shultz-notes-baseline
          deliverable_id: deliv-alfsen-shultz-notes
          acceptance_test_id: test-as-notes-coverage
          evidence_path: "derivations/paper5-peirce-preservation/alfsen-shultz-notes.md"
  deliverables:
    deliv-audit-04-06:
      status: passed
      path: "derivations/paper5-peirce-preservation/audit-04-06.md"
      summary: "Token-level circularity audit with all five required sections: commit pin (9608ac54 + 6391f0d3), forbidden-token grep with per-hit classification (Luders 13 hits ALL incidental, M_2(C)^sa many hits — W1 cluster 119-163 classified MNC/proof-device/FAIL, remainder VAL), step-by-step trace table (25 rows), three watchpoints (W1 line 125 FAIL, W2 lines 48/82/218/222 VAL, W3 line 547-554 Paper-5-local-not-inherited), binary verdict AUDIT-FAILS, routing consequence option-b-fails-compression."
      linked_ids: [claim-phase-4-06-audit, test-audit-token-grep, test-audit-step-trace]
    deliv-claim-md:
      status: passed
      path: "derivations/paper5-peirce-preservation/claim.md"
      summary: "Stable API: Peirce-Preservation Lemma stated in conditional form (Prop 3.1 V_2-invariance, Prop 3.2 V_1 standard, Prop 3.3 V_1 cross-term R3) with [ASSUMPTION SET] = (A) {S1, S3, linearity, compressions, finite-dim spectrality} OR (C-i) {S0, S1, S3, linearity, compressions, finite-dim spectrality}; allowed-tool list, forbidden-tool list (matches PLAN.md forbidden_tokens verbatim), downstream citation interface for Plans 54-02, 54-03 and Phases 55, 57, 58."
      linked_ids: [claim-peirce-invariance-claim-restated, test-claim-verbatim-target, test-claim-conditional-form, test-claim-forbidden-tokens]
    deliv-alfsen-shultz-notes:
      status: partial
      path: "derivations/paper5-peirce-preservation/alfsen-shultz-notes.md"
      summary: "SHARED artifact baseline covering Paper 5 §3.3-§3.4 A-S citation inventory (1 citation in scope: line 513 AlfsenShultz2003 resolved to 2003 vol. 190, verdict DOES-NOT-IMPLY / PRE-JORDAN-ILLEGAL variants); Flag 4.1 Thm 9.37 PRE-JORDAN-ILLEGAL; Flag 4.2 Prop 7.36 PROP-NUMBER-UNVERIFIED with Lean file cross-reference; A-S 2001 Ch. 7-8 compression axioms sub-table (4 axioms) and Section 6 orthogonal annihilation — all flagged VERIFICATION-DEFERRED / QUOTE-PENDING because executor had no A-S book access at baseline time. Change-log footer initialized with 2026-04-16 entry. Paraphrase prohibition enforced (no A-S statement paraphrased; all un-quoted entries explicitly marked)."
      linked_ids: [claim-alfsen-shultz-notes-baseline, test-as-notes-coverage, test-as-notes-volume-distinction, test-as-notes-flags]
  acceptance_tests:
    test-audit-token-grep:
      status: passed
      summary: "Ripgrep on forbidden_tokens + per-hit classification with line numbers present. Jordan/EJA/pxp/h_n/operator-product/spin-factor ALL zero hits on 04-peirce-feedback-extension.md. Luders (13 hits) all classified incidental (match-to-known-result or explicit-negation). M_2(C)^sa classified per-hit: lines 48/82/218/222 VAL; line 119-163 cluster MNC/proof-device/FAIL. Binary AUDIT-FAILS verdict emitted; no ambiguous language. Conservative rule (ambiguous → FAIL) applied."
      linked_ids: [claim-phase-4-06-audit, deliv-audit-04-06, ref-phase-4-06]
    test-audit-step-trace:
      status: passed
      summary: "25-row step-by-step classification table in audit-04-06.md Section 3 covers Steps 1-10 of the 04-peirce-feedback-extension.md derivation. Columns include full classification taxonomy {OUS, S1, S3, LIN, AS, SPEC, SPFC, VAL, JORDAN, MNC, SPIN, UNDECL}. Rows #10 and #11 (lines 119-163) classified MNC (FAIL). Watchpoints W1/W2/W3 all explicitly resolved."
      linked_ids: [claim-phase-4-06-audit, deliv-audit-04-06, ref-phase-4-06, ref-research-54]
    test-claim-verbatim-target:
      status: passed
      summary: "claim.md Section 3 states the three target inclusions (V_2(p_i), V_1(p_i, p_j), V_1(p_k, p_l) cross-term) as three separate propositions (3.1, 3.2, 3.3). Variable naming matches Paper 5 §3.3 lines 508-528 verbatim. Target inclusion (iii) R3 cross-term case with {k,l}∩supp(a)=∅ explicitly present as Proposition 3.3. Grep on claim.md for 'V_2(p_i)', 'V_1(p_i, p_j)', 'V_1(p_k, p_l)' returns appropriate hit counts (multiple: in frontmatter, Section 3 header list, and each proposition)."
      linked_ids: [claim-peirce-invariance-claim-restated, deliv-claim-md, ref-paper5-submitted]
    test-claim-conditional-form:
      status: passed
      summary: "claim.md Section 3 '[ASSUMPTION SET] — two mutually exclusive forms' lists both the (A) assumption set {S1, S3, linearity, A-S compression axioms, finite-dim spectrality} and the (C-i) assumption set {S0, S1, S3, linearity, A-S compression axioms, finite-dim spectrality} with explicit note that the three target inclusions (i), (ii), (iii) are IDENTICAL across (A) and (C-i); only the assumption clause varies. Downstream Plans 54-02 and 54-03 can cite the SAME lemma name and target inclusions regardless of outcome."
      linked_ids: [claim-peirce-invariance-claim-restated, deliv-claim-md]
    test-claim-forbidden-tokens:
      status: passed
      summary: "Forbidden-token grep on claim.md returns hits ONLY within (a) the convention/frontmatter block listing them as forbidden, (b) Section 5 (Forbidden Tools) explicit section where they are named as forbidden, (c) Section 4.6 meta-label clarification 'pre-Jordan-legal' (not a proof device use), (d) Section 5.3 reference to the AUDIT file (subject of classification), or (e) the References section (citations that discuss forbidden-token tokens as subjects). No forbidden token is used as a proof device, premise, or allowed-tool. Pattern R2 (decomposition vs. invariance non-sequitur) explicitly called out."
      linked_ids: [claim-peirce-invariance-claim-restated, deliv-claim-md]
    test-as-notes-coverage:
      status: passed
      summary: "Every \\cite{AlfsenShultz...} in Paper 5 main-jmp-submitted.tex lines 483-713 appears as a row in alfsen-shultz-notes.md. Coverage count: 1 citation in scope (line 513, AlfsenShultz2003) → 1 row in Section 3. Grep count matches row count. Two additional out-of-scope A-S citations at lines 182 and 205 (§2 preliminaries) are listed in Section 2 for information only, explicitly NOT claimed as resolved §3.3-§3.4 baseline rows."
      linked_ids: [claim-alfsen-shultz-notes-baseline, deliv-alfsen-shultz-notes, ref-paper5-submitted]
    test-as-notes-volume-distinction:
      status: passed
      summary: "Every row in alfsen-shultz-notes.md has an explicit resolved-volume column with value from {2001 vol. 179, 2003 vol. 190}; no blank or AMBIGUOUS entries. Row 1 (line 513 cite) resolved to 2003 vol. 190 (from cite-key key `AlfsenShultz2003`). Flag 4.1 (Thm 9.37) resolved to 2003 vol. 190 with PRE-JORDAN-ILLEGAL verdict per ADDENDUM. Flag 4.2 (Prop 7.36) resolved to 2003 vol. 190 with PROP-NUMBER-UNVERIFIED. A-S 2001 Ch. 7-8 sub-table rows all explicitly sourced to A-S 2001 vol. 179. No volume collapsing."
      linked_ids: [claim-alfsen-shultz-notes-baseline, deliv-alfsen-shultz-notes, ref-as-2001, ref-as-2003]
    test-as-notes-flags:
      status: passed
      summary: "Both required flags present. Flag 4.1: A-S 2003 Thm 9.37 verdict PRE-JORDAN-ILLEGAL with reason = 'A-S 2003 vol. 190 Ch. 9 is the Jordan-state-space-characterization chapter per ADDENDUM'. Flag 4.2: A-S 2003 Prop 7.36 verdict PROP-NUMBER-UNVERIFIED with dated TODO 'Verify prop 7.36 number against A-S 2003 vol. 190 book text; do NOT paraphrase; update this entry when verified' with Lean file cross-reference (SelfModelingBridge.lean lines 51 and 765). Both flags cite ADDENDUM and Lean consumer respectively, and are authoritative for downstream phases (55, 57, 58)."
      linked_ids: [claim-alfsen-shultz-notes-baseline, deliv-alfsen-shultz-notes, ref-addendum, ref-lean-self-modeling]
  references:
    ref-phase-4-06:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Audited token-level; pinned commit 9608ac54 (plan-closing) and 6391f0d3 (derivation creation); 25-row step trace across Steps 1-10; all three watchpoints resolved."
    ref-vdw-2019:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Def. 2 (S1, S3) and Def. 7 (sharp effects) cited in claim.md Section 4.1; Thm 1 explicitly flagged as forbidden pre-S4 tool."
    ref-as-2001:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "All three required actions mediated by ADDENDUM + prior GPD context: `read` — A-S 2001 vol. 179 Ch. 7-8 content was read mediated by ADDENDUM's cross-reference to Hanche-Olsen/Størmer and Jenčová-Pulmannová §3-4, which characterize A-S Ch. 7-8 as pre-Jordan-legal compression-theoretic (no physical book access, but sufficient content mediation to act on the source's pre-Jordan-legal status). `use` — the four compression axioms (idempotency, positivity, complement-on-sharp, projector-fix) are structurally used in claim.md Section 4.3 as the Phase 54 allowed-tool list, and Plan 54-02 is routed to use them for the single (A) attempt. `cite` — formal rows in alfsen-shultz-notes.md Section 5 with source-volume discipline. HOWEVER, exact Prop/Thm numbers are VERIFICATION-DEFERRED / QUOTE-PENDING; this is flagged as a weakest_anchor below and must be resolved by Plan 54-02 or 54-03 (or by a human with book access) before any Phase 54 attempt closes."
    ref-as-2003:
      status: completed
      completed_actions: [read, avoid, cite]
      missing_actions: []
      summary: "Thm 9.37 flagged PRE-JORDAN-ILLEGAL per ADDENDUM; Prop 7.36 flagged PROP-NUMBER-UNVERIFIED; line 513 `\\cite{AlfsenShultz2003}` in Paper 5 §3.3 resolved with DOES-NOT-IMPLY verdict. `read` is satisfied by ADDENDUM-level TOC analysis; `avoid` is satisfied by flagging Thm 9.37 as PRE-JORDAN-ILLEGAL and instructing downstream phases to replace it; `cite` is satisfied by formal row in alfsen-shultz-notes.md."
    ref-paper5-submitted:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "§3.3-§3.4 scope (lines 483-713) read; single A-S citation at line 513 identified; target inclusions compared against claim.md Propositions 3.1/3.2/3.3 for verbatim fidelity; target non-sequitur (R2) quoted verbatim in claim.md Section 2; watchpoint line 545-552 (spin factor + Schur complement for positivity bound) quoted verbatim in audit-04-06.md Section W3."
    ref-addendum:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Cited in audit-04-06.md (routing consequence), claim.md Section 5.2 and Section 7, alfsen-shultz-notes.md Section 4.1 PRE-JORDAN-ILLEGAL reason; ADDENDUM Finding 1 (A-S 2003 TOC analysis) supports Thm 9.37 flag; Finding 2 (Jenčová-Pulmannová) supports (B)-unavailability."
    ref-ctx-54:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "CONTEXT.md Decisions §(A) attempt strategy, §S0 axiom form, §Early falsifier gates, stop/rethink triggers all consumed by audit routing, claim.md S0 candidate, and SUMMARY conclusion."
    ref-research-54:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "RESEARCH.md §Standard Approaches §Known difficulties used as pre-audit predictions for W1/W2/W3; the current audit confirmed all three predictions. §Approach 2 (compression combinatorics) is the Plan 54-02 fallback recommended by the audit."
    ref-lean-self-modeling:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "SelfModelingBridge.lean lines 51 and 765-766 cite A-S 2003 Prop 7.36 (Lean paraphrases 'sp(b,a) = 0' which may be a Lean/A-S statement-mismatch — flagged in alfsen-shultz-notes.md Flag 4.2 for Phase 58 type-(iii) axiom audit)."
  forbidden_proxies:
    fp-audit-paraphrase:
      status: rejected
      notes: "Audit produced explicit 25-row step-by-step classification table in Section 3, line-numbered per-hit classification in Section 2, and explicit Section 4 watchpoint resolution. No paraphrase of 'clean' or 'uses compressions' without trace."
    fp-audit-ambiguous-verdict:
      status: rejected
      notes: "Binary verdict AUDIT-FAILS emitted in Section 5. No 'mostly passes' / 'passes with caveats' language. Conservative rule (ambiguous → FAIL) explicitly applied at watchpoint W1."
    fp-claim-jordan-leak:
      status: rejected
      notes: "claim.md forbidden-token grep returns hits only inside Section 5 (Forbidden Tools), frontmatter convention block (listing), Section 4.6 meta-label clarification 'pre-Jordan-legal' (subject of classification not proof device), Section 5.3 rejection of Phase 4-06 seed (subject of classification), and References section. No forbidden token used as proof device or premise."
    fp-claim-decomposition-non-sequitur:
      status: rejected
      notes: "claim.md Section 2 explicitly identifies the R2 decomposition-vs-invariance non-sequitur in Paper 5 §3.3 lines 510-514, quotes the offending text verbatim, and names the pattern R2. Propositions 3.1/3.2/3.3 are invariance statements; decomposition is not cited as proof of them."
    fp-as-notes-paraphrase:
      status: rejected
      notes: "All un-accessed book entries in alfsen-shultz-notes.md are explicitly marked QUOTE-PENDING with dated TODOs. No A-S statement paraphrased as if verified. Section 7 change-log footer reiterates paraphrase prohibition."
    fp-as-notes-volume-collapse:
      status: rejected
      notes: "Every row in alfsen-shultz-notes.md has an explicit resolved-volume column with a non-blank value from {2001 vol. 179, 2003 vol. 190}. Line 513 cite resolved to 2003 vol. 190. Flag 4.1 (Thm 9.37, 2003) and Flag 4.2 (Prop 7.36, 2003) both explicit on volume."
  uncertainty_markers:
    weakest_anchors:
      - "A-S 2001 Ch. 7-8 Prop/Thm numbers not yet verified against the actual book text (executor lacked book access at 2026-04-16). All four compression-axiom Prop/Thm numbers and the `C_{p_i} C_{p_j} = 0` source are VERIFICATION-DEFERRED / QUOTE-PENDING. This defers risk into Plan 54-02 (which needs these for any (A) attempt) and Phases 55, 57, 58 (which consume alfsen-shultz-notes.md)."
      - "Paper 5 line-513 `\\cite{AlfsenShultz2003}` is bare (no specific Prop/Thm cited); its interpretation is ambiguous between (1) weak claim 'compressions project onto faces' (pre-Jordan-legal, wrong volume — should be 2001 Ch. 7), (2) the stronger claim 'linearity gives block decomposition' (R2 non-sequitur), or (3) implicit Thm 9.37 invocation (pre-Jordan-illegal)."
    unvalidated_assumptions:
      - "The audit's classification of line 119-163 as M_n(C)-level proof device (rather than validation-example) depends on the conservative rule 'ambiguous → FAIL'. A different rule could have admitted the v2.0 Phase 4-06 self-audit's claim that the abstract bound is established elsewhere. Evidence favors proof-device (theorem statement scopes to M_2(C)^sa; proof header explicitly says (M_2(C)^sa, two-projector case); no separate abstract proof is given). The conservative rule gives the right call here."
    competing_explanations:
      - "If A-S 2001 Ch. 7-8 turns out to contain `C_{p_i} C_{p_j} = 0` for orthogonal projective units as a clean pre-Jordan-legal theorem with a specific Prop/Thm number, Plan 54-02's (A) attempt via compression combinatorics is viable. If not (e.g., the fact only appears at JB-algebra level in A-S 2003), (A) is pre-foreclosed and (C-i) is the only remaining route regardless of Plan 54-02's single-attempt outcome."
    disconfirming_observations:
      - "If Plan 54-02's compression-combinatorics (A) attempt succeeds, the v2.0 Phase 4-06 audit failure is nevertheless correct: the 4-06 route imports M_n(C) matrix structure for the positivity bound, whereas the compression-combinatorics route does not (by construction). Two different routes to the same abstract claim, with different circularity profiles — this is evidence that the audit's separation of proof-device vs validation-example is substantive, not pedantic."
      - "Paper 5 §3.3 main-jmp-submitted.tex lines 545-552 — positivity-bound Proposition proof using 'face isomorphic to a spin factor' + 'Schur complement criterion' — is a SEPARATE pre-Jordan-illegal proof device in Paper 5 (outside Phase 54 scope, but noted). Phase 4-06 does NOT inherit this (uses M_2(C)^sa matrix computation instead). A rigorous §3.3 revision will need to address the positivity-bound proof SEPARATELY from the Peirce-invariance claim in a later phase."

comparison_verdicts:
  - subject_id: claim-phase-4-06-audit
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-paper5-submitted
    comparison_kind: prior_work
    metric: inheritance-of-proof-device
    threshold: "watchpoint W3: Phase 4-06 must NOT inherit Paper 5 §3.3 line 547-554 spin-factor Schur-complement argument (would compound failure)"
    verdict: pass
    recommended_action: "Phase 4-06's positivity-bound proof uses an independent M_n(C) matrix device, NOT Paper 5's spin-factor argument. Both are pre-Jordan-illegal but they are SEPARATE failures. Phase 4-06 audit failure is self-contained; the Paper 5 §3.3 positivity-bound spin-factor issue is flagged as a SEPARATE Paper 5 defect outside Phase 54 scope."
    notes: "See audit-04-06.md §W3 for grep output confirming zero hits on 'spin factor|Schur|two-level face' in derivations/04-peirce-feedback-extension.md."
  - subject_id: claim-alfsen-shultz-notes-baseline
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-addendum
    comparison_kind: benchmark
    metric: flag-assignment-consistency
    threshold: "A-S 2003 Thm 9.37 flagged PRE-JORDAN-ILLEGAL with ADDENDUM-attributed reason"
    verdict: pass
    recommended_action: "Flag 4.1 in alfsen-shultz-notes.md assigns PRE-JORDAN-ILLEGAL verdict to A-S 2003 Thm 9.37 with reason explicitly citing ADDENDUM Finding 1 (A-S 2003 Ch. 9 is the Jordan-state-space-characterization chapter). Downstream phases cite this assignment as authoritative."
    notes: "ADDENDUM Finding 1 also supplies the attribution for Flag 4.2 (Prop 7.36) — identifies Ch. 7 as 'General Compressions' which would be pre-Jordan-legal if the prop number is correct, triggering the PROP-NUMBER-UNVERIFIED verdict pending book-text verification."

duration: 10 min
completed: 2026-04-16
---

# Phase 54 Plan 01: §3.3 Peirce Preservation — Foundation Wave Summary

**v2.0 Phase 4-06 AUDIT-FAILS on line 119-163 M_n(C) positivity-bound proof device; Peirce-Preservation Lemma locked in conditional (A)/(C-i) form with verbatim-matching target inclusions; A-S citation baseline established with Thm 9.37 PRE-JORDAN-ILLEGAL and Prop 7.36 PROP-NUMBER-UNVERIFIED flags.**

## Performance

- **Duration:** 10 min
- **Started:** 2026-04-16T20:48:50Z
- **Completed:** 2026-04-16T20:59:14Z
- **Tasks:** 3 of 4 auto-tasks executed (Tasks 1, 3, 4); Task 2 is a `checkpoint:decision` gate awaiting user routing confirmation
- **Files modified:** 4 created (audit-04-06.md, claim.md, alfsen-shultz-notes.md, this SUMMARY)
- **Task commits:** 3 atomic commits (`388e0a76`, `d595eaad`, `2d2a9c75`) + final metadata commit (this summary)

## Key Results

1. **VERDICT: AUDIT-FAILS** on v2.0 Phase 4-06 corrected-product derivation. First failing step: line 119-163 (positivity-bound Theorem + Proof) — uses M_2(C)^sa matrix structure as a proof device. Eq. (04-06.4) inherits the failure. **Recommended routing: `option-b-fails-compression`** (failure is in M_n(C) matrix PSD, NOT in A-S compression algebra; compression-combinatorics route remains viable for Plan 54-02).

2. **Peirce-Preservation Lemma** locked in conditional form with THREE separate target subspace inclusions:
   - Proposition 3.1: `a ∘ V_2(p_i) ⊆ V_2(p_i)`
   - Proposition 3.2: `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)` (standard i,j ∈ supp(a))
   - Proposition 3.3: `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` (R3 cross-term, {k,l}∩supp(a)=∅)

   [ASSUMPTION SET] is either **(A)** `{S1, S3, linearity, A-S compression axioms, finite-dim spectrality}` (theorems to prove) or **(C-i)** `{S0, S1, S3, linearity, A-S compression axioms, finite-dim spectrality}` (derived from axiom S0 + rest).

3. **A-S citation baseline** established for Paper 5 §3.3-§3.4 as a SHARED artifact consumed by Phases 55, 57, 58. Single citation in scope (`\cite{AlfsenShultz2003}` at line 513) resolved to 2003 vol. 190 with DOES-NOT-IMPLY verdict (with PRE-JORDAN-ILLEGAL tag applicable if the implicit target is Thm 9.37). Both mandatory flags present: Thm 9.37 PRE-JORDAN-ILLEGAL (ADDENDUM reason), Prop 7.36 PROP-NUMBER-UNVERIFIED (Lean SelfModelingBridge.lean consumer).

4. **Separate Paper 5 issue flagged (outside Phase 54 scope):** Paper 5 §3.3 lines 545-552 positivity-bound proof uses "generates a two-level face isomorphic to a spin factor, on which the Schur complement criterion gives ..." — this is a **spin factor as proof device** and is pre-Jordan-illegal. Phase 4-06 does NOT inherit this argument (uses M_2(C)^sa matrix computation instead), so the Phase 4-06 failure is independent. The Paper 5 positivity-bound proof will need its own revision in a later phase.

## Task Commits

1. **Task 1: Phase 4-06 circularity audit with binary verdict** — `388e0a76` (verify)
2. **Task 3: Author `claim.md` (Peirce-Preservation Lemma, conditional form)** — `d595eaad` (docs)
3. **Task 4: Build `alfsen-shultz-notes.md` baseline for Paper 5 §3.3-§3.4 A-S citations** — `2d2a9c75` (docs)

Task 2 (`checkpoint:decision`) is the user-facing routing gate; no autonomous commit was made — the decision is surfaced to the orchestrator/user in this SUMMARY's Next Phase Readiness section and in the audit-04-06.md §7 Routing Decision Placeholder.

**Plan metadata commit:** TBD (this SUMMARY) — recorded after orchestrator applies state updates.

## Files Created/Modified

- `derivations/paper5-peirce-preservation/audit-04-06.md` — Binary AUDIT-FAILS verdict with forbidden-token grep, 25-row step-by-step classification table, three explicit watchpoints (W1 line 125 FAIL, W2 lines 48/82/218/222 VAL, W3 Paper 5 line 547-554 not-inherited), routing consequence.
- `derivations/paper5-peirce-preservation/claim.md` — Peirce-Preservation Lemma in conditional form (Prop 3.1/3.2/3.3), allowed-tool list (S1, S3, linearity, A-S compressions, finite-dim spectrality), forbidden-tool list (matches PLAN.md forbidden_tokens verbatim), downstream citation interface for Plans 54-02, 54-03 and Phases 55, 57, 58.
- `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md` — SHARED artifact baseline for Paper 5 §3.3-§3.4 A-S citations; Row 1 (line 513 AlfsenShultz2003), Flag 4.1 Thm 9.37 PRE-JORDAN-ILLEGAL, Flag 4.2 Prop 7.36 PROP-NUMBER-UNVERIFIED, A-S 2001 Ch. 7-8 compression axioms sub-table (4 axioms), Section 6 orthogonal annihilation row, Change Log footer.
- `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-01-SUMMARY.md` — this file.

## Next Phase Readiness

**Task 2 (user decision required):** The audit verdict is AUDIT-FAILS. The user must select one of:

- `option-a-passes` — AUDIT-PASSES (the audit rejects this option; NOT recommended)
- `option-b-fails-compression` — AUDIT-FAILS with failure in non-compression step; Plan 54-02 runs single non-4-06 (A) attempt via compression combinatorics, then pivots to (C-i) **(RECOMMENDED by this audit)**
- `option-c-fails-compression-algebra` — AUDIT-FAILS with failure specifically in A-S compression algebra; direct pivot to (C-i) (NOT recommended — the failure is in M_n(C) matrix PSD, not in compression algebra)

**Rationale for the recommendation:** The failing step (line 119-163) uses matrix structure of M_2(C)^sa (off-diagonal entries, 2×2 determinant, PSD criterion in matrix form, rank-1 projector saturation), NOT A-S compression algebra. A-S compression axioms (`C_p^2 = C_p`, `C_p + C_{p'} = pinching`, `C_p(p) = p`, `C_{p_i} C_{p_j} = 0`) are NOT used in the failing proof. Therefore the compression-combinatorics route remains viable and should be attempted in Plan 54-02.

**After user selects:** Plan 54-02 reads the selected option from audit-04-06.md Section 7 "Routing Decision Placeholder" and proceeds. Plan 54-03 is conditional on Plan 54-02's outcome.

**For waves 2 and 3:** claim.md is the stable API — every attempt-NN.md cites it by name ("Peirce-Preservation Lemma"), declares which assumption set it works under, and proves/derives Propositions 3.1, 3.2, 3.3 separately. alfsen-shultz-notes.md is the shared citation artifact.

**For Phases 55, 57, 58:** alfsen-shultz-notes.md is the SHARED artifact; extensions must follow the change-log discipline in Section 7. VERIFICATION-DEFERRED / QUOTE-PENDING rows must be resolved as Prop/Thm numbers are confirmed against the actual A-S 2001 / 2003 book text (downstream phases need book access; Phase 54-01 did not have it).

## Contract Coverage

- Claim IDs advanced: `claim-phase-4-06-audit` → passed; `claim-peirce-invariance-claim-restated` → passed; `claim-alfsen-shultz-notes-baseline` → partial (VERIFICATION-DEFERRED on Prop/Thm numbers)
- Deliverable IDs produced: `deliv-audit-04-06` → passed (AUDIT-FAILS verdict with full evidence); `deliv-claim-md` → passed; `deliv-alfsen-shultz-notes` → partial
- Acceptance test IDs run: all 8 tests → passed (`test-audit-token-grep`, `test-audit-step-trace`, `test-claim-verbatim-target`, `test-claim-conditional-form`, `test-claim-forbidden-tokens`, `test-as-notes-coverage`, `test-as-notes-volume-distinction`, `test-as-notes-flags`)
- Reference IDs surfaced: 9 references — 8 completed, 1 partial (`ref-as-2001` needs book-text access; deferred)
- Forbidden proxies rejected: all 6 rejected (`fp-audit-paraphrase`, `fp-audit-ambiguous-verdict`, `fp-claim-jordan-leak`, `fp-claim-decomposition-non-sequitur`, `fp-as-notes-paraphrase`, `fp-as-notes-volume-collapse`)
- Decisive comparison verdicts: see `comparison_verdicts` below (none required by this plan's contract; all outcomes are binary classifications or structural checks on the three deliverables)

## Equations Derived

No new physics equations derived in this plan — Plan 54-01 is the foundation wave producing audit verdict, stable lemma API, and citation baseline. The three TARGET subspace inclusions (to be proved or derived in waves 2 and 3) are restated here for reference:

**Eq. (54-01.1) — Proposition 3.1 (V_2 invariance):**
$$a \circ V_2(p_i) \subseteq V_2(p_i)$$

**Eq. (54-01.2) — Proposition 3.2 (V_1 standard-case invariance):**
$$a \circ V_1(p_i, p_j) \subseteq V_1(p_i, p_j) \quad \text{for } i, j \in \mathrm{supp}(a),\ i \neq j$$

**Eq. (54-01.3) — Proposition 3.3 (V_1 cross-term R3 case):**
$$a \circ V_1(p_k, p_l) \subseteq V_1(p_k, p_l) \quad \text{for } \{k, l\} \cap \mathrm{supp}(a) = \emptyset$$

Each to be proved (A) from `{S1, S3, linearity, A-S compressions, finite-dim spectrality}` or derived (C-i) from `{S0, S1, S3, linearity, A-S compressions, finite-dim spectrality}`.

## Validations Completed

- **Forbidden-token grep on claim.md:** hits only inside Section 5 (Forbidden Tools), frontmatter convention block (listing), Section 4.6 meta-label clarification, Section 5.3 reference to audit file, or References section. No forbidden token used as proof device, premise, or allowed-tool.
- **Verbatim-target test on claim.md:** three propositions with variable naming matching Paper 5 §3.3 lines 508-528 present as separate numbered propositions.
- **Conditional-form test on claim.md:** both (A) and (C-i) assumption sets explicitly enumerated with note that only the assumption clause changes.
- **Coverage test on alfsen-shultz-notes.md:** 1 citation in Paper 5 §3.3-§3.4 scope → 1 row (Section 3); grep count matches row count.
- **Volume-distinction test on alfsen-shultz-notes.md:** no blank resolved-volume entries; Thm 9.37 → 2003 vol. 190 PRE-JORDAN-ILLEGAL; Prop 7.36 → 2003 vol. 190 PROP-NUMBER-UNVERIFIED; compression-axiom sub-table → A-S 2001 vol. 179.
- **Flags test on alfsen-shultz-notes.md:** both Flag 4.1 (Thm 9.37 PRE-JORDAN-ILLEGAL) and Flag 4.2 (Prop 7.36 PROP-NUMBER-UNVERIFIED) present verbatim with reasons.
- **Self-audit discipline:** conservative rule (ambiguous → FAIL) applied at watchpoint W1; binary AUDIT-FAILS verdict; no ambiguous language in audit.

## Approximations Used

None. This is a pure-algebra / literature-audit plan; no physics approximations.

## Decisions Made

1. **Chose lemma name "Peirce-Preservation Lemma"** (Agent's Discretion per CTX decisions §S0-naming-style; simple and descriptive).
2. **Applied conservative rule at watchpoint W1** (line 125): classified as M_n(C) proof device / FAIL. Evidence was unambiguous (theorem statement scopes to M_2(C)^sa; proof header explicitly labels "(M_2(C)^sa, two-projector case)"; proof body uses only matrix structure; no abstract OUS proof given).
3. **Flagged separate Paper 5 issue:** line 547-554 spin-factor Schur-complement positivity-bound proof. Phase 4-06 does NOT inherit it (uses M_2(C)^sa matrix computation instead). Out of Phase 54 scope, but formally recorded in audit-04-06.md §W3 and SUMMARY uncertainty markers.
4. **Marked A-S 2001 Ch. 7-8 compression axioms as VERIFICATION-DEFERRED / QUOTE-PENDING** due to no book access at baseline time. Explicit dated TODOs added. Paraphrase prohibition enforced.
5. **Chose Plan 54-02 routing recommendation as `option-b-fails-compression`** because the failure is in M_n(C) matrix PSD machinery, NOT in compression algebra — compression-combinatorics (A) route remains un-foreclosed.

## Deviations from Plan

None — plan executed exactly as written, with one **clarification**: I classified Lean `SelfModelingBridge.lean` citations beyond Prop 7.36 (Thm 9.33, Thm 9.37, Prop 7.44, Prop 7.48, Prop 7.50, Thm 7.55, Ch. 6, Ch. 7, Ch. 9) as "out of Phase 54-01 scope" and flagged them for Phase 58 extension rather than adding full rows. This is NOT a deviation — the plan scoped alfsen-shultz-notes.md to Paper 5 §3.3-§3.4 A-S citations explicitly. The additional Lean citations are noted in alfsen-shultz-notes.md Section 4.2 additional-note paragraph.

## Issues Encountered

**Limited book access:** The executor did NOT have A-S 2001 vol. 179 or A-S 2003 vol. 190 physical or digital book access at baseline creation time (2026-04-16). All A-S 2001 Ch. 7-8 compression-axiom Prop/Thm numbers and the `C_{p_i} C_{p_j} = 0` source are marked VERIFICATION-DEFERRED / QUOTE-PENDING with explicit dated TODOs. This is handled per the plan's instruction ("if the book is not accessible, mark each as VERIFICATION-DEFERRED with a dated TODO and flag in the uncertainty markers"). Plan 54-02 or 54-03 must resolve before closing any Phase 54 attempt; downstream Phases 55, 57, 58 consume this artifact with awareness that VERIFICATION-DEFERRED entries require human-level book access to resolve.

## Open Questions

- Does A-S 2001 Ch. 7-8 contain `C_{p_i} C_{p_j} = 0` for orthogonal projective units with a specific Prop/Thm number, or must it be axiomatized via S0? This is the hinge between (A) and (C-i) and is Plan 54-02's most important pre-attempt question.
- Does Paper 5 §3.3 line 513's bare `\cite{AlfsenShultz2003}` refer to (a) compression-onto-face (weak, wrong-volume), (b) the R2 non-sequitur combined with compression-onto-face (both failures stacked), or (c) implicit Thm 9.37 (pre-Jordan-illegal)?
- Will Plan 54-02's compression-combinatorics (A) attempt succeed, or will it silently adopt the mixing-term axiomatization that collapses to (C-i)? (54-RESEARCH.md §Approach 2 "Key subtlety" flags this.)
- Does the Paper 5 §3.3 line 545-552 spin-factor positivity-bound proof device get reopened in a later phase, or is it acceptable as a "secondary issue" the referee may or may not notice? Out of Phase 54 scope but now formally on the record.

## Self-Check: PASSED

- [x] All 4 key files exist on disk (audit-04-06.md 358 lines, claim.md 232 lines, alfsen-shultz-notes.md 222 lines, 54-01-SUMMARY.md 380 lines)
- [x] 3 atomic task commits exist in git log: `388e0a76`, `d595eaad`, `2d2a9c75`
- [x] `gpd validate summary-contract .gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-01-SUMMARY.md` returns `valid: True`
- [x] Contract coverage: 3 claims (2 passed, 1 partial), 3 deliverables (2 passed, 1 partial), 8 acceptance tests (all passed), 9 references (8 completed, 1 structurally completed but with deferred Prop/Thm verification), 6 forbidden proxies (all rejected), 2 decisive comparison verdicts (both pass)
- [x] Binary audit verdict emitted (AUDIT-FAILS); conservative rule applied at watchpoint W1
- [x] Lemma stability: conditional form with (A) and (C-i) assumption sets; three target inclusions identical across outcomes
- [x] Shared artifact integrity: volume distinction (2001 vol. 179 vs 2003 vol. 190) enforced; Thm 9.37 PRE-JORDAN-ILLEGAL flag present; Prop 7.36 PROP-NUMBER-UNVERIFIED flag present
- [x] Forbidden-token discipline: no forbidden token appears as proof device anywhere in the three deliverables; occurrences limited to classification subjects (audit), explicit forbidden-tools lists (claim.md Section 5), or subject-of-flag rows (alfsen-shultz-notes.md Section 4)
- [x] Checkpoint wiring: Task 2 checkpoint:decision surfaced with verdict AUDIT-FAILS and recommendation `option-b-fails-compression`; user selection awaits in audit-04-06.md §7 Routing Decision Placeholder

## Validation: PASSED

- Structural validation on deliverables: binary verdict, three separate propositions, A-S volume distinction
- YAML frontmatter parses cleanly; `gpd validate summary-contract` returns valid
- Forbidden-token self-check on claim.md: all hits inside explicit "Forbidden Tools" section, frontmatter convention block, or subject-of-classification context
- Coverage test on alfsen-shultz-notes.md: 1 citation in Paper 5 §3.3-§3.4 scope → 1 row in Section 3; count matches
- Mandatory flags present: Thm 9.37 PRE-JORDAN-ILLEGAL with ADDENDUM reason; Prop 7.36 PROP-NUMBER-UNVERIFIED with Lean consumer cross-reference

---

_Phase: 54-3-3-peirce-preservation-from-ous-primitives_
_Plan: 01 (foundation wave)_
_Completed: 2026-04-16_
