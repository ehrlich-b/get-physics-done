# Research Summary: Paper 5 JMP Revision (v14.0)

**Project:** Quantum Mechanics from Self-Modeling -- JMP Revision (JMP26-AR-00922)
**Domain:** Operational quantum theory / Order unit spaces / Sequential effect algebras / Euclidean Jordan algebras / Axiomatic reconstruction / Lean 4 formalization
**Milestone scope:** Six jigsaw-piece gaps (Phases 54-59) identified pre-referee in submitted Paper 5
**Researched:** 2026-04-16
**Confidence:** MEDIUM-HIGH overall; HIGH on infrastructure/tooling and Phases 55/58/59; MEDIUM on Phase 54 primary strategy (literature is silent in the exact form Paper 5 needs); MEDIUM on Phases 56/57.

---

## Executive Summary

This milestone closes six internal-exposition gaps in Paper 5 before a JMP referee report lands. The gaps are scoped as Phases 54 (§3.3 Peirce preservation from OUS primitives), 55 (S4 facial-structure lemma), 56 (Thm 5.8 upper bound on W), 57 (Phi inert-wrapper disambiguation), 58 (Lean axiom audit of the 16 `axiom` declarations in `RadicalRelativity/`), and 59 (minimal-composite adversarial defense). None of the six alters the physics chain; all are exposition and formalization hardening. However, each gap is a reviewer-attack surface, and at least one (Phase 54) has the structural character of a real derivation-ordering problem, not merely a typographical one.

**The central risk across the milestone is circularity.** Paper 5's derivation spine is: OUS + S1-S7 ⇒ (vdW Theorem 1) ⇒ Euclidean Jordan algebra ⇒ (local tomography + qubit subsystem) ⇒ M_n(ℂ)^sa. Any argument in §3.3-§3.4 that silently invokes Jordan structure to verify an axiom that feeds vdW Thm 1 has inverted the dependency. The Phase 54 §3.3 Peirce-preservation claim is the sharpest instance. An independent literature check (ADDENDUM-independent-literature-check.md) confirms that no pre-Jordan OUS-native Peirce theorem exists in the accessible literature (verified against Alfsen-Shultz 2003 TOC and Jenčová-Pulmannová arXiv:2102.01628 §3-5); Peirce decomposition is consistently post-Jordan. This essentially rules out outcome (B) (clean external citation). Simultaneously, GPD's own v2.0 Phase 4-06 work (commit `9608ac54`) already derived the corrected sequential product `a ∘ b = Σᵢ λᵢ C_{pᵢ}(b) + Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)` whose Peirce structure is built-in by construction. This is a plausible outcome (A) route **conditional on the Phase 4-06 derivation itself not silently importing Jordan structure** — which must be audited as Phase 54's first task.

**Prior on Phase 54 outcomes:** (A) via internal Phase 4-06 prior art, **conditional on circularity audit passing** — MEDIUM probability. (B) external A-S / vdW citation — **essentially ruled out** per ADDENDUM. (C-i) add OUS-level "Peirce coherence" axiom S0 alongside S1-S7 and defend it as natural — HIGH probability as fallback. (C-iii) restructure to derive Jordan structure *before* S4 — **unavailable**: vdW Theorem 1 consumes S4 to produce Jordan, so inversion creates fresh circularity. The recommended Phase 54 strategy is therefore: (1) audit Phase 4-06 for hidden Jordan dependence; (2) if audit passes, rebuild the §3.3 proof from the Phase 4-06 formula using only S1+S3+compression primitives; (3) if audit fails, shift to (C-i) and draft the S0 axiom at OUS level. Phases 55-59 should not start until Phase 54 outcome is classified, because Phase 55 (S4 facial structure) and Phase 57 (Phi inertness) share the same circularity risk and may need shared restructuring if (C-i) is adopted.

---

## Unified Notation

Pin notation across the revision. All phases must use these symbols or explicitly flag deviation.

| Symbol | Quantity | Convention | Source |
|--------|----------|-----------|--------|
| V | Finite-dim order unit space over ℝ | Archimedean, complete, with distinguished unit 1 | A-S 2003 Ch. 1 |
| a ∘ b | Sequential product (Paper 5 notation) | Bilinear on V (S1, S3, S5 in vdW 2019 Def. 2) | vdW 2019 Def. 2; equivalently vdW's `a & b` |
| a · b | Jordan product (when defined) | Distinct from ∘; used only when Jordan structure has been DERIVED | HOS 1984; A-S 2003 Part I |
| C_p(b) | A-S compression by projective unit p | `C_p² = C_p`, `C_p + C_{p'} = id` on its domain, `C_p(p) = p` | A-S 2001 Ch. 7, A-S 2003 Ch. 7; Niestegge 2008 uses `U_e` |
| p ∈ V | Projective unit / sharp effect | Sharp iff `p ∘ p = p` and `p ∘ p' = 0` (vdW Def. 7) | vdW 2019 Def. 7 |
| V₂(p) | Peirce 2-space of p | Range of C_p; `C_p(V) = V₂(p)` | A-S 2003 Ch. 8 (JB-level); abstract OUS version is what Phase 54 needs |
| V₁(p,q) | Peirce 1-space of orthogonal p, q | `(p+q)V(p+q) − C_p(V) − C_q(V)` | v2.0 Phase 4-06 Eq. 04-06.4 |
| V₀ | Peirce 0-space | Range of C_{1-p-...} for a complete orthogonal projection family | A-S 2003 Ch. 8 |
| L_a | Left sequential-product multiplication | L_a(b) := a ∘ b | Paper 5 §3.3 |
| φ (phi) | Self-modeling map | Tracking map B → M; faithfulness selects mixing function f(λ,μ) = √(λμ) | v2.0 Phase 4-06; Paper 5 §2-4 (role varies; see Phase 57) |
| S1-S7 | vdW sequential-product axioms | S1 (additivity in 2nd arg), S3 (unitality), S4 (orthogonality symmetry), S7 (continuity/spectrality); S5, S6 for compatibility | vdW 2019 Def. 2 (arXiv:1803.11139). **Pin verbatim; do not drift.** |
| vdW Thm 1 | S1-S7 + fin-dim ⇒ EJA | Koecher-Vinberg closure | vdW 2019 arXiv:1803.11139 |
| A-S | Alfsen & Shultz | **Distinguish 2001 vol. 179 (State Spaces / C*-) from 2003 vol. 190 (Geometry of State Spaces)** | See "Convention Traps" below |

**Convention traps (do NOT collapse):**
1. **Two A-S volumes.** 2001 vol. 179 = *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products*; 2003 vol. 190 = *Geometry of State Spaces of Operator Algebras*. Compression theory is in 2001 Ch. 7-8; Jordan state-space characterization is in 2003 Ch. 9. Paper 5's current `\cite{AlfsenShultz2003}` may be on the wrong volume for some invocations — Phase 55 must resolve.
2. **Peirce decomposition (structural fact about V) ≠ Peirce invariance (claim about L_a).** Citing "A-S Peirce decomposition" as justification for "L_a preserves V₂(pᵢ)" is a cited non-sequitur (Pitfall R2).
3. **A-S compression C_p (OUS-level) ≠ B(H)-compression pxp (operator-level).** These coincide in M_n(ℂ) but are distinct primitives in an abstract OUS. Using `pxp` implicitly assumes operator structure and is circular for Phase 54 (Pitfall R1).
4. **Sequential product notation.** Paper 5 uses `∘`; vdW uses `&`; v2.0 Phase 4 uses `&`. Keep Paper 5 convention `∘` but state the equivalence explicitly once, and never confuse with Jordan product `·`.

---

## New Results: Key Findings

### From PRIOR-WORK.md

- **GPD v2.0 Phase 4-06 corrected sequential product** (commit `9608ac54`) derived `a ∘ b = Σᵢ λᵢ C_{pᵢ}(b) + Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)` with explicit Peirce 2-space and mixing 1-space terms. **This is the CORE internal prior art for Phase 54.** Its Peirce structure is immediate from the formula; Peirce invariance of L_a then decomposes into per-term checks. [CONFIDENCE: HIGH for formula; MEDIUM for directly solving Phase 54 because the Phase 4-06 derivation itself must be audited for circularity]
- **No external OUS-native Peirce-preservation theorem exists.** Surveyed vdW 2019, A-S 2003, Niestegge 2008, HOS 1984, Gudder-Greechie 2002, WWvdW 2020, Barnum-Wilce 2014, Jenčová 2021, Jenčová-Flaminio-Kroupa 2023. All Peirce-for-sequential-product results either assume JB/JBW structure (post-Jordan, circular for §3.3) or address compressions without the sequential-product L_a claim (single-compression, not composite-map — Pitfall R3). [CONFIDENCE: HIGH absence claim]
- **vdW 2019 Thm 1** (S1-S7 fin-dim ⇒ EJA) and **vdW 2019 Thm 3** (SP + local tomography with self ⇒ C*-algebra) are HIGH-confidence downstream anchors. Paper 5 cites these correctly; no revision needed to those citations.
- **WWvdW 2020 three-type classification** (normal SEA = commutative ⊕ quantum ⊕ spin-factor; associativity ⇒ commutativity) is the relevant machinery for Phase 56 upper bound on W. [MEDIUM confidence for this specific use]
- **Barnum-Wilce 2014** (EJA + local tomography + qubit ⇒ M_n(ℂ)^sa) completes Phase 59's defense chain. [HIGH confidence]

### From ADDENDUM-independent-literature-check.md (author-sourced, 2026-04-16)

- **Alfsen-Shultz 2003 TOC analysis** (subagent verified): Ch. 7 "General Compressions" has no Peirce section; Ch. 8 "Spectral Theory" has no Peirce section; Ch. 9 is explicitly a Jordan-state-space characterization (Thm 9.37 is cited by Paper 5 but is circular at pre-Jordan §3.3 level); Part I Ch. 1-3 develops Peirce theory Jordan-algebraically. [HIGH confidence structural finding]
- **Jenčová-Pulmannová arXiv:2102.01628 direct read**: This is THE literature comparison paper for OUS spectrality (Alfsen-Shultz vs. Foulis). Peirce decomposition does not appear in Sections 3-4 (OUS-level); first appears in Section 5 "Spectrality for JB-algebras" (5.9 Theorem, citing A-S 2003 Thm 1.4 — the Jordan-algebraic Peirce chapter). [HIGH confidence]
- **Refined prior on Phase 54 outcomes:**
  - (A) Proof from OUS primitives: **plausible but difficult**; must bypass Peirce in proving S4 or find non-Peirce characterization. Internal GPD v2.0 Phase 4-06 is the only plausible route, and only if it does not import Jordan.
  - (B) A-S citation: **essentially ruled out**.
  - (C) Structural gap: **most likely outcome**.
    - (C-i) Add OUS-level "Peirce coherence" axiom S0 alongside S1-S7 — RECOMMENDED fallback.
    - (C-ii) Alternative S4 proof routing around Peirce — worth exploring but speculative.
    - (C-iii) Restructure to derive Jordan before S4 — **UNAVAILABLE** (vdW Thm 1 consumes S4 to produce Jordan; inverting is fresh circularity).

### From METHODS.md (6 actionable methods, one per phase, with critical-path ordering)

- **Phase 54:** Spectral-OUS preservation argument via A-S compressions + vdW 2018 functional-calculus characterization; fallback is Gudder-Greechie S1+linearity collapse. Method recognizes that both routes require regime verification.
- **Phase 55:** Foulis-Holland symmetric orthogonality (pre-Jordan, preferred) or Hanche-Olsen facial symmetry (post-Jordan, circular if invoked before S4 is verified).
- **Phase 56:** Product-form closure via Koecher-Vinberg (vdW 2019 Thm 1 applied to W as a face). Requires verifying W is a face (not just closed subspace).
- **Phase 57:** Hardy-style ancilla elimination + grep-based Phi occurrence audit. Pure exposition, 4-6 hour pass.
- **Phase 58:** `#print axioms` + axiom-to-citation mapping table. **Bottleneck of the milestone (~2-3 working days); critical path.** 16 axioms → classify each as (i) theorem-in-disguise, (ii) definition-as-axiom, (iii) statement-mismatch, or (iv) genuine primitive.
- **Phase 59:** Adversarial minimal-composite defense comparing to Hardy 2001, Dakić-Brukner 2009, Masanes-Müller 2011, Masanes-Galley-Müller 2019, Barnum-Wilce 2014, Kent 2024 critique.

### From PITFALLS.md

- **R1 (circularity via Jordan):** the central pitfall; forbidden-token grep (`M_n`, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`) must pass on every Phase 54 RESULT.md.
- **R2 (decomposition vs. invariance):** citing Peirce decomposition as justification for Peirce invariance is a cited non-sequitur.
- **R3 (single vs. composite compression):** A-S gives properties of individual `C_{pᵢ}`; Phase 54 needs properties of the sum Σᵢ λᵢ C_{pᵢ} plus the mixing term Σ √(λᵢλⱼ) P_{ij}. These are separate case analyses.
- **R4 ("obvious" rate limit):** revised §3.3 must be at least as long as the submitted 20 lines at lines 508-528.
- **R5 (vague A-S citations):** every `\cite{AlfsenShultz...}` must become `\cite[Ch. X, Thm Y.Z]{AlfsenShultz...}` with correct volume (2001 vs 2003).
- **R7 ("carries" equivocation in Thm 5.8):** Phase 56 must distinguish closure from induced-structure from functorial preservation.
- **R10 (minimal-composite adversarial magnet):** Phase 59 must preempt Hardy-simplicity-critique pattern.
- **R11 (cross-phase cascade):** if Phase 54 outcome is (C), phases 55-59 must pause and potentially restructure.

---

## Recommended Methods

Critical-path ordering (Phase 58 is the longest; others can run in parallel pairs after Phase 54 classifies):

| Phase | Method | Confidence | Effort | Blocks/Blocked-by |
|-------|--------|-----------|--------|------------------|
| 54 | Circularity audit of v2.0 Phase 4-06, then spectral-OUS preservation from corrected SP formula; fallback = draft (C-i) axiom S0 | MEDIUM | 1-2 days | **Gates 55, 56, 57.** Phase 58 can start in parallel. |
| 55 | Foulis-Holland (pre-Jordan) for S4; produces `alfsen-shultz-notes.md` as shared deliverable for 54/57/58 | MEDIUM-HIGH | 0.5-1 day | Depends on Phase 54 classification (shared A-S citation audit); consumed by 57, 58. |
| 56 | vdW 2019 KV closure applied to W; first verify W is a face, then inherit S1-S7 | MEDIUM | 1-2 days | Depends on Phase 54 (Peirce-invariance used downstream in Thm 5.8 proof). Address R7 "carries" ambiguity explicitly. |
| 57 | Hardy-style Phi ancilla elimination + grep audit; produces `phi-audit.md` as shared deliverable for 54/58/59 | MEDIUM | 0.5-1 day | Depends on 54 and 55 (phi-independence requires Peirce + facial structure to be phi-independent). |
| 58 | `lake build` → `#print axioms` per headline theorem → classify 16 axioms → fix or document. **Critical path bottleneck.** Starts with axiom inventory. | MEDIUM-HIGH | 2-3 days | **Longest phase.** Runs concurrently with 54-57; re-audit after 54-57 close. |
| 59 | Adversarial defense comparing to Hardy/Dakić-Brukner/Masanes-Müller/Chiribella/Barnum-Wilce/Kent | HIGH | 1-2 days | Mostly independent. Depends weakly on Phase 56 formalization of composite. |

**Total estimated effort:** 6-11 working days across phases. JMP typical review window is 2-6 months; plenty of runway assuming no early referee report.

**Shared deliverables (created early, consumed throughout):**
- `alfsen-shultz-notes.md` — produced in Phase 54 (as part of circularity audit); consumed by 55, 57, 58. Contains, per Paper 5 citation: (volume 2001 vs 2003, chapter, section, theorem number, exact statement, match-to-Paper-5-invocation verdict).
- `phi-audit.md` — produced in Phase 57; consumed by 54, 58, 59. Enumerates every φ occurrence in `main.tex`, classifies role (tracking / inert wrapper / notational), and resolves overloading.

---

## Watch Out For (pitfalls organized by phase)

### Phase 54 (primary attack surface)
- **R1 Circularity via Jordan.** Forbidden tokens in any proof or RESULT.md: `M_n(ℂ)`, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, "operator product". Allowed tools: OUS, ≤, 1, A-S compression axioms, S1, S3, linearity, finite-dim. First task: audit v2.0 Phase 4-06 commit `9608ac54` for hidden Jordan imports.
- **R2 Decomposition vs. invariance.** State Peirce DECOMPOSITION and Peirce INVARIANCE as two separate propositions.
- **R3 Composite-map case analysis.** The corrected SP formula has TWO sums; verify invariance independently for the compression sum AND the mixing-term sum. Also handle cross-terms V₁(pₖ,pₗ) for k,l ∉ {i,j}.
- **R4 No "obvious" shortcuts.** Revised §3.3 should be ≥ submitted 20 lines at lines 508-528.

### Phase 55
- **R6 Face-phi-independence via state separation.** Beware that "states separate effects" in an OUS requires A-S spectrality (not free). If the phi-independence argument routes through Jordan-level separation, it is circular.
- **R5 A-S citation precision.** Replace bare `\cite{AlfsenShultz2003}` with `\cite[Ch.Sec.Thm]{AlfsenShultz2003}` or `\cite[...]{AlfsenShultz2001}` per claim. This is Phase 55's primary cleanup deliverable.

### Phase 56
- **R7 "Carries" equivocation.** Distinguish (1) closure: a ∘ b ∈ W when a,b ∈ W; (2) induced structure: W with restricted ∘ is itself an SPS; (3) functorial preservation: inclusion W ↪ V is an SPS morphism. Thm 5.8's downstream use requires (2) or (3); prove that, not just (1). Gudder-Greechie Example 39 (associative non-EJA SEA) is the archetypal counterexample to naive equivocation.
- **Check W is a face** before invoking vdW 2019 Thm 1. Peirce range of a projective unit IS a face, but state this explicitly.

### Phase 57
- **R8 Phi overloading across sections.** φ may play different roles in §2 (self-modeling map), §3 (tracking map with faithfulness), §4 (inert wrapper), §5-6 (local-tomo specialization). Enumerate every occurrence; either prove roles coincide or rename.
- **Phi = id on measurement-relevant states but NOT globally.** If φ is a self-modeling projection, it is NOT globally the identity. State which sub-state-space carries the inertness.

### Phase 58
- **R9 Three axiom failure types.** For each of the 16 axioms: (i) theorem-in-disguise (prove it, demote to theorem), (ii) definition-as-axiom (refactor to `def`/`structure`), (iii) statement-mismatch (weaken or prove stronger form from cited source). Type (iii) is the most dangerous: type-correct but cited-justification wrong.
- **Start with axiom inventory.** `grep -rn "^axiom " RadicalRelativity/*.lean` gives 19 total; user claims 16 Paper-5-specific. First task: reconcile by running `#print axioms` on paper-cited theorems only and counting distinct non-builtin axioms that appear.
- **Lean docstrings already cite A-S.** Existing axiom docstrings in `SelfModelingBridge.lean` reference A-S theorems; Phase 58 verifies accuracy, not invents citations. Cuts audit time ~50%.
- **Build green before audit.** `lake build` under pinned `leanprover/lean4:v4.28.0` + mathlib v4.28.0 must succeed before `#print axioms` outputs are trustworthy.

### Phase 59
- **R10 Minimal-composite adversarial magnet.** Hardy's Simplicity axiom (2001) was immediately critiqued; every subsequent reconstruction (Masanes-Müller, Chiribella et al., Dakić-Brukner, Barnum-Wilce) has had to defend its composite-system assumption. Paper 5's will be attacked. Mandatory preemption: comparison table to Hardy / Masanes-Müller / Chiribella / Barnum-Wilce / Kent 2024 critique.

### Cross-phase (all)
- **R11 Cascade from Phase 54 outcome (C).** If Phase 54 closes as (C), Phase 55's S4 phi-independence and Phase 57's phi-inertness share the same circularity pattern. Orchestrator must gate 55-59 on Phase 54 outcome.
- **R12 JMP timeline.** 16+ days at associate editor is normal pacing (typical JMP first response is 3-6 months). Do not rush. Each phase's RESULT.md should be revision-letter-ready as a standalone deliverable.

---

## Phase 54 Strategy: The Reconciled Plan

The ADDENDUM and PRIOR-WORK scouts appear to conflict on Phase 54 outcome probability but are actually complementary:

**ADDENDUM:** External literature has no pre-Jordan Peirce theorem. (B) ruled out. (C) most likely. (C-i) recommended fallback.

**PRIOR-WORK:** GPD v2.0 Phase 4-06 (commit `9608ac54`) already derived a sequential product with explicit Peirce structure. Apparent (A) route via internal prior art.

**Reconciliation (NOT a contradiction, a refinement):** External literature has no citable OUS-native Peirce-preservation theorem (ADDENDUM). Internally, GPD v2.0 Phase 4-06's corrected product formula exhibits Peirce structure by construction, giving a potential constructive (A) route — but **only if the Phase 4-06 derivation itself does not silently import Jordan structure**.

### The three-step Phase 54 plan

1. **Circularity audit of v2.0 Phase 4-06 (mandatory first task).** Read `04-06-PLAN.md` and `04-06-SUMMARY.md`. For every step in the derivation of Eq. 04-06.4, classify the tool used (OUS primitive / A-S compression axiom / S1-S3 / linearity / Jordan-level machinery). Run forbidden-token grep on the Phase 4-06 prose. Verdict: `AUDIT-PASSES` (no Jordan imports) or `AUDIT-FAILS` (Jordan-level step identified).

2. **If audit passes → attempt outcome (A).** Rebuild the §3.3 Peirce-invariance proof using only the Phase 4-06 formula plus S1+S3+compression axioms. Expected length: 30-50 lines (longer than the submitted 20 lines — anti-R4). Each Peirce subspace (V₂(pᵢ), V₁(pᵢ,pⱼ), V₀, cross-terms V₁(pₖ,pₗ) for {k,l} ∩ {i,j} = ∅) must be addressed case-by-case (anti-R3). Deliver proof + forbidden-token grep log showing zero hits.

3. **If audit fails OR attempt (A) cannot be completed in reasonable time → shift to (C-i).** Draft the "Peirce coherence" axiom S0 at OUS level. S0 should state: "for any a with spectral decomposition a = Σ λᵢ pᵢ in the sense of A-S 2001 Ch. 8, the map L_a: V → V preserves the Peirce decomposition induced by {pᵢ}." Defend S0 as natural by (i) showing it is automatic in every standard example (M_n(ℂ)^sa, C(X), spin factors), (ii) motivating from the physical content of sequential measurement (compatible measurements act block-diagonally on the joint spectral decomposition), (iii) comparing to analogous post-hoc axioms in the literature (e.g., Niestegge's "compression base" assumption). Add §3.3 paragraph explicitly introducing S0 and flagging it as an OUS-level assumption distinct from S1-S7.

**What is NOT available:** (C-iii) "restructure to derive Jordan before S4." vdW Theorem 1 consumes S4 to produce Jordan structure; inverting the derivation creates fresh circularity. **Flag this to the roadmapper as unavailable.**

**Gating Phases 55-59:** Do not start Phase 55 or Phase 57 until Phase 54 outcome is classified (A, C-i, or C-ii). Phase 58 can start in parallel (axiom inventory is independent of the §3.3 mathematical outcome). Phase 56 needs the Peirce-invariance result (as lemma) and so depends on Phase 54 closing. Phase 59 is mostly independent.

---

## Approximation Landscape

| Method / Axiom Route | Valid Regime | Breaks Down When | Controlled? | Complements |
|----|----|----|----|----|
| Phase 4-06 constructive Peirce (if audit passes) | Finite-dim spectral OUS with S1, S3, A-S compressions | Phase 4-06 silently used Jordan structure | Yes (formula is explicit) | (C-i) S0 axiom |
| OUS-primitive proof via S1+linearity (Gudder-Greechie 2002 Thm 3.2) | Effect-algebra embeds in real vector space, S1 holds | S1 is only right-linear in vdW; left-linearity must be proved separately | Partial | Spectral-OUS proof via A-S |
| (C-i) S0 "Peirce coherence" axiom | OUS-level with spectral decomposition | If defense cannot motivate S0 operationally, Phase 54 fails | No (axiom, not theorem) | Constructive proof (if available) |
| vdW 2019 KV closure (Phase 56) | Finite-dim OUS with S1-S7, W is face | W not a face; or S1-S7 not inherited on W | Yes (KV is theorem) | WWvdW 2020 three-type classification |
| Foulis-Holland S4 (Phase 55) | Orthomodular sublattice of sharp effects | P_e^{0,1} not orthomodular; non-sharp effects involved | Yes (lattice theorem) | Hanche-Olsen facial symmetry (circular pre-Jordan) |
| Hardy ancilla elimination (Phase 57) | φ commutes with all measurements OR is a fiducial relabeling | φ is genuinely state-dependent (fails inertness) | Yes (classify each use) | Chiribella purification (stronger assumption) |
| Lean `#print axioms` audit (Phase 58) | All headline theorems compile under pinned toolchain | Build fails; type-(iii) axioms hidden in subtle statement mismatches | Yes (deterministic) | Manual docstring-vs-paper cross-check |

**Coverage gaps:** No reliable pre-Jordan literature route to Peirce invariance exists. This IS the gap that Phase 54 must resolve. If (A) fails and (C-i) proves undefensible, Paper 5 has a real ordering problem requiring more than exposition work.

---

## Theoretical Connections

- **Established:** vdW 2019 Thm 1 (S1-S7 ⇒ EJA) is the hinge. Paper 5 and its v2.0 Phase 4-6 internal derivations are downstream of this theorem; any Phase 54-59 work must respect it.
- **Established:** Peirce decomposition is Jordan-algebraic in all accessible literature (HOS 1984 Ch. 2; A-S 2003 Part I; McCrimmon 2004 Ch. 17; Jenčová-Pulmannová 2021 Sec. 5 quoting A-S Thm 1.4). No OUS-native version exists.
- **Established:** Barnum-Wilce 2014 + vdW 2019 Thm 3 jointly give the EJA→C*-algebra completion used in Phase 59 defense. Paper 5 cites both correctly.
- **Conjectured:** The v2.0 Phase 4-06 corrected product formula provides a constructive (A) route to Phase 54. Status pending circularity audit.
- **Speculative:** (C-ii) "alternative S4 proof routing around Peirce entirely" — not explored in literature; attempted only if (A) and (C-i) both fail.
- **Cross-validation:** Phase 54's outcome cross-validates with the Lean formalization (Phase 58). If the 16 axioms contain one of the form "sequential product preserves Peirce subspaces", it IS Paper 5's §3.3 claim, and Phase 54's resolution (A), (C-i), or (C-ii) determines whether that axiom is (i) theorem-in-disguise, (ii) genuine primitive (defend as S0), or (iii) something else. Phase 54 ↔ Phase 58 consistency is a required check.

---

## Implications for Roadmap

### Phase dependency graph

```
Phase 54 (§3.3 Peirce preservation)  [ROOT — gates downstream]
    |-- outcome classification determines 55, 56, 57 shape
    |
    +-- Phase 55 (S4 facial structure, shared A-S citation audit)
    |       |-- produces alfsen-shultz-notes.md (shared deliverable)
    |
    +-- Phase 56 (Thm 5.8 upper bound on W)
    |       |-- uses Peirce-invariance result from 54
    |       |-- needs W-is-a-face check
    |
    +-- Phase 57 (phi inertness)
            |-- depends on 54 AND 55 (phi-independence needs Peirce + facial)
            |-- produces phi-audit.md (shared deliverable for 54, 58, 59)

Phase 58 (Lean axiom audit)  [PARALLEL, critical path]
    |-- starts with axiom inventory (independent of §3.3 outcome)
    |-- consumes alfsen-shultz-notes.md when available
    |-- consumes phi-audit.md when available
    |-- re-audit after 54-57 close

Phase 59 (minimal composite defense)  [MOSTLY INDEPENDENT]
    |-- weak dependency on 56 (composite structure formalization)
```

### Suggested phase order

1. **Phase 54** (circularity audit → attempt (A) → pivot to (C-i) if fails). MEDIUM-HIGH risk; outcome determines downstream reshape.
2. **Phase 58** (axiom inventory, build-green check) — can start in parallel with Phase 54 because axiom inventory is independent of the §3.3 outcome. Critical-path bottleneck overall.
3. **Phase 55** (S4 facial, A-S citation audit) — after Phase 54 classifies; produces shared `alfsen-shultz-notes.md`.
4. **Phase 57** (phi audit) — after 54 and 55; produces shared `phi-audit.md`.
5. **Phase 56** (Thm 5.8) — after 54; address R7 "carries" ambiguity. Can run parallel to 55/57 if 54 closes (A) or (C-i).
6. **Phase 59** (minimal composite defense) — can start any time after 56's formalization is stable; mostly independent.
7. **Phase 58 completion** — final `#print axioms` audit after 54-57 close, resolving any newly discovered axiom statement changes.

### Research flags

**Needs deeper investigation (open questions, pivot risk):**
- **Phase 54** — literature silent in required form; outcome classification will drive (or not drive) downstream phase reshape. Run the Phase 4-06 circularity audit FIRST.
- **Phase 56** — "carries" ambiguity and W-is-a-face verification are non-trivial; if W is not a face, method changes entirely.

**Follows established procedures (well-documented):**
- **Phase 59** — literature is complete (vdW 2019 Thm 3 + Barnum-Wilce 2014); this is mostly exposition/defense writing.
- **Phase 58** — Lean `#print axioms` workflow is standard; axiom-to-citation mapping is manual but mechanical. Existing docstrings in `SelfModelingBridge.lean` already carry A-S references; Phase 58 verifies rather than invents.

**Genuinely open (outcome uncertain):**
- **Phase 54** outcome (A vs C-i vs C-ii) cannot be predicted before the Phase 4-06 circularity audit completes.
- **Phase 57** outcome (phi globally inert vs. needs rename) depends on the grep-and-classify enumeration; could fall either way.

---

## Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | No OUS-native pre-Jordan Peirce-preservation theorem exists in accessible literature | ADDENDUM (A-S TOC + Jenčová-Pulmannová §5.9 direct read) | Cross-check PRIOR-WORK.md survey of vdW, HOS, Niestegge, WWvdW, Jencova, Barnum-Wilce | CONFIRMED (independent survey + author-sourced TOC + direct-read of comparison paper) |
| 2 | vdW 2019 Thm 1 cannot be inverted (consumes S4 to produce Jordan) | ADDENDUM + PRIOR-WORK | Cross-check vdW 2019 Def. 2 (S1-S7) and Thm 1 statement | CONFIRMED (structural fact about vdW's proof) |
| 3 | GPD v2.0 Phase 4-06 derived the corrected SP with explicit Peirce structure | PRIOR-WORK (commit `9608ac54`) | File references in PRIOR-WORK.md and PITFALLS.md both cite Eq. 04-06.4 | CONFIRMED (internal to GPD repository; not yet audited for circularity) |
| 4 | Paper 5 has 16 Lean axioms, 0 sorry | Milestone context + COMPUTATIONAL.md | COMPUTATIONAL.md notes `grep -rn "^axiom "` returns 19; user claims 16 Paper-5-specific | UNVERIFIED — Phase 58 first step must reconcile 16 vs 19 |
| 5 | WWvdW 2020 three-type classification supports Phase 56 upper-bound argument | PRIOR-WORK + METHODS | WWvdW 2020 classification is established; direct applicability to Thm 5.8 "carries" requires proof that W decomposes into classifiable blocks | MEDIUM — classification HIGH-confidence; application MEDIUM |

---

## Cross-Validation Matrix

|                    | A-S compressions | vdW Thm 1 (KV) | v2.0 Phase 4-06 | Lean `#print axioms` | Literature (external) |
|--------------------|:---:|:---:|:---:|:---:|:---:|
| A-S compressions   | — | vdW assumes A-S spectrality; agrees on compression existence | Phase 4-06 built on A-S compression axioms | Axiom `has_compression` should match A-S Ch. 7 | Alfsen-Shultz 2001/2003 |
| vdW Thm 1          | — | — | Phase 4-06 consistent with vdW's spectral decomposition | Axiom `spectral_reconstruct` = vdW Cor. 7 | vdW 2019 |
| v2.0 Phase 4-06    | — | — | — | Axioms encode Peirce-invariance claim (→ Phase 58 classification) | NO external check available (gap) |
| Phase 54 outcome   | Cross-check via A-S Ch. 7-8 citation precision (Phase 55) | Cross-check via vdW Def. 2 (Phase 58 must match) | Cross-check via Phase 4-06 circularity audit | Phase 58 must classify axiom (i)/(ii)/(iii) | External silence is the diagnostic |

**High-risk cell (no cross-validation available):** v2.0 Phase 4-06 against external literature. This is why the ADDENDUM's recommendation to audit Phase 4-06 internally is critical: no external check exists.

---

## Uncertainty Propagation Assessment

| Input | Quality | Affected Recommendations | Impact if Wrong |
|-------|---------|-------------------------|----------------|
| METHODS.md | GOOD | Method selection for all 6 phases; critical-path ordering | Phase 58 effort estimate may be off; alternative methods well-documented so substitution is low-risk |
| PRIOR-WORK.md | GOOD (HIGH on external literature, HIGH on Phase 4-06 existence, MEDIUM on circularity status of Phase 4-06) | Phase 54 (A) feasibility; Phase 59 completeness | If Phase 4-06 has hidden Jordan use, Phase 54 shifts (A) → (C-i); downstream phases reshape |
| COMPUTATIONAL.md | GOOD | Phase 58 tooling and time estimate; Phase 54/56 sanity-check infrastructure | Low impact; `#print axioms` well-documented, SymPy sanity checks small |
| PITFALLS.md | GOOD | Risk mitigation in all phases; phase gating logic | Medium impact; R1/R11 central to milestone success |
| ADDENDUM | AUTHORITATIVE (author-sourced, direct literature read) | Phase 54 prior probability (B essentially ruled out); (C-iii) unavailability | Shifts Phase 54 planning toward (A)-with-circularity-audit OR (C-i) |

---

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| External literature survey (vdW, A-S, HOS, Niestegge, WWvdW, Barnum-Wilce) | HIGH | Published, peer-reviewed, stable; multiple independent confirmations |
| ADDENDUM author-sourced finding (A-S TOC + Jenčová-Pulmannová direct read) | HIGH | Direct reads of authoritative sources; two independent signals converging |
| v2.0 Phase 4-06 corrected SP formula existence | HIGH | Internal GPD commit `9608ac54`, verified by SymPy numerical checks on M_2(ℂ)^sa |
| v2.0 Phase 4-06 circularity status | MEDIUM — PENDING AUDIT | No circularity audit has been run; Phase 54's mandatory first task |
| Phase 54 outcome prediction (A vs C-i) | MEDIUM | Depends on Phase 4-06 audit result |
| Phase 55-59 method recommendations | MEDIUM-HIGH | Well-documented methods; standard in field |
| Phase 58 axiom count (16 vs 19) | LOW-MEDIUM | User's 16 vs grep's 19 must be reconciled in Phase 58 first step |
| Phase 56 W-is-a-face claim | MEDIUM | Paper 5 likely has the verification but not surfaced in scouts |
| Overall milestone feasibility in 6-11 working days | HIGH | All estimates consistent; no individual phase requires new physics |

**Overall confidence:** MEDIUM-HIGH. The milestone is well-scoped for exposition hardening; risk is concentrated in Phase 54 (central structural question) and Phase 58 (bottleneck).

### Gaps to address

- **Phase 4-06 circularity audit has not been run.** Phase 54's first task must be this audit; do not begin proof attempts until audit result classifies the internal prior art.
- **Axiom count 16 vs 19.** Phase 58 first task must reconcile; downstream audit time estimate depends on count.
- **Phase 56 W-is-a-face verification.** Not surfaced in scouts; proof infrastructure assumes it but explicit check not confirmed.
- **Phase 57 phi enumeration not yet run.** `grep -n 'phi\|\\Phi\|varphi' main.tex` needs to execute before outcome can be predicted.

---

## Open Questions

| # | Question | Priority | Blocks Phase |
|---|---------|----------|-------------|
| 1 | Does v2.0 Phase 4-06 derivation silently import Jordan structure? | HIGH | 54 (mandatory first task) |
| 2 | Is the Phase 54 outcome (A), (C-i), or (C-ii)? | HIGH | 55, 56, 57 (cascading) |
| 3 | Is Paper 5's W in Thm 5.8 a face of the ambient OUS, and in what sense does it "carry" a product-form SP? | HIGH | 56 |
| 4 | How many of the 16 Lean axioms are type-(i)/(ii)/(iii)/(iv)? | HIGH | 58 |
| 5 | Is φ globally inert in Paper 5's §3-6? | MEDIUM | 57 |
| 6 | Which specific Alfsen-Shultz theorems (2001 vs 2003, chapter, proposition) are cited in each Paper 5 invocation? | MEDIUM | 55 (primary cleanup task) |
| 7 | Will an S0 "Peirce coherence" axiom be defensible in referee-response if (C-i) is adopted? | MEDIUM | 54 fallback + 59 |
| 8 | Does the JMP referee report arrive before milestone completion? | LOW (monitor) | All |

---

## Rejected Alternatives

- **(C-iii) Restructure Paper 5 to derive Jordan structure before verifying S4.** REJECTED because vdW Theorem 1 consumes S4 to produce Jordan structure; inverting creates fresh circularity. Flagged by the ADDENDUM as unavailable.
- **Cite A-S Theorem 9.37 for §3.3 Peirce claim.** REJECTED because Ch. 9 is explicitly a Jordan-state-space characterization chapter; citing it at pre-Jordan §3.3 is the circularity it is meant to solve.
- **Prove Peirce preservation by checking on M_n(ℂ)^sa and claiming it generalizes.** REJECTED (Pitfall R1 anti-pattern).
- **Collapse §3.3 to "it follows immediately".** REJECTED (Pitfall R4). Revision should be at least as long as submitted 20 lines.
- **Defer Phase 58 Lean audit to post-revision.** REJECTED: 0 sorry with unaudited axioms is not a certificate of correctness; type-(iii) statement-mismatches would silently invalidate the formalization's cited justification.

---

## Sources

### Primary (HIGH confidence)

- van de Wetering (2019), "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201. [arXiv:1803.11139](https://arxiv.org/abs/1803.11139).
- van de Wetering (2018), "Three characterisations of the sequential product," J. Math. Phys. 59, 082202. [arXiv:1803.08453](https://arxiv.org/abs/1803.08453).
- Westerbaan, Westerbaan, van de Wetering (2020), "Three types of normal sequential effect algebras," Quantum 4, 378. [arXiv:2004.12749](https://arxiv.org/abs/2004.12749).
- Alfsen & Shultz (2001), *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products*, Birkhäuser v. 179. ISBN 978-0817638900.
- Alfsen & Shultz (2003), *Geometry of State Spaces of Operator Algebras*, Birkhäuser v. 190. [Springer](https://link.springer.com/book/10.1007/978-1-4612-0019-2).
- Hanche-Olsen & Størmer (1984), *Jordan Operator Algebras*, Pitman. [Free PDF](https://hanche.folk.ntnu.no/joa/).
- Niestegge (2008), "A Representation of Quantum Measurement in Order-Unit Spaces," Found. Phys. 38, 783. [arXiv:1001.3633](https://arxiv.org/abs/1001.3633).
- Gudder & Greechie (2002), "Sequential products on effect algebras," Rep. Math. Phys. 49, 87.
- Barnum & Wilce (2014), "Local Tomography and the Jordan Structure of Quantum Theory," Found. Phys. 44, 192. [arXiv:1202.4513](https://arxiv.org/abs/1202.4513).

### Secondary (MEDIUM)

- Jenčová (2021), "Geometric and algebraic aspects of spectrality in OUS: a comparison," [arXiv:2102.01628](https://arxiv.org/abs/2102.01628).
- Jenčová, Flaminio, Kroupa (2023), [arXiv:2312.13003](https://arxiv.org/abs/2312.13003).
- Chiribella, D'Ariano, Perinotti (2011), Phys. Rev. A 84, 012311. [arXiv:1011.6451](https://arxiv.org/abs/1011.6451).
- Hardy (2001), [quant-ph/0101012](https://arxiv.org/abs/quant-ph/0101012).
- Masanes & Müller (2011), NJP 13, 063001. [arXiv:1004.1483](https://arxiv.org/abs/1004.1483).
- Masanes, Galley, Müller (2019), Nat. Comm. 10, 1361.
- Dakić & Brukner (2009), [arXiv:0911.0695](https://arxiv.org/abs/0911.0695).
- Kent (2024), [arXiv:2405.17733](https://arxiv.org/abs/2405.17733).
- Barnum, Graydon, Wilce (2020), Quantum 4, 359. [arXiv:1606.09331](https://arxiv.org/abs/1606.09331).

### Tooling and formalization

- Lean 4 manual, "Axioms and Computation", [lean-lang.org](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/).
- mathlib4, [github.com/leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4) (v4.28.0 pinned).
- Ax-Prover team (2025), "A Formalization of the Generalized Quantum Stein's Lemma in Lean," [arXiv:2510.08672](https://arxiv.org/abs/2510.08672).
- Gebhard, "Using git-latexdiff for paper rebuttals," [timothygebhard.de](https://timothygebhard.de/posts/using-git-latexdiff-for-paper-rebuttals/).

### Internal GPD prior art (HIGH confidence, directly load-bearing)

- GPD v2.0 Phase 4-06, "Peirce Feedback Extension," commit `9608ac54`, 2026-03-21. `.gpd/phases/04-sequential-product-formalization/04-06-PLAN.md` and `04-06-SUMMARY.md`. **Core internal prior art for Phase 54; circularity audit pending.**
- GPD v2.0 Phase 4 research, `.gpd/phases/04-sequential-product-formalization/04-RESEARCH.md`.
- GPD v2.0 Phase 5, local tomography and C*-promotion.
- Paper 5 source, `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` at tag `paper5-jmp-submitted`. §3.3 lines 508-528.
- Paper 5 Lean formalization, `~/repos/research/lean/RadicalRelativity/` at pinned `leanprover/lean4:v4.28.0` + mathlib v4.28.0. 16-19 `axiom` decls, 0 sorry.

---

_Synthesis completed: 2026-04-16. Overwrites prior SUMMARY.md (v13.0 Paper 6 closure content)._
_Ready for roadmapper to consume Phase 54-59 suggested structure and build the v14.0 milestone roadmap._

---

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Quantum Mechanics from Self-Modeling -- JMP Revision (v14.0)"
  synthesis_date: "2026-04-16"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md, ADDENDUM-independent-literature-check.md]
  input_quality:
    METHODS: good
    PRIOR-WORK: good
    COMPUTATIONAL: good
    PITFALLS: good
    ADDENDUM: authoritative

conventions:
  unit_system: "N/A (axiomatic / algebraic framework)"
  framework: "finite-dim order unit space over R"
  sequential_product: "a o b (Paper 5); equivalently vdW's a & b"
  axiom_set: "vdW 2019 S1-S7, arXiv:1803.11139 Def. 2"
  compression: "A-S compression C_p (Alfsen-Shultz 2001 Ch. 7)"
  renormalization_scheme: N/A
  lean_toolchain: "leanprover/lean4:v4.28.0 + mathlib v4.28.0 (pinned)"

methods_ranked:
  - name: "v2.0 Phase 4-06 corrected SP formula + circularity audit + per-term Peirce invariance"
    regime: "finite-dim spectral OUS with S1+S3+A-S compressions; conditional on Phase 4-06 audit passing"
    confidence: MEDIUM
    cost: "1-2 days"
    complements: "(C-i) axiom S0 as fallback if audit fails"
  - name: "(C-i) OUS-level 'Peirce coherence' axiom S0 + defense"
    regime: "any OUS with spectral decomposition; fallback when constructive route unavailable"
    confidence: MEDIUM
    cost: "1-2 days"
    complements: "constructive proof (if available)"
  - name: "Foulis-Holland orthomodular symmetric orthogonality for S4"
    regime: "orthomodular sublattice of sharp effects in spectral OUS"
    confidence: MEDIUM-HIGH
    cost: "0.5-1 day"
    complements: "Hanche-Olsen facial symmetry (post-Jordan only)"
  - name: "vdW 2019 Koecher-Vinberg closure on W"
    regime: "W is a face of the ambient finite-dim OUS; S1-S7 inherited"
    confidence: MEDIUM
    cost: "1-2 days"
    complements: "WWvdW 2020 three-type classification"
  - name: "Hardy-style ancilla elimination + grep audit of phi"
    regime: "phi classified per occurrence; editorial/exposition"
    confidence: MEDIUM-HIGH
    cost: "0.5-1 day"
    complements: "Chiribella purification (heavier assumption)"
  - name: "Lean #print axioms + axiom-to-citation mapping"
    regime: "pinned Lean 4.28 + mathlib v4.28.0; build green required"
    confidence: HIGH (workflow); MEDIUM (semantic match to cited sources)
    cost: "2-3 days (bottleneck)"
    complements: "manual docstring-vs-paper cross-check"
  - name: "Adversarial minimal-composite defense (Hardy/DB/MM/CDP/BW/Kent comparison)"
    regime: "editorial; no new theorems"
    confidence: HIGH
    cost: "1-2 days"
    complements: "Phase 56 composite formalization"

phase_suggestions:
  - name: "Phase 54: section 3.3 Peirce preservation"
    goal: "Prove a o V_j(p_i) subset V_j(p_i) from OUS primitives OR commit to S0 axiom with defense"
    methods: ["v2.0 Phase 4-06 corrected SP formula + circularity audit + per-term Peirce invariance", "(C-i) OUS-level 'Peirce coherence' axiom S0 + defense"]
    depends_on: []
    needs_research: false
    risk: HIGH
    pitfalls: ["R1-circularity-via-jordan", "R2-decomposition-vs-invariance", "R3-composite-map-case-analysis", "R4-obvious-rate-limit"]
    mandatory_first_task: "circularity audit of v2.0 Phase 4-06 commit 9608ac54"
  - name: "Phase 58: Lean axiom audit"
    goal: "Classify 16 (or 19?) axioms as (i)/(ii)/(iii)/(iv); verify each has literature citation matching statement"
    methods: ["Lean #print axioms + axiom-to-citation mapping"]
    depends_on: []
    needs_research: false
    risk: MEDIUM
    pitfalls: ["R9-three-axiom-failure-types", "R1-circularity-encoded-as-axiom"]
    parallel_to: ["Phase 54"]
    mandatory_first_task: "reconcile 16 vs 19 axiom count; confirm lake build green"
  - name: "Phase 55: S4 facial structure lemma"
    goal: "Prove or cite S4 (orthogonality symmetry) for P_e^{0,1}; produce alfsen-shultz-notes.md"
    methods: ["Foulis-Holland orthomodular symmetric orthogonality for S4"]
    depends_on: ["Phase 54"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["R5-vague-alfsen-shultz-citations", "R6-facial-phi-independence-via-jordan"]
    produces_shared: "alfsen-shultz-notes.md"
  - name: "Phase 57: phi inert-wrapper disambiguation"
    goal: "Classify every phi occurrence; prove global inertness or rename subsidiary roles; produce phi-audit.md"
    methods: ["Hardy-style ancilla elimination + grep audit of phi"]
    depends_on: ["Phase 54", "Phase 55"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["R8-phi-overloading-across-sections"]
    produces_shared: "phi-audit.md"
  - name: "Phase 56: Thm 5.8 upper bound on W"
    goal: "Prove W carries product-form SP in the sense required by downstream use"
    methods: ["vdW 2019 Koecher-Vinberg closure on W"]
    depends_on: ["Phase 54"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["R7-carries-equivocation", "W-is-a-face-not-verified"]
    parallel_to: ["Phase 55", "Phase 57"]
  - name: "Phase 59: minimal composite defense"
    goal: "Adversarial defense of minimal-composite assumption vs Hardy/DB/MM/CDP/BW/Kent"
    methods: ["Adversarial minimal-composite defense (Hardy/DB/MM/CDP/BW/Kent comparison)"]
    depends_on: ["Phase 56"]
    needs_research: false
    risk: LOW-MEDIUM
    pitfalls: ["R10-minimal-composite-adversarial-magnet"]

critical_benchmarks:
  - quantity: "v2.0 Phase 4-06 corrected SP formula"
    value: "a o b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b)"
    source: "GPD internal commit 9608ac54"
    confidence: HIGH
  - quantity: "Lean formalization state at JMP submission"
    value: "16 axioms (claimed); 19 top-level axiom decls in RadicalRelativity/ (verified); 0 sorry"
    source: "COMPUTATIONAL.md grep + milestone context; reconciliation needed"
    confidence: MEDIUM
  - quantity: "Classical limit of SP"
    value: "a o b = a * b (pointwise product) on C(X)"
    source: "Gudder-Greechie 2002; verified by SymPy in v2.0 Phase 4-06"
    confidence: HIGH
  - quantity: "Quantum limit of SP"
    value: "a o b = sqrt(a) * b * sqrt(a) (Lueders) on M_n(C)^sa"
    source: "vdW 2018 uniqueness; verified by SymPy on M_2(C)^sa in v2.0 Phase 4-06"
    confidence: HIGH

open_questions:
  - question: "Does v2.0 Phase 4-06 derivation silently import Jordan structure?"
    priority: HIGH
    blocks_phase: "Phase 54"
  - question: "Phase 54 outcome: (A), (C-i), or (C-ii)?"
    priority: HIGH
    blocks_phase: "Phase 55, Phase 56, Phase 57 (cascading)"
  - question: "Is Paper 5's W in Thm 5.8 a face of the ambient OUS?"
    priority: HIGH
    blocks_phase: "Phase 56"
  - question: "How many of the 16-19 Lean axioms are type-(iii) statement-mismatch?"
    priority: HIGH
    blocks_phase: "Phase 58"
  - question: "Is phi globally inert in sections 3-6, or does its role shift?"
    priority: MEDIUM
    blocks_phase: "Phase 57"
  - question: "Is S0 'Peirce coherence' axiom defensible if (C-i) is adopted?"
    priority: MEDIUM
    blocks_phase: "Phase 54 fallback + Phase 59"

contradictions_unresolved: []
# All contradictions resolved in prose:
# - ADDENDUM vs PRIOR-WORK on Phase 54 outcome was a refinement, not a contradiction:
#   external literature silent (ADDENDUM) + internal Phase 4-06 plausible (PRIOR-WORK)
#   = (A) route via internal construction, conditional on Phase 4-06 circularity audit passing.
# - 16 vs 19 axiom count is a reconciliation task for Phase 58, not a true contradiction.
```

---

**Output:** Orchestrator must write the above content (overwriting stale v13.0 content) to: `/Users/ehrlich/scratch/get-physics-done/.gpd/research/SUMMARY.md`

### Unified Notation
12 symbols reconciled, 4 convention conflicts resolved (A-S two-volume split; Peirce decomposition vs invariance; OUS compression C_p vs operator pxp; SP notation ∘ vs & vs ·).
Unit system: N/A (axiomatic/algebraic framework); all quantities dimensionless within vdW/OUS formalism.

### Executive Summary
Six internal-exposition gaps in Paper 5 (Phases 54-59); central risk is circularity via Jordan structure in §3.3 Peirce-preservation; outcome (B) external citation essentially ruled out, (C-iii) restructure unavailable (vdW Thm 1 irreversible), so recommended strategy is internal Phase 4-06 circularity audit → attempt (A) → fallback to (C-i) axiom S0. Phase 58 Lean axiom audit is critical-path bottleneck (2-3 days).

### Approximation Landscape
7 methods mapped across 6 phases. Coverage gap: no reliable pre-Jordan OUS-native Peirce-invariance method exists externally; v2.0 Phase 4-06 is the sole plausible (A) route pending audit.

### Theoretical Connections
3 established (vdW Thm 1 hinge; Peirce = post-Jordan; Barnum-Wilce + vdW Thm 3 completes EJA→C*), 1 conjectured (Phase 4-06 constructive Peirce), 1 speculative ((C-ii) non-Peirce S4 proof), plus Phase 54↔58 consistency cross-validation requirement.

### Roadmap Implications

Suggested phases: 6 (54-59)

1. **Phase 54 (ROOT)** — Peirce preservation; mandatory Phase 4-06 circularity audit first; gates downstream.
2. **Phase 58 (PARALLEL)** — Lean axiom audit; critical-path bottleneck; independent of §3.3 outcome.
3. **Phase 55** — S4 facial structure; produces shared `alfsen-shultz-notes.md`.
4. **Phase 57** — Phi disambiguation; produces shared `phi-audit.md`.
5. **Phase 56** — Thm 5.8 W upper bound; parallel to 55/57.
6. **Phase 59** — Minimal composite defense; mostly independent.

### Research Flags
Needs deeper investigation: Phase 54 (literature-silent; audit mandatory), Phase 56 (W-is-a-face verification).
Well-established procedures: Phase 59 (literature complete), Phase 58 (standard Lean workflow + existing docstrings).
Genuinely open: Phase 54 outcome (A/C-i/C-ii), Phase 57 φ inertness.

### Confidence
Overall: MEDIUM-HIGH
Gaps: Phase 4-06 circularity status (pending audit); 16 vs 19 axiom count; Phase 56 face verification; Phase 57 φ enumeration.
Open questions: 8 identified, 4 HIGH-priority.

### Ready for Research Planning
SUMMARY.md content prepared. Orchestrator must write to `.gpd/research/SUMMARY.md` (overwriting stale v13.0 content) and commit all research files, then proceed to roadmapper to build the v14.0 Paper 5 Revision milestone roadmap.
