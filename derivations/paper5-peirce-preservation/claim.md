# Peirce-Preservation Lemma — Conditional Restatement for Paper 5 §3.3 (Phase 54 Target)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; peirce_2_space=V_2(p_i):=range(C_{p_i}); peirce_1_space=V_1(p_i,p_j):=(C_{p_i}+C_{p_j})V - C_{p_i}V - C_{p_j}V; allowed_axiom_scope={S1 (additivity in 2nd arg), S3 (unitality + sharp constraint), linearity (derived from S1 + finite-dim), A-S compression axioms; S4-S7 FORBIDDEN pre-S4; Jordan product FORBIDDEN}; forbidden_tokens={M_n(ℂ) as proof device, Jordan, EJA, Lüders, pxp, √a b √a, operator product, f(λ,μ)=√(λμ) as primitive, h_n(ℂ), spin factor as proof device}

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 01 (Foundation wave, Task 3)
**Purpose:** Stable API for all Phase 54 attempt files (`attempt-NN.md`), the closeout SymPy artifact (`closeout-sympy.py`), and the final §3.3 revision text in `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`. Referenced by Phases 55, 57, 58 for downstream citation stability.
**Status:** LOCKED at plan 54-01 foundation wave.

---

## Section 1: Header and Convention Block

**Lemma name (chosen by executor per CTX decisions §S0-naming-style / Agent's Discretion):** "Peirce-Preservation Lemma". Downstream Plans 54-02 and 54-03 cite this lemma by this name.

**Convention block (copied from PLAN.md frontmatter, verbatim):**

- **Units:** N/A (pure algebra)
- **Sequential product symbol:** `a ∘ b` (Paper 5 convention; `a & b` from vdW 2019 / v2.0 Phase 4 is NOT used in revision text; state equivalence to `&` once)
- **Compression symbol:** `C_p` (vdW / v2.0 Phase 4 convention; state equivalence to A-S `c_p` and Niestegge `U_e` once)
- **Order unit space:** finite-dim archimedean OUS over ℝ with distinguished unit 1
- **Peirce 2-space:** `V_2(p_i) := range(C_{p_i})`
- **Peirce 1-space:** `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V - C_{p_i}V - C_{p_j}V`
- **Allowed-axiom scope:** S1 (additivity in 2nd arg), S3 (unitality + sharp constraint), linearity (derived from S1 + finite-dim), A-S compression axioms. S4-S7 FORBIDDEN pre-S4. Jordan product FORBIDDEN.
- **Forbidden tokens** (full list): `M_n(ℂ)` as proof device, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, `operator product`, `f(λ,μ) = √(λμ)` as primitive, `h_n(ℂ)`, `spin factor` as proof device.

---

## Section 2: Context

**Target text:** `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` §3.3 (subsection "The Corrected Product via Peirce Feedback") lines 483-562; **key claim lines 508-528** (frozen at git tag `paper5-jmp-submitted`).

**Frozen text inventory (the three target inclusions that this lemma replaces):**

- Paper 5 line 514: "`\seqp{a}{\cdot}` maps each Peirce subspace to itself."

The frozen text expands this to three separate inclusions (which this lemma states as three separate propositions, see Section 3):

- (i) `a ∘ V_2(p_i) ⊆ V_2(p_i)` for every `i`
- (ii) `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)` for every pair `(i, j)` with `i ≠ j` where `i, j ∈ supp(a)`
- (iii) `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` for every pair `(k, l)` with `{k, l} ∩ supp(a) = ∅` (cross-term invariance)

**Target non-sequitur being replaced (R2 — Decomposition vs. Invariance):** Paper 5 submitted §3.3 lines 510-514:

> "The Peirce decomposition with respect to the spectral projectors of~$a$ decomposes $V$ into subspaces $V_2(p_i)$ and $V_1(p_i, p_j)$. Compressions project onto these subspaces (Alfsen--Shultz~\cite{AlfsenShultz2003}), so linearity gives a block decomposition: `\seqp{a}{\cdot}` maps each Peirce subspace to itself."

This is the R2 non-sequitur: cited A-S fact is that V DECOMPOSES into Peirce subspaces (and the compressions `C_{p_i}` project onto them); the claim is that `L_a(b) := a ∘ b` RESPECTS this decomposition (i.e., is invariant on each summand). **Decomposition does not imply invariance.** The lemma below makes the invariance claim explicit, separates the three subspace cases, and lists allowed and forbidden proof tools.

**Outcome routing (per CONTEXT.md Decisions):** The SAME lemma statement closes under either outcome:

- **(A)** Rigorous proof from OUS primitives with assumption set `{S1, S3, linearity, A-S compression axioms}`
- **(C-i)** OUS-level "Peirce coherence" axiom `S0` stated explicitly, with assumption set `{S0, S1, S3, linearity, A-S compression axioms}`

Only the assumption clause changes between outcomes. The three target inclusions (i), (ii), (iii) are IDENTICAL across (A) and (C-i). Outcome **(C-ii)** replaces this lemma entirely with an S4-routing-around-Peirce strategy (not a variant of this lemma). Outcome **(B)** is UNAVAILABLE per ADDENDUM.

---

## Section 3: Lemma Statement (Conditional Form)

### Peirce-Preservation Lemma

**Under [ASSUMPTION SET]**, let `V` be a finite-dimensional spectral order unit space over ℝ, let `{p_1, ..., p_n}` be an orthogonal family of projective units in `V` (i.e., `p_i ⊥ p_j` for `i ≠ j` with mutual compressional annihilation `C_{p_i} C_{p_j} = 0`), and let `a = Σ_i λ_i p_i` with `λ_i ∈ ℝ` be a spectral decomposition. Write `supp(a) := {i : λ_i ≠ 0}`. Let `L_a(b) := a ∘ b` denote the left-multiplication map. Then:

#### Proposition 3.1 (Peirce 2-space invariance; anti-R3 case (i))

For every `i ∈ {1, ..., n}`,

> `a ∘ V_2(p_i) ⊆ V_2(p_i).`

Equivalently, `L_a(V_2(p_i)) ⊆ V_2(p_i)`.

#### Proposition 3.2 (Peirce 1-space invariance, standard (on-support) case; anti-R3 case (ii))

For every pair `(i, j)` with `i ≠ j` and `i, j ∈ supp(a)`,

> `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j).`

Equivalently, `L_a(V_1(p_i, p_j)) ⊆ V_1(p_i, p_j)`.

#### Proposition 3.3 (Peirce 1-space invariance, cross-term (off-support) case; anti-R3 case (iii), **R3 subtle case**)

For every pair `(k, l)` with `k ≠ l` and `{k, l} ∩ supp(a) = ∅`,

> `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l).`

Equivalently, `L_a(V_1(p_k, p_l)) ⊆ V_1(p_k, p_l)`.

### [ASSUMPTION SET] — two mutually exclusive forms (see Section 5)

Exactly one of:

- **(A) assumption set:** `{S1, S3, linearity of L_a, A-S compression axioms, finite-dim spectrality}`. Under this assumption set, Propositions 3.1, 3.2, 3.3 are THEOREMS to be proved.
- **(C-i) assumption set:** `{S0, S1, S3, linearity of L_a, A-S compression axioms, finite-dim spectrality}`, where S0 is the Peirce-coherence axiom stated at the compression level (see CONTEXT.md Decisions §S0 axiom form and 54-RESEARCH.md §Approach 3). Under this assumption set, Propositions 3.1, 3.2, 3.3 are DERIVED from S0 + A-S compression primitives + spectral decomposition. The S0 axiom is defended (not further derived) via canonical-example inspection (see 54-RESEARCH.md §Approach 3).

The three target inclusions (3.1), (3.2), (3.3) are **identical** across (A) and (C-i). Only the assumption clause varies. The outcome tag in the final RESULT.md for Phase 54 selects which assumption set is in force.

**Outcome (C-ii)** — alternative S4 routing around Peirce — replaces this lemma entirely with a different strategy and is NOT a variant of this lemma.

---

## Section 4: Allowed Tools

Every proof under either (A) or (C-i) is built ONLY from the following. (The `p_i` below denote projective units in a finite-dim spectral OUS unless otherwise noted; `b, c ∈ V`; `λ ∈ ℝ`.)

### 4.1 vdW 2019 Def. 2 axioms (the ONLY S-axioms allowed in Phase 54)

- **S1 (additivity in 2nd arg):** `a ∘ (b + c) = a ∘ b + a ∘ c`. Source: vdW 2019 (arXiv:1803.11139) Definition 2.
- **S3 (unitality + sharp constraint):** `1 ∘ a = a`; moreover `p ∘ b = C_p(b)` when `p` is a sharp effect. Source: vdW 2019 Definition 2 and Definition 7 (sharp effects).

> **Scope:** S2, S4, S5, S6, S7 are FORBIDDEN in Phase 54 proofs. S4-S7 would be pre-S4 use and invert the dependency on vdW Thm 1 (Pitfall R1). S2 (continuity in first arg) is not used in Phase 54 — the lemma is about algebraic invariance, not limits.

### 4.2 Linearity of `L_a` (derived from S1 + finite-dim)

- `L_a(b) := a ∘ b` is a linear endomorphism of `V`. Derivation: S1 gives additivity; finite-dim + continuity (S2 when needed only for scalar-multiplication compatibility, although in the purely algebraic Phase 54 setting, `L_a(λ b) = λ L_a(b)` for `λ ∈ ℝ` is taken as part of the "linearity" toolkit under the standard OUS-bilinearity conventions in vdW Def. 2).

### 4.3 A-S compression axioms

The four A-S compression axioms used in Phase 54 (exact Prop/Thm numbers in `alfsen-shultz-notes.md`; **A-S 2003 vol. 190 Ch. 2 "Abstract characterization of compressions" / Ch. 7 "General Compressions" / Ch. 8 "Spectral Theory"** — corrected 2026-04-16 from earlier misattribution to "A-S 2001 Ch. 7-8"; see `alfsen-shultz-notes.md` change-log):

- **Idempotency:** `C_p² = C_p`.
- **Positivity:** `C_p ≥ 0` (preserves the positive cone of `V`).
- **Complement on sharp effects:** `C_p + C_{p'} = pinching` (NOTE: **NOT** `= id` in non-commutative OUS; see v2.0 Phase 4-06 C4 correction in `derivations/04-peirce-feedback-extension.md` Step 1). `p' := 1 - p` when `p` is sharp.
- **Projector fix:** `C_p(p) = p`.

Plus the structural fact for orthogonal families:

- **Orthogonal mutual annihilation:** `C_{p_i} C_{p_j} = 0` for `i ≠ j` in an orthogonal family of projective units.

### 4.4 Finite-dim spectrality

- Existence of an orthogonal projective-unit family `{p_i}` and scalars `λ_i ∈ ℝ` such that `a = Σ_i λ_i p_i` (spectral decomposition). Source: vdW 2019 Definition 9 (spectrality) and **A-S 2003 vol. 190 Ch. 8 "Spectral Theory"** (spectral duality; corrected 2026-04-16 from earlier misattribution to "A-S 2001 Ch. 8").

### 4.5 Peirce 1-space definition (derived, not primitive)

- `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V − C_{p_i}V − C_{p_j}V` (abstract OUS definition; matches Paper 5 convention and v2.0 Phase 4-06 via the pinching complement). This is a DEFINITION derived from the A-S compression axioms, not an additional primitive.

### 4.6 (C-i)-only: S0 axiom (Peirce coherence, compression-level form)

Under outcome (C-i) only, the following is ADDED to the allowed-tool list as an axiom (not derivable from S1-S7):

- **S0 (candidate compression-level form):** For any orthogonal family `{p_i}` of projective units in a spectral OUS `V`, the compressions `{C_{p_i}}` pairwise commute, and `C_{p_i} C_{p_j} = 0` for `i ≠ j`. (Equivalent reformulations at the same level: "orthogonal projective units generate a commutative projection algebra" or Niestegge-2008-style `U_e` coherence.)

Final S0 wording is LOCKED in Plan 54-03 at the (C-i) drafting step; this is the candidate form (see 54-RESEARCH.md §Approach 3). Under (A), S0 is NOT invoked.

> **Key clarification:** The statement `C_{p_i} C_{p_j} = 0` for orthogonal `i ≠ j` appears in BOTH the (A) allowed-tool list (Section 4.3, derived as a structural fact from A-S Ch. 7-8 — `alfsen-shultz-notes.md` entry to verify) AND in (C-i)'s S0. The distinction: under (A) it is cited as a theorem of A-S compression theory with a specific Prop/Thm number (pre-Jordan-legal); under (C-i), if the A-S Prop/Thm for it turns out to be post-Jordan or ambiguous, S0 stands in as the axiomatized version. `alfsen-shultz-notes.md` Section 6 tracks which case applies — see that file's §Section 6: Orthogonal-projective-unit compressional annihilation.

---

## Section 5: Forbidden Tools

The following are FORBIDDEN as proof devices or premises. They may appear in this file only as the subject of classification (naming what is forbidden), not as a step in the proof.

### 5.1 Full forbidden_tokens list (verbatim from PLAN.md frontmatter)

- `M_n(ℂ)` (and `M_n(C)`) as proof device
- `Jordan`
- `EJA`
- `Lüders` (and `Luders`)
- `pxp`
- `√a b √a` (and `sqrt(a) b sqrt(a)`)
- `operator product`
- `f(λ,μ) = √(λμ)` (and `f(lambda,mu) = sqrt(lambda*mu)`) **as a primitive** (it is a CONCLUSION of Paper 5 §4, downstream of §3.3, and must not be used in §3.3 as a starting input)
- `h_n(ℂ)` (and `h_n(C)`)
- `spin factor` (as proof device; spin-factor appearance is allowed only in the (C-i) canonical-example defense paragraph as a defense example, NOT as a proof step)

### 5.2 Explicit call-outs (non-exhaustive; illustrative)

- **Jordan product** `a · b := (a ∘ b + b ∘ a) / 2` — FORBIDDEN as a proof device in Phase 54. Using Jordan structure to prove Peirce invariance inverts the dependency on vdW Thm 1 (Pitfall R1): vdW Thm 1 consumes S1-S7 to PRODUCE Jordan structure; deriving it before S4 creates circularity.

- **Peirce decomposition theorem cited as justification for INVARIANCE of `L_a`** — FORBIDDEN. This is R2 (decomposition vs. invariance non-sequitur). Decomposition (`V = V_2 ⊕ V_1 ⊕ V_0`) is a cited A-S fact; invariance (`L_a(V_k) ⊆ V_k`) is the claim to prove. Paper 5 submitted §3.3 lines 510-514 fell into this non-sequitur.

- **A-S 2003 Theorem 9.37** — FORBIDDEN. A-S 2003 vol. 190 Ch. 9 is the Jordan-state-space characterization chapter per ADDENDUM (`.gpd/research/ADDENDUM-independent-literature-check.md`). Any invocation of Thm 9.37 at the pre-Jordan level is circular. Replace with **A-S 2003 vol. 190 Ch. 2 / Ch. 7 / Ch. 8** compression citation (pre-Jordan-legal within the same volume) OR with (C-i) S0 axiom. (Previously this file said "A-S 2001 vol. 179 Ch. 7-8" — that was a misattribution; the compression material is in the 2003 volume. Corrected 2026-04-16.)

- **SP closed-form `f(λ, μ) = √(λμ)` as primitive** — FORBIDDEN. In Paper 5, this is a CONCLUSION of §4 (via positivity bound + self-modeling faithfulness); in §3.3 it is not yet available. Using it as a premise in §3.3 inverts dependency.

- **Spin factor as proof device** — FORBIDDEN in (A) and (C-i) proofs. Spin factors are JB-algebras (Jordan-level structure). The ONLY legal appearance of "spin factor" in Phase 54 output is inside the (C-i) canonical-example defense paragraph, where spin factors are cited as a model in which S0 holds (defense example, not proof step).

- **`M_n(ℂ)^sa` as proof device** — FORBIDDEN in the body of §3.3's revision text and in any attempt's PROOF body. Permissible inside:
  - model-instantiation sanity checks (early falsifier gate #3 per CONTEXT.md Decisions)
  - the (C-i) canonical-example defense paragraph (where `pxp` matrix-block computation is legal **inside the model** per CONTEXT.md Decisions §S0 axiom form)

- **`pxp`, `√a b √a`, `operator product`, `h_n(ℂ)`** — FORBIDDEN as proof devices. Same logic as `M_n(ℂ)^sa`: these are C\*-algebraic / post-Jordan constructs; using them as §3.3 proof devices imports structure not yet derived.

### 5.3 Rejection of the Phase 4-06 seed (audit outcome)

Per `audit-04-06.md` VERDICT = AUDIT-FAILS (line 119-163 is an `M_n(ℂ)`-level proof device for the positivity bound), the Phase 4-06 corrected-product formula `a ∘ b = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} √(λ_i λ_j) P_{ij}(b)` MAY NOT be used as a starting premise in any Phase 54 (A) attempt. Plan 54-02 takes Approach 2 (compression combinatorics) as the single (A) attempt; if that fails, Plan 54-03 pivots to (C-i).

Plan 54-02's single (A) attempt and Plan 54-03's (C-i) draft BOTH prove/derive Propositions 3.1, 3.2, 3.3 above — unchanged in statement, varying only in assumption set.

---

## Section 6: Downstream Citation Interface

### 6.1 Every attempt file references this lemma

- Every `derivations/paper5-peirce-preservation/attempt-NN.md` in Phase 54 Plan 54-02 or 54-03 cites this lemma by its name ("Peirce-Preservation Lemma"), states which assumption set ((A) or (C-i)) the attempt is working under, and proves (or derives from S0) Propositions 3.1, 3.2, 3.3 SEPARATELY.
- Each attempt MUST prove / derive all three propositions. An attempt that only handles 3.1 and 3.2 but not 3.3 (the R3 cross-term case) is INCOMPLETE — per PITFALLS.md R3 mandatory case coverage.

### 6.2 §3.3 revision text uses the lemma verbatim

- The final §3.3 revision text, written into `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` (NOT `main-jmp-submitted.tex`, which is frozen at tag `paper5-jmp-submitted`), states this lemma VERBATIM modulo whitespace and LaTeX-display formatting. The chosen assumption set (either (A) or (C-i)) is announced at the top of §3.3.
- **Exit gate (CONTEXT.md user guidance):** automated grep of the lemma statement from this file against §3.3 revision text AND manual semantic review. Both must pass before Phase 54 closes.

### 6.3 Consumption by downstream Phases 55, 57, 58

- **Phase 55 (S4 phi-independence):** if Phase 54 closes (C-i), Phase 55's rewritten S4 argument invokes S0 + this lemma; the lemma's conditional form means only the assumption set propagates, not the target inclusions.
- **Phase 57 (phi-audit):** shares `alfsen-shultz-notes.md` and this lemma's conditional form; phi-inertness analysis uses the Peirce structure stated here.
- **Phase 58 (Lean axiom audit):** the Lean axiom `_peirce_preservation` in `~/repos/research/lean/RadicalRelativity/SelfModelingBridge.lean` is RELABELED based on Phase 54's outcome tag. Under (A), it becomes a theorem (type-(i) theorem-in-disguise resolved). Under (C-i), it becomes a type-(iv) primitive axiom with S0 defense (and Phase 58 checks that the Lean encoding matches S0's statement).

### 6.4 SymPy validation wiring

- **Per-attempt gate (CONTEXT.md VALD-54-01):** each `attempt-NN.py` runs a rank-1 sanity check on `H_3(ℝ)` with two orthogonal rank-1 projectors; runtime < 1 sec; attempt cannot be sealed until it passes. Checks 3.1 and 3.2 (standard case).
- **Closeout artifact (CONTEXT.md VALD-54-01):** `closeout-sympy.py` runs a fuller check INCLUDING R3 cross-term Proposition 3.3 (`V_1(p_k, p_l)` with `{k, l} ∩ supp(a) = ∅`). This is the R3-mandatory coverage gate. Referenced in the final RESULT.md, not embedded in the winning attempt file.

---

## Section 7: References

- **Paper 5 submitted (frozen):** `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` §3.3 lines 483-562 (key claim 508-528), frozen at git tag `paper5-jmp-submitted`.
- **Paper 5 living (revision target):** `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` §3.3 (NOT the frozen submitted copy).
- **vdW 2019:** van de Wetering (2019), "Sequential product spaces are Jordan algebras," JMP 60, 062201, arXiv:1803.11139. Def. 2 (S1, S3), Def. 7 (sharp effects), Def. 9 (spectrality), Thm 1 (S1-S7 finite-dim ⇒ EJA; forbidden as pre-S4 tool).
- **A-S 2003 vol. 190** (primary compression-theory source): Alfsen & Shultz (2003), *Geometry of State Spaces of Operator Algebras*, Birkhäuser Progress in Mathematics vol. 190, ISBN 978-1461265757, DOI 10.1007/978-1-4612-0019-2. **Ch. 2 §"Abstract characterization of compressions"** (p. 75), **Ch. 7 "General Compressions"** (p. 211), **Ch. 8 "Spectral Theory"** (p. 251) — pre-Jordan-legal within this volume; compression-axiom rows in `alfsen-shultz-notes.md`. (Earlier versions of this reference line said "A-S 2001 vol. 179 Ch. 7-8" — corrected 2026-04-16; the compression material is in the 2003 volume, not 2001.)
- **A-S 2001 vol. 179** (for reference; NOT the compression-axiom source): Alfsen & Shultz (2001), *State Spaces of Operator Algebras: Basic Theory, Orientations, and C\*-products*, Birkhäuser Progress in Mathematics vol. 179, ISBN 978-0817638900. Cited by Paper 5 elsewhere (C*-flavored material); does not carry the compressions used in Phase 54.
- **ADDENDUM:** `.gpd/research/ADDENDUM-independent-literature-check.md` (2026-04-16) — justifies (B)-unavailability; confirms Peirce is post-Jordan in accessible literature; supplies pre-Jordan-illegal verdict on A-S 2003 Thm 9.37.
- **CONTEXT.md:** `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-CONTEXT.md` — locked user decisions: outcome classification (A / C-i / C-ii), forbidden-token list, allowed-axiom scope, stop/rethink triggers, exit gate.
- **RESEARCH.md:** `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-RESEARCH.md` — audit protocol design, (A) attempt routes, S0 axiom design, A-S citation audit protocol, per-attempt SymPy gate design, adversarial review priming specification.
- **Audit (companion artifact in this directory):** `derivations/paper5-peirce-preservation/audit-04-06.md` — binary VERDICT: AUDIT-FAILS on v2.0 Phase 4-06 Eq. (04-06.4) derivation; failure in line 119-163 (M_n(C) positivity-bound proof device); routing consequence = `option-b-fails-compression`.
- **Alfsen-Shultz citation notes (companion SHARED artifact):** `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md` — per-citation resolution of every A-S citation in Paper 5 §3.3-§3.4 (scoped here; extended by Phases 55, 57, 58).

---

_Locked at Phase 54-01 Task 3 (2026-04-16). Downstream attempt files and RESULT.md reference this lemma by name. Do not edit the lemma statement without a dated change-log entry and a cross-reference to the Phase 54 plan that authorized the edit._
