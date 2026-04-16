# Phase 54: §3.3 Peirce Preservation from OUS Primitives - Research

**Researched:** 2026-04-16
**Domain:** Operational quantum theory / Order unit spaces / Spectral OUS / Pre-Jordan algebraic audit (pure algebra, no fields/units/dimensional analysis)
**Confidence:** MEDIUM-HIGH on decision tree, forbidden-token discipline, and audit protocol. MEDIUM on outcome (A) feasibility pending audit. HIGH on outcome (C-i) fallback structure (literature analogues exist). LOW on outcome (C-ii) (speculative, not explored in literature).

## User Constraints

See `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-CONTEXT.md` for locked decisions and constraints. Key binding constraints for this research:

- **Outcome space is locked** to (A) / (C-i) / (C-ii). (B) is ruled out per ADDENDUM; (C-iii) restructure-before-S4 is UNAVAILABLE (vdW Thm 1 consumes S4 to produce Jordan; inversion is fresh circularity).
- **Allowed tool list for any (A) proof:** S1, S3, linearity, finite-dim, A-S compression primitives (idempotency `C_p² = C_p`, positivity `C_p ≥ 0`, complement `C_p + C_{p'} = pinching` on sharp effects, `C_p(p) = p`). Nothing else.
- **Forbidden token list (any hit in RESULT.md = failure):** `M_n(ℂ)` as a proof device, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, "operator product", `f(λ,μ) = √(λμ)` as a primitive (it is a conclusion of §4, not a §3.3 tool), `h_n(ℂ)`.
- **Phase 4-06 circularity audit (DERV-54-01) is the MANDATORY FIRST TASK.** No proof attempt begins before the audit verdict is in.
- **S0 naming, placement, independence-defense form, SymPy projector family, A-S verification mechanics** are Agent's Discretion — recommend, don't over-specify.
- **Out of scope:** (B) external citation, (C-iii) restructure, Phase 55/57 cascade handling, latexdiff, website fixes, minimal-composite defense.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| GPD v2.0 Phase 4-06 (commit `9608ac54`, `derivations/04-peirce-feedback-extension.md` + `04-06-SUMMARY.md`) | Prior artifact / candidate (A) seed | Corrected SP formula Eq. 04-06.4 has explicit Peirce structure; audit determines whether it can seed (A) | DERV-54-01 audit first; inline seeded-from / avoiding-because in every (A) attempt | Planning (mandatory first task), execution (seed or avoid), verification (token-level trace) |
| `.gpd/research/ADDENDUM-independent-literature-check.md` | Benchmark (literature-silence finding) | Justifies (B)-unavailability; confirms Peirce is post-Jordan in accessible literature (A-S Ch. 9 Thm 9.37, A-S Part I Ch. 1 Thm 1.4, Jenčová-Pulmannová §5 all Jordan-level) | Cite in RESULT.md as "(B) ruled out per ADDENDUM §[Implication for Phase 1]" | RESULT.md (B-unavailability justification) |
| `.gpd/research/SUMMARY.md` | Benchmark (project-level research) | Establishes the decision tree (audit → A or C-i → C-ii fallback) and the MEDIUM prior on (A) conditional on audit | Inherit decision tree; do not re-derive | Planning block ordering |
| Alfsen-Shultz 2001 vol. 179 (*State Spaces of Operator Algebras*), Ch. 7-8 | Method anchor | Pre-Jordan-legal compression axioms `C_p² = C_p`, `C_p ≥ 0`, `C_p + C_{p'} = pinching`, `C_p(p) = p`; primary (A) foundation | Read actual book text; Prop/Thm numbers verified against book, **not paraphrased** | Every (A) attempt; `alfsen-shultz-notes.md` (shared artifact for 55/57/58) |
| Alfsen-Shultz 2003 vol. 190 (*Geometry of State Spaces of Operator Algebras*), Part I Ch. 1-3 & Ch. 9 | Benchmark (flag as pre-Jordan-illegal) | Thm 9.37 cited by Paper 5 is in the Jordan-state-space chapter; Prop 7.36 cited by Lean `SelfModelingBridge.lean` has unverified prop number | Flag both in `alfsen-shultz-notes.md`; DO NOT cite in §3.3 revision text | `alfsen-shultz-notes.md` (with explicit "pre-Jordan-illegal" verdict on 9.37) |
| vdW 2019 (arXiv:1803.11139), Def. 2 (S1-S7) and Theorem 1 | Method anchor (scope boundary) | S1 + S3 are the ONLY SN-axioms usable; S4-S7 forbidden pre-S4; Thm 1 is the sink (consumes S1-S7 to produce EJA) not a tool for (A) | Restrict (A) proofs to S1 + S3 + linearity + compressions; treat Thm 1 as the forbidden downstream | Every (A) attempt; RESULT.md scope statement |
| Paper 5 `main-jmp-submitted.tex` §3.3 lines 483-562 (key claim 508-528), frozen at git tag `paper5-jmp-submitted` | Baseline (frozen submitted text) | 20-line floor for R4; §3.3 submitted text contains the cited non-sequitur ("Compressions project onto these subspaces (Alfsen-Shultz 2003), so linearity gives a block decomposition: `seqp{a}{·}` maps each Peirce subspace to itself") that Phase 54 must replace or axiomatize | Read; measure revision against frozen text; write into `main.tex`, never `main-jmp-submitted.tex` | Every attempt (what we're replacing); exit-gate grep |
| Niestegge 2008 (arXiv:1001.3633), `U_e` compression convention | Method anchor (C-i defense) | Literature precedent for OUS-level axiomatization of compression-related coherence; S0 defense framework | Cite in the S0 defense paragraph if (C-i) is outcome | C-i §3.3 revision text |
| `peirce-post-jordan-finding` memory | Pitfall record | Paper 5's §3.3 already fell into the Jordan-smuggling trap once; load into adversarial reviewer priming | Load into `gpd-review-math` priming prompt (VALD-54-02) | Review prompt; RESULT.md as disconfirming-history note |
| Lean `~/repos/research/lean/Paper5/` (lean4 v4.28.0 + mathlib v4.28.0) | Downstream coupling | Phase 58 re-classifies `_peirce_preservation` axiom based on outcome tag (A → theorem; C-i → type-iv primitive with S0 defense) | Produce explicit outcome tag in RESULT.md | RESULT.md outcome tag |

**Missing or weak anchors:**

- **A-S 2001 Prop/Thm numbers are not yet verified against the actual book.** SUMMARY.md and CONTEXT.md both flag this as the second-most-common A-S failure mode after 2001-vs-2003 confusion. The planner must schedule an explicit "verify Prop/Thm numbers against physical book or scanned pages, do not paraphrase" task for `alfsen-shultz-notes.md`.
- **A-S 2003 Prop 7.36 (Lean `SelfModelingBridge.lean`) prop number is unverified.** Flag in `alfsen-shultz-notes.md` with an explicit research note; Phase 58 consumes.
- **No external cross-validation exists for GPD v2.0 Phase 4-06 Eq. 04-06.4.** The formula is internally consistent with SymPy checks on M_2(ℂ)^sa, but no literature source derives the same expression. This is why the circularity audit is MANDATORY and cannot be substituted by literature cross-check.
- **C-ii is genuinely speculative.** No prior work routes S4 verification around Peirce. If (A) and (C-i) both fail, (C-ii) should probably be declared BLOCKED rather than attempted.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Sequential product notation | `a ∘ b` (Paper 5 convention; keep throughout revision) | `a & b` (vdW 2019, v2.0 Phase 4); `a · b` (Jordan product, FORBIDDEN in §3.3) | Paper 5 main.tex |
| Compression notation | `C_p` (vdW and v2.0 Phase 4) | `c_p` (A-S 2001); `U_e` (Niestegge) | vdW Def. 2 notation; state equivalence once |
| Order unit space | Finite-dim archimedean OUS over ℝ with distinguished unit `1` | None — Paper 5 is finite-dim throughout | A-S 2003 Ch. 1 |
| Peirce 2-space | `V_2(p_i) := range(C_{p_i})` | `V₂(p_i)` in Unicode; identical | A-S 2003 Ch. 8 (JB-level); abstract OUS version is Phase 54's deliverable |
| Peirce 1-space | `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V - C_{p_i}V - C_{p_j}V` (equivalently `(p_i+p_j)V(p_i+p_j)` minus 2-spaces in JB setting) | Paper 5's `\peirce{ij}(b)` projector notation | v2.0 Phase 4-06 Eq. 04-06.4 definition |
| Projective unit vs. sharp effect | `p` projective iff `p² = p` via compression: `C_p(p) = p`, `C_p + C_{p'} = pinching`. Sharp iff `p ∘ p = p` and `p ∘ p' = 0` (vdW Def. 7). These coincide in finite-dim SPS but are conceptually distinct axiomatic roles. | Collapsing them is a Pitfall R5-convention trap | Convention Traps in PITFALLS.md |
| Allowed-axiom scope | S1 (additivity in 2nd arg), S3 (unitality `1 ∘ a = a` and sharp constraint `p ∘ b = C_p(b)`), linearity (derived from S1 + finite-dim), compression axioms | S4-S7 FORBIDDEN (would be pre-S4 use); Jordan product FORBIDDEN (post-vdW-Thm-1) | vdW 2019 Def. 2 + ADDENDUM |

**CRITICAL:** §3.3 revision text and all attempt files use the Paper 5 `∘` convention. `a · b` in §3.3 means what Paper 5 says it means (typically undefined pre-Jordan) and must be avoided. If any attempt slips into `&`, the forbidden-token grep should also flag notation drift for consistency audit (not a hard fail, but a drift signal).

Convention loading: the planner should emit a single convention-pin block at the top of each PLAN.md that restates this table verbatim, so executor attempts cannot drift.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `a ∘ b = Σᵢ λᵢ C_{pᵢ}(b) + Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)` | Corrected SP formula (v2.0 Eq. 04-06.4) | `derivations/04-peirce-feedback-extension.md` line ~79-82; Phase 4-06 summary §claim-corrected-product | **Candidate (A) seed IF DERV-54-01 audit PASSES.** Do not use as seed otherwise. |
| `C_p² = C_p`, `C_p ≥ 0`, `C_p(p) = p`, `C_p + C_{p'} = pinching` | A-S compression axioms | A-S 2001 Ch. 7-8 (Prop/Thm numbers to be verified) | Foundation for every (A) proof route; allowed tool |
| `a ∘ V_2(p_i) ⊆ V_2(p_i)` | Peirce 2-space invariance (target claim #1) | Paper 5 §3.3 lines 508-528 | Goal of (A) proof OR axiomatized by S0 in (C-i) |
| `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)` | Peirce 1-space invariance (target claim #2) | Paper 5 §3.3 | Goal of (A) proof OR axiomatized by S0 in (C-i); R3 cross-term case is the subtle one |
| `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` for `{k,l} ∩ {i,j} = ∅` where `a = Σ λᵢ pᵢ` with `i,j` in support of `a` | Cross-term invariance (R3 subtle case) | Pitfall R3 (PITFALLS.md); CONTEXT.md limiting-cases §5 | Mandatory coverage — most commonly missed; SymPy closeout must probe |
| S1: `a ∘ (b + c) = a ∘ b + a ∘ c` | Additivity in 2nd argument | vdW 2019 Def. 2 | Linearity of `L_a(b) := a ∘ b` follows from S1 + finite-dim |
| S3: `1 ∘ a = a`; `p ∘ b = C_p(b)` when `p` is a sharp effect | Unitality + sharp constraint | vdW 2019 Def. 2 and Def. 7 | Key identity: reduces `L_a` on sharp components to compression action |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Forbidden-token grep audit | Mechanical pass/fail on proof prose for circularity | DERV-54-01 (Phase 4-06 audit), DERV-54-02…06 (every attempt), exit gate | Phase 4-06 pattern (Step 9 circularity audit in `04-peirce-feedback-extension.md`); PITFALLS.md R1 |
| Token-level derivation trace | Step-by-step classification of each derivation step as {OUS primitive / S1 / S3 / linearity / A-S compression axiom / Jordan-level / M_n(ℂ)-level / undeclared} | DERV-54-01 (primary deliverable) | New protocol; modeled on Phase 4-06 Step 9 but more granular |
| Compression-algebra case analysis | Prove invariance separately on V_2(p_i), V_1(p_i, p_j), V_1(p_k, p_l) cross-terms, V_0 | Every (A) attempt | Pitfall R3 explicit requirement |
| Model-instantiation sanity check | Verify (A) argument does not prove too much (would mean it imports structure not present in the abstract OUS) | Early falsifier gate #3 (CONTEXT.md Decisions §Early falsifier gates) | CONTEXT.md Early falsifier gates |
| Spectral decomposition in OUS | `a = Σᵢ λᵢ pᵢ` with `{pᵢ}` orthogonal projective units; spectral OUS defines when this is available | Entry point to every (A) attempt | A-S 2001 Ch. 8 (spectral duality); vdW Def. 9 (spectrality) |
| S0 axiom formulation + canonical-example verification | State S0 at compression level; verify automatic in M_n(ℂ)^sa, C(X), spin factors | (C-i) branch | Niestegge 2008 compression-base pattern |

### Approximation Schemes

**N/A.** This is a pure-algebra derivation. No small parameter, no controlled approximation, no regime of validity in the physics sense. The "regimes" here are:

| "Regime" | Scope | Breaks Down When | Alternatives |
| -------- | ----- | ---------------- | ------------ |
| Finite-dim spectral OUS with `a = Σ λᵢ pᵢ` | Paper 5's entire setting | Infinite-dim or non-spectral OUS | Out of scope |
| Orthogonal projective unit family `{pᵢ}` | Spectral decomposition of any self-adjoint | Continuous spectrum (not Paper 5) | Out of scope |
| 4-06-audit-passed branch (attempt (A) via 4-06 route + compression combinatorics route) | If Phase 4-06 derivation is clean | Audit fails | Single non-4-06 (A) attempt then (C-i) |
| 4-06-audit-failed branch (single non-4-06 (A) attempt, then (C-i)) | If audit fails | Circularity is specifically compression-algebra (in which case (C-i) directly) | Direct pivot to (C-i) per CONTEXT.md stop/rethink trigger #2 |

## Standard Approaches

### Approach 1: Outcome (A) via v2.0 Phase 4-06 Corrected SP Formula (RECOMMENDED if audit passes)

**What:** After DERV-54-01 audit passes, use Eq. 04-06.4 as the starting expression. Prove Peirce invariance term-by-term:

- First sum `Σᵢ λᵢ C_{pᵢ}(b)`: each `C_{pᵢ}` is an A-S compression. Invariance on `V_2(p_k)` follows from compression algebra: `C_{pᵢ}(V_2(p_k)) ⊆ V_2(p_k)` when `i = k` (fixes pointwise), `= {0}` when `i ≠ k` (orthogonal projectors annihilate each other's Peirce 2-spaces via `C_{pᵢ} C_{pⱼ} = 0` for `i ≠ j`). Sum preserves subspace by linearity.
- Second sum `Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)`: each `P_{ij}` is the Peirce 1-space projection, defined as `P_{ij}(b) := b - Σ_k C_{p_k}(b)` restricted to the `(p_i, p_j)`-support. Invariance on `V_1(p_k, p_l)` is a SEPARATE claim requiring explicit case analysis (R3). The scalar weight `√(λᵢλⱼ)` is a number, not a structural tool — linearity handles it.
- Cross-terms `V_1(p_k, p_l)` with `{k,l} ∩ {i,j} = ∅`: the subtle case. `L_a` on these subspaces must be examined: the first sum contributes via compressions that annihilate (since `{k,l} ∩ {i,j} = ∅`), the second sum contributes via `P_{ij}` which by definition annihilates Peirce-2-components and preserves Peirce-1-components orthogonal to `(p_i, p_j)`. Explicit computation required.

**Why standard:** This is the only plausible (A) route. Compression-algebra-only arguments without 4-06 tend to collapse into either (i) invoking Jordan structure (forbidden) or (ii) just re-deriving 4-06. The 4-06 formula makes the block structure manifest.

**Track record:** SymPy-validated on M_2(ℂ)^sa (all Peirce-2 and mixing-1 checks pass). Has NOT been validated on M_3(ℝ)^sa with cross-term V_1(p_k, p_l) for k,l ∉ {i,j} — VALD-54-01 closeout closes this gap.

**Key steps:**

1. **DERV-54-01 audit of Phase 4-06 derivation.** Run forbidden-token grep on `derivations/04-peirce-feedback-extension.md`; classify every step of Eq. 04-06.1 → 04-06.4 derivation as {OUS primitive / S1 / S3 / linearity / A-S compression / Jordan-level / M_n(ℂ)-level proof device}. Verdict: PASS (no Jordan / M_n(ℂ)-proof-device tokens appear as proof devices, only as validation examples) or FAIL (Jordan / M_n(ℂ) used as proof device). Specific watchpoints from initial scan:
   - Line 125: "Proof (M_2(C)^sa, two-projector case)" for positivity bound — is this used as proof of the abstract bound, or only as a worked example? If proof, that's a leak.
   - Lines 119, 218, 222: `M_2(C)^sa` appears in theorem statements and "concrete realization" — classify each as proof-device vs. validation-example.
   - Paper 5 line ~543 inherits "generates a two-level face isomorphic to a spin factor, on which the Schur complement criterion gives" — this is a **spin factor** invocation in the proof of the positivity bound. Spin factors are JB-algebras; this is a Jordan-level proof device. Flag.
2. **If audit PASSES:** open `derivations/paper5-peirce-preservation/attempt-01.md` seeded from Eq. 04-06.4. State Peirce decomposition and Peirce invariance as two separate propositions (anti-R2). Prove term-by-term, case-by-case on each Peirce subspace type (anti-R3). Target length ≥ 20 lines (R4 floor), expected 30-50 lines.
3. **Early falsifier gates (all three must pass before adversarial review per CONTEXT.md Decisions):** forbidden-token self-grep; SymPy H_3(ℝ) rank-1 per-attempt gate; model-instantiation check (instantiate in M_n(ℂ)^sa and C(X), must not produce false statement).
4. **Objection routing:** if adversarial reviewer objects with non-forbidden-token argument, mark attempt-NN.md FAILED with objection quoted verbatim; open attempt-(NN+1).md with "addresses prior objection: [quote]" at top.
5. **Adversarial fresh-eyes review (VALD-54-02):** `gpd-review-math` with Phase 54 priming (load `peirce-post-jordan-finding` memory + A-S 2001 vs 2003 distinction + forbidden-token list + R1-R7). Primary. Escalate to Paper-5-primed rubric-pass Opus only on borderline verdict.
6. **Attempt cap:** 3 attempts outer bound; pause-and-rethink trigger at end of attempt-02 regardless of outcome (CONTEXT.md stop/rethink #1).

**Known difficulties at each step:**

- **Step 1 (audit):** The M_2(ℂ)^sa references in `04-peirce-feedback-extension.md` are dense. Distinguishing proof-device from validation-example requires careful reading. If ambiguous, treat as FAIL (conservative).
- **Step 2 (Peirce 1 invariance):** `P_{ij}` is defined as `b - Σ_k C_{p_k}(b)`. Proving `L_a(P_{ij}(V)) ⊆ V_1(p_i, p_j)` requires showing `L_a` commutes with the pinching `Σ_k C_{p_k}` (up to structure on Peirce 2-spaces). This is where compression combinatorics gets dense.
- **Step 2 (cross-terms V_1(p_k, p_l), k,l ∉ {i,j}):** Need to show both the first sum (compressions `C_{p_i}`, `C_{p_j}` with i,j in support of `a`) and the second sum (`P_{ij}`) map V_1(p_k, p_l) to itself. For the first sum, need `C_{p_i}(V_1(p_k, p_l)) ⊆ V_1(p_k, p_l)` — this is an A-S fact about how compressions interact with Peirce 1-spaces of orthogonal projectors, must be cited with precise Prop/Thm number.
- **Step 5 (reviewer):** distinguish "CIRCULAR" verdict from "IDENTITY" verdict per sms:minimal lesson — calling a definitional clause "circular" is framing error.

### Approach 2: Outcome (A) via Direct Compression Combinatorics (FALLBACK within audit-passed branch; PRIMARY in audit-failed branch)

**What:** Do not seed from Eq. 04-06.4. Instead build Peirce invariance directly from A-S compression primitives: if `{C_{pᵢ}}` commute pairwise and satisfy `C_{pᵢ} C_{pⱼ} = 0` for `i ≠ j` (standard A-S facts for orthogonal projective units), and `L_a = Σ λᵢ C_{pᵢ} + (mixing term)`, argue that the map block-decomposes by showing `C_{pₖ} ∘ L_a ∘ C_{pₖ} = L_a` on `V_2(p_k)` (equivalently `L_a` commutes with `C_{pₖ}` on `V_2(p_k)`).

**When to switch:** Primary approach in the audit-failed branch (single attempt per CONTEXT.md Decisions). In audit-passed branch, use as independent cross-check of Approach 1 OR as the route for attempt-02 if attempt-01 (4-06 seeded) fails on a subtle point.

**Tradeoffs:** More foundational (no reliance on 4-06 being clean) but requires reconstructing the mixing-term contribution from scratch, which is where Phase 4-06's work lives. Risk: if the mixing term is not constructible from compressions alone, Approach 2 collapses to axiomatizing the mixing term = silently adopts (C-i).

**Key subtlety:** SUMMARY.md skeptical-review §Unvalidated-assumption-2 flags that "the compression-algebra-only (A) attempt route is substantively different from the 4-06 route" may be false — if 4-06's formula is itself derivable from A-S compressions alone, the two routes degenerate. The planner should note this as a known risk; if the two routes produce identical proofs, that's evidence for soundness, not a problem.

### Approach 3: Outcome (C-i) S0 "Peirce Coherence" Axiom at Compression Level (FALLBACK if (A) fails)

**What:** Declare S0 as a new OUS-level axiom alongside S1-S7, stated at the COMPRESSION LEVEL (weakest form per CONTEXT.md Decisions §S0 axiom form):

> **S0 (candidate statement, compression-level):** Let `{pᵢ}` be a finite orthogonal family of projective units in a spectral OUS `V`. Then the compressions `{C_{pᵢ}}` pairwise commute: `C_{pᵢ} C_{pⱼ} = C_{pⱼ} C_{pᵢ}` for all `i, j`. Moreover `C_{pᵢ} C_{pⱼ} = 0` for `i ≠ j` (mutual annihilation on orthogonal Peirce 2-spaces).

Peirce invariance is then **derived** from S0 + A-S compression axioms + spectral decomposition + S1 + S3, not posited directly. The revision text states S0, proves a short lemma "S0 + S1 + S3 + compression axioms ⇒ Peirce invariance of `L_a` on V_2(p_i), V_1(p_i, p_j), V_1(p_k, p_l)", and defends S0 as natural.

**Defense strategy (CONTEXT.md Decisions §S0 axiom form):** Inline paragraph per canonical example in §3.3 revision text:

- **M_n(ℂ)^sa:** S0 holds by spectral theorem + pxp matrix-block computation. NOTE: pxp is forbidden in §3.3 broad scope, but "legal *inside* the model" per CONTEXT.md Decisions — the defense paragraph is allowed to reference the concrete model-level verification.
- **C(X):** Trivial. Projectors are characteristic functions of disjoint sets; compressions are multiplications by those functions; they pairwise commute and annihilate.
- **Spin factors:** From the Clifford relation `{e_i, e_j} = 2 δ_{ij} 1`. Non-trivial but well-known.

**Independence defense (Agent's Discretion form):** Show S0 is NOT derivable from S1-S7. Options: counterexample-model (construct a hypothetical OUS satisfying S1-S7 but violating S0), parameter-counting argument, hybrid.

**Literature analogue:** Niestegge 2008 `U_e` compression convention is canonical OUS-level-axiomatization-of-compression-behavior precedent. A-S compression-base formalism (A-S 2001 Ch. 7, and follow-ups by Foulis et al.) is the broader framework.

**Why compression-level (weakest) and not higher-level:** Directly axiomatizing "Peirce invariance of `L_a`" short-circuits the derivation (CONTEXT.md false-progress rejection §contract_coverage). Compression-level S0 is the weakest assumption that yields the needed invariance, and Peirce invariance remains a *derived* consequence of the (stated) axiom + compression primitives — the referee sees a substantive lemma, not "by S0, done".

**Downstream coupling:** If outcome is (C-i), Phase 55 (S4 phi-independence) and Phase 57 (phi-inertness) may need shared restructuring (R11). The named lemma's conditional form insulates Phase 55/56/57/58 citation interface but the *assumption set* (S0 vs. S1+S3+compressions) propagates. Flagged here; Phase 55 planning addresses.

### Approach 4: Outcome (C-ii) Alternative S4 Routing Around Peirce (NOT RECOMMENDED)

**What:** Attempt to prove S4 (orthogonality symmetry `a ∘ b = 0 ⇒ b ∘ a = 0`) without ever using Peirce invariance. Then §3.3's Peirce claim becomes unnecessary for the axiom chain, and the gap is circumvented.

**Why not recommended:** Not explored in literature (MEDIUM-LOW feasibility prior). Requires vdW Thm 1 machinery that itself uses post-S4 structure — likely collapses into (C-iii) which is UNAVAILABLE. CONTEXT.md contract coverage treats (C-ii) as a nominal outcome label but the physics_research_focus item #4 flags: "If it requires vdW Thm 1 machinery that uses post-S4 structure, flag circularity risk and note (C-ii) may collapse back to (C-i)."

**Recommendation for planner:** Do NOT schedule a dedicated (C-ii) attempt. If both (A) and (C-i) fail, declare Phase 54 BLOCKED rather than pursuing (C-ii) blindly. (C-ii) remains a label for RESULT.md outcome tag in the contract but should be treated as structurally not an active work stream.

### Anti-Patterns to Avoid

- **"Since `a ∘ b` is a Jordan product…"** — uses derived structure. The whole point of §3.3 is that Jordan structure is derived LATER (via vdW Thm 1 post-S4); invoking it here inverts the dependency.
  - _Example:_ "Because `(a ∘ b + b ∘ a)/2` is a Jordan product and Jordan multiplication respects Peirce decomposition, …" — this is exactly what the submitted §3.3's implicit assumption looks like if unpacked.
- **Citing Peirce decomposition theorem as justification for Peirce invariance of `L_a`.** (Pitfall R2.) Decomposition = V splits into subspaces (cited fact). Invariance = `L_a` respects the splitting (claim to prove). Paper 5's submitted text falls into this non-sequitur on lines ~524-528.
- **Conflating "compressions `C_{pᵢ}` preserve Peirce subspaces" with "`a ∘ (−)` preserves Peirce subspaces".** (Pitfall R3.) First is an A-S fact about individual compressions. Second is a claim about the composite map `L_a = Σ λᵢ C_{pᵢ} + Σ √(λᵢλⱼ) P_{ij}`. These are different.
- **Citing A-S Thm 9.37.** (ADDENDUM finding.) Ch. 9 is the Jordan-state-space characterization chapter; Thm 9.37 is pre-Jordan-illegal.
- **Using any of the forbidden tokens in RESULT.md:** `M_n(ℂ)`, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, "operator product", `f(λ,μ) = √(λμ)` as a primitive, `h_n(ℂ)`, `spin factor` as a proof device (vs. defense example — defense is OK in a (C-i) canonical-examples paragraph, but "generates a face isomorphic to a spin factor" as a proof step is forbidden).
- **Silently shifting to (C-iii).** If any attempt starts constructing Jordan structure before S4, stop and quote the drift line verbatim in escalation (CONTEXT.md stop/rethink #3).
- **"By S0, done" short-circuit.** (CONTEXT.md contract_coverage false-progress.) If outcome is (C-i), revision text must have a substantive derivation of V_2 and V_1 invariance from S0 + compressions, not merely state S0 and conclude.
- **Padding to meet R4's 20-line floor.** Length must come from substantive new content, not rhetorical filler.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| A-S compression idempotency | `C_p² = C_p` | A-S 2001 Ch. 7 (Prop/Thm number to verify in `alfsen-shultz-notes.md`) | Cite; use in every (A) proof |
| A-S compression positivity | `C_p ≥ 0` (preserves positive cone) | A-S 2001 Ch. 7 (verify prop number) | Cite; use |
| A-S compression complement on sharp effects | `C_p + C_{p'} = pinching` (annihilates Peirce 1-space; NOT identity in non-commutative OUS — corrected from v2.0 Phase 4 Plan 01 C4) | A-S 2001 Ch. 7 + v2.0 Phase 4-06 C4 correction | Cite; use; explicitly note NOT identity |
| A-S compression fixing projector | `C_p(p) = p` | A-S 2001 Ch. 7 | Cite; use |
| A-S Peirce DECOMPOSITION (not invariance) | `V = V_2(p) ⊕ V_1(p, p') ⊕ V_0` for a projective unit `p` and complement `p'` (in Jordan setting; abstract OUS version requires spectrality) | A-S 2003 Ch. 8 (JB-level statement); abstract OUS version is what Phase 54 works with | Cite the decomposition; do NOT conflate with invariance (R2) |
| vdW 2019 S1 | `a ∘ (b + c) = a ∘ b + a ∘ c` | vdW 2019 Def. 2 (arXiv:1803.11139) | Cite; use to get linearity of `L_a` |
| vdW 2019 S3 | `1 ∘ a = a`; `p ∘ b = C_p(b)` when `p` sharp | vdW 2019 Def. 2 + Def. 7 | Cite; use to reduce projector action |
| Phase 4-06 Eq. 04-06.4 | `a ∘ b = Σᵢ λᵢ C_{pᵢ}(b) + Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)` | `derivations/04-peirce-feedback-extension.md` | **Candidate seed for (A) attempt 01 if DERV-54-01 audit PASSES.** Do not re-derive; audit and then cite. |
| Phase 4-06 C4 correction | In non-commutative OUS, `C_p + C_{p^perp} = pinching ≠ id` | `04-06-SUMMARY.md` line 198-199 | Cite; fixes a common pitfall where `C_p + C_{p'} = id` is assumed |
| ADDENDUM finding | "No pre-Jordan OUS-native Peirce-preservation theorem exists" (verified via A-S 2003 TOC + Jenčová-Pulmannová §5.9 direct read) | `.gpd/research/ADDENDUM-independent-literature-check.md` | Cite in RESULT.md as justification for "(B) ruled out" |

**Key insight:** The planner should NOT schedule executor time to derive A-S compression properties, vdW's S1/S3, the Peirce decomposition theorem, or Eq. 04-06.4 itself. These are inputs. Executor time goes to: auditing 4-06 (DERV-54-01), constructing the invariance proof FROM these inputs, or drafting S0 + derivation + defense (C-i branch).

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `C_{pᵢ} C_{pⱼ} = 0` for orthogonal projective units `i ≠ j` | Off-diagonal compressions annihilate; simplifies `L_a` block computation | A-S 2001 Ch. 7-8 (verify precise statement) | In a spectral OUS with orthogonal projective family |
| `C_{pᵢ}(V_2(p_k)) = {0}` for `i ≠ k`, `= V_2(p_k)` pointwise for `i = k` | Block-diagonality of compression sum on Peirce 2-spaces | Direct consequence of Peirce decomposition + compression algebra | Abstract OUS with spectrality |
| `C_{pᵢ} + C_{pⱼ} = C_{pᵢ + pⱼ}` when `pᵢ, pⱼ` orthogonal | Compressions add on disjoint supports | A-S 2001 Ch. 7-8 (verify) | Orthogonal projective units |
| Sharp constraint via S3: `pᵢ ∘ b = C_{pᵢ}(b)` | Reduces linear action on sharp components to compression | vdW 2019 Def. 2 + Def. 7 | `pᵢ` sharp |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| "Sequential product spaces are Jordan algebras" | van de Wetering | 2019 | arXiv:1803.11139 | S1, S3, Def. 7 (sharp effects) — the ONLY axioms allowed in Phase 54 proofs |
| "Three characterisations of the sequential product" | van de Wetering | 2018 | arXiv:1803.08453 | Functional-calculus characterization (used in `ref-vdw2018` of 4-06); secondary reference |
| *State Spaces of Operator Algebras* (vol. 179) | Alfsen & Shultz | 2001 | ISBN 978-0817638900 | Compression theory Ch. 7-8 (pre-Jordan-legal); primary (A) foundation |
| *Geometry of State Spaces of Operator Algebras* (vol. 190) | Alfsen & Shultz | 2003 | Springer 10.1007/978-1-4612-0019-2 | Flag Thm 9.37 (pre-Jordan-illegal); flag Prop 7.36 (Lean `SelfModelingBridge.lean` citation, prop number unverified) |
| "Geometric and algebraic aspects of spectrality in OUS: a comparison" | Jenčová & Pulmannová | 2021 | arXiv:2102.01628 | ADDENDUM evidence: §5.9 cites A-S Thm 1.4 for Peirce-in-JB-algebras; OUS-level §3-4 has no Peirce |
| "A Representation of Quantum Measurement in Order-Unit Spaces" | Niestegge | 2008 | arXiv:1001.3633 | `U_e` compression convention; literature analogue for OUS-level axiomatization (C-i defense) |
| GPD v2.0 Phase 4-06 | — | 2026-03-21 | Internal commit `9608ac54` | **CORE internal prior art.** Audit target. |
| Paper 5 `main-jmp-submitted.tex` §3.3 lines 508-528 | — | 2026-03-28 | Frozen at tag `paper5-jmp-submitted` | Baseline text being revised; identifies the exact non-sequitur ("Compressions project onto these subspaces (A-S 2003), so linearity gives a block decomposition: `seqp{a}{·}` maps each Peirce subspace to itself") that Phase 54 must replace |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | Latest (available in project venv; symbolic matrices, `Rational` eigenvalues) | Per-attempt rank-1 sanity gate on H_3(ℝ) (VALD-54-01 per-attempt); closeout artifact with cross-term V_1(p_k, p_l) coverage | Used throughout v2.0 Phase 4 (`code/sp_verification.py`); symbolic-exact rank-1 matrix algebra; no numerical tolerance issues for small matrices |
| `grep` / ripgrep | System | Forbidden-token audit on attempt files, `main.tex`, and Phase 4-06 derivation text | Standard; deterministic; integrates with CI |
| `git log`, `git show 9608ac54 --stat` | System | Access v2.0 Phase 4-06 derivation at the specified commit | Standard git |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| `gpd-review-math` agent | Adversarial fresh-eyes review (VALD-54-02 primary) | At the end of each attempt that passes the three early falsifier gates |
| General-purpose Opus subagent | Paper-5-primed rubric pass (VALD-54-02 escalation) | ONLY when `gpd-review-math` returns borderline (per CONTEXT.md Decisions §Adversarial fresh-eyes review). Not belt-and-suspenders. |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| SymPy (symbolic-exact) | NumPy numerical with `np.testing.assert_allclose` | Introduces floating-point tolerance; R3 cross-term check where difference may be exactly zero symbolically but small-nonzero numerically is risky. Stay with SymPy unless runtime exceeds 1 sec (unlikely). |
| `gpd-review-math` primary | Cold-read Opus primary | Cold-read "feels decisive but can be wrong in program-specific ways" per sms:minimal lesson; Phase 54-primed `gpd-review-math` is the right combination of context-aware + framing-neutral (CONTEXT.md rationale). |
| Paper-5-primed Opus primary | `gpd-review-math` + Phase-54-priming | Paper-5-primed Opus amplifies framing (priming + general-purpose model = priming dominates). Wrong choice for primary. Right for escalation. |
| Full A-S textbook scan | TOC-driven targeted lookup | TOC-driven is faster and ADDENDUM already gives the key structural findings. But Prop/Thm numbers MUST be verified against the book text (CONTEXT.md user guidance), not paraphrased. |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| SymPy per-attempt rank-1 gate on H_3(ℝ) (VALD-54-01 per-attempt) | < 1 sec (CONTEXT.md constraint) | None — trivial 3x3 symbolic matrix algebra | No mitigation needed |
| SymPy closeout with V_1(p_k, p_l) cross-term coverage (R3) | < 5 sec (estimate) | Slightly more projectors (≥ 3 orthogonal rank-1 on H_3(ℝ) or larger) | Consider H_4(ℝ)^sa if cross-terms need 4 orthogonal projectors; still under 10 sec |
| Forbidden-token grep on 400-line Phase 4-06 derivation | < 1 sec | None | Standard |
| Token-level derivation trace classification (DERV-54-01) | 2-4 hours of reading | Human/agent attention; `04-peirce-feedback-extension.md` is 423 lines and dense | Split trace into step-by-step table; one row per derivation step |
| `gpd-review-math` adversarial review | ~5-15 min per attempt | Review latency; context load | Provide attempt file + CONTEXT.md + ADDENDUM + `peirce-post-jordan-finding` memory + forbidden-token list as priming |

**Installation / Setup:**

```bash
# SymPy should already be in the project venv. If not:
pip install sympy  # or: uv add sympy

# No additional installation needed; grep/ripgrep and git are system tools.
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| Forbidden-token grep on attempt draft | No circularity via token leak | `rg -n -w "(Jordan\|EJA\|Lüders\|pxp\|h_n\|operator product)" derivations/paper5-peirce-preservation/attempt-NN.md` — also check `M_n\(ℂ\)` and `√a\s*b\s*√a` as regex | Zero hits. Any hit = attempt unsalvageable, close and open next. |
| Forbidden-token grep on RESULT.md (exit gate) | Final output has no circular content | Same grep pattern on RESULT.md | Zero hits |
| SymPy per-attempt rank-1 gate | Numerical prediction of lemma on H_3(ℝ) with 2 orthogonal rank-1 projectors | `python3 derivations/paper5-peirce-preservation/attempt-NN.py` | PASS on `a ∘ V_2(p_1) ⊆ V_2(p_1)` and `a ∘ V_1(p_1, p_2) ⊆ V_1(p_1, p_2)` |
| SymPy closeout (R3 cross-term) | Cross-term V_1(p_k, p_l) invariance for `{k,l} ∩ {i,j} = ∅` on H_3(ℝ) or H_4(ℝ) | `python3 derivations/paper5-peirce-preservation/closeout-sympy.py` | PASS on V_1(p_k, p_l) cross-term; separate artifact referenced in RESULT.md |
| Model-instantiation sanity check | Proof not stronger than true | Instantiate the (A) argument in M_n(ℂ)^sa, C(X), spin factors; check it doesn't imply a false statement | All three models agree with known Peirce invariance |
| Lemma-verbatim-in-revision exit gate | Named lemma statement appears verbatim in §3.3 revision text | `diff <(extract_lemma_from RESULT.md) <(extract_lemma_from main.tex §3.3)` + manual semantic review | Both grep exact-match AND manual semantic review PASS before Phase 54 closes |
| Outcome-tag routing | RESULT.md has exactly one of (A)/(C-i)/(C-ii) labels for Phase 58 routing | `grep -E "^Outcome: (A|C-i|C-ii)$" RESULT.md` | Exactly one hit |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| M_n(ℂ)^sa instantiation | Finite-dim complex self-adjoint matrices | Peirce invariance holds by spectral theorem + pxp matrix-block computation (legal INSIDE the model, NOT in the §3.3 proof) | Standard JB-algebra theorem |
| C(X) (commutative) instantiation | Classical effect algebra | Peirce invariance trivial: projectors commute, compressions = multiplication by characteristic functions, decomposition collapses | Gudder-Greechie 2002; v2.0 Phase 4-06 classical-limit SymPy verification |
| Spin factor instantiation | Clifford algebra with `{e_i, e_j} = 2 δ_{ij} 1` | Peirce invariance follows from Clifford anti-commutation | Standard JB-algebra theorem |
| Rank-1 projectors on H_3(ℝ)^sa | SymPy per-attempt gate | `a = λ_1 p_1 + λ_2 p_2` with `p_1 ⊥ p_2` rank-1 on H_3(ℝ); `a ∘ b` must land in V_j for `b ∈ V_j` | v2.0 Phase 4 SymPy methodology |
| Cross-term V_1(p_k, p_l), `{k,l} ∩ {i,j} = ∅`, on H_3(ℝ)^sa or larger | SymPy closeout | At least 3 orthogonal rank-1 projectors (H_3) for non-trivial cross-terms; closeout probes explicitly | R3 (PITFALLS.md); CONTEXT.md limiting-cases |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| Per-attempt rank-1 SymPy | Symbolic-exact (via `sympy.Rational`) or equality-check in Symbol form | 0 (symbolic exact) or 1e-12 (numeric fallback) | `a ∘ b` lies in expected Peirce subspace: checked via `C_{p_k}(a ∘ b) = a ∘ b` for `b ∈ V_2(p_k)` and similar for V_1 |
| Closeout cross-term | Symbolic-exact preferred | 0 (symbolic exact) | Same as above, extended to V_1(p_k, p_l) for disjoint index sets |
| Model instantiation | Compare (A) argument's prediction to known result on M_n(ℂ)^sa / C(X) / spin factor | N/A (conceptual check) | Agreement with established theorem |

### Red Flags During Computation

- **Forbidden-token grep returns ANY hit** on an attempt file or RESULT.md — the attempt is unsalvageable; close and open next with drift note.
- **SymPy per-attempt gate fails** — the lemma's prediction is numerically wrong on a concrete rank-1 case. Structural red flag; do not attempt to patch, open next attempt.
- **SymPy closeout cross-term case fails** — even if per-attempt gate passed, cross-term failure indicates R3 was not addressed. Attempt closure blocked until addressed.
- **Model instantiation produces a FALSE statement** — means the (A) argument proved something stronger than actually holds (e.g., implies associativity that C(X) lacks, or something). Fatal; not patchable.
- **Adversarial reviewer (`gpd-review-math`) returns CIRCULAR with non-forbidden-token argument** — the circularity is subtler than the grep catches. Quote objection verbatim in next attempt's header.
- **Any attempt invokes S5-S7** — pre-S4 forbidden axiom use. The Paper 5 submitted §3.3 proof at `main-jmp-submitted.tex` line ~530 "compatible associativity (\ref{ax:S5}), eigenvalue symmetry, and coalescence force E_{ij} to be a scalar multiple" uses S5. This is a downstream claim (Proposition coherence) but §3.3 Peirce-INVARIANCE (Phase 54's scope) must NOT use S5.
- **Any attempt introduces a spin-factor proof device** — Paper 5's positivity bound proof at line ~547-554 "generates a two-level face isomorphic to a spin factor, on which the Schur complement criterion gives …" is a spin-factor proof device. Spin factors are JB-algebras. This is the kind of drift to catch.
- **Attempt-02 ends (outcome irrelevant)** — pause (CONTEXT.md stop/rethink #1). Human reviews before attempt-03 or pivot.
- **4-06 audit FAIL at the branch point** — pause (CONTEXT.md stop/rethink #2). Confirm routing: default is single non-4-06 (A) attempt then (C-i), but audit failure trace may argue for direct (C-i).
- **Attempt begins constructing Jordan structure before S4** — pause (CONTEXT.md stop/rethink #3). Escalate with explicit drift-line quote, NOT a summary.

## Common Pitfalls

### Pitfall 1: R1 — Circularity via Jordan (the central pitfall)

**What goes wrong:** Using `a · b = (1/2)(a ∘ b + b ∘ a)` treated as operator product, or invoking `M_n(ℂ)^sa` as a proof device, or citing vdW Thm 1's conclusion ("SP is a Jordan algebra") to verify a property needed INSIDE the proof of S4 or pre-vdW-Thm-1 claims.
**Why it happens:** Mental model of `L_a` on M_n(ℂ)^sa is the prototype; reflexive verification-on-M_n instinct; "compression" ambiguity between A-S compression `C_p` (OUS-level) and B(H) compression `pxp` (operator-level).
**How to avoid:** Pin allowed-tool list at top of every attempt (S1, S3, linearity, finite-dim, A-S compression axioms); forbidden-token grep on every draft before sealing.
**Warning signs:** "Since `a ∘ b` is a Jordan product...", `(1/2)(ab + ba)` notation, `pxp` notation, "self-adjoint operator multiplication", "by the Lüders rule", "matrix block structure".
**Recovery:** Attempt unsalvageable; close; open next with drift-token note at top.

### Pitfall 2: R2 — Decomposition vs. Invariance Non-Sequitur

**What goes wrong:** Citing "A-S Peirce decomposition" as justification for "`a ∘ V_2(pᵢ) ⊆ V_2(pᵢ)`". Decomposition = V splits (cited fact). Invariance = `L_a` respects the split (claim to prove). Paper 5 submitted §3.3 line ~525 does exactly this: "Compressions project onto these subspaces (A-S 2003), so linearity gives a block decomposition: `seqp{a}{·}` maps each Peirce subspace to itself."
**Why it happens:** "Peirce" is load-bearing language; in Jordan theory, decomposition and Jordan-action-on-decomposition are often stated together (because in a Jordan algebra, both are theorems). Paper 5 reflexively imports the combined statement.
**How to avoid:** State Peirce DECOMPOSITION and Peirce INVARIANCE as two separate propositions in every attempt. Decomposition is cited (A-S 2003 Ch. 8); invariance needs a proof.
**Warning signs:** "By the Peirce decomposition theorem, `L_a` respects …", "Compressions project onto these subspaces, so linearity gives a block decomposition: `L_a` respects the splitting."
**Recovery:** Separate the two claims in next draft; the decomposition is fine to cite, invariance needs a constructed proof.

### Pitfall 3: R3 — Single-Compression vs. Composite-Map Invariance

**What goes wrong:** Proving "compressions `C_{pᵢ}` preserve their own Peirce 2-spaces" (A-S fact about the LIST of compressions) and claiming this gives "`L_a = Σ λᵢ C_{pᵢ} + Σ √(λᵢλⱼ) P_{ij}` preserves Peirce subspaces" (claim about the SUM). The mixing term `P_{ij}` is a separate object with separate invariance properties; cross-terms V_1(p_k, p_l) with `{k,l} ∩ {i,j} = ∅` are the most subtle case, commonly missed.
**Why it happens:** Formula visual pattern: "compressions appear; compressions preserve their subspaces; therefore L_a does". Misses that each TERM needs separate analysis and that the scalar weights don't help.
**How to avoid:** Every (A) proof does case analysis on L_a's action on V_2(p_i), V_1(p_i, p_j), V_1(p_k, p_l) with disjoint index set, V_0. SymPy closeout artifact (VALD-54-01 closeout) explicitly probes the disjoint-index cross-term.
**Warning signs:** Proof shorter than ~30 lines; absence of the string `P_{ij}`, `Peirce 1`, or `cross-term`; SymPy code tests only V_2 and V_1(p_i, p_j) with matching indices.
**Recovery:** Expand case analysis; add cross-term SymPy test to closeout.

### Pitfall 4: R4 — "Obvious" Rate-Limit / Padding / Silent Shortening

**What goes wrong:** Paper 5 §3.3 lines 508-528 spends 20 lines on the claim. A shorter revision loses content. A revision that is 20 lines of padding ("by the structure of the decomposition, it follows that …") doesn't count either.
**Why it happens:** Pressure to tighten; correct intuition that the claim is TRUE on M_n(ℂ)^sa combined with wrong inference that it is OBVIOUS.
**How to avoid:** R4 floor = 20 lines in §3.3 alone (default) or distributed across §3.2 + §3.3 (Agent's Discretion). Length must come from substantive case analysis, not rhetorical filler. Forbidden words: "obvious", "clearly", "immediately follows" (acceptable only following a cited theorem number with a page reference).
**Warning signs:** Revised §3.3 is shorter than submitted; contains "obvious"/"clearly"; or is 40 lines but removes substantive content and adds rhetoric.
**Recovery:** Restore substantive content; add case analysis; attempt-NN.md FAILED if the revision text passes R4's line count but the line-by-line audit shows padding.

### Pitfall 5: Framing Error in Adversarial Review (sms:minimal lesson)

**What goes wrong:** `gpd-review-math` or a general-purpose reviewer returns "CIRCULAR" when the actual objection is about a definitional clause (which by nature is self-referential without being circular in the proof-theoretic sense).
**Why it happens:** "Circular" is easy to say; distinguishing circularity-as-proof-error from identity-as-definition requires the reviewer to state its framing.
**How to avoid:** Review prompt explicitly tells reviewer to distinguish "CIRCULAR" (proof inverts dependency) from "IDENTITY" (definitional clause looks self-referential but isn't a proof step). Reviewer must state which framing it's applying.
**Warning signs:** Reviewer verdict "CIRCULAR" without a specific line-number quote of the circularity.
**Recovery:** Escalate to Paper-5-primed rubric-pass Opus only if the `gpd-review-math` verdict is genuinely inconclusive (borderline). Do NOT routinely escalate.

### Pitfall 6: Silent (C-iii) Drift

**What goes wrong:** An attempt quietly starts constructing Jordan structure (e.g., defining `a · b := (a ∘ b + b ∘ a)/2` and using its properties) before S4 has been verified. This is (C-iii), which is UNAVAILABLE per CONTEXT.md / ADDENDUM / SUMMARY.md.
**Why it happens:** Natural mathematical instinct to symmetrize the product; once you have the Jordan product, Peirce machinery is available; but the whole POINT of §3.3 is to NOT assume Jordan.
**How to avoid:** CONTEXT.md stop/rethink #3: any attempt that constructs Jordan structure pre-S4 must escalate with explicit drift-line quote.
**Warning signs:** Attempt introduces `·` notation; attempt uses `{a, b, c}` (Jordan triple product); attempt uses Macdonald's theorem; attempt invokes EJA classification.
**Recovery:** Escalate IMMEDIATELY with explicit quote of the drift line (not just "Jordan detected"). Do not attempt to salvage.

## Level of Rigor

**Required for this phase:** Formal proof (in mathematical style) grounded in a pinned axiom set.

**Justification:** This is pure algebra, not physics approximation. The claim is either proved or not; there is no "controlled approximation" mode. The rigor must be sufficient to withstand a JMP referee's scrutiny of whether the proof uses only the stated primitives.

**What this means concretely:**

- Every equation must be typeable from preceding equations + the allowed-tool list.
- Case analysis must be exhaustive: V_2(p_i), V_1(p_i, p_j), V_1(p_k, p_l) disjoint, V_0.
- Citations must be precise: A-S 2001 Ch. 7 Prop/Thm X.Y (verified against book text, not paraphrased).
- SymPy sanity checks are necessary but NOT sufficient — they catch wrong lemmas, not right-lemma-wrong-proof.
- R4's 20-line floor is a measure of substantive content, not a stylistic target.
- No hand-waving: "a standard argument shows" is forbidden without a specific reference.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Cite A-S 2003 Thm 9.37 for Peirce direct sum | Flag as pre-Jordan-illegal; must cite A-S 2001 Ch. 7-8 or add S0 axiom | 2026-04-16 (ADDENDUM finding) | Paper 5 submitted §3.3 cannot rely on Thm 9.37; requires constructive proof or S0 |
| Cite Peirce decomposition theorem as justification for L_a invariance | State decomposition and invariance separately; prove invariance (or axiomatize) | 2026-04-16 (Paper 5 §3.3 audit) | Submitted §3.3 has this non-sequitur explicitly (R2) |
| Invoke `M_n(ℂ)^sa` pxp matrix block structure in §3.3 proof | Forbidden; allowed only inside canonical-example defense paragraph if (C-i) | v2.0 GPD circularity discipline | Paper 5 §3.3 positivity-bound proof at line ~547-554 uses spin-factor / Schur-complement — pre-Jordan-illegal proof device |

**Superseded approaches to avoid:**

- **Spin-factor Schur-complement proof of positivity bound:** JB-algebraic; pre-Jordan-illegal. Paper 5 submitted uses this at line ~547-554. Must be replaced for the POSITIVITY BOUND (out of Phase 54 scope, but noted) and not repeated for PEIRCE INVARIANCE in Phase 54.
- **"Since `a ∘ b` is a Jordan product…":** Classic circularity.
- **Cite A-S Thm 9.37:** Chapter 9 is Jordan state-space characterization; Thm 9.37 is pre-Jordan-illegal per ADDENDUM.

## Open Questions

1. **Does the Phase 4-06 derivation silently import Jordan structure?**
   - What we know: SUMMARY.md's internal review (via `04-06-SUMMARY.md` line 121-133) says `fp-hilbert-import` is REJECTED — "Circularity audit passed. No operator sqrt, trace, inner product, or C*-multiplication in the formal construction." SUMMARY.md confidence: MEDIUM-PENDING-AUDIT.
   - What's unclear: (a) The positivity-bound proof in `04-peirce-feedback-extension.md` line 125 is explicitly "Proof (M_2(C)^sa, two-projector case)" — is this a proof of the abstract bound or a validation example? (b) Paper 5 §3.3 at line ~547-554 inherits a spin-factor / Schur-complement argument that is JB-algebraic. (c) Eq. 04-06.4's derivation via "positivity bound + self-modeling faithfulness selects f = √(λᵢλⱼ)" may implicitly use S5 (compatible associativity, required for Paper 5's `prop:coherence` Proposition).
   - Impact on this phase: If audit FAILS, the 4-06 route is closed; single non-4-06 (A) attempt then (C-i).
   - Recommendation: DERV-54-01 must be the planner's first task. Treat ambiguous M_n(ℂ)^sa uses as proof-device (conservative FAIL) unless the derivation makes the validation-example role explicit.

2. **Is the compression-algebra-only (A) route substantively different from the 4-06 route?**
   - What we know: SUMMARY.md skeptical review §unvalidated-assumption-2 flags this.
   - What's unclear: If the 4-06 formula is itself derivable from A-S compressions alone, the two routes collapse into one.
   - Impact: May reduce (A) attempt diversity; degraded pivot options.
   - Recommendation: Treat as distinct routes in planning; if execution shows they're identical, this is evidence for soundness and reduces worry, not a structural problem.

3. **Is `gpd-review-math` with Phase 54 priming substantively better than cold read at catching Jordan-smuggling?**
   - What we know: SUMMARY.md skeptical review §unvalidated-assumption-3 flags this as an unvalidated meta-claim (based on sms:minimal reasoning).
   - What's unclear: No previous controlled comparison; framing-aware review is plausibly better but unverified.
   - Impact on this phase: If primary reviewer has a blind spot, escalation to Paper-5-primed Opus should catch it. The two-layer design mitigates the risk.
   - Recommendation: Proceed with primary-plus-borderline-escalation; record any escalation outcomes for future meta-research.

4. **Does the "submitted §3.3 always meant (C-i) implicitly" framing improve referee optics?**
   - What we know: SUMMARY.md skeptical review §competing-explanation suggests Paper 5's original authorship may have relied on Peirce invariance as an OUS-level intuition without axiomatizing it — in which case (C-i) is "correction of the original argument's implicit assumption" not "new fallback."
   - What's unclear: How the referee will read the framing.
   - Impact: If (C-i) is the outcome, the §3.3 revision text's framing matters for referee response.
   - Recommendation: Agent's Discretion per CONTEXT.md; executor picks framing during (C-i) drafting. Recommend: "in revising we found that the Peirce invariance step requires an OUS-level input beyond S1-S7; we introduce this explicitly as S0."

5. **What Prop/Thm numbers in A-S 2001 Ch. 7-8 correspond to the compression axioms actually used?**
   - What we know: Idempotency, positivity, complement, projector-fix are standard; precise numbers are not verified.
   - What's unclear: Paraphrase drift risk is flagged by CONTEXT.md as second-most-common A-S failure mode.
   - Impact: `alfsen-shultz-notes.md` shared artifact (consumed by 55, 57, 58) depends on this; referee will attack vague citations (R5).
   - Recommendation: Schedule explicit "verify Prop/Thm numbers against physical book or scanned pages, not paraphrased" task in `alfsen-shultz-notes.md` plan.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Approach 1 (4-06 seeded (A)) | DERV-54-01 audit FAILS | Approach 2 (compression combinatorics (A), single attempt) then (C-i) | ~0.5 day to open non-4-06 attempt; (C-i) is ~1 day |
| Approach 2 (compression combinatorics (A)) | 2-3 attempts exhausted without clean proof | Approach 3 (C-i) S0 axiom | ~1 day to draft S0 + derivation + defense paragraphs |
| Approach 3 (C-i) | S0 independence defense cannot be constructed | Declare BLOCKED (do NOT pursue Approach 4 / C-ii) | Escalate to user; milestone-level decision |
| Audit-fail route: single non-4-06 attempt | The circularity trace shows the issue is specifically compression-algebra | Direct pivot to (C-i), skipping single attempt | ~0 cost; saves half a day |

**Decision criteria:**

- **Abandon Approach 1 when:** (a) DERV-54-01 audit FAILS with Jordan-import identified in 4-06 derivation, OR (b) attempt-02 ends without clean proof (CONTEXT.md stop/rethink #1).
- **Abandon Approach 2 when:** compression combinatorics can't construct the mixing-term contribution, OR the argument re-derives Eq. 04-06.4 that the audit failed on.
- **Abandon Approach 3 when:** S0 cannot be stated without being equivalent to the thing being proved (circular axiomatization), OR the three canonical-example defenses cannot be written without invoking pre-Jordan-illegal tools.
- **Do NOT abandon Approach 3 just because the axiom is "ugly"** — a defensible axiom is the outcome, not failure. The question is whether it is a defensible OUS-level input.

## Sources

### Primary (HIGH confidence)

- **van de Wetering (2019)**, "Sequential product spaces are Jordan algebras," JMP 60, 062201. [arXiv:1803.11139](https://arxiv.org/abs/1803.11139). — Def. 2 (S1-S7 verbatim), Theorem 1 (S1-S7 fin-dim ⇒ EJA). S1 and S3 are the ONLY allowed SN-axioms here.
- **Alfsen & Shultz (2001)**, *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products*, Birkhäuser Progress in Math v. 179. ISBN 978-0817638900. — Compression theory Ch. 7-8 (pre-Jordan-legal). Primary (A) foundation.
- **Alfsen & Shultz (2003)**, *Geometry of State Spaces of Operator Algebras*, Birkhäuser Progress in Math v. 190. [Springer](https://link.springer.com/book/10.1007/978-1-4612-0019-2). — Thm 9.37 cited by Paper 5 is pre-Jordan-illegal. Part I Ch. 1-3 develops Peirce Jordan-algebraically. Flag in `alfsen-shultz-notes.md`.
- **Paper 5 `main-jmp-submitted.tex` §3.3 lines 483-562** (frozen at git tag `paper5-jmp-submitted`). — Baseline text being revised.
- **v2.0 Phase 4-06** (`derivations/04-peirce-feedback-extension.md` + `.gpd/phases/04-sequential-product-formalization/04-06-SUMMARY.md`), commit `9608ac54`, 2026-03-21. — Candidate (A) seed; audit target.
- **`.gpd/research/ADDENDUM-independent-literature-check.md`** (2026-04-16). — (B)-unavailability justification.
- **`.gpd/research/SUMMARY.md`** (2026-04-16). — Decision tree and MEDIUM prior on (A) conditional on audit.
- **`.gpd/research/PITFALLS.md`** (2026-04-16). — R1-R11 pitfall catalogue, especially R1-R4 for Phase 54.

### Secondary (MEDIUM)

- **Jenčová & Pulmannová (2021)**, "Geometric and algebraic aspects of spectrality in OUS: a comparison," [arXiv:2102.01628](https://arxiv.org/abs/2102.01628). — §5.9 cites A-S Thm 1.4; §3-4 OUS-level has no Peirce. ADDENDUM evidence.
- **Niestegge (2008)**, "A Representation of Quantum Measurement in Order-Unit Spaces," Found. Phys. 38, 783. [arXiv:1001.3633](https://arxiv.org/abs/1001.3633). — `U_e` compression convention; C-i defense framework.
- **Gudder & Greechie (2002)**, "Sequential products on effect algebras," Rep. Math. Phys. 49, 87. — Classical limit; Example 39 non-EJA SEA (Phase 56 concern, but referenced for awareness).
- **Hanche-Olsen & Størmer (1984)**, *Jordan Operator Algebras*, Pitman. [Free PDF](https://hanche.folk.ntnu.no/joa/). — §2.6 Peirce decomposition (Jordan-only) — reference for what (C-i) is NOT importing.
- **van de Wetering (2018)**, "Three characterisations of the sequential product," JMP 59, 082202. [arXiv:1803.08453](https://arxiv.org/abs/1803.08453). — Referenced by `ref-vdw2018` in 4-06 audit.

### Tertiary (LOW — methodological / framing)

- **`peirce-post-jordan-finding` memory** — prior incident record; load into adversarial reviewer priming.
- **`sms:minimal` framing lesson** — "CIRCULAR" vs. "IDENTITY" distinction in reviewer prompt discipline.

## Caveats and Alternatives (Pre-Submission Self-Critique)

**What assumption am I making that might be wrong?**
I'm assuming the CONTEXT.md's (A)/(C-i)/(C-ii) outcome space is exhaustive. It is possible there's a fourth outcome: restate §3.3 without the Peirce invariance claim at all, and route around it in §3.4/§3.5. This is not (C-ii) (which preserves the claim but routes S4 around it) nor (C-iii) (which derives Jordan before S4). It's "drop the claim entirely and find downstream consequences that don't need it." This is not in the CONTEXT.md outcome space and should probably stay there — but the planner should note it as a last-resort option if all three listed outcomes fail.

**What alternative did I dismiss too quickly?**
I dismissed (C-ii) as speculative. It's possible that a clever S4 proof routing around Peirce exists in the literature under a different name (e.g., via Gudder-Greechie's direct construction, or via spectral ordering arguments). A dedicated literature sweep might turn something up. But CONTEXT.md explicitly says (C-ii) is a label not an active work stream, so this dismissal is policy-grounded, not truth-grounded.

**What limitation of my recommended method am I understating?**
The SymPy closeout check uses H_3(ℝ) or similar small matrices. If the (A) argument subtly depends on real-vs-complex structure (e.g., the order-theoretic argument works for H_n(ℝ) but not H_n(ℂ)), SymPy on H_3(ℝ) won't catch it. H_n(ℂ) SymPy testing is heavier but prudent for a true belt-and-suspenders check. VALD-54-01 closeout should probably add an H_2(ℂ)-or-larger cross-check.

**Is there a simpler method I overlooked?**
Possibly: directly cite Jenčová-Pulmannová (2021) §3-4 as the OUS-level compression theory and adapt whatever machinery they use for their OUS-level spectrality results to Peirce invariance. The ADDENDUM explicitly says §3-4 has no Peirce — but absence of the claim doesn't mean absence of the tools. The planner could schedule a targeted read of §3-4 to see if their OUS spectrality machinery can be re-combined to yield Peirce invariance. Lower-priority than DERV-54-01 but worth considering as a parallel research thread.

**Would a physicist/mathematician specializing in this subfield disagree with my recommendation?**
A JB-algebra specialist would likely say "just use the Peirce machinery from HOS 1984 §2.6 — it's standard." They'd be wrong for Phase 54's purpose because HOS's Peirce is Jordan-level, but the instinct is strong and worth anticipating. The review-math adversarial prompt should preload this objection: "If the reviewer says 'this is standard Peirce theory,' the reviewer is treating it post-Jordan, which is exactly the gap."

A referee not versed in axiomatic reconstruction might say "why not just work in finite matrix algebras?" — this is the R1 circularity pitfall in plain language. The §3.3 revision text should briefly preempt: "The claim is made at the OUS level because at the matrix-algebra level it is trivially true, but Paper 5's derivation chain cannot assume matrix structure at this point without circularity."

## Metadata

**Confidence breakdown:**

- Mathematical framework (S1, S3, compressions, Peirce): HIGH — these are standard objects; only the precise Prop/Thm numbers in A-S need verification.
- Standard approaches (audit → A or C-i → C-ii fallback): HIGH — inherited from SUMMARY.md + CONTEXT.md consensus.
- Computational tools (SymPy, grep, gpd-review-math): HIGH — standard tooling, validated in v2.0 Phase 4.
- Validation strategies (forbidden-token grep, SymPy per-attempt + closeout, three early falsifier gates): HIGH — concrete, mechanical.
- Audit protocol (DERV-54-01): MEDIUM-HIGH — design is concrete (token grep + step-level classification table); verdict execution depends on reading density of `04-peirce-feedback-extension.md` which is dense but tractable.
- Outcome (A) feasibility: MEDIUM — depends on audit; two specific watchpoints (positivity-bound spin-factor proof; M_2(ℂ)^sa proof-device usage) are flagged.
- Outcome (C-i) defensibility: MEDIUM-HIGH — literature analogue (Niestegge, A-S compression base) exists; three canonical-example verifications are well-understood.
- Outcome (C-ii) feasibility: LOW — not explored in literature.

**Research date:** 2026-04-16
**Valid until:** Physics/algebra content is stable. The JMP referee timeline (R12) is the only time-sensitive element and is milestone-level, not Phase 54-local.
