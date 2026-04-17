---
phase: 56-thm-5-8-upper-bound-w-carries-product-form-sequential-product
plan: 02
type: execute
status: COMPLETE
wave: 2
outcome: SENSE-(b)-AND-(c)-ESTABLISHED
interactive: false
plan_contract_ref: .gpd/phases/56-thm-5-8-upper-bound-w-carries-product-form-sequential-product/56-02-PLAN.md#contract
conventions:
  allowed_axiom_scope: "{S0, S1-S7, linearity of L_a, A-S 2003 Ch. 2/7/8, finite-dim spectrality}"
  as_2003_chapter_limit: "Ch. <= 8 (Ch. 9 FORBIDDEN)"
  primary_proof_route: vdW 2019 Def. 4 (locally tomographic composite) + vdW 2019 Thm 1 (finite-dim SPS -> EJA)
  fallback_proof_route: explicit per-axiom table (S1-S7)
  sense_established_core: (b) [induced-structure SPS, per carries-senses.md §2]
  sense_established_free_corollary: (c) [functorial SPS-morphism, per carries-senses.md §3]
  sympy_verdict: 5/5 PASS, exit 0, elapsed 0.006 s, Python 3.14.2 / SymPy 1.14.0
  frozen_file_zero_diff: verified at Task 1, Task 5
one_liner: "Phase 56-02 COMPLETE: (W, ∘|_W) is a sequential product space (sense (b) per carries-senses.md §2) via vdW 2019 Def. 4 + Thm 1; ι: W ↪ V_{BM} is an SPS-morphism (sense (c) per carries-senses.md §3), free corollary since 1_W = 1_{V_{BM}} and ∘|_W is set-theoretic restriction; SymPy H_3(R) ⊗ H_3(R) certificate 5/5 PASS in 0.006 s; all 18+ §5/§6 downstream consumers served at sense (c); Plan 56-03 revision-text language inventory (L1-L7) staged for composite-lt.tex:203-221 + appendix-proofs.tex:228-238 integration."
contract_results:
  schema_version: 1
  status: complete
  claims:
    - id: claim-sympy-passes
      status: proved
      evidence:
        - "derivations/paper5-peirce-preservation/w-closeout-sympy.py"
        - "derivations/paper5-peirce-preservation/w-closeout-sympy.log"
      notes: "5/5 tests PASS (TEST-CLOSURE/TEST-S1/TEST-S3/TEST-S4/TEST-NEGATIVE); exit 0; elapsed 0.006 s (<< 30 s budget); Python 3.14.2 / SymPy 1.14.0; reuses Phase 54 compress+seq_prod helpers (copied verbatim with attribution comments)."
      confidence: HIGH
    - id: claim-s1-s7-on-w-proof
      status: proved
      evidence:
        - "derivations/paper5-peirce-preservation/w-sps-proof.md"
      notes: "Section 2 (primary route) invokes vdW 2019 Def. 4 (locally tomographic composite) + Thm 1 (finite-dim SPS → EJA) in ≤ 2 pages; Section 3 (fallback route) has 7-row per-axiom table (S1-S7) with ≥ 3-sentence proof + citation per axiom; Section 5 citation inventory (only A-S citation is Ch.~1, Thm.~1.23 — Ch. 1 ≤ 8 ✓); Section 6 R11 cross-check explicitly records S5/S6/S7 as Peirce-invariance touchpoints citing \\ref{lem:peirce-preservation}."
      confidence: HIGH
    - id: claim-sense-c-upgrade
      status: proved
      evidence:
        - "derivations/paper5-peirce-preservation/ci-sps-morphism.md"
      notes: "(c1)-(c4) each proved in Sections 2-5 with explicit derivation; (c2) proves 1_W = 1_B ⊗ 1_M ∈ W and ι(1_W) = 1_{V_{BM}}; (c4) proves ι(a ∘|_W b) = ι(a) ∘_V ι(b) is AUTOMATIC since ∘|_W is set-theoretic restriction; Section 6 states sense (c) holds freely as cheap upgrade from (b) in the Paper 5 setting."
      confidence: HIGH
    - id: claim-three-sense-table
      status: proved
      evidence:
        - "derivations/paper5-peirce-preservation/carries-three-sense-table.md"
      notes: "Section 2 has 20-row consumer-by-sense matrix covering all 18 argumentative rows from downstream-consumer-scan.md §§2-5 (plus 2 additional split-site rows); Section 3 explicitly establishes sense (c) for all consumers; Section 4 contains L1-L7 revision-text language inventory for Plan 56-03 integration at composite-lt.tex:203-221 + appendix-proofs.tex:228-238."
      confidence: HIGH
  deliverables:
    - id: deliv-w-closeout-sympy
      status: produced
      path: "derivations/paper5-peirce-preservation/w-closeout-sympy.py"
      notes: "Task 1 commit f99c8c55; 564 lines; reuses Phase 54 compress + seq_prod helpers; 5 test functions + main runner; exit code semantics (0 = PASS, 1 = FAIL)."
    - id: deliv-w-closeout-log
      status: produced
      path: "derivations/paper5-peirce-preservation/w-closeout-sympy.log"
      notes: "Task 1 commit f99c8c55; captured stdout of script execution; contains SymPy version (1.14.0), Python version (3.14.2), per-test PASS markers (16 total PASS hits, 0 FAIL), final status line 'ALL TESTS PASS', EXIT=0, total elapsed 0.006 s."
    - id: deliv-w-sps-proof
      status: produced
      path: "derivations/paper5-peirce-preservation/w-sps-proof.md"
      notes: "Task 2 commit f07cdc48; 257 lines; Sections 1-6; Section 2 condensed primary route (vdW 2019 Def. 4 + Thm 1, ≤ 2 pages); Section 3 explicit fallback per-axiom table; Section 5 citation inventory with Ch. ≤ 8 verification; Section 6 R11 cross-check identifying S5/S6/S7 as Peirce-invariance touchpoints."
    - id: deliv-ci-sps-morphism
      status: produced
      path: "derivations/paper5-peirce-preservation/ci-sps-morphism.md"
      notes: "Task 3 commit 596650ba; 237 lines; Sections 1-6; (c1)-(c4) each proved in dedicated section; (c2) key identity 1_W = 1_B ⊗ 1_M = 1_{V_{BM}} demonstrated; (c4) shown AUTOMATIC from set-theoretic restriction of ∘_{V_{BM}}; Section 6 free-upgrade statement."
    - id: deliv-three-sense-table
      status: produced
      path: "derivations/paper5-peirce-preservation/carries-three-sense-table.md"
      notes: "Task 4 commit 9b3958ac; 299 lines; Section 1 compressed three-sense definitions (reusing carries-senses.md); Section 2 20-row consumer-by-sense matrix (all 18 downstream-consumer-scan.md argumentative rows covered); Section 3 Phase 56 establishes sense (c) for all; Section 4 L1-L7 revision-text language inventory for Plan 56-03."
  acceptance_tests:
    - id: test-sympy-exit-zero
      outcome: pass
      evidence: "w-closeout-sympy.log tail -1 = 'EXIT=0'; script sys.exit(0) on all-pass code path."
    - id: test-sympy-all-pass
      outcome: pass
      evidence: "grep -c 'PASS' w-closeout-sympy.log = 16 (≥ 5 threshold); grep -c 'FAIL' = 0; all five test names (TEST-CLOSURE, TEST-S1, TEST-S3, TEST-S4, TEST-NEGATIVE) have PASS markers."
    - id: test-sympy-runtime-budget
      outcome: pass
      evidence: "Log line 'TOTAL elapsed: 0.006 s (budget: < 30 s)' — well under budget (0.02% of 30 s)."
    - id: test-sympy-reuses-phase54
      outcome: pass
      evidence: "w-closeout-sympy.py lines 71-106 contain compress(B, i, n) and seq_prod(a_diag_coeffs, B, n) copied verbatim from Phase 54 closeout-sympy.py with attribution comments '# Copied verbatim from derivations/paper5-peirce-preservation/closeout-sympy.py — Phase 54 helper'."
    - id: test-s1-s7-all-axioms-covered
      outcome: pass
      evidence: "w-sps-proof.md Section 3 has 7-row table covering S1, S2, S3, S4, S5, S6, S7 — each with ≥ 3-sentence proof sketch and citation trail in the 'Citations' column."
    - id: test-s1-s7-citation-discipline
      outcome: pass
      evidence: "grep of AlfsenShultz2003 returns 5 hits, all bracketed form `\\cite[Ch.~1, Thm.~1.23]{AlfsenShultz2003}` or structural mentions in frontmatter/section-headings; zero Ch. 9 references outside allowed discipline-statement contexts (e.g., 'Ch. 9 FORBIDDEN' in notes)."
    - id: test-s1-s7-vdw-def-4-anchor
      outcome: pass
      evidence: "w-sps-proof.md Section 2 uses phrase 'vdW 2019 Def. 4' and 'locally tomographic composite' at lines 73, 84, 86, 89, 97, 107, 116, 134, 136, 202 — vdW 2019 Def. 4 is explicitly named as the primary framing of the sense-(b) proof."
    - id: test-s5-s7-lem-peirce-preservation-cited
      outcome: pass
      evidence: "w-sps-proof.md Section 3 axiom rows S5, S6, S7 each cite `\\ref{lem:peirce-preservation}` and `\\ref{ax:S0}` explicitly; Section 6 R11 cross-check tabulates S5/S6/S7 as the Peirce-invariance touchpoints with 'YES' entries."
    - id: test-sense-c-four-conditions
      outcome: pass
      evidence: "ci-sps-morphism.md Sections 2, 3, 4, 5 each contain a dedicated proof of (c1), (c2), (c3), (c4) respectively; Section 3 (c2) explicitly proves 1_W = 1_B ⊗ 1_M ∈ W and ι(1_W) = 1_{V_{BM}}; Section 5 (c4) explicitly proves ∘|_W = set-theoretic restriction of ∘_{V_{BM}}, so ι preserves ∘ automatically."
    - id: test-sense-c-upgrade-note
      outcome: pass
      evidence: "ci-sps-morphism.md Section 6 states: 'Sense (c) per carries-senses.md §3 is ESTABLISHED' and 'In the Paper 5 setting, sense (c) holds freely as a corollary of sense (b)', followed by 'Plan 56-03 revision text may quote sense (c) directly'."
    - id: test-three-sense-row-per-consumer
      outcome: pass
      evidence: "carries-three-sense-table.md Section 2 has 20 rows (grep -c '^| [0-9]' = 20); all 18 argumentative rows from downstream-consumer-scan.md §§2-5 are covered, plus 2 additional split-site rows (theorem statement + proof rows treated separately). Row count check: Section 2 cross-check table confirms every scan row has a matching row here."
    - id: test-three-sense-phase56-establishes-all
      outcome: pass
      evidence: "carries-three-sense-table.md Section 3 explicitly states 'Phase 56 establishes sense (c) for all consumers' and provides the Plan 56-03 quote block. Every row in Section 2 has 'Phase 56 establishes' column = (c)."
  must_surface_refs:
    - id: ref-phase56-plan-56-01
      status: completed
      actions_done: [read]
      notes: "Read Plan 56-01 SUMMARY hand-off block; all routing locked per user's 2026-04-17T19:37:24Z confirmation; applied throughout (sense (b)+(c), direct S1-S7 via vdW 2019 Def. 4, Peirce-1 off-diagonal wedge interpretation)."
    - id: ref-phase56-sympy-design
      status: completed
      actions_done: [read, use]
      notes: "Plan 56-01 sympy-design.md §§2-5 implemented in w-closeout-sympy.py Task 1: V_test = H_3(R) ⊗ H_3(R), W_full = 36-dim, W_wedge = 9-dim Peirce-1 off-diagonal (Interpretation A), 5 test cases."
    - id: ref-phase56-face-status
      status: completed
      actions_done: [read]
      notes: "w-face-status.md verdict = NOT-FACE honored: Plan 56-02 uses direct S1-S7 on W via vdW 2019 Def. 4 regardless (primary route), not face-restriction shortcut."
    - id: ref-phase56-carries-senses
      status: completed
      actions_done: [read, cite]
      notes: "carries-senses.md §§1-5 cited throughout: every 'carries' usage in the three new artifacts is sense-tagged per carries-senses.md discipline."
    - id: ref-phase56-consumer-scan
      status: completed
      actions_done: [read]
      notes: "downstream-consumer-scan.md §§2-5 consumer list transcribed to carries-three-sense-table.md Section 2 (20 rows)."
    - id: ref-phase56-identity
      status: completed
      actions_done: [read]
      notes: "thm-5-8-identity-verbatim.md Sections 2-3 verbatim quotes (composite-lt.tex:203-221, appendix-proofs.tex:228-238) are the target identity locked by w-sps-proof.md Section 1 Statement."
    - id: ref-vdw-2019
      status: completed
      actions_done: [cite]
      notes: "Cited in w-sps-proof.md (Def. 2 S1-S7, Def. 4, Thm 1) and ci-sps-morphism.md (Def. 2 referenced via w-sps-proof.md)."
    - id: ref-as-2003
      status: completed
      actions_done: [cite]
      notes: "Cited in w-sps-proof.md S4 row: `\\cite[Ch.~1, Thm.~1.23]{AlfsenShultz2003}` (state separation). Ch. 1 ≤ 8 ✓. Zero Ch. 9 references."
    - id: ref-phase54-lemma
      status: completed
      actions_done: [cite]
      notes: "`\\ref{lem:peirce-preservation}` cited in w-sps-proof.md S5, S6, S7 axiom rows + Section 6 R11 cross-check."
    - id: ref-phase54-s0
      status: completed
      actions_done: [cite]
      notes: "`\\ref{ax:S0}` cited in w-sps-proof.md S5, S6, S7 axiom rows via the compatibility-reduction step."
    - id: ref-composite-lt-prop-inheritance
      status: completed
      actions_done: [cite]
      notes: "`prop:inheritance` (composite-lt.tex L67-90) referenced in w-sps-proof.md Section 3 S1 row and S4 row; Phase 56 reuses the proof structure at the W-level."
    - id: ref-phase54-closeout-sympy
      status: completed
      actions_done: [read, use]
      notes: "derivations/paper5-peirce-preservation/closeout-sympy.py compress+seq_prod helpers copied verbatim into w-closeout-sympy.py with attribution comments."
    - id: ref-phase55-s4-sympy
      status: completed
      actions_done: [read]
      notes: "derivations/paper5-peirce-preservation/s4-sympy-spot-check.py pattern (symbolic-exact, sp.simplify assertion idiom) mirrored in w-closeout-sympy.py test functions."
    - id: ref-bgw-2020
      status: completed
      actions_done: [cite]
      notes: "Cited in ci-sps-morphism.md Section 1 as the source of the SPS-morphism definition (§2 of BGW 2020)."
  forbidden_proxies:
    - id: fp-sympy-mock-pass
      outcome: rejected
      evidence: "Actual log file derivations/paper5-peirce-preservation/w-closeout-sympy.log captures SymPy version, Python version, per-test timings (all ≤ 0.002 s), final EXIT=0. Task 1 executed the script and captured output — no mock PASS."
    - id: fp-s1-s7-skip-axiom
      outcome: rejected
      evidence: "w-sps-proof.md Section 3 table has all 7 rows S1-S7 with ≥ 3-sentence proof sketch and explicit citation per axiom. No axiom is declared 'trivially factor-level' without citation."
    - id: fp-ch-9-leak
      outcome: rejected
      evidence: "Only A-S 2003 citation in the three .md artifacts is `\\cite[Ch.~1, Thm.~1.23]{AlfsenShultz2003}`. Grep for `Ch.~9` returns only zero-hit verification lines. No out-of-scope Ch. 9 references."
    - id: fp-r11-implicit-peirce
      outcome: rejected
      evidence: "S5, S6, S7 in w-sps-proof.md each explicitly cite `\\ref{lem:peirce-preservation}` + `\\ref{ax:S0}`. S4 explicitly does NOT use Peirce invariance (state separation via A-S 2003 Thm 1.23 instead). Section 6 R11 cross-check tabulates exactly which axioms touch Peirce invariance."
    - id: fp-sense-c-claim-without-c4-proof
      outcome: rejected
      evidence: "ci-sps-morphism.md Section 5 contains full (c4) proof showing ι(a ∘|_W b) = ι(a) ∘_{V_{BM}} ι(b) via set-theoretic restriction; both sides reduce to the same element of V_{BM}."
    - id: fp-three-sense-table-single-sense-default
      outcome: rejected
      evidence: "carries-three-sense-table.md Section 3 explicitly states 'Phase 56 establishes sense (c) for all consumers' (not (b) default). Every Section 2 row has 'Phase 56 establishes' = (c)."
    - id: fp-frozen-file-edit
      outcome: rejected
      evidence: "`git -C /Users/ehrlich/repos/blog diff --stat HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` returns empty at Task 1 start and Task 5 close. `git diff` on living paper files also empty — Plan 56-02 writes zero paper-file diffs."
  uncertainty_markers:
    weakest_anchors:
      - "Paper 5 §4 `prop:inheritance` proof is the factor-level S1-S7 source. Its sign conventions and measure-theoretic details are not re-verified in Plan 56-02; Phase 54 + Phase 55 audited the relevant §S4 and Peirce regions, but the non-S4 parts of `prop:inheritance` (S1, S3 proofs in particular) are consumed as a black box. Risk: low — the proof structure at composite-lt.tex L67-90 is straightforward bilinearity + factor-level axioms."
      - "vdW 2019 Definition 4 'locally tomographic composite' is invoked as a STRUCTURE-PRESERVATION theorem: if V_B and V_M are SPSs, then V_B ⊗_R V_M is also an SPS. Verification: the text of Def. 4 in arXiv:1803.11139 is cited but not re-proved. Risk: low — Def. 4 is a standard construction, and vdW 2019 Thm 1 applies straightforwardly."
      - "SymPy spot-check covers sense-(a) closure + factor-level S1 bilinearity + S3 unitality + S4 orthogonality symmetry on H_3(R) ⊗ H_3(R) but does NOT directly exercise S5, S6, S7 (these are treated as factor-level reductions with Peirce invariance). Risk: low — Phase 54 C-i closeout-sympy.py already verified Peirce invariance on H_3(R) and H_4(R)."
    disconfirming_observations:
      - "None surfaced. If Plan 56-03 discovers that the `sms:minimal` clause requires sense (c) strictly (not (b)), the current proof still satisfies it via the free corollary. If a new §5/§6 consumer requires only sense (a), the proof strictly over-delivers but does not weaken."
  links:
    - id: link-sympy-feeds-proof
      source: deliv-w-closeout-log
      target: deliv-w-sps-proof
      relation: supports
      verified_by: [test-sympy-all-pass, test-s1-s7-all-axioms-covered]
    - id: link-carries-senses-feeds-proof
      source: ref-phase56-carries-senses
      target: deliv-w-sps-proof
      relation: depends_on
      verified_by: [test-s1-s7-vdw-def-4-anchor]
    - id: link-proof-feeds-morphism
      source: deliv-w-sps-proof
      target: deliv-ci-sps-morphism
      relation: supports
      verified_by: [test-sense-c-four-conditions, test-sense-c-upgrade-note]
    - id: link-morphism-feeds-table
      source: deliv-ci-sps-morphism
      target: deliv-three-sense-table
      relation: supports
      verified_by: [test-three-sense-phase56-establishes-all]
    - id: link-consumer-scan-feeds-table
      source: ref-phase56-consumer-scan
      target: deliv-three-sense-table
      relation: depends_on
      verified_by: [test-three-sense-row-per-consumer]
comparison_verdicts:
  - id: vd-phase56-vs-prop-inheritance
    kind: internal-reuse
    proof_structure_matches: "Section 3 S4 row in w-sps-proof.md reuses `prop:inheritance` proof at composite-lt.tex L81-90 verbatim pattern: state separation + orthogonality symmetry at factor level."
    verdict: CONSISTENT
    notes: "Plan 56-02's S4-on-W proof pattern is identical to Paper 5 §4's S4-on-V_{BM} proof pattern. This is deliberate: Phase 56 reuses the established proof structure, applied to W in place of V_{BM}. No convention drift."
  - id: vd-phase56-vs-phase54-ci
    kind: cross-phase
    match: "w-sps-proof.md Section 6 R11 cross-check names S5/S6/S7 as the Peirce-invariance touchpoints, citing `\\ref{lem:peirce-preservation}` (Phase 54 C-i) + `\\ref{ax:S0}` (Phase 54 S0 axiom)."
    verdict: CONSISTENT
    notes: "Phase 54 (C-i) made Peirce invariance conditional on S0; Plan 56-02's S5/S6/S7 proofs honor this conditionality without introducing unconditional use. Zero circularity."
  - id: vd-phase56-vs-plan-56-01-routing
    kind: same-phase
    match: "All three Plan 56-01 routing decisions (sense (b)+(c), direct S1-S7 via vdW 2019 Def. 4, Peirce-1 off-diagonal wedge interpretation) are honored throughout Plan 56-02."
    verdict: CONSISTENT
    notes: "User-confirmed routing from 2026-04-17T19:37:24Z applied without deviation."
---

# Plan 56-02 SUMMARY — Sense (b) + Sense (c) ESTABLISHED on W

## Outcome

**SENSE-(b)-AND-(c)-ESTABLISHED.** All 5 tasks complete.

`(W, ∘|_W)` is a finite-dim sequential product space (sense (b) per
`carries-senses.md §2`) proven via vdW 2019 Def. 4 + Thm 1 (primary route,
Section 2 of w-sps-proof.md, ≤ 2 pages) with a fallback per-axiom table
(Section 3). The inclusion `ι : W ↪ V_{BM}` is an SPS-morphism (sense (c)
per `carries-senses.md §3`) proven in ci-sps-morphism.md — the upgrade from
(b) to (c) is free because `1_W = 1_{V_{BM}}` and `∘|_W` is a set-theoretic
restriction of `∘_{V_{BM}}`. SymPy H_3(ℝ) ⊗ H_3(ℝ) certificate (5/5 PASS in
0.006 s, exit 0) validates the small-case grounding.

**All 18+ §5/§6 downstream consumers (per Plan 56-01 downstream-consumer-scan.md)
are served at sense (c)** — the strongest of the three senses — since sense (c)
⇒ (b) ⇒ (a) by the collapse diagram of `carries-senses.md §4`.

## One-liner

Phase 56-02 COMPLETE: (W, ∘|_W) is an SPS (sense (b)) via vdW 2019 Def. 4 +
Thm 1; ι: W ↪ V_{BM} is an SPS-morphism (sense (c)) as free corollary since
1_W = 1_V and ∘|_W is set-theoretic restriction; SymPy H_3(R)⊗H_3(R)
certificate 5/5 PASS in 0.006 s; Plan 56-03 revision-text L1-L7 phrase
inventory staged for composite-lt.tex:203-221 + appendix-proofs.tex:228-238.

## Artifact Inventory

| # | Artifact | Path | Commit | Lines | Role |
|---|---|---|---|---|---|
| 1 | w-closeout-sympy.py | `derivations/paper5-peirce-preservation/w-closeout-sympy.py` | f99c8c55 | 564 | Executable SymPy spot-check; reuses Phase 54 helpers; 5 tests + main runner. |
| 2 | w-closeout-sympy.log | `derivations/paper5-peirce-preservation/w-closeout-sympy.log` | f99c8c55 | 35 | Captured stdout: Python 3.14.2, SymPy 1.14.0, 5/5 PASS, exit 0, elapsed 0.006 s. |
| 3 | w-sps-proof.md | `derivations/paper5-peirce-preservation/w-sps-proof.md` | f07cdc48 | 257 | Sense (b) proof: Section 2 primary route (vdW 2019 Def. 4 + Thm 1); Section 3 fallback per-axiom table (S1-S7); Section 6 R11 cross-check. |
| 4 | ci-sps-morphism.md | `derivations/paper5-peirce-preservation/ci-sps-morphism.md` | 596650ba | 237 | Sense (c) upgrade: (c1)-(c4) each in dedicated section; 1_W = 1_{V_{BM}} + ∘|_W restriction = free upgrade. |
| 5 | carries-three-sense-table.md | `derivations/paper5-peirce-preservation/carries-three-sense-table.md` | 9b3958ac | 299 | R7 mitigation: 20-row consumer × sense matrix; Phase 56 establishes (c) for all; L1-L7 revision-text language inventory. |

## Hand-off block for Plan 56-03

```
PLAN 56-02 SEAL — 2026-04-17 (Phase 56 Wave 2 close)

SENSE ESTABLISHED
  Core:            (b) induced-structure SPS per carries-senses.md §2
  Free corollary:  (c) functorial SPS-morphism per carries-senses.md §3
                   (since 1_W = 1_{V_{BM}} and ∘|_W = set-theoretic restriction)

PROOF SOURCES FOR PLAN 56-03 REVISION TEXT
  - w-sps-proof.md §2 (PRIMARY ROUTE; vdW 2019 Def. 4 + Thm 1; ≤ 2 pages)
    Use this for the compact composite-lt.tex:204-221 integration.
  - w-sps-proof.md §3 (FALLBACK ROUTE; per-axiom S1-S7 table)
    Include as appendix / supplementary for deep-dive referees.
  - ci-sps-morphism.md §1-6 (sense (c) upgrade)
    Quote Section 6 statement for the cheap-upgrade paragraph.
  - carries-three-sense-table.md §4 (revision-text language inventory L1-L7)
    Selection policy: L5 for composite-lt.tex:204-221; L6 for sms:minimal
    restatement; L7 for appendix-proofs.tex:228-238.

REVISION-TEXT INTEGRATION SITES (from Plan 56-01 downstream-consumer-scan.md)
  - composite-lt.tex:204-221 (upper-bound step of thm:local-tomo; LIVING)
  - appendix-proofs.tex:228-238 (upper-bound step of thm:lt-full; LIVING)
  - Line numbers may drift between Plan 56-02 and Plan 56-03 due to text edits;
    Plan 56-03 must re-locate the semantic anchor ("upper bound. Let W ⊆ V_{BM}...")
    and substitute accordingly.

SYMPY CERTIFICATE (for any reproducibility / reviewer challenge)
  - Script: derivations/paper5-peirce-preservation/w-closeout-sympy.py
  - Log:    derivations/paper5-peirce-preservation/w-closeout-sympy.log
  - Verdict: 5/5 PASS, exit 0, 0.006 s runtime, Python 3.14.2 / SymPy 1.14.0

FROZEN-FILE DISCIPLINE
  - main-jmp-submitted.tex: ZERO-DIFF preserved (git tag paper5-jmp-submitted).
  - No blog repo files touched by Plan 56-02.
  - Plan 56-03 IS the paper-integration plan; Plan 56-02 is proof-artifacts only.

SCOPE BOUNDARY FOR PLAN 56-03
  - Plan 56-03 MAY write to:
      * /Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/sections/composite-lt.tex
      * /Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/sections/appendix-proofs.tex
      * Related bibliography entries if vdW 2019 / BGW 2020 keys need updating
  - Plan 56-03 MUST NOT touch main-jmp-submitted.tex (frozen).

CAVEAT TO TRACK IN PLAN 56-03 CONTRACT
  - Per ci-sps-morphism.md §5 caveat: Plan 56-03 revision text MUST define
    ∘|_W as the set-theoretic restriction of ∘_{V_{BM}}, NOT as a new
    W-internal formula. If an alternative internal definition is introduced,
    (c4) requires additional proof showing internal and restricted operations
    coincide. Current proof does NOT supply that additional argument.

R11 CROSS-PHASE CASCADE (Phase 54 C-i ↔ Plan 56-02)
  - S5/S6/S7 on W each cite \ref{lem:peirce-preservation} + \ref{ax:S0}.
  - S4 on W does NOT use Peirce invariance (state separation via A-S 2003
    Thm 1.23 only).
  - S1/S2/S3 on W do NOT touch Peirce invariance.
  - No implicit Peirce invariance used anywhere in the proof; all uses
    bracketed.
```

## Forbidden-proxy rejections (plan-level)

| Proxy | Outcome | Evidence |
|---|---|---|
| fp-sympy-mock-pass | REJECTED | Actual log file with SymPy version, Python version, per-test timings, EXIT=0; see `w-closeout-sympy.log`. |
| fp-s1-s7-skip-axiom | REJECTED | w-sps-proof.md Section 3 has all 7 axioms S1-S7 covered with proof sketches + citations. |
| fp-ch-9-leak | REJECTED | Only A-S citation is `\cite[Ch.~1, Thm.~1.23]{AlfsenShultz2003}`. Zero Ch. 9 argumentative references. |
| fp-r11-implicit-peirce | REJECTED | S5/S6/S7 explicitly cite `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`; S4 explicitly uses state separation (NOT Peirce). |
| fp-sense-c-claim-without-c4-proof | REJECTED | ci-sps-morphism.md Section 5 contains explicit (c4) proof via set-theoretic restriction. |
| fp-three-sense-table-single-sense-default | REJECTED | carries-three-sense-table.md Section 3 claims sense (c) for all; every row in Section 2 has (c) in Phase-56-establishes column. |
| fp-frozen-file-edit | REJECTED | Zero-diff verified at Task 1 start and Task 5 pre-commit; living paper files also zero-diff. |

## Deviations

None. All 5 tasks executed per plan specification. No deviation rules (1-6)
triggered. No context-pressure forced checkpoint (remained in GREEN/YELLOW
throughout, never hit ORANGE).

## Conventions (active throughout)

- **A-S citation discipline:** Ch. ≤ 8 only; bracketed form `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` (inherited from Phase 55 Flag 4.1).
- **Allowed axiom scope:** `{S0, S1-S7, linearity of L_a, A-S 2003 Ch. 2/7/8, finite-dim spectrality}`.
- **W definition:** `W := span_R{a_i ⊗ b_j : a_i basis V_B, b_j basis V_M} ⊆ V_{BM}`.
- **Restriction product:** `∘|_W := ∘_{V_{BM}} |_{[0,1]_W × [0,1]_W}` (set-theoretic).
- **Sense framework:** carries-senses.md is the authoritative reference for (a)/(b)/(c).
- **Peirce-invariance citation pattern:** `\ref{lem:peirce-preservation}` resting on `\ref{ax:S0}` (Phase 54 C-i).
- **Jordan product:** `a ∘ b = (1/2)(ab + ba)` (from state.json convention_lock custom_conventions).
- **Peirce eigenvalues:** `{0, 1/2, 1}` (from state.json convention_lock).

## Frozen-file discipline

Verified at three points during Plan 56-02:
1. Task 1 start — `git -C /Users/ehrlich/repos/blog diff --stat HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` returned empty.
2. Task 5 pre-checkpoint — same command returned empty.
3. Task 5 close — also empty.

`main-jmp-submitted.tex` remains at git tag `paper5-jmp-submitted` with no
modifications. Living paper files (`main.tex`, `sections/*.tex`) also
unmodified — Plan 56-02 writes zero paper-file diffs.

## Self-Check: PASSED

- [x] SymPy script exists and executes (exit 0, 5/5 PASS, 0.006 s).
- [x] w-sps-proof.md has Sections 1-6; Section 2 invokes vdW 2019 Def. 4 + Thm 1; Section 3 covers S1-S7 with per-axiom citations; Section 6 R11 cross-check documents S5/S6/S7 as Peirce touchpoints.
- [x] ci-sps-morphism.md has Sections 1-6; (c1)-(c4) proved; Section 6 states cheap upgrade.
- [x] carries-three-sense-table.md has 20-row matrix covering all 18 downstream-consumer-scan.md argumentative rows; Section 3 claims sense (c) for all; Section 4 has 7-phrase revision-text inventory.
- [x] A-S citation discipline: only Ch. 1 Thm 1.23 used; bracketed; zero Ch. 9 refs.
- [x] Forbidden-token scan: zero hits outside transcription/declaration scope.
- [x] R11 cross-phase: S5/S6/S7 cite `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`; S4 uses state separation (NOT Peirce).
- [x] Frozen-file: `main-jmp-submitted.tex` zero-diff preserved.
- [x] Living paper files: zero-diff preserved (Plan 56-03 handles integration).
- [x] Contract coverage: every claim has contract_results.claims entry; every deliverable has produced status + path; every acceptance test has outcome + evidence; every must-surface ref has completed status; every forbidden proxy explicitly rejected with evidence; every comparison verdict recorded.
- [x] All five tasks committed individually (f99c8c55, f07cdc48, 596650ba, 9b3958ac; Task 5 commit follows this SUMMARY).

## Structured return envelope

```yaml
gpd_return:
  status: completed
  files_written:
    - derivations/paper5-peirce-preservation/w-closeout-sympy.py
    - derivations/paper5-peirce-preservation/w-closeout-sympy.log
    - derivations/paper5-peirce-preservation/w-sps-proof.md
    - derivations/paper5-peirce-preservation/ci-sps-morphism.md
    - derivations/paper5-peirce-preservation/carries-three-sense-table.md
    - .gpd/phases/56-thm-5-8-upper-bound-w-carries-product-form-sequential-product/56-02-SUMMARY.md
  issues: []
  next_actions:
    - "Plan 56-03: integrate revised proof text into composite-lt.tex:203-221 + appendix-proofs.tex:228-238 using language inventory L1-L7 from carries-three-sense-table.md §4 (recommended: L5 for composite-lt, L6 for sms:minimal restatement, L7 for appendix)."
    - "Plan 56-03 contract MUST track the ci-sps-morphism.md §5 caveat: define ∘|_W as set-theoretic restriction only; do NOT introduce alternative W-internal formula."
    - "Phase 56 close: update STATE.md with Plan 56-02 completion; Plan 56-03 becomes next executable."
  phase: "56-thm-5-8-upper-bound-w-carries-product-form-sequential-product"
  plan: "02"
  tasks_completed: 5
  tasks_total: 5
  duration_seconds: 360
  state_updates:
    current_plan: "02 -> 03 pending"
    last_activity: "2026-04-17 Plan 56-02 complete: sense (b)+(c) established on W; SymPy certificate 5/5 PASS; R7 mitigation table built; hand-off to Plan 56-03 staged"
    intermediate_results:
      - "Plan 56-02 SEAL: sense (b) via vdW 2019 Def. 4 + Thm 1; sense (c) free-corollary via 1_W = 1_V and set-theoretic restriction of ∘|_W. 5 artifacts committed (commits f99c8c55, f07cdc48, 596650ba, 9b3958ac, and Task 5 final)."
  metrics:
    label: "Phase 56 P56-02"
    tasks: 5
    files: 6
    sympy_runtime_sec: 0.006
    sympy_tests_passed: 5
    sympy_tests_total: 5
    axioms_covered: "S1-S7 (per-axiom fallback table) + vdW Def. 4 + Thm 1 primary route"
    sense_established: "(b) core + (c) free corollary"
    frozen_file_zero_diff: true
```
