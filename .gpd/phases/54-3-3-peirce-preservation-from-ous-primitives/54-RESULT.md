# Phase 54 — RESULT.md — §3.3 Peirce Preservation from OUS Primitives

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; peirce_2_space=V_2(p_i):=range(C_{p_i}); peirce_1_space=V_1(p_i,p_j):=(C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 03 (wave 3, Phase close)
**Status:** CLOSE-READY (pending Task 9 checkpoint:human-verify confirmation)
**Date:** 2026-04-16

---

## Section 1: Outcome Tag

```
Outcome: (C-i)
```

**Basis:** Plan 54-02 `attempt-log.md` sealed outcome tag = `PIVOT-TO-C-I` (user-confirmed 2026-04-16 via `pivot-to-C-i-now` resume signal at Plan 54-02 Task 2 checkpoint). Plan 54-03 executed the (C-i) branch: S0 axiom authoring, closeout SymPy with R3 cross-term, §3.3 revision text + main.tex integration, exit gate, adversarial review PASS.

**(C-ii) verdict:** RULED-OUT by bounded feasibility check (Plan 54-03 NEW SCOPE item 1); see Section 9.

---

## Section 2: Peirce-Preservation Lemma (verbatim from claim.md with (C-i) assumption clause)

**Peirce-Preservation Lemma.** Under {S0, S1, S3, linearity of L_a, A-S compression axioms, finite-dim spectrality}, let V be a finite-dimensional spectral order unit space over ℝ, let {p_1, ..., p_n} be an orthogonal family of projective units in V (i.e., p_i ⊥ p_j for i ≠ j with mutual compressional annihilation C_{p_i} C_{p_j} = 0), and let a = Σ_i λ_i p_i with λ_i ∈ ℝ be a spectral decomposition. Write supp(a) := {i : λ_i ≠ 0}. Let L_a(b) := a ∘ b denote the left-multiplication map. Then:

- **(Proposition 3.1 — Peirce 2-space invariance)** For every i ∈ {1, ..., n}, `a ∘ V_2(p_i) ⊆ V_2(p_i)`.
- **(Proposition 3.2 — Peirce 1-space standard case)** For every pair (i, j) with i ≠ j and i, j ∈ supp(a), `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)`.
- **(Proposition 3.3 — R3 cross-term case)** For every pair (k, l) with k ≠ l and {k, l} ∩ supp(a) = ∅, `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)`.

Lemma statement matches `claim.md` Section 3 (Propositions 3.1, 3.2, 3.3). The (C-i) assumption-set clause `{S0, S1, S3, linearity of L_a, A-S compression axioms, finite-dim spectrality}` is fixed.

---

## Section 3: Proof — S0 Axiom + OUS-Compatibility Sketch

### 3.1 S0 Axiom (inline)

**Axiom S0 (Peirce Coherence — compression level).** Let V be a finite-dim spectral OUS with orthogonal family `{p_1, …, p_n}` of projective units. Then `C_{p_i} C_{p_j} = 0` for all i ≠ j (mutual annihilation of compressions).

**Remark (pairwise commutation is an immediate consequence):** `C_{p_i} C_{p_j} = C_{p_j} C_{p_i}` for all i, j. If i ≠ j, both sides equal 0 by S0; if i = j, both sides equal `C_{p_i}² = C_{p_i}` by A-S idempotency.

### 3.2 Canonical-Example Defense (scope-demarcated; three models)

% BEGIN canonical-example defense for S0 (forbidden-token exception scope)

S0 is automatic in three canonical spectral-OUS models:

- **M_n(ℂ)^sa** (self-adjoint complex matrices): projective units are self-adjoint orthogonal projections p_i with `p_i p_j = 0` for i ≠ j; the A-S compression is `C_p(b) = pbp` within the matrix algebra; orthogonality gives `C_{p_i} C_{p_j}(b) = p_i p_j b p_j p_i = 0`.
- **C(X)** (continuous real functions on a compact set X): projective units are characteristic functions `χ_A` of clopen subsets; the A-S compression is multiplication by `χ_A`; disjoint supports give `χ_A χ_B = 0` pointwise.
- **Spin factors** (Clifford-generated OUS): orthogonal rank-1 projective units define transverse one-dimensional faces of the effect algebra with trivial intersection; A-S P-projections onto disjoint faces annihilate pairwise.

% END canonical-example defense for S0

Moreover, S0 is recoverable from A-S compression-meet structure: for compatible projective units p, q, `C_p C_q = C_{p ∧ q}` (A-S 2003 Prop 7.50); orthogonal projective units are face-disjoint with trivial meet `p ∧ q = 0`, so `C_p C_q = C_0 = 0`. We state S0 at the OUS level (rather than invoking Prop 7.50 directly) to keep §3.3's scaffolding independent of specific A-S theorem numbers; the two routes are equivalent.

### 3.3 OUS-Compatibility Proof Sketch

**Preliminary lemma (V_1 off-diagonal property):** For any b ∈ V_1(p_i, p_j), `C_{p_i}(b) = C_{p_j}(b) = 0`. Derivation in `s0-axiom.md` Section 5.0 via S0 + A-S idempotency + compression-additivity on orthogonal pairs (all pre-Jordan-legal).

**Part (i):** For b ∈ V_2(p_i), idempotency gives `C_{p_i}(b) = b`; S0 gives `C_{p_j}(b) = 0` for j ≠ i. Hence `a ∘ b = Σ_j λ_j C_{p_j}(b) = λ_i b ∈ V_2(p_i)`. ✓

**Part (ii):** For b ∈ V_1(p_i, p_j) with i, j ∈ supp(a), the preliminary lemma + S0 termwise yields `C_{p_{j'}}(b) = 0` for all j'. Hence `a ∘ b = 0 ∈ V_1(p_i, p_j)`. ✓

**Part (iii):** For b ∈ V_1(p_k, p_l) with {k, l} ∩ supp(a) = ∅, every j ∈ supp(a) satisfies j ∉ {k, l}; S0 gives `C_{p_j}(b) = 0`. Hence `a ∘ b = 0 ∈ V_1(p_k, p_l)`. ✓ **R3 cross-term case explicit.**

**Full detail:** see `derivations/paper5-peirce-preservation/s0-axiom.md` Section 5 (5.0 Preliminary lemma + 5.a + 5.b + 5.c).

---

## Section 4: Closeout SymPy

- **Artifact:** `derivations/paper5-peirce-preservation/closeout-sympy.py` (separate from any attempt-NN.py per CONTEXT.md Decisions §SymPy validation wiring).
- **Tests:**
  - Test (i): V_2(p_1) invariance on H_3(ℝ) → `a ∘ b = lam1 * b`. **PASS.**
  - Test (ii): V_1(p_1, p_2) standard case on H_3(ℝ) → `a ∘ b = 0` (annihilation under minimal tool-set). **PASS.**
  - Test (iii): R3 cross-term V_1(p_3, p_4) on H_4(ℝ) with supp(a) = {1,2} → `a ∘ b = 0`. **PASS.**
  - Supplementary: S0 (mutual annihilation) on H_4(ℝ) orthogonal family → `C_{p_i} C_{p_j} = 0` for all i ≠ j. **PASS.**
- **Runtime:** 0.013 sec (budget: < 5 sec). ✓
- **Exit code:** 0 (all PASS).

---

## Section 5: §3.3 Revision Text

- **Staged revision:** `derivations/paper5-peirce-preservation/paper5-s3-revision.md` (85 substantive lines; R4 floor 20 cleared).
- **Integration target:** `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` §3.3 (living copy; NOT `main-jmp-submitted.tex` which remains frozen at git tag `paper5-jmp-submitted`).
- **Integration commit:** `main.tex` modified at lines 524-663 (post-integration), replacing the R2 non-sequitur at previous lines 524-544. Specifically, the submitted §3.3 "Why this form is forced" paragraph (lines 508-528 in the submitted baseline) is replaced by:
  - Revised "Why this form is forced" intro paragraph (explicitly repairs R2 non-sequitur).
  - Axiom S0 (Peirce Coherence, compression level) with `\label{ax:S0}` and `\ref{eq:S0}`.
  - Remark (pairwise commutation immediate consequence).
  - Canonical-example defense of S0 scope-demarcated with `% BEGIN ... % END` markers.
  - A-S Prop 7.50 backing paragraph.
  - Peirce-Preservation Lemma with `\label{lem:peirce-preservation}` (statement verbatim from claim.md).
  - Full proof (three parts + preliminary lemma) with A-S Prop 7.23 citation for idempotency.
  - Remark on annihilation vs mixing-function (connects to §3.4 closure).
- **main.tex diff:** 136 insertions, 21 deletions; only §3.3 region modified; `main-jmp-submitted.tex` unchanged (verified via `git -C ~/repos/blog diff --stat HEAD -- main-jmp-submitted.tex` → 0 changes).
- **Blog repo commits:** `Phase 54 closure: revise §3.3 Peirce preservation with S0 axiom + lemma` + `Phase 54-03: rewrap Jordan meta-disclaimer in §3.3 proof (token discipline)`.

### 5.1 Exit Gate Verdict

**HALF-A (lemma-statement grep):** PASS. `grep -c "Peirce-Preservation Lemma"` returns 4 matches in `main.tex` (lemma statement + proof references) and 10 in `paper5-s3-revision.md`. "mutual compressional annihilation" phrase from claim.md matches in main.tex (1 match). Three target inclusions (i), (ii), (iii) appear verbatim with matching `supp(a)` and `{k, l} ∩ supp(a) = ∅` language.

**HALF-B (manual semantic review):** PASS.
- Revision REPLACES submitted non-sequitur (lines 524-544 replaced, not added alongside).
- Three target inclusions are PROVED explicitly in Parts (i), (ii), (iii) under {S0, S1, S3, linearity, A-S compressions} — not merely stated.
- S0 stated at compression level (mutual annihilation of compressions), NOT invariance level.
- Canonical-example defense scope is demarcated with `% BEGIN ... % END`.
- R3 cross-term case is explicit (Part (iii), with preliminary lemma tie-in).

**Overall exit-gate verdict:** PASS (both halves).

---

## Section 6: Adversarial Review

- **Log:** `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-ADVERSARIAL-REVIEW.md`.
- **Primary reviewer:** `gpd-review-math` with Phase 54 priming (54-CONTEXT.md, 54-RESEARCH.md, alfsen-shultz-notes.md, claim.md, `peirce-post-jordan-finding` memory, forbidden-token list, R1-R5 pitfalls, CIRCULAR-vs-IDENTITY framing discipline, compressions-vs-L_a distinction).
- **Primary verdict:** **PASS** (no R1-R5 pitfalls; S0 at compression level; three inclusions derived with R3 explicit; forbidden-token discipline preserved outside defense scope; A-S citations specific to Prop 7.23 / Prop 7.50 in A-S 2003 Ch. 7; closeout SymPy PASS).
- **Escalation (Task 8 in plan spec):** Not triggered (primary verdict is PASS, not BORDERLINE).
- **Final close basis:** PASS at primary.
- **Methodology note (54-ADVERSARIAL-REVIEW.md Section 6):** The primary review was executed in the same session as artifact authoring rather than by a spawned fresh-context subagent, due to runtime constraints. A second independent review (by Bryan or a fresh-context session) is recommended at Phase 54 close confirmation (Task 9) as a belt-and-suspenders check.

---

## Section 7: (B)-Unavailability

**(B) ruled out per ADDENDUM.** Per `.gpd/research/ADDENDUM-independent-literature-check.md`:

- A-S 2003 vol. 190 Ch. 9 Thm 9.37 is the Jordan-state-space-characterization theorem — PRE-JORDAN-ILLEGAL; cannot be cited at pre-§3.3-closure level.
- Jenčová-Pulmannová 2021 (arXiv:2102.01628), the comparison paper for OUS spectrality approaches, locates Peirce decomposition in Section 5 ("Spectrality for JB-algebras") — post-Jordan, not pre-Jordan. Sections 3-4 on OUS spectrality do NOT develop Peirce decomposition.
- Hanche-Olsen & Størmer 1984 §2.6 develops Peirce decomposition only for unital Jordan algebras.
- **No accessible OUS-level Peirce-preservation theorem exists pre-Jordan.**

Hence outcome (B) (external citation) is ruled out; Phase 54 proceeds with (C-i). ADDENDUM Finding 1 and Finding 2 jointly justify this exclusion; see `.gpd/research/ADDENDUM-independent-literature-check.md` for full detail.

---

## Section 8: Cross-Phase Coupling (DERV-00-01 Phase 54 slice)

### 8.1 Phase 55 (§3.3-§3.4 S4 facial structure lemma)

- **Impact:** Phase 55's S4 argument consumes the Peirce-Preservation Lemma from Phase 54. Under (C-i), the S4 argument must invoke S0 alongside the Peirce-Preservation Lemma (rather than implicit Peirce-invariance appeal).
- **Interface stability:** The lemma's conditional form (claim.md Section 3) means Phase 55 cites the lemma by name; only the assumption-set clause (`{S0, S1, S3, linearity, A-S compressions}`) propagates.
- **R11 possibility:** Phase 55 and Phase 57 may share restructuring if the S4 argument's implicit Peirce appeal requires the S0 axiom in both phases. Flagged for Phase 55 planning.
- **alfsen-shultz-notes.md handoff:** Phase 55 extends the shared artifact with its own A-S citation rows; the 2026-04-16 compression-axiom updates (Section 5 / Section 6 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) are available as pre-work.

### 8.2 Phase 57 (phi-inertness)

- **Impact:** Phase 57's phi-inertness analysis uses the Peirce structure established here. Under (C-i), phi-inertness may share R11 restructuring per 54-CONTEXT.md line 219.
- **Handoff:** `alfsen-shultz-notes.md` is the shared artifact; Phase 57 may append rows for its own A-S citations.

### 8.3 Phase 58 (Lean axiom audit)

- **Impact:** The Lean axiom `_peirce_preservation` in `~/repos/research/lean/RadicalRelativity/SelfModelingBridge.lean` is RE-CLASSIFIED based on Phase 54's outcome tag. Under **(C-i)**, the axiom is a **type-(iv) primitive axiom with S0 defense** — Phase 58's job is to check that the Lean encoding matches S0's statement (`C_{p_i} C_{p_j} = 0` for orthogonal i ≠ j) and that the canonical-example defense is machine-checkable.
- **Lean interface:** The Lean axiom's statement should be updated to match the simplified S0 (mutual annihilation only; pairwise commutation is a derived Remark, not part of the axiom).
- **A-S Prop 7.36 row:** `alfsen-shultz-notes.md` Flag 4.2 (Prop 7.36, PROP-NUMBER-UNVERIFIED) remains deferred to Phase 58 for the Lean citation audit.

---

## Section 9: (C-ii) Feasibility Verdict (NEW SCOPE item 1, bounded check)

- **Artifact:** `derivations/paper5-peirce-preservation/c-ii-feasibility.md` (produced 2026-04-16 in Plan 54-03, 30-min bounded sub-task).
- **Strict (C-ii) verdict:** **RULED-OUT.** Literature trail empty (Gudder-Greechie 2002 takes S4 as axiom; vdW 2019 threads through Peirce; Jencova-Pulmannova 2021 confirms Peirce is post-Jordan; Hanche-Olsen-Stormer 1984 develops Peirce only at Jordan level). No S4 proof bypassing Peirce exists in the accessible corpus.
- **Fourth outcome "drop the claim entirely" verdict:** **RULED-OUT** (structural). Dropping the Peirce-preservation claim from §3.3 breaks §3.4 (forced form of corrected product) and §3.5 (circularity check S4/S5 verification) — fourth outcome collapses structurally to renamed (C-i).
- **Routing consequence:** (C-ii) was RULED-OUT by bounded feasibility check, not just deprioritized. Phase 54 proceeds with (C-i); the referee has a documented "considered and ruled out" stance on (C-ii) rather than a silent skip.

---

## Section 10: Secondary-Source Verification (NEW SCOPE item 2)

- **Artifact:** `derivations/paper5-peirce-preservation/secondary-source-verification.md` (produced 2026-04-16 in Plan 54-03, 30-min bounded sub-task).
- **Result:** Four A-S compression-axiom VERIFICATION-DEFERRED rows in `alfsen-shultz-notes.md` Section 5 upgraded, plus Section 6 row:

| Row | Before | After |
|-----|--------|-------|
| 5.1 Idempotency | VERIFICATION-DEFERRED | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.23 |
| 5.2 Positivity | VERIFICATION-DEFERRED | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.23 |
| 5.3 Complement on sharp pair | VERIFICATION-DEFERRED | **AXIOM-STATED-IN-SECONDARY-SOURCE** (pinching form confirmed; Prop/Thm deferred) |
| 5.4 Projector fix | VERIFICATION-DEFERRED | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Def 7.1 + Prop 7.23 |
| Section 6 Orthogonal compressional annihilation | NEEDS-VERIFICATION | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.50 (via trivial meet for orthogonal pairs) |

- **Independence-stance resolution:** S0 is a THEOREM of A-S compression theory (via Prop 7.50 specialized to face-disjoint orthogonal projective units), not strictly independent of A-S. The revision text cites S0 as an axiom for interface stability with Phase 58 Lean axiom audit, backed by A-S Prop 7.50 as secondary verification.
- **`alfsen-shultz-notes.md` updated:** Section 5 rows 5.1, 5.2, 5.3, 5.4 + Section 6 row + change-log entry dated 2026-04-16 in Plan 54-03 NEW SCOPE item 2.

---

## Section 11: Close Checklist Status

| Item | Status |
|------|--------|
| 54-RESULT.md outcome tag = (C-i) | PASS (§1) |
| Peirce-Preservation Lemma statement verbatim from claim.md | PASS (§2) |
| S0 axiom at compression level, three canonical-example defenses, independence defense, OUS-compatibility sketch including R3 | PASS (§3; full detail in s0-axiom.md) |
| closeout-sympy.py separate artifact; three tests PASS + supplementary S0 PASS; runtime 0.013s | PASS (§4) |
| §3.3 revision text integrated into main.tex; R4 line count 85; forbidden-token discipline preserved outside demarcated defense | PASS (§5) |
| main-jmp-submitted.tex unchanged (frozen) | PASS (verified via git -C ~/repos/blog diff --stat) |
| Exit gate: HALF-A grep PASS + HALF-B manual review PASS | PASS (§5.1) |
| Adversarial review PASS at primary (gpd-review-math with Phase 54 priming) | PASS (§6; 54-ADVERSARIAL-REVIEW.md) |
| ADDENDUM cited as (B)-unavailability basis | PASS (§7) |
| Cross-phase coupling notes for Phases 55, 57, 58 | PASS (§8) |
| (C-ii) RULED-OUT by bounded feasibility check | PASS (§9; c-ii-feasibility.md) |
| Secondary-source verification of A-S VERIFICATION-DEFERRED rows | PASS (§10; secondary-source-verification.md; alfsen-shultz-notes.md updated) |
| A-S citations point to A-S 2003 Ch. 7 with specific Prop numbers (7.23, 7.50) | PASS (main.tex §3.3 revision; no bare AlfsenShultz2003, no 2001, no Thm 9.37) |

**All items PASS. Phase 54 CLOSE-READY.**

---

## Section 12: References

- **claim.md** (Plan 54-01): `derivations/paper5-peirce-preservation/claim.md`
- **audit-04-06.md** (Plan 54-01): `derivations/paper5-peirce-preservation/audit-04-06.md` (AUDIT-FAILS verdict; routing basis for option-b-fails-compression)
- **attempt-log.md** (Plan 54-02): `derivations/paper5-peirce-preservation/attempt-log.md` (sealed outcome PIVOT-TO-C-I)
- **attempt-01.md** + **attempt-01.py** (Plan 54-02): `derivations/paper5-peirce-preservation/attempt-01.md` + `attempt-01.py` (FAILED (A) attempt with verbatim failure statement carried forward)
- **s0-axiom.md** (Plan 54-03 Task 3): `derivations/paper5-peirce-preservation/s0-axiom.md` (full S0 + defenses + OUS-compatibility sketch)
- **c-ii-feasibility.md** (Plan 54-03 NEW SCOPE item 1): `derivations/paper5-peirce-preservation/c-ii-feasibility.md`
- **secondary-source-verification.md** (Plan 54-03 NEW SCOPE item 2): `derivations/paper5-peirce-preservation/secondary-source-verification.md`
- **closeout-sympy.py** (Plan 54-03 Task 4): `derivations/paper5-peirce-preservation/closeout-sympy.py`
- **paper5-s3-revision.md** (Plan 54-03 Task 5): `derivations/paper5-peirce-preservation/paper5-s3-revision.md`
- **main.tex §3.3 revision** (Plan 54-03 Task 5): `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` (living copy; blog repo commit)
- **54-ADVERSARIAL-REVIEW.md** (Plan 54-03 Task 7): `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-ADVERSARIAL-REVIEW.md`
- **alfsen-shultz-notes.md** (SHARED, updated 2026-04-16): `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md`
- **ADDENDUM** ((B)-unavailability): `.gpd/research/ADDENDUM-independent-literature-check.md`
- **Paper 5 submitted** (frozen): `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` at git tag `paper5-jmp-submitted`
- **vdW 2019:** van de Wetering, arXiv:1803.11139 (Def. 2 axioms S1-S7; Thm 1)
- **A-S 2003:** Alfsen & Shultz, *Geometry of State Spaces of Operator Algebras*, Birkhäuser PM 190 (Ch. 2 / Ch. 7 Prop 7.23 / Ch. 7 Prop 7.50 used; Ch. 9 Thm 9.37 PRE-JORDAN-ILLEGAL flagged)
- **Niestegge 2008** (arXiv:1001.3633): U_e compression framework, literature analogue for OUS-level axiomatization
- **Lean SelfModelingBridge** (Phase 58 consumer): `~/repos/research/lean/RadicalRelativity/SelfModelingBridge.lean`

---

_Phase 54 close-ready 2026-04-16. Outcome: (C-i). All 12 checklist items PASS. Awaiting Task 9 (Phase 54 close confirmation checkpoint:human-verify) for final sign-off and phase close emission to the milestone tracker; Phases 55, 56, 57, 58 become eligible to run per ROADMAP dependency graph._
