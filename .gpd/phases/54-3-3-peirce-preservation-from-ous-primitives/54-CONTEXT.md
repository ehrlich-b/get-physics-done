# Phase 54: §3.3 Peirce Preservation from OUS Primitives - Context

**Gathered:** 2026-04-16
**Status:** Ready for planning

<domain>
## Phase Boundary

Close the §3.3 Peirce-preservation claim of Paper 5 (`main-jmp-submitted.tex` lines 483-562; key claim lines 508-528) with outcome classification:

- **(A)** Rigorous proof from OUS primitives (S1, S3, linearity, A-S compressions only), or
- **(C-i)** OUS-level "Peirce coherence" axiom S0 stated explicitly, with defense, or
- **(C-ii)** Alternative S4 proof routing around Peirce entirely.

Specifically: `a ∘ V_2(p_i) ⊆ V_2(p_i)` and `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)` for `a = Σᵢ λᵢ p_i` in a spectral OUS.

**Explicitly out of scope:**
- (B) external citation — essentially ruled out by ADDENDUM (Peirce is post-Jordan in accessible literature).
- (C-iii) restructure-before-S4 — UNAVAILABLE; would create fresh circularity via vdW Thm 1.
- Any use of Jordan multiplication, EJA, sequential-product closed-form `f(λ,μ) = √(λμ)`, C*-structure, `h_n(ℂ)`, `pxp`, `√a b √a`, "operator product" is circular and prohibited.

Requirements: DERV-54-01, DERV-54-02, DERV-54-03, DERV-54-04, DERV-54-05, DERV-54-06 (conditional), VALD-54-01, VALD-54-02, DERV-00-01 (Phase 54 slice)

</domain>

<contract_coverage>
## Contract Coverage

- **Phase 4-06 circularity audit (DERV-54-01, mandatory first task):** pass/fail verdict with step-by-step token-level trace of every tool used in the derivation of Eq. 04-06.4; forbidden-token grep on Phase 4-06 prose has zero hits (pass) or identifies every hit (fail).
- **Outcome classification:** exactly one of (A), (C-i), or (C-ii) declared in RESULT.md.
- **Named invariance lemma:** stable citation target in conditional form — downstream (Phases 55, 56, 57, 58) cites the lemma name; the assumption set (A uses S1+S3+linearity+compressions; C-i uses S0) changes without the interface changing.
- **Outcome tag:** explicit (A)/(C-i)/(C-ii) label for routing Phases 58 and Lean sync decision trees.
- **§3.3 revision text:** ≥ 20 lines (per R4); referee-facing; goes into `main.tex` (not `main-jmp-submitted.tex`).
- **Exit gate:** lemma statement must appear verbatim (modulo whitespace) in the §3.3 revision text — automated grep + manual semantic review (both required). Divergence at closeout means RESULT.md is structurally broken.
- **SymPy sanity check (VALD-54-01):** per-attempt rank-1 gate + separate closeout artifact `closeout-sympy.py` with V_1(p_k,p_l) cross-term coverage (R3); closeout artifact referenced in RESULT.md, not buried inside the winning attempt file.
- **Adversarial fresh-eyes review (VALD-54-02):** gpd-review-math with Phase 54 priming (primary); Paper-5-primed rubric pass (general-purpose Opus) as escalation only if primary returns borderline.
- **`alfsen-shultz-notes.md` SHARED ARTIFACT:** every Paper 5 `\cite{AlfsenShultz...}` in §3.3-§3.4 resolved to (volume 2001 vol. 179 vs 2003 vol. 190, chapter, section, theorem number, exact statement, match-to-Paper-5 verdict). Explicit flag on Thm 9.37 (pre-Jordan-illegal) and Prop 7.36 (Lean `SelfModelingBridge.lean` citation; prop number unverified). Consumed by Phases 55, 57, 58.

**False progress to reject:**
- "Since `a ∘ b` is a Jordan product..." (uses derived structure).
- Citing the Peirce decomposition theorem as if it proves invariance of `L_a` (R2 non-sequitur).
- Conflating "compressions `C_{p_i}` preserve Peirce subspaces" (A-S fact) with "`a ∘ (−)` preserves Peirce subspaces" (claim about composite map).
- Citing A-S Thm 9.37 (pre-Jordan-illegal).
- Forbidden tokens appearing anywhere in RESULT.md: `M_n(ℂ)`, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, "operator product".
- Silently shifting to (C-iii) restructure-before-S4.
- "We axiomatized it, done" short-circuit revision text (must have substantive derivation of V_2 and V_1 invariance from S0 + compressions).

</contract_coverage>

<user_guidance>
## User Guidance To Preserve

- **User-stated observables:**
  - Named conditional-form invariance lemma (stable citation target unifying (A) and (C-i) at the API).
  - Outcome tag (A / C-i / C-ii) explicit in RESULT.md for Phase 58 + Lean sync routing.
  - §3.3 revision text (≥ 20 lines per R4) that the referee reads.

- **User-stated deliverables (all three artifacts must agree at closeout):**
  1. Named lemma statement (conditional form).
  2. Outcome tag.
  3. §3.3 revision text containing the lemma statement verbatim.
  - Exit gate: `grep` the lemma statement against the revision text AND manual semantic review; both must pass before Phase 54 closes.

- **Must-have references / prior outputs (must stay visible during attempts):**
  - Phase 4-06 audit verdict + token-level trace — cited inline by every (A) attempt (seeded-from / avoiding-because).
  - Alfsen-Shultz 2001 vol. 179 Ch. 7-8 compression text — **Prop/Thm numbers verified against the actual book, not paraphrased.** (Paraphrase drift is the second-most-common A-S failure mode after 2003-vs-2001 confusion.)
  - Paper 5 `main-jmp-submitted.tex` lines 483-562 at git tag `paper5-jmp-submitted` (frozen).
  - `.gpd/research/ADDENDUM-independent-literature-check.md` — (B)-unavailability justification; must remain visible in RESULT.md as the reason (B) is not attempted.

- **Stop / rethink conditions (all three active as pause triggers):**
  1. **End of attempt-02** — pause regardless of outcome; human reviews before authorizing attempt-03 or pivot. (Budget discipline. Fires only in the 4-06-audit-passed branch where multi-attempt is in scope.)
  2. **4-06 audit FAIL** — pause immediately at the branch point; confirm routing before proceeding. Default is single (A) attempt on non-4-06 route then (C-i), but the audit failure trace may argue for going straight to (C-i) (e.g., if circularity is specifically about compression algebra, non-4-06 route also won't work).
  3. **C-iii drift detected** — if any attempt starts constructing Jordan structure before S4, escalate with an explicit quote of the drift-introducing line (not just "Jordan structure detected"). Paper 5's §3.3 already fell into this trap once; escalation message must make the drift mechanism concrete.

</user_guidance>

<decisions>
## Methodological Decisions

### (A) attempt strategy

- **Seed for attempt 1:** A-S compression combinatorics. Build Peirce invariance from C_p + C_{p'} = id, idempotency, positivity; derive via compression algebra only; never introduce the SP closed-form as a primitive. (Avoid 4-06 corrected SP formula as seed until the audit verdict confirms it is safe.)
- **Attempt cap:** 3 attempts as outer bound; **probably won't use all 3** — if we're still failing after two, strategy needs to change before attempt-03, not just another draft. User explicitly deprecated over-proscribing: "Just be reasonable... we probably won't let it get that far though."
- **Attempt naming/location:** `derivations/paper5-peirce-preservation/attempt-NN.md` (prose + embedded claim + drift log) + sibling `attempt-NN.py` (SymPy per-attempt rank-1 gate).
- **Objection routing:** non-forbidden-token adversarial objection → mark attempt-NN.md FAILED with the objection quoted verbatim; open attempt-(NN+1).md with an explicit "addresses prior objection: [quote]" paragraph at the top.
- **If Phase 4-06 audit FAILS:** single (A) attempt using non-4-06 route (compression combinatorics), then pivot to (C-i). Subject to the "audit-FAIL pause" trigger — the failure trace may argue for skipping (A) entirely and going straight to (C-i) if the circularity is specifically compression-algebra.

### S0 axiom form (if C-i)

- **Level:** Compression-level (weakest) — S0 asserts a property on compressions themselves (e.g., pairwise commutation of C_{p_i} for orthogonal p_i, or C_{p_i} ∘ C_{p_j} = 0 for i ≠ j). Peirce invariance is then *derived* from S0 + A-S compression primitives + spectral decomposition, not posited.
- **Scope covered:** V_2 and V_1 as stated — axiom-plus-derivation must yield both `a ∘ V_2(p_i) ⊆ V_2(p_i)` and `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)`, matching the Paper 5 claim verbatim. Referee cannot argue "you only axiomatized half."
- **Defense depth:** Inline sketch per model in §3.3 revision text — one paragraph each for M_n(ℂ)^sa (spectral theorem + pxp matrix-block computation, legal *inside* the model), C(X) (trivial by pointwise multiplication), spin factors (from Clifford relation). Referee-legible; Lean axiom audit in Phase 58 will do the formal-verification layer.
- **Literature analogue:** Niestegge 2008 `U_e` compression convention + A-S compression axioms as canonical framework.
- **Independence defense:** S0 is NOT derivable from S1-S7 — otherwise we would prove it, not axiomatize it. Defense form is **Agent's Discretion** (see below).
- **Downstream coupling:** If Phase 54 closes (C-i), Phases 55 (S4 phi-independence) and 57 (phi-inertness) may need shared restructuring per R11; the named lemma's conditional form insulates downstream citation but the *assumption set* propagates.

### Early falsifier gates (all three must pass before adversarial review)

1. **Forbidden-token self-grep on the attempt draft** — any hit on {M_n(ℂ), Jordan, EJA, Lüders, pxp, √a b √a, "operator product", √(λμ), h_n(ℂ)} means the attempt is unsalvageable; close and open next with a note on which token drifted in.
2. **SymPy H_3(ℝ) rank-1 sanity check per attempt** — numerical disagreement with the lemma's prediction on any Peirce subspace tested is an instant structural red flag.
3. **Model-instantiation check** — the compression-only argument, when instantiated in M_n(ℂ)^sa or C(X), must not produce a false statement (would mean the argument proved something stronger than actually holds).

### Adversarial fresh-eyes review (VALD-54-02)

- **Primary reviewer:** gpd-review-math with Phase 54 priming — the subtle-Jordan-smuggling failure mode is a structural non-sequitur, which gpd-review-math is specifically tuned for.
- **Escalation path:** If gpd-review-math returns **borderline** (not clean PASS, not clean FAIL), escalate to a Paper-5-primed rubric pass using a general-purpose Opus subagent primed with: peirce-post-jordan-finding memory, A-S 2001 vs 2003 distinction, forbidden-token list, R1-R7 pitfalls, "compressions preserve Peirce ≠ L_a preserves Peirce" (R2) explicitly. Not routine belt-and-suspenders — only if primary is inconclusive.
- **Prompt discipline:** explicitly tell the reviewer that a "CIRCULAR" verdict must be distinguished from an "IDENTITY" verdict (per sms:minimal lesson — calling a definitional clause "circular" is a framing error, not an argument error). The reviewer should state which framing it is applying when it flags something circular.
- **Rationale for rejecting alternatives:** cold-read subagents produce verdicts that "feel decisive but can be wrong in program-specific ways" (sms:minimal incident). Paper-5-primed *general-purpose* Opus is plausible but primed-with-wrong-frame is worse than cold read — priming amplifies framing. gpd-review-math's priming is about *context*, not about how to review, which is the right combination.

### SymPy validation wiring

- **Per-attempt gate:** rank-1 sanity check on H_3(ℝ) with two orthogonal rank-1 projectors; runtime < 1 sec; attempt cannot be sealed until it passes.
- **Closeout artifact:** separate file (`closeout-sympy.py`) with fuller check including R3 cross-term V_1(p_k, p_l) for {k,l}∩{i,j}=∅. Referenced in RESULT.md, not embedded in the winning attempt file. Downstream phases (58, Lean sync) should be able to re-run the closeout check against the final lemma statement without excavating it from an attempt file.

### Agent's Discretion

- **S0 naming** (S0 / "Peirce coherence" / "Compression coherence axiom" / with equation label) — executor picks during (C-i) drafting for referee optics + downstream citation stability.
- **S0 placement** (§3.2 alongside S1-S7 / top of §3.3 at point of use / split between §3.2 statement and §3.3 use) — executor decides; "too much detail, we'll work it out in review."
- **Independence-of-S0 argument form** (counterexample model / parameter-counting / hybrid) — executor produces whichever is cleanest and defensible during drafting.
- **R4 length distribution** (≥20 lines in §3.3 alone vs. counting §3.2 intro + §3.3 use) — executor decides; constraint is that R4 is satisfied.
- **SymPy projector family** (symbolic random vs. canonical diagonal vs. parametric) and tolerance (symbolic-exact vs. numeric) — executor picks; constraint is that closeout check covers R3 cross-terms unambiguously.
- **alfsen-shultz-notes.md depth** — baseline is per-citation fields (volume/ch/thm/exact statement/verdict) for every §3.3-§3.4 citation; chapter-level summaries optional as executor sees fit for 55/57/58 downstream needs.
- **A-S 2001 vs 2003 verification mechanics** (photocopy/scan vs. re-derivation from ToC) — executor decides, but **Prop/Thm numbers must be verified against the actual book text, not paraphrased.**

</decisions>

<assumptions>
## Physical Assumptions

- **Phase 4-06 corrected SP formula is a candidate seed for (A), not a given result.** The formula `a ∘ b = Σᵢ λᵢ C_{pᵢ}(b) + Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)` (commit `9608ac54`) looks OUS-level but has not been audited for circularity. Assumption: the audit may pass or fail; plan must handle both. | **If audit FAILS:** 4-06 is unusable as seed, single non-4-06 (A) attempt then (C-i). If audit PASSES, 4-06 becomes a valid seed alongside compression combinatorics.
- **(C-iii) "restructure-before-S4 to derive Jordan" is not a lurking escape hatch.** | **If any attempt quietly drifts toward (C-iii):** escalation required; the trap is that vdW Thm 1 consumes S4 to produce Jordan, so any pre-S4 Jordan derivation is circular.
- **Referee hasn't arrived yet (19 days with associate editor as of 2026-04-16).** JMP typical 3-6 month window means there's still time for a serious revision, but the revision must be ready fast when the report lands. | **If referee report arrives mid-phase:** milestone-level rescope, not a Phase 54-local concern.
- **A-S 2001 (vol. 179) and A-S 2003 (vol. 190) are distinct volumes with distinct content.** Vol. 179 has the compression Ch. 7-8 (pre-Jordan-legal target); Vol. 190 Ch. 9 is the Jordan state-space characterization (Thm 9.37 pre-Jordan-illegal per ADDENDUM). | **If collapsed:** instant R5 violation; `alfsen-shultz-notes.md` must keep the volume distinction explicit per citation.

</assumptions>

<limiting_cases>
## Expected Limiting Behaviors

- **In M_n(ℂ)^sa:** Peirce invariance holds by spectral theorem + pxp matrix-block computation (legal inside the model, since M_n(ℂ)^sa is Jordan-algebraic). The S0-derivation-or-(A)-proof must reproduce this. If it doesn't, structural red flag.
- **In C(X) (commutative):** Peirce invariance is trivial — projectors commute, compressions are multiplications by characteristic functions, Peirce decomposition collapses. S0-derivation must be consistent with this trivial case; (A) proof must not fail here.
- **In spin factors (Clifford):** Peirce invariance follows from Clifford anti-commutation {e_i, e_j} = 2 δ_{ij} 1; non-trivial but well-known. Must be consistent.
- **Rank-1 projectors on H_3(ℝ) (SymPy per-attempt gate):** a = λ_1 p_1 + λ_2 p_2 with p_1 ⊥ p_2 rank-1; a ∘ b for b ∈ V_j must land in V_j. Failure = attempt broken.
- **Cross-term V_1(p_k, p_l) with {k,l} ∩ {i,j} = ∅ (SymPy closeout, R3):** on H_3(ℝ) this requires at least three orthogonal rank-1 projectors for non-trivial cross-terms; closeout must probe this explicitly.

</limiting_cases>

<anchor_registry>
## Active Anchor Registry

- **GPD v2.0 Phase 4-06 corrected SP formula (commit `9608ac54`, 2026-03-21)**
  - Why it matters: CORE internal prior art; candidate (A) seed if audit passes; gate for A vs C-i per ADDENDUM prior.
  - Carry forward: planning (mandatory first task), execution (seed or avoid), verification.
  - Required action: audit (forbidden-token grep + token-level derivation trace); cite verdict inline in every attempt.

- **Alfsen-Shultz 2001 vol. 179, *State Spaces of Operator Algebras*, Ch. 7-8**
  - Why it matters: pre-Jordan-legal compression axioms; primary (A) foundation and S0 framework anchor.
  - Carry forward: planning, execution, writing.
  - Required action: read (actual book text); use; cite with explicit volume + chapter + Prop/Thm number (Prop/Thm numbers **verified against the book, not paraphrased**).

- **Alfsen-Shultz 2003 vol. 190, *Geometry of State Spaces of Operator Algebras*, Part I Ch. 1-3 & Ch. 9**
  - Why it matters: distinct volume from 2001; Jordan state-space characterization; Thm 9.37 is pre-Jordan-illegal per ADDENDUM and must be flagged.
  - Carry forward: planning (explicit flag), writing (volume distinction in every cite).
  - Required action: cite only in post-Jordan contexts; flag pre-Jordan-illegal uses in `alfsen-shultz-notes.md`.

- **van de Wetering 2019 (arXiv:1803.11139), Def. 2**
  - Why it matters: S1, S3 statements (verbatim) — the *only* SN axioms allowed in Phase 54 proofs. S4-S7 forbidden pre-S4.
  - Carry forward: planning, execution, writing.
  - Required action: read Def. 2 exactly; restrict (A) proofs to S1 + S3 + linearity + compressions.

- **Paper 5 `main-jmp-submitted.tex` §3.3 lines 483-562 (frozen at tag `paper5-jmp-submitted`)**
  - Why it matters: frozen source; 20-line baseline for R4; revision lands in `main.tex`.
  - Carry forward: planning, execution, writing.
  - Required action: read; compare every revision against frozen text; write into `main.tex`.

- **`.gpd/research/ADDENDUM-independent-literature-check.md`**
  - Why it matters: justifies (B)-unavailability; must remain visible in RESULT.md as the reason external citation is not attempted.
  - Carry forward: writing (RESULT.md references).
  - Required action: cite in RESULT.md "(B) ruled out per ADDENDUM §X".

- **Niestegge 2008 (arXiv:1001.3633)**
  - Why it matters: Niestegge `U_e` compression convention; literature precedent for OUS-level axiomatization; defense anchor for (C-i) S0.
  - Carry forward: writing (if C-i).
  - Required action: cite in the S0 defense paragraph.

- **peirce-post-jordan-finding memory**
  - Why it matters: prior incident where Paper 5's §3.3 already fell into the Jordan-smuggling trap; must be loaded into the adversarial reviewer's priming prompt.
  - Carry forward: execution (adversarial review prompt).
  - Required action: load into reviewer prompt; explicitly warn about the mechanism.

- **Lean formalization at `~/repos/research/lean/Paper5/` (pinned lean4 v4.28.0 + mathlib v4.28.0)**
  - Why it matters: Phase 58 axiom audit is parallel-path; Phase 54 outcome tag gates how Phase 58 re-classifies axioms (proof → theorem; C-i → S0 relabel).
  - Carry forward: execution (outcome tag), writing (RESULT.md routes Phase 58).
  - Required action: produce outcome tag explicitly; Lean sync is a separate concern but needs the tag.

</anchor_registry>

<skeptical_review>
## Skeptical Review

- **Weakest anchor:** GPD v2.0 Phase 4-06 corrected SP formula — CORE internal prior art, but circularity audit is pending. ADDENDUM prior puts (A)-via-4-06 at MEDIUM (not HIGH). We are acting as if it may fail; assumption captured in audit-FAIL single-attempt path.
- **Unvalidated assumptions:**
  1. That A-S 2001 Ch. 7-8 actually gives the compression primitives we need without silently importing Jordan structure. We are using the chapter as "pre-Jordan-legal" based on TOC reading; the actual theorems' proofs may themselves cite later chapters.
  2. That the compression-algebra-only (A) attempt route is substantively different from the 4-06 route (if the 4-06 formula is itself derivable from A-S compressions alone, our two routes degenerate to one).
  3. That "gpd-review-math with Phase 54 priming" is substantively better than cold read at catching subtle Jordan-smuggling. This is an unvalidated meta-claim based on the sms:minimal incident reasoning.
- **Competing explanation:** Paper 5's §3.3 may have always been a C-i — the original author may have implicitly relied on the Peirce invariance as an OUS-level intuition without axiomatizing it. In that case (C-i) is not a "fallback" but a "correction of the original argument's implicit assumption"; framing matters for referee optics.
- **Disconfirming check:** If the (A) attempt via compression combinatorics produces a proof that is *itself* derivable inside vdW 2019 from S1-S3 alone (without S4-S7), that would imply the Peirce invariance was always available pre-Jordan and ADDENDUM's (B)-unavailability conclusion is wrong. Low probability; would be big news.
- **False progress to reject:**
  - Rewriting §3.3 with slightly more words but the same implicit Jordan appeal — R4's 20-line floor cannot be satisfied by padding. Must be *substantive* new content.
  - SymPy agreement on rank-1 H_3(ℝ) projectors while the lemma actually fails on V_1 cross-terms (R3) — per-attempt gate alone is insufficient; closeout must probe cross-terms.
  - A "CIRCULAR" verdict from gpd-review-math that is actually a framing error (calling a definitional clause circular, per sms:minimal). The reviewer-prompt discipline specifically guards against this.
  - Adopting (C-i) with a defensible S0 but a §3.3 revision text that reduces to "by S0, invariance holds" — revision must have substantive derivation of V_2 and V_1 invariance from S0 + A-S compressions.

</skeptical_review>

<deferred>
## Deferred Ideas

- **Phase 55 cascade handling** — if Phase 54 closes (C-i), Phase 55's S4 argument must be rewritten to invoke S0 instead of implicit Peirce appeal; Phase 57 may share restructuring (R11). Not acted on in Phase 54; flagged for Phase 55 planning.
- **Phase 58 Lean axiom relabeling** — if Phase 54 closes (C-i), the Lean axiom encoding `_peirce_preservation` gets re-classified (type-iv primitive with S0 defense) rather than type-i theorem-in-disguise. Phase 58 concern.
- **latexdiff revision-letter integration** — Phase 59 concern; requires `brew install latexdiff` + `git-latexdiff` prerequisite; not in Phase 54 scope.
- **Website wording fix** — public-facing Paper 5 wording on the landing page may need the same patch; out of scope for Phase 54.
- **Minimal-composite defense** (Hardy / Masanes-Müller / Chiribella / Dakić-Brukner / Barnum-Wilce / Kent 2024 patterns) — Phase 59 concern; orthogonal to Phase 54 closure.

</deferred>

---

*Phase: 54-3-3-peirce-preservation-from-ous-primitives*
*Context gathered: 2026-04-16*
