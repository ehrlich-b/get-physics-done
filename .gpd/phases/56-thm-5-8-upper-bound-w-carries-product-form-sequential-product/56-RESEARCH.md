# Phase 56: Thm 5.8 Upper Bound — W Carries Product-Form Sequential Product — Research

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; peirce_2_space=V_2(p_i):=range(C_{p_i}); peirce_1_space=V_1(p_i,p_j):=(C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V; as_2001=Alfsen-Shultz 2001 vol 179 (Birkhäuser PM 179); as_2003=Alfsen-Shultz 2003 vol 190 (Birkhäuser PM 190; Ch. 1-8 pre-Jordan-legal; Ch. 9 post-Jordan-illegal per Phase 55 Flag 4.1); allowed_axiom_scope={S0, S1-S7, linearity, A-S compression axioms Ch. 2/7/8, finite-dim spectrality}; W=product-effect subspace spanned by {a_i ⊗ b_j} inside V_{BM}

**Researched:** 2026-04-17
**Domain:** Operational quantum theory / Order unit spaces / Sequential effect algebras / Euclidean Jordan algebras / Paper 5 §5 internal-exposition gap closure
**Confidence:** HIGH for literature anchors and "carries" disambiguation; MEDIUM-HIGH for face-status determination of W (the decisive unknown); MEDIUM for SymPy design (infrastructure exists from Phase 54); MEDIUM for downstream-consumer sense of "carries" (requires reading §5 Thm-local-tomo proof carefully).

---

## Summary

Phase 56 closes Paper 5's §5 Theorem **`thm:local-tomo`** (Local Tomography; referred to in the roadmap scope as "Thm 5.8") at the upper-bound step, lines 203-221 of `sections/composite-lt.tex` and lines 228-238 of `sections/appendix-proofs.tex`. The exact identity to defend is: *"Let W ⊆ V_{BM} be the d²-dimensional span of the product effects {a_i ⊗ b_j}. ... W, equipped with this induced order and the product-form sequential product, satisfies (C1)-(C4)"* and *"the product-form SP maps W into W since `a_i ⊗ b_j ∘ a_k ⊗ b_l = (a_i ∘ a_k) ⊗ (b_j ∘ b_l)` is again a product effect."* The word **"carries"** is overloaded (R7): it can mean (a) set-closure `a ∘ b ∈ W`, (b) induced-structure `(W, ∘|_W)` is itself an SPS, or (c) functorial preservation `W ↪ V_{BM}` is an SPS-morphism. Downstream use inside the minimality / upper-bound argument needs **sense (b)** at minimum: the minimality clause `sms:minimal` says V_{BM} is the *smallest OUS satisfying (C1)-(C4) and the product-form SP*, so to be a competitor, W must satisfy S1-S7 with its induced product, not merely be closed.

**Primary recommendation:** Follow **Method 5** from `.gpd/research/METHODS.md` (Phase 56 primary): (i) quote the current identity verbatim from `composite-lt.tex` (L204-221) + `appendix-proofs.tex` (L228-238); (ii) resolve whether W is a face of V_{BM} (the single decisive structural question — vdW 2019 Thm 1's face-restriction is NOT the workhorse here, because W is a *subspace spanned by product effects*, which is an algebraic, not an order-theoretic, construction — the face question may have answer NO); (iii) if W is NOT a face, shift to a direct S1-S7 verification on `W = V_B ⊗ V_M` viewed as a tensor-product SPS, invoking vdW 2019 Theorem 1 (not the face-restriction corollary) to conclude W is an EJA, and WWvdW 2020 only if normality is relevant (it probably is not, since V_B, V_M are finite-dim); (iv) disambiguate the three "carries" senses and prove sense (b) directly; (v) SymPy spot-check on H_3(ℝ) ⊗ H_3(ℝ) wedge component to falsify naive closure claims. The "carries" disambiguation is the R7 mitigation and is the highest-value deliverable for the referee.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| **vdW 2019 Theorem 1** (arXiv:1803.11139, JMP 60, 062201) | Method (primary) | "Finite-dimensional SPS is order-isomorphic to a Euclidean Jordan algebra." Applied to W with its induced product ⟹ W is an EJA ⟹ product-form closure follows. | Cite by theorem number; apply to W after S1-S7 verified on W. | Plan 56-XX proof of W's SPS-ness; RESULT.md. |
| **vdW 2019 Definition 2** (S1-S7 axioms, verbatim below) | Method (primary) | The exact axioms W must satisfy for vdW 2019 Thm 1 to apply. Each axiom must be checked on W with `∘|_W`. | Quote verbatim; use as checklist for the S1-S7 verification. | Plan 56-XX S1-S7-on-W proof table. |
| **WWvdW 2020** (arXiv:2004.12749, Quantum 4, 378) | Method (fallback) | Three-type normal SEA classification: normal SEA ≡ Boolean ⊕ convex ⊕ purely-almost-convex. Relevant only IF W fails to be convex-normal; probably not needed in finite-dim (all finite-dim SEAs are automatically normal). | Cite if a classification decomposition of W becomes necessary; otherwise flag as "not triggered." | Plan 56-XX fallback section; only if W has mixed type. |
| **Gudder-Greechie 2002** (RMP 49, 87, "Sequential products on effect algebras") | Counterexample / pitfall source | Example 39 (and analogous examples) exhibits a SEA with associative sequential product that is NOT order-isomorphic to an EJA. This is the canonical precedent for "closure without structural preservation" (R7 sense-(a) without sense-(b)). | Cite as the motivating counterexample for why sense (a) is insufficient; confirm W does NOT fall into this pathology. | Plan 56-XX R7 disambiguation section. |
| **Paper 5 §5 current text** (`~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` + `sections/composite-lt.tex` L204-221, `sections/appendix-proofs.tex` L228-238) | Prior artifact (living; must NOT edit main-jmp-submitted.tex) | The exact "carries" identity to defend. Living `main.tex` is the editable target; `main-jmp-submitted.tex` is FROZEN. | Quote verbatim with line numbers; diff living vs submitted if already edited. | Plan 56-01 (text-extraction task) and RESULT.md Section 2. |
| **Phase 54 RESULT.md (C-i)** | Prior artifact; hard constraint (R11) | Phase 54 closed at (C-i): Peirce-invariance of `L_a` now rests on new axiom S0. Any §5 Thm 5.8 proof that implicitly uses Peirce-invariance of the SP on V_B or V_M (factor-level) must cite the Peirce-Preservation Lemma, which rests on S0. **Forbidden:** using the submitted-era (A)-proof Peirce-invariance. | Cite `\ref{lem:peirce-preservation}` (which in turn depends on `\ref{ax:S0}`) wherever factor-level Peirce-invariance is used. | Plan 56-XX proof of factor-level SPS axioms; cross-phase coupling notes. |
| **Phase 55 RESULT.md (C-i)** | Prior artifact; post-Jordan constraint | §S4 facial-structure closed pre-Jordan. Post-Jordan (A-S 2003 Ch. 9) material remains FORBIDDEN per Phase 55 Flag 4.1. All A-S citations in Phase 56 must be `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` form, Ch. ≤ 8 OR A-S 2001. | Inherit bracketed citation discipline; forbid Thm 9.37 and all Ch. 9 material. | Plan 56-XX every A-S citation. |
| **`alfsen-shultz-notes.md`** (shared artifact, `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md`) | Shared living artifact | Shared A-S citation index (Props 7.23, 7.43, 7.49, 7.50, Def 7.1) already VERIFIED-VIA-INTERNAL-CROSS-REFERENCE. Phase 56 appends rows without re-verifying prior entries. | Append new rows for any Phase-56-specific A-S citation; cite existing verified rows by row number. | Plan 56-XX citations table. |
| **Phase 54 `closeout-sympy.py`** (`derivations/paper5-peirce-preservation/closeout-sympy.py`) | Prior computational artifact | Established the H_3(ℝ) / H_4(ℝ) compression/Peirce SymPy infrastructure (runtime 0.013s). Phase 56 reuses this framework for H_3(ℝ) ⊗ H_3(ℝ) composite checks. | Reuse `compress(B, i, n)` and `seq_prod(...)` helpers; extend to tensor composites. | Plan 56-XX SymPy test design. |
| **Phase 55 `55-01-CLASSIFICATION.md`** + `s4-sympy-spot-check.py` | Prior artifact | H_3(ℝ) rank-2 Case A and H_4(ℝ) Case B established; φ-independence under f=λ·μ alternative verified symbolically. | Reuse pattern (symbolic-exact, two mixing-function cases) for W-closure spot-check. | Plan 56-XX SymPy test. |

**Missing or weak anchors:**

- **Face status of W in V_{BM}.** Whether `W = span{a_i ⊗ b_j}` is a face of `V_{BM}` (in the A-S order-theoretic sense: order-convex, hereditary) is a non-trivial structural question. If W is NOT a face, vdW 2019 Thm 1's face-restriction is unavailable and the argument must bypass face structure entirely. Pre-research status: **UNKNOWN; decisive for (C) routing.** Plan must schedule an explicit face-check task as its first wave.
- **Downstream consumer of "carries" in §5.** The roadmap scope asserts "downstream use requires (b) or (c); establish that, not just (a)" but does not explicitly name the §5/§6 site that consumes the stronger sense. Before Plan 56-XX proves sense (b), a prerequisite is to locate the ≥1 consumers in `main.tex` / `composite-lt.tex` / `type-exclusion.tex` / `discussion.tex` and confirm which sense each needs. Pre-research status: **weak anchor — must be made explicit in Plan 56-01.**
- **Gudder-Greechie 2002 Example 39 exact statement.** Search results confirm the existence of non-EJA associative SEA examples but do not give the precise structural details of Example 39. Plan should either obtain the RMP paper via JSTOR/ScienceDirect or cite the result at a lower verification tier (AXIOM-STATED-IN-SECONDARY-SOURCE style) per the Phase 55 verification discipline.

---

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Sequential product notation | `a ∘ b` (Paper 5) / `a & b` (vdW) | identical operation; Paper 5 uses `∘` throughout | Paper 5 v14.0 convention; vdW 2019 Def. 2 |
| Compression | `C_p` (Paper 5, vdW, GPD v2.0) | `c_p` (A-S), `U_e` (Niestegge) | `alfsen-shultz-notes.md` Section 5 |
| Peirce spaces | `V_2(p_i) := range(C_{p_i})`; `V_1(p_i,p_j) := (C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V` | — | Phase 54 CUSTOM_CONVENTION, claim.md |
| Order unit space | Finite-dim archimedean OUS over ℝ with distinguished unit 1 | infinite-dim JB-algebras (vdW 2019 §VI; not used here) | vdW 2019 Def. 1 |
| Composite OUS notation | `V_{BM}` (Paper 5) | `V_B ⊗ V_M` when algebraic tensor product is meant; distinct per `rem:bootstrap` | Paper 5 Def. composite (composite-lt.tex L18-40) |
| Product-effect subspace | `W := span{a_i ⊗ b_j}` (d²-dimensional) inside V_{BM} | `span_ℝ(V_B ⊗_alg V_M)` (same object, different language) | composite-lt.tex L204 |
| A-S volume convention | A-S 2003 Ch. 1-8 pre-Jordan-legal; A-S 2003 Ch. 9 FORBIDDEN; A-S 2001 permitted | — | Phase 55 Flag 4.1 |
| Bracketed A-S citations | `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` | bare `\cite{AlfsenShultz2003}` FORBIDDEN | Phase 55 `55-03-ADVERSARIAL-REVIEW.md` R5 |
| Axiom scope | `{S0, S1-S7, linearity, A-S compression axioms Ch. 2/7/8, finite-dim spectrality}` | adding any Ch. 9 material ⟹ circularity | Phase 54 CUSTOM_CONVENTION |
| Self-modeling tracking map | `φ: V_B → V_M` order isomorphism | — | Paper 5 Def. `def:self-modeling-system` (iii) |

**CRITICAL: All equations and results below use these conventions. Converting results from other conventions (e.g., vdW `a & b` or A-S `c_p`) requires notational substitution only, not numerical rescaling.**

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `a ∘ b = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} √(λ_i λ_j) P_{ij}(b)` | Corrected product with mixing function `f(λ,μ)=√(λμ)` (factor-level SP) | main-jmp-submitted.tex L667-674 `eq:corrected-product` | The SP defined on each of V_B, V_M individually. |
| `(a ⊗ b) ∘_{W} (c ⊗ d) = (a ∘ c) ⊗ (b ∘ d)` | Product-form SP on product effects | composite-lt.tex L58-63 `eq:product-sp`, Def. `def:product-sp` | The identity whose closure in W is being defended; Phase 56 must prove S1-S7 for this on W. |
| `W := span_ℝ{a_i ⊗ b_j : a_i basis V_B, b_j basis V_M}` | Product-effect subspace of V_{BM} | composite-lt.tex L204; appendix-proofs.tex L229 | The subspace of V_{BM} whose structural status is the content of Phase 56. `dim W = d_B · d_M`. |
| `V_{BM} = V_B ⊗ V_M` (conclusion) | Tensor-product composite | composite-lt.tex L106, `rem:bootstrap` | The conclusion that depends on W-carries-SP being sense (b) rather than sense (a). |
| **vdW 2019 Def. 2 (S1-S7)** (quoted verbatim below) | Axioms for SPS | vdW 2019 arXiv:1803.11139 §II Def. 2 | Axiom-checklist for verifying W is a SPS with `∘|_W`. |
| **vdW 2019 Theorem 1:** "Let V be a finite-dimensional sequential product space. Then V is order-isomorphic to a Euclidean Jordan algebra." | Main result | vdW 2019 Thm in §I (unnumbered in intro; proven as Thm 1 in §III.4) | Applied to W to conclude W is an EJA, IF S1-S7 verified on W. |
| **Peirce-Preservation Lemma** (Phase 54 RESULT §2) | Factor-level Peirce-invariance of `L_a` | Phase 54 RESULT.md §2; `\ref{lem:peirce-preservation}` in main.tex | Used to justify factor-level S1/S5/S6/S7 inheritance; must cite LEMMA NAME (not the submitted (A)-proof). |

### vdW 2019 Definition 2 — S1-S7 axioms (verbatim from arXiv:1803.11139 p. 3)

Let `(V, ≤, 1, &)` be an order unit space equipped with a binary operation `& : [0,1]_V × [0,1]_V → [0,1]_V`. Write `a | b` and say a, b are *compatible* when `a & b = b & a`. V is a *sequential product space* and `&` a *sequential product* when `&` satisfies, for all `a, b, c ∈ [0,1]_V`:

- **(S1) Additivity:** `a & (b + c) = a & b + a & c.`
- **(S2) Continuity:** The map `a ↦ a & b` is continuous in the norm.
- **(S3) Unitality:** `1 & a = a.`
- **(S4) Compatibility of orthogonal effects:** If `a & b = 0` then also `b & a = 0.`
- **(S5) Associativity of compatible effects:** If `a | b` then `a & (b & c) = (a & b) & c.`
- **(S6) Additivity of compatible effects:** If `a | b` then `a | (1 − b)`, and if also `a | c` then `a | (b + c).`
- **(S7) Multiplicativity of compatible effects:** If `a | b` and `a | c` then `a | (b & c).`

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| S1-S7 axiom-checklist on W | Direct verification each axiom holds with `∘|_W` | Plan 56-XX primary proof task | vdW 2019 Def. 2 |
| Tensor product SPS construction | Given (V_B, ∘_B) and (V_M, ∘_M), equip V_B ⊗_alg V_M with `(a⊗b) ∘ (c⊗d) := (a∘c)⊗(b∘d)` and extend bilinearly | Plan 56-XX: the object on which S1-S7 are verified | vdW 2019 Def. 4 (locally tomographic composite); Paper 5 `def:product-sp` |
| Order-extension of cone | Show W ∩ V_{BM}^+ generates W as a cone (induced cone is proper) | Plan 56-XX (C1) check | A-S 2003 Ch. 1 (basic OUS definitions); `alfsen-shultz-notes.md` row for A-S 2003 Prop 1.5 (to be added) |
| Face characterization via projective units | In an EJA, every face corresponds to a unique projective unit (Peirce 2-space of a projection) | Plan 56-XX face-check task (decisive) | A-S 2003 Ch. 7 (Peirce decomposition in the OUS/compression framework); `alfsen-shultz-notes.md` Row 7.50 |
| Three-"carries"-senses matrix | Distinguish closure / induced-structure / functorial preservation | Plan 56-XX R7 disambiguation | Barnum-Graydon-Wilce 2020 §2-3 (composite morphisms); vdW 2019 §V (locally tomographic composite) |
| SymPy symbolic exact tensor SP | Verify `(a⊗b) ∘ (c⊗d) ∈ W` on H_3(ℝ) ⊗ H_3(ℝ) (9x9 = 81-dim ambient, W is dim 9 if spin factor or 36 if full H_3 ⊗ H_3) | Plan 56-XX computational spot-check | Phase 54 `closeout-sympy.py` (compression infrastructure); SymPy `Matrix` `.tensor_product()` |

### "Three Senses of Carries" — Formal Definitions

Let V be an OUS with sequential product `∘ : [0,1]_V × [0,1]_V → [0,1]_V` satisfying S1-S7, and let W ⊆ V be a subspace.

- **Sense (a) — set-level closure:** For all `a, b ∈ [0,1]_W := [0,1]_V ∩ W`, `a ∘ b ∈ W`.
  - *Formally:* `∘([0,1]_W × [0,1]_W) ⊆ W.`
  - *Status:* Weakest. Gudder-Greechie 2002 Example 39 shows this is compatible with W failing to be EJA-like. Closure alone is **not enough** for the minimality clause of Paper 5.

- **Sense (b) — induced-structure SPS:** W with the induced order unit `1_W` (if W contains 1_V, else 1_W needs justification), induced cone `W^+ := W ∩ V^+`, and restricted product `∘|_W := ∘|_{[0,1]_W × [0,1]_W}` is itself an order unit space satisfying S1-S7.
  - *Formally:* `(W, ≤|_W, 1_W, ∘|_W)` is an SPS in the vdW 2019 Def. 2 sense.
  - *Status:* The sense needed by the `sms:minimal` clause. The minimality clause says V_{BM} is the SMALLEST OUS satisfying (C1)-(C4) + product-form SP; for W to be a competitor one must have W satisfy the same structure, i.e., sense (b).

- **Sense (c) — functorial preservation (SPS-morphism):** The inclusion map `ι : W ↪ V` is a morphism of sequential product spaces: `ι` is unital positive linear AND `ι(a ∘|_W b) = ι(a) ∘_V ι(b)` for all `a, b ∈ [0,1]_W`. The latter is automatic if `∘|_W` is defined by restriction (set-theoretically identical), but the morphism-ness requires that `ι` preserves the order unit AND the positive cone.
  - *Formally:* ι : (W, ≤|_W, 1_W, ∘|_W) → (V, ≤, 1, ∘) is an SPS-morphism in the sense of Barnum-Graydon-Wilce 2020 §2 (completely Jordan-preserving maps).
  - *Status:* Strongest. Required if one wants to speak of W as a sub-SPS functorially. Not strictly required for the minimality argument, but cleaner for the EJA classification downstream.

**Collapse diagram:**
- (a) ⇐ (b): automatic (SPS requires closure).
- (b) ⇐ (c): automatic (morphism of SPS's implies domain is SPS).
- (a) ⇏ (b) in general: **Gudder-Greechie 2002 Example 39 witness**.
- (b) ⇏ (c) in general: the induced order unit on W might differ from `1_V|_W` (e.g., if W ∌ 1_V, one needs to choose a new order unit).

### Approximation Schemes

Phase 56 is analytical/structural — no approximation scheme. The SymPy spot-check is symbolic-exact (rational-arithmetic), not numerical.

---

## Standard Approaches

### Approach 1: Direct S1-S7 verification on W with `∘|_W`, then vdW 2019 Thm 1 (RECOMMENDED — Method 5 from METHODS.md)

**What:** Verify each of S1-S7 directly on `(W, ≤|_W, 1_V, ∘|_W)`, exploiting the product-effect structure. Once all seven axioms hold, invoke vdW 2019 Theorem 1 to conclude W is order-isomorphic to an EJA — which gives sense (b) of "carries" as a theorem, not an assumption.

**Why standard:** This is the route taken by all Paper 5 §6 type-exclusion arguments (see `sections/type-exclusion.tex` L216, L245 referencing `V_{BM}` with product-form SP inheriting S1-S7) and is consistent with METHODS.md Method 5 Phase 56 designation.

**Track record:** vdW 2019 Theorem 1 is peer-reviewed (JMP 60, 062201); its hypothesis (finite-dim SPS) is exactly what S1-S7 give. Barnum-Graydon-Wilce 2020 used the same pattern to establish composites of EJAs are EJAs under analogous constraints.

**Key steps (for plan construction):**

1. **Quote the identity** — Paper 5 Thm-local-tomo §upper-bound text verbatim from composite-lt.tex L204-221 and appendix-proofs.tex L228-238, with line numbers. Flag any ambiguity in "carries" / "inherits" / "is closed under."

2. **Resolve W's face status in V_{BM}.** Two sub-cases:
   - (a) **W is a face of V_{BM}:** Then W inherits OUS structure automatically (A-S 2003 Ch. 1 facial-OUS theory; Ch. 7 compression-to-face correspondence). Proceed to Step 3 cleanly.
   - (b) **W is NOT a face of V_{BM}** (likely; see `Open Question 1` below): Then sense (b) cannot be obtained by face-restriction. Must construct `(W, ≤|_W, 1_V, ∘|_W)` as an SPS in its own right, checking (i) `1_V = 1_B ⊗ 1_M ∈ W` (true), (ii) induced cone `W^+ := W ∩ V_{BM}^+` is proper, (iii) `[0,1]_W := [0,1]_V ∩ W` is well-defined, (iv) restricted product takes `[0,1]_W × [0,1]_W → [0,1]_W`. Only (ii) and (iv) are non-trivial.

3. **Verify S1-S7 on W with `∘|_W`:**
   - **S1 (additivity):** `(a⊗b) ∘_W ((c⊗d) + (c'⊗d')) = (a⊗b)∘_W(c⊗d) + (a⊗b)∘_W(c'⊗d')` by bilinearity of tensor product + S1 factor-wise. NOTE: (c⊗d) + (c'⊗d') is in general NOT a product effect; must prove additivity using the product-state evaluation and state-separation (A-S 2003 Thm 1.23).
   - **S2 (continuity):** Inherits from factor-level continuity (vdW 2019 S2 on V_B, V_M) + continuity of tensor product.
   - **S3 (unitality):** `1_V ∘_W (a⊗b) = (1_B ⊗ 1_M) ∘_W (a⊗b) = (1_B ∘ a) ⊗ (1_M ∘ b) = a ⊗ b.` Direct.
   - **S4 (orthogonality symmetry):** The subtle axiom. Paper 5 `prop:inheritance` proof at composite-lt.tex L81-90 already treats this via state separation (A-S 2003 Thm 1.23). Plan 56 can cite this proof; it is NOT a new derivation needed. **R11 check:** this proof does NOT use factor-level Peirce-invariance, so Phase 54 (C-i) S0 dependency does not propagate to S4-on-W. ✓
   - **S5 (compatible associativity):** Reduces to factor-level associativity since compatibility of `a⊗b` and `c⊗d` in W is equivalent to factor-wise compatibility `a|c` and `b|d` (proved in composite-lt.tex L77-79). **R11 check:** factor-level S5 was verified in submitted Paper 5 §4; Phase 54 (C-i) changed the PROOF of Peirce-invariance, not the VALIDITY of S5 on V_B/V_M. Cite Peirce-Preservation Lemma by name for the Peirce-invariance step if explicitly used.
   - **S6 (additivity of compatible):** Same pattern as S5. Reduces to factor-level.
   - **S7 (multiplicativity of compatible):** Same pattern.

4. **Invoke vdW 2019 Theorem 1.** W is a finite-dim SPS (Step 3) ⟹ W is order-isomorphic to a EJA. ✓

5. **Sense-(b) conclusion.** W with `∘|_W` is an SPS (Step 3 output). Record this as the exact sense of "carries" established.

6. **Sense-(c) upgrade (optional, cleaner):** Show `ι : W ↪ V_{BM}` is an SPS-morphism. Since `∘|_W` is literally the restriction of `∘_{V_{BM}}` (not a new operation), the functorial identity `ι(a ∘_W b) = ι(a) ∘_{V_{BM}} ι(b)` is trivially satisfied. The non-trivial content is unitality (1_W = 1_V) and positivity (ι carries W^+ into V_{BM}^+). Both hold.

**Known difficulties at each step:**

- **Step 1:** Frozen-file discipline — `main-jmp-submitted.tex` must not be touched. All edits go to living `main.tex`. Risk of accidentally `git blame`-ing the frozen file.
- **Step 2a (face check):** No standard theorem says "span of product effects is a face of the composite OUS." The face check must be done explicitly using the A-S definition (order-convex, hereditary under ≤). **This is the decisive step; failure here routes to Step 2b.**
- **Step 2b (non-face route):** Proving W^+ is proper requires showing `(W^+) − (W^+) = W` (cone generates subspace) and `W^+ ∩ (−W^+) = {0}` (cone is pointed). Both follow from W being spanned by product effects (each a_i ⊗ b_j is positive), but need explicit checks.
- **Step 3, S1:** Non-product elements `(c⊗d) + (c'⊗d')` are not in general of form `x⊗y`. The product-form `∘|_W` was defined ON product effects and extended bilinearly; the identity `(a⊗b) ∘_W x = (a⊗b) ∘_{V_{BM}} x` for general `x ∈ W` requires proving bilinear extension is well-defined, which is where state separation enters.
- **Step 3, S4:** Although `prop:inheritance` proof handles S4 via state separation, that proof uses A-S 2003 Thm 1.23 (pre-Jordan-legal, Ch. 1). Phase 55 Flag 4.1 compliance: ✓ (Ch. 1 is allowed).
- **Step 4:** vdW 2019 Thm 1 requires FINITE-DIMENSIONAL SPS. W is finite-dim (dim = d_B · d_M ≤ (dim V_{BM})), so ✓.

### Approach 2: Route via face-restriction of V_{BM} (FALLBACK — only if W turns out to be a face)

**What:** If Step 2a above succeeds — W is a face of V_{BM} — then W inherits SPS structure automatically by a face-restriction corollary of vdW 2019 Thm 1 combined with the A-S 2003 Ch. 7 face ↔ projective-unit correspondence.

**When to switch:** Only if the explicit face check in Step 2a passes. Do not assume face status; prove it.

**Tradeoffs:** Cleaner proof (no direct S1-S7 verification needed on W), but at the cost of depending on a face theorem that may not apply. Gain ~2 pages of proof text, but risk a referee asking "why is W a face?" which is not obvious.

### Approach 3: Gudder-Greechie 2002 "closure without structural preservation" precedent (PRECEDENT / CAUTIONARY)

**What:** If Phase 56 finds that W satisfies sense (a) only (closure) but not sense (b), use Gudder-Greechie 2002 Example 39 as explicit precedent that the downstream argument must be revised to require only sense (a).

**When to switch:** Only if Approaches 1 and 2 both fail AND reading §5/§6 reveals that the downstream use actually needs only sense (a). This would be a Phase 56 outcome (C): structural revision required.

**Tradeoffs:** Thm-local-tomo becomes weaker (only shows `dim V_{BM} ≤ d_B · d_M` *assuming* W is a valid competitor, which requires minimality to be defined in sense (a)). May cascade into Paper 5 §5/§6 rewrites.

### Anti-Patterns to Avoid

- **Claiming W is a face "because it's spanned by product effects."** Span of positive elements is not automatically a face. Face = hereditary AND order-convex.
  - *Example:* In M_2(ℂ)^{sa}, the diagonal subspace is spanned by {diag(1,0), diag(0,1)} (positive), but the diagonal is a face (in fact a 0-dim face of the state space, or 2-dim algebraic subspace). However, in V ⊗ V, a subspace spanned by {a_i ⊗ b_j} where `{a_i}` and `{b_j}` are generic bases (not necessarily positive-semidefinite sums) may fail hereditary.

- **Collapsing the three "carries" senses.** Writing "W carries the product-form SP" without specifying sense is exactly R7 equivocation. Every plan task involving this language must cite which sense is meant.

- **Using `main-jmp-submitted.tex` as the integration target.** Frozen-file discipline. Always living `main.tex`.

- **Using Phase 54 submitted-era (A)-proof Peirce-invariance.** Under Phase 54 (C-i), factor-level Peirce-invariance is justified by the Peirce-Preservation Lemma (which depends on S0). Any §5 proof that appeals to "the obvious Peirce-invariance of `a ∘ (·)`" without citing `\ref{lem:peirce-preservation}` is a R1 circularity (same token discipline as Phase 54).

- **Citing A-S 2003 Ch. 9.** FORBIDDEN per Phase 55 Flag 4.1 (Thm 9.37 is post-Jordan).

- **Citing WWvdW 2020 for W when decomposition is not established.** WWvdW 2020's classification applies to NORMAL SEAs (σ-complete with suprema). Finite-dim OUSs are automatically normal in the relevant sense, but invoking the three-type classification for W without first establishing what "type" W is (Boolean, convex, purely-almost-convex) would be a lazy citation.

- **Omitting the sense (c) upgrade.** If sense (c) is easily obtainable (which it is, since `∘|_W` is literally a restriction), providing it is a cheap add-on that makes the theorem's quotability in downstream Paper 5 sections stronger.

---

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| vdW 2019 Theorem 1 | "Let V be a finite-dimensional sequential product space. Then V is order-isomorphic to a Euclidean Jordan algebra." | arXiv:1803.11139 §III.4 | CITE and apply to W after S1-S7 verified on W. |
| vdW 2019 Def. 2 S1-S7 | (verbatim above) | arXiv:1803.11139 §II p. 3 | The checklist for the S1-S7 verification task. Do NOT restate in proof body; cite. |
| **Peirce-Preservation Lemma** (Phase 54) | (verbatim Phase 54 RESULT.md §2) | Phase 54 RESULT.md, `\ref{lem:peirce-preservation}` in main.tex | Cite by label for any factor-level Peirce-invariance invocation. |
| Paper 5 `prop:inheritance` proof of S4-on-W via state separation | (composite-lt.tex L81-90, quoted) | composite-lt.tex L66-90 | Reuse verbatim for S4 on W; do not re-derive. |
| A-S 2003 Thm 1.23 (states separate effects in OUS) | A-S 2003 Ch. 1 | `alfsen-shultz-notes.md` (to be added) | Used inside `prop:inheritance` S4 proof; pre-Jordan-legal. |
| Corrected factor-level SP `a∘b = Σ λ_i C_{p_i}(b) + Σ √(λ_iλ_j) P_{ij}(b)` | main.tex `eq:corrected-product` L667-674 | Paper 5 submitted (Section 3) | Defines `∘_B` and `∘_M`. Used inside product-form SP `(a⊗b)∘(c⊗d) = (a∘c)⊗(b∘d)`. |
| vdW 2019 Def. 4 (locally tomographic composite) | "V and W have locally tomographic composite when V⊗W is SPS with `(a⊗b) & (c⊗d) = (a&c)⊗(b&d)`" | arXiv:1803.11139 §I p. 3-4 | Template for Paper 5 product-form SP; the tensor-SPS structure is literally this definition. |
| A-S 2003 Prop 7.50 | Compression-meet: for compatible projective units `p, q`: `C_p C_q = C_{p∧q}` | `alfsen-shultz-notes.md` Section 6 (VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Backing for S0 / factor-level compression algebra. NOT used directly for Phase 56 unless W's face structure reduces to this. |

**Key insight:** Re-deriving vdW 2019 Thm 1's proof (spectral theorem → homogeneity → self-duality → Koecher-Vinberg) in Paper 5 would be ~30 pages. Cite it. Paper 5 already does via `\ref{thm:vdw1}` at main-jmp-submitted.tex L301-304.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| Tensor product of order unit spaces is an OUS | `(V_B ⊗ V_M, V_B^+ ⊗_π V_M^+, 1_B ⊗ 1_M)` with projective tensor cone | Plavala 2023 (cited in composite-lt.tex L15); Barnum 2023 | Used as the scaffold for the product-form SP; need the positive cone to be well-defined. |
| Bilinearity of tensor product over ℝ | `(a + a') ⊗ b = a⊗b + a'⊗b` and `a ⊗ (b + b') = a⊗b + a⊗b'` | Standard linear algebra | Used in S1-on-W verification; the bilinear extension is how `∘|_W` is extended from product effects to general elements of W. |
| State separation in finite-dim OUS | `∀ω ∈ States(V): ω(v) = 0 ⟹ v = 0` | A-S 2003 Thm 1.23 | Used in S1 and S4 on W proofs; pre-Jordan-legal. |
| Finite-dim tensor product: `dim(V_B ⊗ V_M) = dim V_B · dim V_M` | Dimension formula | Standard linear algebra | Motivates W being `d²`-dim. |
| `1_B ⊗ 1_M ∈ span{a_i ⊗ b_j}` when `1_B ∈ span{a_i}` and `1_M ∈ span{b_j}` | Ensures W contains the order unit | composite-lt.tex L207-208 | Trivial but essential; confirmed by `{a_i}` being a basis. |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| "Sequential product spaces are Jordan algebras" | van de Wetering | 2019 | **Method 5 primary anchor** | Theorem 1 + Def. 2 (S1-S7) + Def. 4 (locally tomographic composite). |
| "Three characterisations of the sequential product" | van de Wetering | 2018 | Method anchor for the explicit Lüders form on EJAs | Thm 2: on a JB-algebra, the standard SP is `a&b = √a · b · √a` (Jordan form). Supporting for sense (b). |
| "The three types of normal sequential effect algebras" | Westerbaan, Westerbaan, van de Wetering | 2020 | **Fallback classification** | Classification: normal SEA ≡ Boolean ⊕ convex ⊕ purely-almost-convex. Cite only if W fails to be uniformly convex. |
| "Sequential products on effect algebras" | Gudder, Greechie | 2002 | **R7 precedent** | Example 39 (and analogues): associative SEA that is NOT order-isomorphic to EJA. Cite as "closure without structural preservation" witness. |
| "Composites and Categories of Euclidean Jordan Algebras" | Barnum, Graydon, Wilce | 2020 | **Sense (c) / morphism machinery** | Definition of completely Jordan-preserving maps; category of embedded EJAs. Supporting for sense-(c) upgrade. Also: "no composite of simple non-exceptional EJAs has the exceptional EJA as summand" — cross-check for §6 type-exclusion. |
| "Local Tomography and the Jordan Structure of Quantum Theory" | Barnum, Wilce | 2014 | Local tomography + qubit subsystem classification | Background for §5/§6 local-tomography argument; referenced for the `thm:local-tomo` theorem motif. |
| Paper 5 §5 Thm `thm:local-tomo` + §Appendix `thm:lt-full` | (Paper 5 authors) | 2026 submission | **The theorem being defended** | Exact proof text at composite-lt.tex L162-222 + appendix-proofs.tex L164-243. |
| Paper 5 §5 `prop:inheritance` | (Paper 5 authors) | 2026 submission | **S1-S7 on W — factor-level reduction** | Proof at composite-lt.tex L66-90. Phase 56 REUSES this proof for S4 on W. |
| Alfsen-Shultz 2003 Ch. 1-8 (pre-Jordan-legal) | Alfsen, Shultz | 2003 | Face theory / compression theory | Thm 1.23 (state separation), Ch. 7 (compressions), Prop 7.50 (compression meet). All pre-Jordan-legal. |
| Faraut-Korányi 1994 Ch. III | Faraut, Korányi | 1994 | **EJA trace form** | Prop III.4.2 (trace form non-degeneracy on simple EJA). Used in appendix-proofs.tex L195; verify usage is post-Jordan (it IS — invoked AFTER vdW 2019 Thm 1 gives EJA structure). |
| Plavala 2023 "General probabilistic theories: An introduction" | Plavala | 2023 | **GPT tensor product** | Cited at composite-lt.tex L16 as background for (C1)-(C4) axioms. Confirms tensor product composite is a standard GPT construction. |

---

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | `sympy` ≥ 1.12 (existing venv `/Users/ehrlich/scratch/get-physics-done/.venv` or blog-repo equivalent) | Symbolic-exact verification of tensor-SP closure on W; reuse `compress(B,i,n)` and `seq_prod(...)` from Phase 54 closeout-sympy.py | Same tool used in Phase 54 closeout and Phase 55 s4-sympy-spot-check; zero-cost extension. |
| Python 3.11+ | stdlib | Runner | Native on system. |
| `unittest` or `pytest` | stdlib / pytest | Test harness (optional; can use exit code 0/1 + assertion pattern from Phase 54 `closeout-sympy.py`) | Matches existing Phase 54/55 SymPy pattern. |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| `grep` / `ripgrep` | Locate Thm 5.8 identity in living `main.tex`, check `main-jmp-submitted.tex` for frozen-diff discipline | Plan 56-01 text-extraction task. |
| `git` (blog repo) | Diff living `main.tex` against `main-jmp-submitted.tex` to see what Phase 55 / Phase 54 already changed; verify `main-jmp-submitted.tex` has zero diff | Plan 56-XX pre-integration check. |
| `pdflatex` (user-side) | Full compile verification of revised `main.tex` | Plan 56-XX final integration (user-gated, as in Phase 55). |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| SymPy (symbolic-exact) | NumPy (floating-point numerical) | SymPy gives exact answers for rational-coefficient matrices, catches algebraic identity violations; NumPy faster but subject to floating-point noise. Phase 54/55 pattern is symbolic-exact; maintain consistency. |
| Python | Mathematica / Maple | SymPy is open-source and matches the existing GPD SymPy infrastructure. No reason to switch. |
| Direct S1-S7 verification (Approach 1) | Full Koecher-Vinberg re-derivation | KV proof is ~20 pages; cite vdW 2019 Thm 1 instead. |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| H_3(ℝ) ⊗ H_3(ℝ) tensor SP closure check | <5 sec (Phase 54 closeout runtime 0.013s for H_3/H_4 scalar; tensor case ~10-100x) | Symbolic simplification of 6×6=36 entries of tensor product | Use representative samples (not exhaustive basis enumeration); test with specific spectral decompositions, as in Phase 54. |
| "Wedge component" of H_3(ℝ) ⊗ H_3(ℝ) (antisymmetric subspace) | <5 sec | Identifying the 3-dim wedge; this is the `Λ^2(ℝ^3) ≅ ℝ^3` subspace | If "wedge component" is interpreted literally as antisymmetric traceless matrices of H_3(ℝ) — note H_3(ℝ) consists of SYMMETRIC matrices, so the antisymmetric "wedge" is dimension 0 INSIDE H_3(ℝ). Must clarify in plan scope. See Open Question 2. |

**Installation / Setup:**

```bash
# SymPy is already in the project venv from Phase 54/55 work.
# Verify it is available:
python3 -c "import sympy; print(sympy.__version__)"
# Expected: sympy >= 1.12
# If not:
pip install sympy  # or: uv add sympy
```

---

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| (a) Closure `(a⊗b)∘(c⊗d) ∈ W` on H_3(ℝ) ⊗ H_3(ℝ) with random rational coefficients | Sense-(a) of "carries" | SymPy: compute `(a∘c)⊗(b∘d)` using factor-level corrected product; verify it equals the product-form SP's output and lies in `span{e_i ⊗ e_j}` for standard basis | Entries are rational; match to symbolic precision. |
| (b) S1 (additivity) on W: `(a⊗b) ∘ [(c⊗d) + (c'⊗d')] = (a⊗b)∘(c⊗d) + (a⊗b)∘(c'⊗d')` | Sense-(b) axiom S1 on W | SymPy with mixed product-effect + sum | Symbolic equality. |
| (c) S3 (unitality) on W: `(1_B ⊗ 1_M) ∘ (a⊗b) = a⊗b` | Sense-(b) axiom S3 on W | SymPy with `a ⊗ b` for generic `a ∈ [0,1]_{H_3(ℝ)}`, `b ∈ [0,1]_{H_3(ℝ)}` | Equality. |
| (d) S5 (associativity for compatible) on W | Sense-(b) axiom S5 on W; Phase 54 (C-i) coupling | SymPy: take `a, b` compatible at factor level (shared spectral decomposition); compute LHS = `(a⊗b) ∘ [(b⊗a) ∘ (c⊗d)]` and RHS = `[(a⊗b)∘(b⊗a)] ∘ (c⊗d)` | Symbolic equality, leveraging factor-level S5. |
| (e) vdW 2019 Thm 1 applicability: W is finite-dim SPS | Sense (b) established ⟹ EJA | After (b)-(d) pass, cite theorem; conceptual not computational | Theorem conclusion: W order-isomorphic to EJA. |
| (f) **Face-status falsifier** for W in V_{BM} | Whether W is a face | Construct `v ∈ V_{BM}^+` and `0 ≤ w ≤ v` with `v ∈ W` but `w ∉ W`; if successful, W is NOT a face | Depending on W's actual face status. (The fact that `V_B ⊗ V_M` equals `V_{BM}` by sms:minimal complicates this; see Open Question 1.) |
| (g) Forbidden-token grep (R1 / R5 discipline) | No circularity in proof | `grep -n "Thm 9.37\|AlfsenShultz.*Ch.~9\|Luders\|M_n(C)^{sa}" 56-proof.tex` | Zero hits outside explicit scope-demarcated example-defense blocks. |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| `W = V_{BM}` (degenerate limit) | `sms:minimal` with `dim V_{BM} = d²` exactly | Three senses (a)=(b)=(c) collapse; Thm 5.8 trivially true | Paper 5 `rem:bootstrap` L92-107 |
| `W = {0, 1}` (trivial face) | Spin-factor-of-1 scenario, not physical | SPS axioms trivial on 2-element set | N/A (not invoked by Paper 5) |
| `V_B = V_M = M_n(ℂ)^{sa}` (complex case) | Standard complex QM | `V_{BM} = M_{nm}(ℂ)^{sa}` with Lüders form; local tomography holds; all three senses of "carries" established | composite-lt.tex L234-237; Barnum 2023 |
| `V_B = V_M = M_2(ℝ)^{sa}` (real QM case) | `d = 3, d² = 9` | Local tomography FAILS; `dim V_{BM} = 10 > 9`; `W` is proper 9-dim subspace with product-SP closure — sense (a) holds, sense (b) holds, but Thm-local-tomo's dimension equality FAILS | composite-lt.tex L254 (Table in `rem:negative-checks`) |
| `V_B = V_M = M_2(ℍ)^{sa}` (quaternionic) | `d = 6, d² = 36` | `dim V_{BM} = 28 < 36`; product effects are LINEARLY DEPENDENT in V_{BM} ⟹ sense (a) actually FAILS (dim W < d², so state-separation lower bound fails) | composite-lt.tex L256 |
| `V_B = V_M = M_2(ℂ)^{sa}` (qubit × qubit) | `d = 4, d² = 16` | `dim V_{BM} = 16 = d²`; W = V_{BM} (the degenerate case); three senses collapse | composite-lt.tex L255 |

**The real-case and quaternion-case limits are the critical validation:** they show that the sense-(b) question is non-vacuous — for real QM, W is a proper sub-SPS of V_{BM} with DIFFERENT state space (dim 9 vs dim 10), and the §6 type-exclusion argument uses this discrepancy.

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| Symbolic closure `(a⊗b)∘(c⊗d) = (a∘c)⊗(b∘d) ∈ W` | SymPy `sp.simplify` on entry-by-entry difference | Exact symbolic equality (zero remainder) | Entries of `W` in product-effect basis. |
| S1-S7 axiom checks on W | Symbolic equality of LHS/RHS expression trees | Exact | Vanishing difference. |
| Face-check (if performed symbolically) | Construction of `w ∈ V_{BM}^+ \ W` with `w ≤ v ∈ W^+` | Exact existence | If constructed: W is NOT a face. If no such w constructible: indicates W may be a face (not a proof). |

### Red Flags During Computation

- **Non-zero residual after `sp.simplify` for S1-S7 identity:** The product-form SP is not satisfying the axiom on W. Diagnose: is it factor-level error (check Phase 54 closeout still passes), or tensor-level error (misdefined `∘|_W`)?
- **`dim V_{BM}` != d² in test models where it should be:** Probably `sms:minimal` clause is mis-applied. Re-check Plan 56 definitions.
- **"Wedge component" interpretation yields dim 0 subspace of H_3(ℝ):** H_3(ℝ) is 6-dimensional (symmetric real matrices), not Clifford. The "antisymmetric wedge" inside H_3(ℝ) is {0}. If the roadmap intended "the Peirce 1-space components inside H_3(ℝ)" (which IS 3-dim), clarify in Plan. **See Open Question 2.**
- **Gudder-Greechie Ex 39 analogue appearing in W:** If the SymPy test shows W is closed under ∘ but FAILS S5 (associativity), W is a sense-(a)-only SEA à la Gudder-Greechie Ex 39. Route to Approach 3.
- **S4-on-W proof trying to use Jordan multiplication:** R1 circularity. Must use state separation (A-S 2003 Thm 1.23) only.

---

## Common Pitfalls

### Pitfall 1: R7 "Carries" Equivocation (CENTRAL)

**What goes wrong:** Writing "W carries the product-form SP" without specifying which of the three senses is intended. The proof may establish sense (a) while the downstream use requires sense (b) or (c).

**Why it happens:** Natural-language "carries" reads as sense (c) to a permissive reader but is formally sense (a) in the span-of-product-effects construction. Gudder-Greechie 2002 Example 39 is the canonical witness that (a) ⇏ (b).

**How to avoid:** Plan 56-XX must produce an explicit three-column table in RESULT.md distinguishing the three senses for EVERY use of "carries" in the Phase 56 revision text. For each downstream Paper 5 consumer, state which sense is needed and verify the proof establishes at least that sense.

**Warning signs:** The proof text uses "carries", "inherits", "respects" without qualification. Any such token in Plan 56-XX output file is a flag.

**Recovery:** If sense (b) or (c) cannot be established, route to Approach 3 (Gudder-Greechie precedent) and consider Phase 56 outcome (C): structural revision required.

### Pitfall 2: Face-Status Blind Spot (DECISIVE)

**What goes wrong:** Assuming W is a face of V_{BM} without verifying, and invoking vdW 2019 Thm 1's face-restriction implicitly.

**Why it happens:** In textbook EJA theory (post-Jordan), every face of an EJA corresponds to a projective unit (Peirce 2-space). The instinct is to map this back to W. But W is constructed algebraically (span of product effects), not order-theoretically (hereditary convex subset of positive cone), and these are different.

**How to avoid:** Plan 56-01 must include an explicit "resolve W's face status" task as Wave 1, with a DEFAULT outcome of "NOT A FACE" and a burden-of-proof on showing it IS a face. Proceed with Approach 1 (direct S1-S7) regardless of face status; only add Approach 2 shortcut if face status proven.

**Warning signs:** Plan text says "W is a face" or "W inherits from V_{BM}" without citation.

**Recovery:** Discard face-based shortcut; use Approach 1's direct S1-S7 verification.

### Pitfall 3: R11 Cross-Phase Cascade from Phase 54 (C-i)

**What goes wrong:** Phase 56 proof of S5/S6/S7 on W reduces to factor-level S5/S6/S7, which require factor-level Peirce-invariance, which is Phase 54's Peirce-Preservation Lemma. Under Phase 54 (C-i), this lemma depends on axiom S0. Any §5 proof that cites "the obvious Peirce-invariance" rather than `\ref{lem:peirce-preservation}` silently bypasses S0.

**How to avoid:** Every citation of factor-level Peirce-invariance in Phase 56 proof text uses `\Cref{lem:peirce-preservation}` and `\ref{ax:S0}` explicitly.

**Warning signs:** Grep for "Peirce" in Phase 56 proof text. Any occurrence without accompanying `\ref{lem:peirce-preservation}` or `\ref{ax:S0}` is a candidate for R11 violation.

**Recovery:** Add the citation. S0 is now a paper-level axiom (Phase 54 close); using it is the correct discipline.

### Pitfall 4: Frozen-File Violation

**What goes wrong:** Editing `main-jmp-submitted.tex` (frozen at git tag `paper5-jmp-submitted`) when all revisions should target living `main.tex`.

**How to avoid:** Every file-editing task in Plan 56-XX targets `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` or `~/repos/blog/landing/papers/qm-from-self-modeling/sections/*.tex` (living). No task may modify `main-jmp-submitted.tex`. Verification: `git -C ~/repos/blog diff --stat HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` must return zero changes throughout Phase 56.

**Recovery:** Revert `main-jmp-submitted.tex` via `git -C ~/repos/blog checkout HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex`.

### Pitfall 5: A-S Ch. 9 Citation (Post-Jordan-Illegal)

**What goes wrong:** Citing A-S 2003 Thm 9.37 or any other Ch. 9 material, which is POST-Jordan (Phase 55 Flag 4.1).

**How to avoid:** All A-S citations are `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` with X ≤ 8, OR `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2001}`. Update `alfsen-shultz-notes.md` with any new Phase 56 citations.

### Pitfall 6: Normality Assumption for WWvdW 2020 Classification

**What goes wrong:** Citing WWvdW 2020 three-type classification (Boolean ⊕ convex ⊕ purely-almost-convex) for W without verifying W is "normal" (σ-complete with suprema).

**Why it happens:** The classification is powerful; citing it gives structural information for free. But it only applies to normal SEAs.

**How to avoid:** Note that in FINITE-DIMENSION, every OUS is trivially σ-complete (all suprema exist). Finite-dim SPS is automatically normal. Confirm this in Plan 56-XX before citing WWvdW 2020. Even so, the classification is likely UNNECESSARY for Phase 56 because Approach 1 (direct S1-S7 + vdW 2019 Thm 1) already gives W is EJA; WWvdW 2020 would be invoked only as a fallback if vdW 2019 Thm 1 itself does not apply (e.g., infinite-dim). Do not cite unless needed.

---

## Level of Rigor

**Required for this phase:** **Formal proof at referee-ready standard.** The identity being defended is a load-bearing step in Paper 5 §5 Theorem-local-tomo (the upper bound); it is quoted in type-exclusion.tex §6 for the `M_2(ℝ)` exclusion argument. A sloppy proof here cascades into §6 referee objections.

**Justification:** Paper 5 is a JMP submission; all steps in the derivation chain must be reconstructible from the stated axiom list by a skeptical reader. R7 is the documented pitfall; pre-empting it requires formal proof of whichever "carries" sense is needed.

**What this means concretely:**

- Every step in the S1-S7-on-W verification must cite either (a) a vdW 2019 axiom, (b) the Peirce-Preservation Lemma by name, (c) an A-S 2003 Ch. 1-8 proposition with exact number, or (d) a standard linear algebra fact (tensor bilinearity, state separation).
- "Obvious" / "clearly" / "immediately follows" are forbidden in the Phase 56 revision text (R4 from Phase 55/54 pitfalls).
- The three "carries" senses are stated and the proof specifies exactly which sense is established.
- The SymPy spot-check produces an exit code 0 with recorded runtime < 30 sec (budget generous; Phase 54 achieved 0.013s).
- A forbidden-token grep pass MUST return zero hits outside explicit scope-demarcated blocks (same discipline as Phase 54/55).

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Assert "W carries the SP" without sense specification | Explicit three-sense disambiguation | This phase (Phase 56) | Makes R7 defense explicit. |
| Cite vdW 2019 Thm 1 face-restriction without verifying W is a face | Verify face status; use direct S1-S7 if W not a face | This phase | Prevents silent false claim. |
| Verify factor-level Peirce invariance by "obvious" instinct | Cite `\ref{lem:peirce-preservation}` + `\ref{ax:S0}` | Phase 54 (C-i) closure | R11 discipline. |
| Bare `\cite{AlfsenShultz2003}` for face/compression theory | Bracketed `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` with Ch. ≤ 8 | Phase 55 (C-i) closure | R5 discipline. |

**Superseded approaches to avoid:**

- **Hardy 2001 "simplicity" axiom** for motivating minimal composite: superseded by Masanes-Müller continuous reversibility, CDP purification. Paper 5 uses an `sms:minimal` clause, which is Hardy-style. Phase 59 (not Phase 56) handles the defense. Phase 56 takes `sms:minimal` as given.
- **"Every sub-OUS of an EJA is an EJA"** — FALSE in general; only faces inherit EJA structure automatically. This is exactly the R7 trap. Phase 56 must not rely on this.

---

## Open Questions

1. **Is W a face of V_{BM}?** (DECISIVE)
   - **What we know:** `sms:minimal` forces `dim V_{BM} = d²` (for the complex case). But `sms:minimal` is a DIMENSION-counting clause, not a face-structure clause. W could be a face, a hereditary subcone, a general positive subspace, or just an algebraic subspace.
   - **What's unclear:** Whether `W := span{a_i ⊗ b_j}` is order-convex and hereditary in V_{BM}.
   - **Impact on this phase:** If W IS a face, Approach 2 (face-restriction via vdW 2019 Thm 1) works cleanly. If W is NOT a face, Approach 1 (direct S1-S7) is required.
   - **Recommendation:** Plan 56-01 schedules a face-check task as Wave 1. Default expectation: W is NOT a face (span of extremal points is algebraic, not order-hereditary). Proceed with Approach 1 regardless; face check is a short detour.

2. **What does "H_3(ℝ) wedge component (3-dim antisymmetric)" in the roadmap scope mean?** (AMBIGUITY)
   - **What we know:** H_3(ℝ) consists of 3×3 REAL SYMMETRIC matrices — dimension 6. A 3-dim "antisymmetric" subspace of H_3(ℝ) does not exist (the antisymmetric part of a symmetric matrix is zero).
   - **What's unclear:** The roadmap says "H_3(ℝ) wedge component (3-dim antisymmetric)". Three plausible interpretations:
     - (a) The **Peirce 1-space** `V_1(p_i, p_j)` inside H_3(ℝ) with respect to three diagonal rank-1 projectors: this is 3-dim (one V_1 for each of {(1,2), (1,3), (2,3)}).
     - (b) The **off-diagonal subspace** of H_3(ℝ) parametrized by three real off-diagonal entries (the (1,2), (1,3), (2,3) entries): also 3-dim. Identical to (a) when the Peirce family is the diagonal projectors.
     - (c) A literal exterior-algebra wedge, `Λ²(ℝ³) ≅ ℝ³`: 3-dim but not naturally inside H_3(ℝ).
   - **Impact:** The SymPy test design depends on this. Interpretation (a)/(b) coincides and is the natural one for Paper 5; interpretation (c) is a non-sequitur in this context.
   - **Recommendation:** Plan 56 interprets "H_3(ℝ) wedge component" as the 3-dim off-diagonal Peirce-1-space of H_3(ℝ) w.r.t. the diagonal rank-1 projector family. Flag the ambiguity explicitly in RESULT.md so the planner/orchestrator can correct if needed.

3. **Which §5/§6 consumer needs sense (b) vs. sense (c) of "carries"?** (DOWNSTREAM SCOPE)
   - **What we know:** Roadmap scope declares "downstream use requires (b) or (c)." Section `composite-lt.tex §subsec:lt-proof` (Thm-local-tomo upper bound) uses the minimality clause, which needs sense (b). Section `type-exclusion.tex` uses `V_{BM}` for the real/quaternionic exclusion.
   - **What's unclear:** Whether `type-exclusion.tex` needs sense (b) (SPS on W with its induced structure) or sense (c) (functorial embedding).
   - **Impact:** If sense (c) is needed, Plan 56-XX must upgrade from (b) to (c). The upgrade is cheap (positivity of ι + unitality); just needs to be stated.
   - **Recommendation:** Plan 56-01 schedules a "downstream consumer scan" task: grep `type-exclusion.tex` and `discussion.tex` for `V_{BM}` uses and classify each by required sense. Aim: establish sense (c) by default; note downgrade to sense (b) if (c) is not achievable.

4. **Does Phase 54 (C-i) affect the `prop:inheritance` S4-on-W proof?** (R11 CHECK)
   - **What we know:** `prop:inheritance` S4 proof uses A-S 2003 Thm 1.23 (state separation), which is pre-Jordan-legal. It does NOT use factor-level Peirce-invariance.
   - **What's unclear:** Nothing — this one is clean.
   - **Impact:** S4-on-W is independent of Phase 54 (C-i). Reuse `prop:inheritance` proof verbatim.
   - **Recommendation:** Cite `prop:inheritance` in Plan 56-XX S4-on-W subproof; no adaptation needed.

5. **Does Paper 5 use "Theorem 5.8" numbering anywhere visible?** (LABELING)
   - **What we know:** No `\label{thm:5.8}` or `\label{thm:upper-bound}` in main-jmp-submitted.tex. The roadmap scope uses "Thm 5.8" as a logical name; the actual LaTeX label is `\label{thm:local-tomo}` (composite-lt.tex L162) or `\label{thm:lt-full}` (appendix-proofs.tex L164).
   - **What's unclear:** Whether the roadmap's "Thm 5.8" refers to `thm:local-tomo` or a sub-statement (the upper-bound lemma embedded in its proof at L203-222).
   - **Impact:** Plan 56-01 must explicitly map "Thm 5.8 upper bound" to `thm:local-tomo`-upper-bound (lines 203-221 of composite-lt.tex + lines 228-238 of appendix-proofs.tex).
   - **Recommendation:** Plan 56-01 names the target as `thm:local-tomo` upper-bound step; treat "Thm 5.8" as informal shorthand.

---

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Approach 1 (direct S1-S7 on W) | S1-on-W fails because tensor bilinear extension not well-defined | Approach 2 (face-restriction) IF W turns out to be a face | Moderate — requires establishing face status, which was supposed to be optional. |
| Approach 1 (direct S1-S7 on W) | S5/S6/S7-on-W fails because compatibility doesn't reduce cleanly | Gudder-Greechie 2002 Example 39 precedent (Approach 3) | High — implies Phase 56 outcome (C): §5/§6 downstream structurally revised to need only sense (a). |
| Approach 2 (face-restriction) | W is not a face of V_{BM} | Approach 1 (already default) | Low — Approach 1 is the base plan. |
| SymPy spot-check | H_3(ℝ) ⊗ H_3(ℝ) computation too slow | Restrict to a specific low-dim slice (e.g., V_1(p_1, p_2) × V_1(p_1, p_2)) | Low — analogous to Phase 54/55 patterns. |
| vdW 2019 Theorem 1 invocation | W's order-isomorphism status is ambiguous in the product-effect basis | Use vdW 2019 Theorem 1 on `V_B` and `V_M` separately, then invoke vdW 2019 Definition 4 (locally tomographic composite) + explicit tensor-SPS construction | Low — Def 4 is exactly the product-form SP template. |

**Decision criteria:** Switch to Gudder-Greechie 2002 precedent (Approach 3) only if SymPy spot-check produces a CONCRETE counterexample to sense (b) on H_3(ℝ) ⊗ H_3(ℝ) — e.g., finds `a⊗b, c⊗d` with `(a⊗b)∘((c⊗d)∘(e⊗f)) ≠ ((a⊗b)∘(c⊗d))∘(e⊗f)` despite factor-compatibility. Absent such counterexample, stay with Approach 1.

---

## Proposed Plan Structure

**Recommended:** THREE plans across three waves, with human-decision checkpoint at Wave 1 close.

### Plan 56-01 (Wave 1: Text extraction + face-status resolution + SymPy design)

**Scope:**
- Task 1: Extract the "Thm 5.8 upper bound" identity verbatim from `composite-lt.tex` (L162-222 full proof, L203-221 upper-bound step specifically) + `appendix-proofs.tex` (L164-243 full proof, L228-238 upper-bound step specifically). Produce `thm-5-8-identity-verbatim.md` with line numbers, anomaly notes, and ambiguity annotations.
- Task 2: Scan §5/§6 downstream consumers of "W carries" language (grep `composite-lt.tex`, `type-exclusion.tex`, `discussion.tex`, `appendix-proofs.tex` for `V_{BM}`, `product-form`, `inherits`, `carries`). Classify each by required "carries" sense. Produce `downstream-consumer-scan.md`.
- Task 3: Resolve W's face status in V_{BM}. Two sub-tasks: (3a) attempt to prove W is a face via A-S 2003 Ch. 1 face-definition check; (3b) if (3a) fails, exhibit a concrete non-face witness. Produce `w-face-status.md` with outcome tag {IS-FACE, NOT-FACE, INCONCLUSIVE}.
- Task 4: Formalize the three "carries" senses in explicit mathematical notation. Produce `carries-senses.md` with a three-sense table and explicit collapse/non-collapse notes.
- Task 5: Design SymPy spot-check for H_3(ℝ) ⊗ H_3(ℝ). Specify (i) which sense to test, (ii) axiom checks S1, S3, S4 (S5 is factor-level, cite Phase 54), (iii) closure test, (iv) one negative test (sense (a) counterexample attempt). Produce `sympy-design.md`.
- Task 6: **Human-decision checkpoint.** Present face-status outcome + downstream consumer scan + three-senses formalization. User confirms which "carries" sense Phase 56 targets (default: sense (b) + upgrade to (c) if cheap). User confirms face-status handling.

**Wave gates:** Task 1-5 must all complete before Task 6.

### Plan 56-02 (Wave 2: SymPy execution + S1-S7-on-W proof authoring)

**Scope (conditional on Plan 56-01 Task 6 outcome):**
- Task 1: Execute SymPy spot-check per `sympy-design.md`. Produce `closeout-sympy.py` + exit log (exit 0 = PASS). Runtime budget < 30 sec.
- Task 2: Author the sense-(b) proof on W with `∘|_W`. For each axiom S1-S7, produce a `claim-si.md` + proof text. Reuse Paper 5 `prop:inheritance` for S4; reuse factor-level derivations + `\ref{lem:peirce-preservation}` for S5/S6/S7. Produce `w-sps-proof.md`.
- Task 3: Author the sense-(c) upgrade: show `ι : W ↪ V_{BM}` is unital, positive, and preserves `∘`. Produce `ci-sps-morphism.md`.
- Task 4: Produce `carries-three-sense-table.md` — the R7 disambiguation table naming which sense Phase 56 established and which sense each downstream consumer needs.

### Plan 56-03 (Wave 3: Revision text integration + adversarial review + phase close)

**Scope:**
- Task 1: Author Phase 56 revision text for `composite-lt.tex` (upper-bound proof L203-221 augmented with three-sense disambiguation + explicit sense-(b)/(c) claims) and `appendix-proofs.tex` (upper-bound proof L228-238 similarly augmented). Produce `phase56-revision.md`.
- Task 2: Integrate revision into living `main.tex` / `sections/composite-lt.tex` / `sections/appendix-proofs.tex`. Commit to blog repo. Verify `main-jmp-submitted.tex` zero-diff.
- Task 3: Exit-gate check: (HALF-A) grep for three-sense language in integrated files; (HALF-B) manual semantic review. Both must PASS.
- Task 4: Adversarial review via `gpd-review-math` with Phase 56 priming artifacts (56-CONTEXT.md if exists, 56-RESEARCH.md, `carries-three-sense-table.md`, `w-face-status.md`, forbidden-token list, R1-R7 + R11 pitfalls). Produce `56-ADVERSARIAL-REVIEW.md`.
- Task 5: Cross-check against Phase 54/55 RESULTs: all R11 touch points cited correctly; no token violations. Produce `CONSISTENCY-CHECK.md`.
- Task 6: **Phase 56 close confirmation checkpoint:human-verify.** Produce `56-RESULT.md` with outcome tag {(A), (B), (C)}.

**Wave dependencies:** Plan 56-01 → Plan 56-02 → Plan 56-03 (strict sequential; face-status outcome from 56-01 Task 6 may reshape 56-02 if (C) triggered).

---

## Sources

### Primary (HIGH confidence)

- **van de Wetering, J. (2019). "Sequential product spaces are Jordan algebras." J. Math. Phys. 60, 062201.** [arXiv:1803.11139](https://arxiv.org/abs/1803.11139). Theorem 1 (finite-dim SPS → EJA) + Definition 2 (S1-S7 axioms) + Definition 4 (locally tomographic composite). Verified verbatim via PDF fetch of v3 (2020-12-15). Confidence: HIGH.
- **van de Wetering, J. (2018). "Three characterisations of the sequential product." J. Math. Phys. 59, 082202.** [arXiv:1803.08453](https://arxiv.org/abs/1803.08453). Thm 2 (Lüders form on EJA). Confidence: HIGH.
- **Westerbaan, A., Westerbaan, B., van de Wetering, J. (2020). "The three types of normal sequential effect algebras." Quantum 4, 378.** [arXiv:2004.12749](https://arxiv.org/abs/2004.12749). Three-type classification: Boolean ⊕ convex ⊕ purely-almost-convex. Confidence: HIGH.
- **Gudder, S., Greechie, R. (2002). "Sequential products on effect algebras." Rep. Math. Phys. 49, 87-111.** [NASA ADS](https://ui.adsabs.harvard.edu/abs/2002RpMP...49...87G/abstract). Example 39: associative non-EJA SEA (R7 precedent). Confidence: HIGH for existence; MEDIUM for exact Ex. 39 content (full-text verification deferred).
- **Alfsen, E.M., Shultz, F.W. (2003). *Geometry of State Spaces of Operator Algebras*. Birkhäuser PM 190.** Ch. 1 (state separation Thm 1.23), Ch. 7 (compressions: Def 7.1, Prop 7.23, Prop 7.43, Prop 7.49, Prop 7.50). Ch. 9 FORBIDDEN per Phase 55 Flag 4.1. Confidence: HIGH (Phase 54/55 verified).
- **Barnum, H., Graydon, M.A., Wilce, A. (2020). "Composites and Categories of Euclidean Jordan Algebras." Quantum 4, 359.** [arXiv:1606.09331](https://arxiv.org/abs/1606.09331). Definition of completely Jordan-preserving maps; sub-composite morphism structure; "no composite has exceptional EJA as summand" theorem. Confidence: HIGH.
- **Phase 54 RESULT.md** (`.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-RESULT.md`). Peirce-Preservation Lemma + S0 axiom. Confidence: HIGH (Phase 54 CLOSED at (C-i) 2026-04-16).
- **Phase 55 RESULT.md** (`.gpd/phases/55-s4-facial-structure-lemma/55-RESULT.md`). S4 facial structure closed pre-Jordan; bracketed A-S citation discipline. Confidence: HIGH (Phase 55 CLOSED at (C-i) 2026-04-17).
- **Paper 5 living main.tex + sections/*.tex** (`~/repos/blog/landing/papers/qm-from-self-modeling/`). The Thm-local-tomo identity. Confidence: HIGH (directly inspected).

### Secondary (MEDIUM confidence)

- **Faraut, J., Korányi, A. (1994). *Analysis on Symmetric Cones*. OUP.** Ch. III (Euclidean Jordan algebras); Prop III.4.2 (trace form non-degeneracy on simple EJA). Used in appendix-proofs.tex L195. Confidence: HIGH for the cited proposition; MEDIUM for general chapter content (not verified against book pages).
- **Barnum, H., Wilce, A. (2014). "Local Tomography and the Jordan Structure of Quantum Theory." Found. Phys. 44, 192-212.** [arXiv:1202.4513](https://arxiv.org/abs/1202.4513). Motivation for local-tomography arguments in operational reconstructions. Confidence: HIGH.
- **`.gpd/research/METHODS.md`** (GPD project research). Method 5 (Phase 56 primary) specification. Confidence: HIGH (Paper 5 project-level research).
- **`.gpd/research/PITFALLS.md`** (GPD project research). R1-R12, especially R7 (carries equivocation) and R11 (cross-phase cascade). Confidence: HIGH.

### Tertiary (LOW confidence)

- Plavala, M. (2023). "General probabilistic theories: An introduction." Cited at composite-lt.tex L16. Not directly consulted in Phase 56 research. Confidence: LOW (Paper 5 secondary citation).
- Niestegge, G. (2020). "Local tomography and the role of the complex numbers in quantum mechanics." arXiv:2001.11421. Not directly consulted. Confidence: LOW.

---

## Caveats and Alternatives (Pre-Submission Self-Critique)

**Q: What assumption am I making that might be wrong?**
A: I am assuming that the "Thm 5.8 upper bound" the roadmap refers to is `thm:local-tomo` (composite-lt.tex L162-222), specifically the upper-bound portion (L203-221). There is no Theorem numbered 5.8 anywhere in `main-jmp-submitted.tex` as rendered. If the user means a different theorem, Plan 56-01 Task 1 must surface this immediately.

**Q: What alternative approach did I dismiss too quickly?**
A: I dismissed Approach 2 (face-restriction) as the primary route, treating it as fallback. A case could be made that W IS a face: the product-effect cone `cone(V_B^+ ⊗ V_M^+) ⊆ V_{BM}^+` is a hereditary subcone in the complex case by Barnum-Graydon-Wilce composite theory. If this holds in the Paper 5 setting, Approach 2 works cleanly. I set Approach 1 as primary because it is robust to W being NOT a face; but if the face-status investigation resolves to YES, Approach 2 is cleaner for referee exposition. The Plan 56-01 face-check task is the decision point.

**Q: What limitation of my recommended method am I understating?**
A: The direct S1-S7 verification on W (Approach 1) is conceptually tight but OPERATIONALLY verbose: 7 axiom checks × ~1 page each ≈ 5-7 additional pages in the Paper 5 revision. This may exceed the revision text budget Paper 5 can absorb without disturbing §6/§7. If page-count becomes a concern, a shortcut is to check only the non-trivial axioms (S1, S4, S5) and claim the rest by "same pattern as `prop:inheritance`." The shortcut is probably defensible but is a Phase 56 editorial decision, not a research finding.

**Q: Is there a simpler method I overlooked because the complex one is more impressive?**
A: Yes — vdW 2019 Def. 4 (locally tomographic composite) LITERALLY says `(V_B ⊗ V_M)` equipped with `(a⊗b) & (c⊗d) := (a & c) ⊗ (b & d)` is a sequential product space when factor-level axioms hold. If Paper 5's W is the algebraic tensor product `V_B ⊗_alg V_M`, then the SPS-ness of W is vdW 2019 Def. 4 applied with bilinear extension. The entire S1-S7 verification is OFFLOADED to vdW 2019. Plan 56-XX should lean HEAVILY on this definition; the verification may be ONE paragraph citing vdW 2019 Def. 4 + Thm 1 + state separation (for S4), rather than seven axiom checks.

This is the route I now recommend as the PRIMARY approach within Approach 1. It is the simplest and strongest.

**Q: Would a specialist disagree with my recommendation?**
A: A specialist in operational reconstructions (e.g., Wilce, Barnum, Graydon) would likely NOT object to the vdW 2019 Def. 4 route, but MIGHT object to the face-status framing. Barnum-Graydon-Wilce 2020 treats composites categorically (as objects of a monoidal category of EJAs) rather than via face inclusions. The "face of V_{BM}" framing is natural for AS-style order-theoretic exposition but not for the operational-composite literature. The Plan should present BOTH framings and let the reader pick whichever sounds more natural; no content is lost.

A specialist in foundational algebraic QM (e.g., Heunen, Jacobs) would likely focus on sense-(c) functorial preservation and might push the plan toward a category-theoretic statement (W as sub-object in a monoidal category of SPSs). Phase 56 should offer sense-(c) as optional upgrade, not primary; the JMP audience cares about S1-S7 verification, not monoidal-category machinery.

---

## Metadata

**Confidence breakdown:**

- Mathematical framework: **HIGH** — vdW 2019 S1-S7 verified verbatim; Peirce-Preservation Lemma from Phase 54 cited by name; factor-level corrected product from Paper 5 already verified.
- Standard approaches: **HIGH** — Approach 1 (direct + vdW 2019 Def 4 + Thm 1) is well-established; Approach 2 (face restriction) and Approach 3 (Gudder-Greechie precedent) are documented fallbacks.
- Computational tools: **HIGH** — SymPy infrastructure exists from Phase 54 closeout + Phase 55 s4 spot check; extending to tensor products is straightforward.
- Validation strategies: **HIGH** — complex/real/quaternionic cases give three independent limit validations; symbolic-exact SymPy matches factor-level outputs.
- W face status: **LOW** — decisive but unresolved pre-plan; Plan 56-01 Task 3 is precisely scoped to resolve this.
- Downstream consumer (sense (b) vs (c)): **MEDIUM** — Plan 56-01 Task 2 scoped to resolve.
- H_3(ℝ) "wedge component" interpretation: **MEDIUM** — Open Question 2 flags ambiguity; natural interpretation is Peirce-1-space off-diagonal subspace.

**Research date:** 2026-04-17
**Valid until:** Physics results stable indefinitely; Paper 5 §5 frozen living text is the reference (if Paper 5 v14.0 is revised post-review, re-check `composite-lt.tex` line numbers). vdW 2019 / WWvdW 2020 / Gudder-Greechie 2002 are all stable published results.

---

## RESEARCH COMPLETE

**Phase:** 56 — Thm 5.8 Upper Bound: W Carries Product-Form Sequential Product
**Confidence:** HIGH (primary) / MEDIUM (W face-status + downstream consumer sense; both scoped into Plan 56-01 as explicit tasks)

### Key Findings

- **"Theorem 5.8" in roadmap = `thm:local-tomo` (composite-lt.tex L162-222) + `thm:lt-full` (appendix-proofs.tex L164-243), upper-bound portion (L203-221 + L228-238).** There is no `\label{thm:5.8}` in main-jmp-submitted.tex; "Thm 5.8" is informal shorthand for the upper-bound step of the local-tomography theorem.
- **Primary recommendation: vdW 2019 Def. 4 (locally tomographic composite) + Thm 1.** Since Paper 5's `W := span{a_i ⊗ b_j}` equipped with `(a⊗b) ∘ (c⊗d) = (a∘c) ⊗ (b∘d)` matches vdW 2019 Def. 4 verbatim, SPS-ness of W on product effects is by the definition itself. Sense (b) of "carries" follows from vdW 2019 Thm 1 applied to W. Sense (c) is a cheap upgrade (ι is unital positive with `∘|_W` literally restricted). The verification is ≤2 pages, not ≤7.
- **R7 disambiguation is the highest-value deliverable.** Three senses (closure / induced-structure / functorial) must be formally distinguished; sense (b) is what the minimality clause needs, sense (c) is the clean upgrade. Downstream use scan (Plan 56-01 Task 2) confirms which sense each §5/§6 consumer needs.
- **W's face status is structurally DECISIVE but OPERATIONALLY SECONDARY.** If W is a face of V_{BM}, face-restriction gives sense (b) trivially. If W is NOT a face, direct S1-S7 (via vdW 2019 Def. 4) still works. Either way, Approach 1 closes the phase. Face-check scheduled in Plan 56-01 Task 3; not a blocker.
- **Phase 54 (C-i) R11 inheritance:** S4-on-W proof in `prop:inheritance` uses state separation (A-S 2003 Thm 1.23), which is INDEPENDENT of Phase 54 (C-i). S5/S6/S7 reductions to factor-level DO touch Phase 54 (C-i) via the Peirce-Preservation Lemma; citations must use `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`. This R11 touchpoint is tracked and mitigated.
- **SymPy plan: H_3(ℝ) ⊗ H_3(ℝ) on the Peirce-1-space off-diagonal (3-dim each factor) = 9-dim sample; extend Phase 54 closeout-sympy.py infrastructure.** Runtime budget <30 sec. Interpretation clarification (Open Question 2) for "wedge component" in Plan 56-01.

### File Created

`/Users/ehrlich/scratch/get-physics-done/.gpd/phases/56-thm-5-8-upper-bound-w-carries-product-form-sequential-product/56-RESEARCH.md`

### Confidence Assessment

| Area | Level | Reason |
| ---- | ----- | ------ |
| Mathematical Framework | HIGH | vdW 2019 S1-S7 + Thm 1 + Def 4 verified verbatim via PDF fetch; Phase 54/55 verified-cite chain inherited; Peirce-Preservation Lemma available. |
| Standard Approaches | HIGH | Approach 1 (direct + vdW 2019 Def 4) is METHODS.md Method 5 Phase 56 primary; fallbacks documented (Approach 2 face-restriction, Approach 3 Gudder-Greechie). |
| Computational Tools | HIGH | SymPy infrastructure exists from Phase 54; tensor extension is straightforward; budget generous. |
| Validation Strategies | HIGH | Complex/real/quaternionic cases give three independent limit checks; symbolic-exact SymPy; state-separation benchmark. |
| W face-status | LOW | Unresolved pre-plan. Decisive for routing between Approach 1 (direct) and Approach 2 (face); Plan 56-01 Task 3 is scoped for this. |
| Downstream consumer scope | MEDIUM | Need to grep §5/§6 to confirm which "carries" sense each consumer needs. Plan 56-01 Task 2 is scoped for this. |
| H_3(ℝ) "wedge" interpretation | MEDIUM | Natural reading is Peirce-1-space off-diagonal; flagged as Open Question 2 for plan-level confirmation. |

### Open Questions (handed to planner)

1. Is W a face of V_{BM}? (Decisive; Plan 56-01 Task 3)
2. "H_3(ℝ) wedge component (3-dim antisymmetric)" — interpretation? Recommended: Peirce-1-space off-diagonal 3-dim. (Plan 56-01 Task 5)
3. Which §5/§6 downstream consumer needs sense (b) vs. (c)? (Plan 56-01 Task 2)
4. "Thm 5.8" labeling — map to `thm:local-tomo` or specific sub-statement? Recommended: `thm:local-tomo` upper-bound step. (Plan 56-01 Task 1)

### Convention Choices Made

- SP notation: `a ∘ b` (Paper 5 convention; identical to vdW `a & b`)
- Compression: `C_p` (matches Paper 5 and vdW)
- W definition: `W := span{a_i ⊗ b_j}` (composite-lt.tex L204)
- A-S discipline: bracketed `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` with X ≤ 8 OR `AlfsenShultz2001`; Ch. 9 FORBIDDEN
- Axiom scope: `{S0, S1-S7, linearity, A-S compression axioms Ch. 2/7/8, finite-dim spectrality}` (inherits Phase 54 CUSTOM_CONVENTION + vdW 2019 Def. 2)
- Three "carries" senses formally defined (closure / induced-structure / functorial); downstream use requires sense (b), cleanly upgraded to (c)

### Ready for Planning

Research complete. Planner (`gpd-planner`) can now create PLAN.md files according to the three-plan structure above (Plan 56-01 / 56-02 / 56-03) or re-partition as appropriate. All R7 / R11 / R1 pitfalls surfaced and mitigation strategies documented. Primary recommendation (Approach 1 via vdW 2019 Def. 4 + Thm 1) has HIGH confidence; the two MEDIUM-confidence open questions (W face status, downstream consumer sense) are scoped into Plan 56-01 as explicit Wave-1 tasks ending in a human-decision checkpoint.

```yaml
gpd_return:
  status: completed
  files_written:
    - /Users/ehrlich/scratch/get-physics-done/.gpd/phases/56-thm-5-8-upper-bound-w-carries-product-form-sequential-product/56-RESEARCH.md
  issues:
    - "Open Question 1: W face-status in V_{BM} unresolved pre-plan; decisive but scoped into Plan 56-01 Task 3"
    - "Open Question 2: 'H_3(ℝ) wedge component (3-dim antisymmetric)' roadmap phrasing is ambiguous; H_3(ℝ) itself has no antisymmetric subspace. Recommended interpretation: Peirce-1-space off-diagonal 3-dim. Requires plan-level confirmation"
    - "Open Question 3: Which §5/§6 downstream consumer needs sense (b) vs sense (c) of 'carries'? Scoped into Plan 56-01 Task 2"
    - "Paper 5 has no \\label{thm:5.8}; 'Thm 5.8' is informal shorthand for thm:local-tomo upper-bound step at composite-lt.tex L203-221 + appendix-proofs.tex L228-238"
    - "Gudder-Greechie 2002 Example 39 verification deferred — full RMP paper access not obtained; cited at AXIOM-STATED-IN-SECONDARY-SOURCE tier pending direct book access"
  next_actions:
    - "gpd-planner creates Plan 56-01 with 6 tasks (Wave 1: text extraction + face-status + downstream consumer scan + three-senses formalization + SymPy design + human-decision checkpoint)"
    - "gpd-planner creates Plan 56-02 conditional on 56-01 Task 6 outcome (Wave 2: SymPy execution + S1-S7-on-W proof + sense-(c) upgrade + three-sense table)"
    - "gpd-planner creates Plan 56-03 (Wave 3: revision text integration + adversarial review + phase close)"
    - "Plan 56-01 Task 3 (face-status check) is the highest-value first task; default expectation is W is NOT a face; proceed with Approach 1 regardless"
  confidence: HIGH
```
