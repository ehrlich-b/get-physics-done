# Phase 55: S4 Facial Structure Lemma — Research

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; peirce_2_space=V_2(p_i):=range(C_{p_i}); peirce_1_space=V_1(p_i,p_j):=(C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V; as_2001=Alfsen-Shultz 2001 vol 179 (C*-algebra volume); as_2003=Alfsen-Shultz 2003 vol 190 (geometry of state spaces; compression theory Ch. 2/7/8); pre_jordan_boundary=A-S 2003 Ch. 1-8 (Ch. 9 is post-Jordan-illegal)

**Researched:** 2026-04-16
**Domain:** Operator-algebraic foundations of QM — order unit spaces (OUS), compressions, facial structure, Peirce decomposition, orthomodular lattices
**Research mode:** balanced
**Confidence:** HIGH (S4 classification pipeline, A-S/H-O/F-H literature landscape, forbidden-token discipline); MEDIUM (precise A-S 2003 Prop 7.43 text pending direct book verification); LOW (none — no novel physics here, this is a citation/argument audit)

---

## Summary

Phase 55 audits the S4 (orthogonality symmetry) argument in the two places where it lives in Paper 5: (a) the **main proof sketch** in `sections/axiom-verification.tex` §"S4 (Orthogonality Symmetry)" (lines 95-168), and (b) the **full detailed proof** in `sections/appendix-proofs.tex` §"Proof of S4 (Orthogonality Symmetry)" (lines 9-138, Theorem `thm:S4-full`). The roadmap's reference to "Paper 5 §3.3-§3.4, lines 483-712 of main-jmp-submitted.tex" is **imprecise**: lines 483-712 contain §3.3-§3.4 (sequential product derivation + mixing function), which consume the S4 axiom but do not contain the S4 proof itself. The S4 proof lives in the axiom-verification section and appendix; §3.3-§3.4 only touch S4 via cross-reference. Phase 55 therefore **extends scope** to both locations but does the bulk of its audit work on `axiom-verification.tex` + `appendix-proofs.tex`.

The current S4 argument (both in §S4 of axiom-verification.tex and in the appendix full proof) is a **mixed classification (ii) + (i)**: the rank-deficient Case B explicitly invokes the "Alfsen-Shultz **facial absorption theorem** (Proposition 7.43)" to place `b ∈ face(p_+^⊥)`, followed by an unstated "facial orthogonality theorem" for the reverse product. **Proposition 7.43 is a face-theoretic statement about compressions in A-S 2003 Ch. 7** (pre-Jordan-legal in principle), but the paper cites **Theorem 9.37 of A-S 2003** for the Peirce direct sum earlier — and Theorem 9.37 is **PRE-JORDAN-ILLEGAL** per Phase 54's ADDENDUM Finding 1 (Ch. 9 is the Jordan-state-space-characterization chapter). **The line-125 Thm 9.37 citation is the primary bug** and must be replaced; the Prop 7.43 citation is the primary verification target (number + statement must be confirmed).

**Primary recommendation:** Classify the current S4 argument as **mixed (i)/(ii) with (iii) lurking**: the Peirce direct sum step invokes A-S 2003 Thm 9.37 (ILLEGAL → must be replaced by the Phase 54 Peirce-Preservation Lemma + S0, or by A-S 2003 Ch. 7/8 compression theory), and the facial absorption step invokes Prop 7.43 (pre-Jordan-legal if the prop number is correct; must be verified). Draft the revision as **pre-Jordan-legal Case B via A-S 2003 Prop 7.43 (facial absorption) + Phase 54 S0 axiom (mutual compressional annihilation)**, replacing the Thm 9.37 invocation with the already-authored S0-based Peirce direct sum (Phase 54 deliverable). Do **not** introduce a Hanche-Olsen facial-symmetry argument at §S4 scope — H-O is post-Jordan-circular per Phase 54's R6 pitfall. The Foulis-Holland alternative (METHODS.md Method 4) is held as fallback only if Prop 7.43 cannot be pinned.

---

## User Constraints

No phase CONTEXT.md exists for Phase 55. The **roadmap section supplied in the orchestrator prompt is the effective contract slice** for this phase (state.json `project_contract` is stale per user standing guidance). Key constraints extracted:

- **Decisions (locked, from roadmap):**
  - Audit-and-revision scope: §3.3-§3.4 + (by necessity) `sections/axiom-verification.tex` §S4 + `sections/appendix-proofs.tex` §S4-proof.
  - Consistency with Phase 54 **SEALED (C-i)**: S0 axiom is authored in `preamble.sty` (via `\newtheorem{axiom}`); §3.3 revision is integrated into `main.tex`; every pre-sealing "it follows from Peirce..." must become "by S0, ..." in Phase 55's revision text.
  - Paper 5 frozen at git tag `paper5-jmp-submitted`; living edits go into `main.tex`, never into `main-jmp-submitted.tex`.
  - A-S volume discipline (locked): compression theory lives in **A-S 2003 vol 190 Ch. 2/7/8** (pre-Jordan-legal); Ch. 9 Thm 9.37 is **PRE-JORDAN-ILLEGAL** (R6 circularity). Never collapse 2001 + 2003 into bare `AlfsenShultz`; always `\cite[Ch. X, Prop Y.Z]{AlfsenShultz2003}`.
  - Forbidden tokens in pre-S4 revision text (R7 check): `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`.
  - Outcome (C) triggers milestone pause (backtracking rule).

- **Agent's discretion (freedom areas):**
  - Exact wording of the revision text replacing the Thm 9.37 invocation (substitute with S0 + Peirce-Preservation Lemma citation, but the transition paragraph is editorial).
  - Whether to embed the facial absorption statement inline or cross-reference appendix.
  - Whether Case B's "facial orthogonality theorem" gets its own cited Prop or is absorbed into Prop 7.43 application.

- **Deferred / out of scope:**
  - Phase 57 (φ-inertness) — noted as potential R11 restructuring coupling, not Phase 55 work.
  - Phase 58 (Lean axiom audit) — Prop 7.36 row (Flag 4.2 of alfsen-shultz-notes.md) is their work; Phase 55 only extends rows relevant to §3.3-§3.4 + §S4 + §S4-proof.
  - Extending to §3.5 (Circularity Check) — `alfsen-shultz-notes.md` already notes this is out of §3.3-§3.4 scope but flagged for Phase 55 extension if needed; recommendation is to include §3.5 only to the extent required to keep the revision consistent.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
|-------------------|------|---------------------|-----------------|------------------------|
| **Alfsen-Shultz 2003 vol 190** (Birkhäuser PM 190), *Geometry of State Spaces of Operator Algebras* | method reference (primary) | Compression theory + face theory; contains the Prop 7.43 facial absorption theorem; Ch. 9 Thm 9.37 is the **PRE-JORDAN-ILLEGAL** citation Paper 5 currently uses at line 125 of `axiom-verification.tex` | Extend `alfsen-shultz-notes.md` rows for each §S4/§S4-proof invocation; resolve Prop 7.43 (verify number + quote statement); re-resolve Thm 9.37 usage as REPLACE-WITH-S0 | plan, execution (revision text), verification (exit-gate grep) |
| **Alfsen-Shultz 2001 vol 179** (Birkhäuser PM 179), *State Spaces of Operator Algebras: Basic Theory, Orientations, and C\*-products* | disambiguation anchor | Paper 5 must never cite 2001 for compression theory; volume is C\*-algebra-flavored | Confirm no §S4/§S4-proof citation routes to 2001; if any, correct to 2003 | plan, execution |
| **Hanche-Olsen & Størmer 1984**, *Jordan Operator Algebras*, Pitman §2.1, §2.6 | forbidden anchor (post-Jordan) | H-O §2.6 Peirce decomposition is **post-Jordan-circular** at pre-S4 level; H-O §2.1.3 face-projection correspondence is a JB-algebra theorem (post-Jordan). METHODS.md Method 3 (H-O facial symmetry) is flagged "requires JB-structure; may be circular if invoked too early — CHECK phase ordering" | **Do not invoke at §S4 scope.** Document as R6 forbidden route in revision. If `axiom-verification.tex` or appendix has any H-O invocation (currently none detected), flag as R6 circularity | plan, revision verification |
| **van de Wetering 2019 JMP** arXiv:1803.11139 (cite key `vandeWetering2019b`), Def. 2 (S4 statement), Thm 1 (EJA classification), Thm 3 (LT → C\*) | S4-statement anchor | Paper 5 Definition 3.2 (line 267 of `main-jmp-submitted.tex`) cites vdW Def 2 for axioms S1-S7; S4 appears verbatim as "(S4) **Symmetry of orthogonality:** If `a ∘ b = 0` then `b ∘ a = 0`" | Keep as S4 statement source; do not re-derive | plan |
| **Foulis-Holland theorem** (Kalmbach 1983 Ch. 2 or Beran 1985) | fallback method | Pure orthomodular-lattice proof of S4 that avoids Jordan structure; METHODS.md Method 4 | Hold as fallback if Prop 7.43 cannot be verified AND S0-based Case A + facial rewrite cannot carry Case B | plan (fallback column), execution (if triggered) |
| **Paper 5 main-jmp-submitted.tex** at git tag `paper5-jmp-submitted` (frozen) | prior artifact (baseline) | Submitted text; must never be modified; lines 483-712 are the §3.3-§3.4 surface scope from the roadmap | Use as baseline for classification (compare revised `main.tex` + `sections/*.tex` against this); verify `git diff --stat HEAD -- main-jmp-submitted.tex` returns zero | execution, verification |
| **Paper 5 main.tex + sections/axiom-verification.tex + sections/appendix-proofs.tex** (living copies) | prior artifact (active) | Phase 54 already integrated S0 + Peirce-Preservation Lemma into main.tex §3.3 (lines 524-663); §S4 in axiom-verification.tex (lines 95-168) and §S4-proof in appendix-proofs.tex (lines 9-138) are the Phase 55 edit targets | Edit in-place; replace Thm 9.37 invocation with S0 + lem:peirce-preservation cross-ref; tighten Prop 7.43 citation with chapter + statement | execution |
| **Phase 54 `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md`** (SHARED, 256 lines) | prior artifact (carry-forward) | Already disambiguates A-S volumes; Flag 4.1 marks Thm 9.37 PRE-JORDAN-ILLEGAL; Flag 4.2 marks Prop 7.36 PROP-NUMBER-UNVERIFIED (Phase 58 scope, not 55); Section 5 axioms upgraded to VERIFIED-VIA-INTERNAL-CROSS-REFERENCE for Prop 7.23, Def 7.1, Prop 7.50 (Phase 54 NEW SCOPE item 2) | Extend with new rows for §S4 lines 125 (Thm 9.37 — REPLACE), 137 (Prop 7.43 — VERIFY), 154 ("facial orthogonality theorem" — RESOLVE-OR-DROP); add dated change-log entry | plan, execution (deliverable 2) |
| **Phase 54 `derivations/paper5-peirce-preservation/s0-axiom.md`** | prior artifact (S0 statement source) | S0 axiom at compression level: `C_{p_i} C_{p_j} = 0` for orthogonal i ≠ j. Canonical-example defenses (M_n(C)^sa, C(X), spin factors) scope-demarcated. Derivation of Peirce-Preservation Lemma (Parts i, ii, iii) | Cite as source of S0 when the §S4 revision replaces the Thm 9.37 invocation; S0 backs the Peirce direct sum at §S4 scope via the Remark that S0 gives `p_+ = Σ_{i ∈ I_+} p_i` with `C_{p_+} = Σ_{i ∈ I_+} C_{p_i}` on the support | plan, execution |
| **Phase 54 `main.tex` §3.3 integrated revision** (lines 524-663; commit `Phase 54 closure: revise §3.3 Peirce preservation with S0 axiom + lemma` + `Phase 54-03: rewrap Jordan meta-disclaimer in §3.3 proof (token discipline)`) | prior artifact (integration target template) | Pattern for how to integrate revision text into main.tex; Phase 55 follows the same pattern for `axiom-verification.tex` + `appendix-proofs.tex` | Use as template for edit mechanics; do not modify §3.3 itself | execution |
| **Phase 54 RESULT.md** SEALED **(C-i)** 2026-04-17 | prior artifact (outcome) | Locks the Phase 55 assumption set: `{S0, S1, S3, linearity, A-S compressions}` is the pre-Jordan-legal toolkit | Every §S4 / §S4-proof revision step must stay in this toolkit; any step requiring more flags a (C) outcome and milestone pause | plan, execution, verification |
| **Paper 5 `preamble.sty`** (Phase 54 authored `\newtheorem{axiom}`) | prior artifact (LaTeX scaffolding) | S0 is typeset via `\begin{axiom}[S0, Peirce Coherence (compression level)]...\end{axiom}` with `\label{ax:S0}` | Cross-reference `\ref{ax:S0}` from §S4 revision wherever "by S0, ..." replaces "by Peirce..." | execution |
| **Paper 5 `refs.bib`** cite keys | citation discipline | `AlfsenShultz2003` (line 168), `HancheOlsen1985` (line 51), `Niestegge2009` (line 215), `vandeWetering2019b` (inferred from main-jmp-submitted.tex line 147) | Use exact cite keys; verify bibkey before committing to revision text | execution |

**Missing or weak anchors:**

- **Direct A-S 2003 book text for Prop 7.43 statement** is QUOTE-PENDING. The executor (Phase 54 and this research) does not have the book on disk. Prop 7.43 is cited in Paper 5 `appendix-proofs.tex` line 79 with the *paraphrase* "If `C_p(b) = 0` and `b ≥ 0`, then `b ∈ face(p^⊥)`." Per `alfsen-shultz-notes.md` Section 5A, secondary-source verification via Niestegge 2010 (arXiv:1001.3633), Hanche-Olsen-Størmer 1984, or Jenčová-Pulmannová 2021 is preferred before physical book access. If all secondary routes fail, Phase 55 must carry a **VERIFICATION-DEFERRED** flag on Prop 7.43 with a dated research TODO.
- **"Facial orthogonality theorem"** invoked at `axiom-verification.tex` line 154 and `appendix-proofs.tex` line 108 is **unnamed in the Paper 5 text** — no Prop/Thm number is given. This is the ambiguity Phase 55 must resolve: either (a) the intended theorem is A-S 2003 Prop 7.43 specialized to the complementary face (so the same citation covers both invocations), (b) a distinct A-S 2003 Ch. 7/8 result is needed (identify it), or (c) the step is derivable from the Phase 54 S0 axiom + A-S Prop 7.50 (orthogonal projective units have trivial meet → mutual compressional annihilation → the reverse product `C_{q_j}(a) = 0` follows from S0 termwise). Option (c) is the pre-Jordan-legal recommended route.
- **Niestegge 2010 / Niestegge 2009** (cite key `Niestegge2009` in refs.bib) sequential-product treatment at pre-Jordan level — if it states S4 explicitly with an A-S cite, that is additional backing. `alfsen-shultz-notes.md` Section 5A names Niestegge 2008 (arXiv:1001.3633) and Niestegge 2009 as secondary-source verification candidates.

---

## Conventions

| Choice | Convention | Alternatives | Source |
|--------|-----------|--------------|--------|
| Sequential product | `a ∘ b`, written `\seqp{a}{b}` in LaTeX (Paper 5 notation) | `a · b`, `a; b` | Paper 5 Definition 3.2 / vdW 2019 Def 2 |
| Compression | `C_p`, written `\comp{p}` in LaTeX | `P_p`, `U_p` (Niestegge), `[p]` | Paper 5 §2; A-S 2003 Ch. 7 Def 7.1 |
| Peirce 2-space | `V_2(p_i) := range(C_{p_i})` | `p_i V p_i` (Jordan notation, post-Jordan-illegal here) | Phase 54 s0-axiom.md |
| Peirce 1-space | `V_1(p_i, p_j) := (C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V` | `p_i V p_j + p_j V p_i` (Jordan, post-Jordan-illegal) | Phase 54 s0-axiom.md |
| Orthogonal family | `{p_1, …, p_n}` with `p_i ⊥ p_j` for i ≠ j | — | vdW 2019 Def 2; Paper 5 §2 |
| S0 axiom | `C_{p_i} C_{p_j} = 0` for i ≠ j in orthogonal family | pairwise commutation (weaker; implied by S0); `C_p ∘ C_q = C_{p ∧ q}` via A-S Prop 7.50 (equivalent for face-disjoint pairs) | Phase 54 s0-axiom.md; main.tex lines 534-545 |
| A-S volume shorthand | "A-S 2003" = Birkhäuser PM 190; "A-S 2001" = Birkhäuser PM 179 | Never bare "A-S" or "Alfsen-Shultz" | Phase 54 alfsen-shultz-notes.md convention block |
| Pre-Jordan boundary | A-S 2003 Ch. 1-8 pre-Jordan-legal; Ch. 9 post-Jordan-illegal | — | Phase 54 alfsen-shultz-notes.md Flag 4.1 + ADDENDUM Finding 1 |
| Forbidden tokens (pre-S4 revision text) | `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a` — grep must return zero hits | canonical-example defenses may use these inside `% BEGIN ... % END` markers | Phase 54 R7 pitfall |

**CRITICAL:** All equations and results below use these conventions. The S4 revision text must preserve them verbatim. Any deviation requires a CUSTOM_CONVENTION block in the RESULT.md.

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in Phase 55 |
|----------|------------------|--------|------------------|
| `a ∘ b = 0 ⟹ b ∘ a = 0` | S4 (Orthogonality symmetry) | vdW 2019 Def 2 item S4 / Paper 5 main-jmp-submitted.tex line 283 (`\label{ax:S4}`) | Target property — must be proved under the corrected product |
| `seqp{a}{b} = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} f(λ_i,λ_j) P_{ij}(b)` | Corrected product (eq `corrected-product`) | Paper 5 main.tex line 667 / main-jmp-submitted.tex line 668 (`\eqref{eq:corrected-product}`) | Base product in the S4 proof; f = √(λ_i λ_j) |
| `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i, p_j)` | Peirce direct sum | Paper 5 `\eqref{eq:peirce-proj}`; **currently miscited as A-S 2003 Thm 9.37 at axiom-verification.tex line 125** | Must be re-cited to S0 + Peirce-Preservation Lemma (Phase 54) rather than Thm 9.37 |
| `C_p(b) = 0 ∧ b ≥ 0 ⟹ b ∈ face(p^⊥)` | A-S facial absorption theorem | A-S 2003 Prop 7.43 (cited at appendix-proofs.tex line 79; **VERIFICATION-DEFERRED**) | Case B step that places `b ∈ face(p_+^⊥)`; pre-Jordan-legal if Prop 7.43 confirmed |
| `C_{p_i} C_{p_j} = 0` for i ≠ j in orthogonal family | S0 (Peirce coherence) | Phase 54 `s0-axiom.md` §2 / main.tex line 537-545 `\begin{axiom}[S0]` | Backs the Peirce direct sum without invoking Thm 9.37; enables "p_+ = Σ_{i ∈ I_+} p_i with C_{p_+} = Σ C_{p_i} on support" |
| `C_p ∘ C_q = C_{p ∧ q}` for compatible projective units | A-S Prop 7.50 (compression composition) | A-S 2003 Prop 7.50 (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Alternative route to the S0 annihilation (orthogonal ⟹ trivial meet ⟹ `C_p ∘ C_q = 0`); pre-Jordan-legal |
| `C_p^2 = C_p` and `C_p ≥ 0` | A-S idempotency + positivity | A-S 2003 Prop 7.23 (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Used in Case A diagonal vanishing and in the Preliminary Lemma for V_1 |
| `C_p(1) = p` | A-S projector fix | A-S 2003 Def 7.1 (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Used in linking `C_{p_+}` to support structure |
| `f(0, x) = 0` | Mixing function vanishing at zero | Paper 5 Cor `cor:S4-phi-indep` / appendix-proofs.tex line 124 | Key φ-independence hook; S4 holds for any f with this vanishing |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
|-----------|-------------|---------------|--------------------|
| **Peirce decomposition expansion** | Writes `V = ⊕ V_2(p_i) ⊕ ⊕ V_1(p_i, p_j)` and equates zero-sum to component-wise zero | Case A and Case B opening (appendix-proofs.tex lines 37-49) | Phase 54 Peirce-Preservation Lemma + S0; NOT A-S Thm 9.37 |
| **Rank partitioning** | Split spectral indices of `a` into `I_+ = {i : λ_i > 0}` and `I_0 = {i : λ_i = 0}` | Case B preamble (line 69-76) | Standard spectral-calculus technique |
| **Facial absorption** | `C_p(b) = 0 ∧ b ≥ 0` places b in `face(p^⊥)` | Case B key step (line 78-91) | A-S 2003 Prop 7.43 (verify) |
| **Support-projection argument** | Define `p_+ = Σ_{i ∈ I_+} p_i` as support of `a`; use `C_{p_+} = Σ_{i ∈ I_+} C_{p_i}` via S0 / compression-additivity on orthogonal pairs | Case B, post-absorption (line 85-91) | Phase 54 S0 + A-S compression-additivity |
| **Facial orthogonality** | b ∈ face(p_+^⊥) and a supported on face(p_+) ⟹ `C_{q_j}(a) = 0` for every spectral projector q_j of b with μ_j > 0 | Case B reverse product (line 106-114) | A-S 2003 Prop 7.43 specialized to complementary faces, OR S0 termwise; **currently unnamed — must be resolved** |
| **φ-independence via f(0, x) = 0 abstraction** | Prove S4 depends only on mixing function's vanishing at zero, not its form | Corollary `cor:S4-phi-indep` (appendix-proofs.tex lines 121-137) | Paper 5 internal; already correct post-Phase 54 |

### Approximation Schemes

N/A — this is a pure-algebra audit on finite-dim archimedean OUS. No approximation, no small parameter, no regime of validity beyond "finite-dim spectral OUS." Every technique holds exactly.

---

## Standard Approaches

### Approach 1: S0 + A-S Prop 7.43 (RECOMMENDED; pre-Jordan-legal)

**What:** Replace the Thm 9.37 invocation for the Peirce direct sum with a citation to the Phase 54 Peirce-Preservation Lemma (backed by S0 axiom). Keep the A-S Prop 7.43 facial absorption citation but verify the Prop number and transcribe the exact statement. Resolve the "facial orthogonality theorem" at `axiom-verification.tex` line 154 and `appendix-proofs.tex` line 108 as either (a) Prop 7.43 specialized to the complementary face, or (b) S0 termwise (`C_{p_j}(b) = 0` for all j ∈ I_+ combined with the support structure on `a`).

**Why standard:** Matches the Phase 54 (C-i) SEALED outcome. S0 is already authored in `preamble.sty` and integrated into `main.tex`. The Peirce-Preservation Lemma is already stated with `\label{lem:peirce-preservation}` and proved. All that remains is to thread the citation through §S4 + §S4-proof. Prop 7.43 in A-S 2003 Ch. 7 is pre-Jordan-legal (Ch. 1-8 boundary per Phase 54 ADDENDUM). The whole chain stays in the `{S0, S1, S3, linearity, A-S compressions}` allowed-tool scope.

**Track record:** Phase 54 closed (C-i) with a PASSES-WITH-CAVEATS adversarial review; the identical S0-based pattern works for Phase 55 by construction (the S4 proof consumes the same Peirce structure §3.3 proves).

**Key steps (revision-text skeleton):**

1. **Case A opening** (axiom-verification.tex line 120-130 / appendix-proofs.tex line 52-64):
   - Replace the bare Peirce direct sum invocation at line 125 (`(Alfsen-Shultz\cite{AlfsenShultz2003}, Theorem~9.37)`) with: "`by Lemma~\ref{lem:peirce-preservation} (Peirce-Preservation Lemma, §3.3) together with the Peirce direct sum structure from A-S compressions (Alfsen-Shultz\cite[Ch.~7, Prop.~7.23 + Prop.~7.50]{AlfsenShultz2003})`" or more concisely: "`by axiom~\ref{ax:S0} (§3.3)`".
   - Note: Paper 5 main.tex line 537-545 has `\begin{axiom}[S0]` with `\label{ax:S0}` already in scope after Phase 54.

2. **Case B facial absorption** (axiom-verification.tex line 136-141 / appendix-proofs.tex line 78-91):
   - Keep `\cite[Prop.~7.43]{AlfsenShultz2003}` but verify the Prop number and add the exact-statement quote as a blockquote (already present in both files).
   - Add a parenthetical pointing to alfsen-shultz-notes.md for the volume + chapter + section resolution: "`(A-S 2003 vol.~190, Ch.~7; see ancillary citation audit for exact statement)`" — or if alfsen-shultz-notes.md closes the VERIFICATION-DEFERRED row with a book-text quote, inline the quote verbatim.

3. **Case B support-projection step** (appendix-proofs.tex line 85-91):
   - Add explicit S0 citation for "`compressions for orthogonal projective units act independently on their respective faces`" — this is exactly S0: `C_{p_i} C_{p_j} = 0` for i ≠ j. Cross-reference as `\ref{ax:S0}` or `\cite[Prop.~7.50]{AlfsenShultz2003}` (equivalent routes).

4. **Case B facial orthogonality** (axiom-verification.tex line 154 / appendix-proofs.tex line 106-114):
   - Replace unnamed "facial orthogonality theorem" with explicit citation. Primary option: cite A-S 2003 Prop 7.43 again, specialized to the complementary face: "`since q_j ≤ p_+^⊥ and a is supported on face(p_+), the facial absorption theorem (Alfsen-Shultz\cite[Prop.~7.43]{AlfsenShultz2003}) applied in reverse gives C_{q_j}(a) = 0`". Alternative: derive directly from S0 termwise (since every spectral projector `p_i` with i ∈ I_+ has `p_i ≤ p_+`, and `q_j ≤ p_+^⊥` gives `p_i ⊥ q_j`, so S0 gives `C_{q_j}(p_i) = 0`, and by linearity `C_{q_j}(a) = Σ_i λ_i C_{q_j}(p_i) = 0`).
   - **Recommended:** use S0-termwise derivation; it is more direct, does not require a second Prop 7.43 invocation, and keeps the argument in the Phase 54 toolkit.

5. **Peirce 1-space cross-terms `Q_{jk}(a)`** (axiom-verification.tex line 155-157 / appendix-proofs.tex line 109-113):
   - The current text says these "vanish by facial structure (when both μ_j, μ_k > 0)." This is another unnamed facial-structure appeal. Replace with: "`by the Peirce-Preservation Lemma Part (iii) (R3 cross-term case, §3.3) applied to a's spectral decomposition: since both q_j, q_k ≤ p_+^⊥ and supp(a) ⊆ I_+, we have {q_j, q_k} ∩ supp(a) = ∅, so a ∘ v = 0 for v ∈ V_1(q_j, q_k)` (Part (iii) gives stronger: annihilation, hence Q_{jk}(a) = 0)."
   - **Cross-coupling with Phase 54 deliverable:** Part (iii) of the Peirce-Preservation Lemma (the "R3 cross-term case") was authored specifically for this kind of invocation in §S4. See main.tex lines 641-644.

6. **`alfsen-shultz-notes.md` extension** (deliverable 2 from roadmap):
   - Add rows for: `axiom-verification.tex` line 125 (Thm 9.37 — CLASSIFICATION: REPLACED-WITH-S0); line 137 (Prop 7.43 — Ch. 7 pre-Jordan-legal, VERIFICATION-DEFERRED if book not accessed); line 180 (Prop 7.49); line 228 (Prop 7.49 again); line 232 (Prop 7.50, already VERIFIED-VIA-INTERNAL-CROSS-REFERENCE in Phase 54); line 321 (Prop 7.50 again).
   - Add rows for: `appendix-proofs.tex` line 79 (Prop 7.43 — same as line 137 of axiom-verification.tex).
   - Dated change-log entry: `2026-04-16 (Phase 55 extension): added rows for §S4 axiom-verification.tex + §S4-proof appendix-proofs.tex; Thm 9.37 invocations replaced by S0 + Peirce-Preservation Lemma; Prop 7.43 verification status [VERIFIED/VERIFICATION-DEFERRED depending on secondary-source access].`

**Known difficulties at each step:**

- **Step 1:** The text at axiom-verification.tex line 125 is currently inside a `\begin{proof}[Proof sketch]` that is itself inside `\begin{theorem}\label{thm:S4}`. Editing in-place must preserve the theorem statement and the proof sketch's overall structure; only the citation changes. Parallel edit required at appendix-proofs.tex line 37-49 (the `\begin{theorem}\label{thm:S4-full}` block) — but appendix-proofs.tex does not cite Thm 9.37 directly; it cites `\eqref{eq:peirce-proj}` (the Peirce-projection equation). The Thm 9.37 citation is only in axiom-verification.tex.
- **Step 2:** If Prop 7.43 is renumbered in later A-S 2003 printings (unlikely but possible), the citation breaks. Mitigation: verify against the first-edition A-S 2003 (ISBN 978-0-8176-4319-8).
- **Step 3:** The S0 citation is typeset via `\ref{ax:S0}` — must verify this label resolves to main.tex §3.3, not to a duplicate definition. Phase 54's main.tex has `\label{ax:S0}` at line 540; check no collision with axiom-verification.tex.
- **Step 4:** The S0-termwise derivation requires `C_{q_j}(p_i) = 0` for `q_j ≤ p_+^⊥` and `p_i ≤ p_+`. This needs `q_j ⊥ p_i` in the projective-unit sense, which follows from the face-inclusion `q_j ≤ p_+^⊥` and the complementary-face fact `face(p_+) ∩ face(p_+^⊥) = {0}`. If this chain cannot be made explicit with pre-Jordan A-S citations, fall back to direct Prop 7.43 application.
- **Step 5:** The Peirce-Preservation Lemma Part (iii) is about `L_a(V_1(p_k, p_l))` where the Peirce 1-space is with respect to **a's** spectral projectors. In the S4 argument, the Peirce 1-space `V_1(q_j, q_k)` is with respect to **b's** spectral projectors. The Part (iii) invocation must swap roles: `b = Σ_j μ_j q_j` is the "a" of Part (iii), and `a = Σ_i λ_i p_i` is the "b". This role-swap is licit (Part (iii) does not distinguish the roles; it is a statement about the left-multiplication map applied to a Peirce 1-space of an orthogonal family). But the revision text must be explicit about this or the referee will flag it.
- **Step 6:** alfsen-shultz-notes.md is a SHARED artifact. Phase 55 extension must not silently overwrite existing rows. Always append with dated change-log entry.

### Approach 2: Foulis-Holland alternative (FALLBACK)

**What:** Prove S4 via the Foulis-Holland theorem on orthomodular lattices: in the projection lattice of a spectral OUS, if `a ⊥ b` means `a ≤ b'` (order-theoretic), the orthomodular law gives `a ≤ b' ⟺ b ≤ a'`, so `a ⊥ b ⟺ b ⊥ a`.

**When to switch:** If A-S 2003 Prop 7.43 cannot be pinned (verification fails in all secondary-source attempts AND direct book access is infeasible within Phase 55 timeline), fall back to F-H for Case B.

**Tradeoffs:**
- **Gain:** Avoids any A-S 2003 Ch. 7 citation beyond what Phase 54 already verified (Prop 7.23, Def 7.1, Prop 7.50). Pure order-theoretic.
- **Lose:** Requires Paper 5's effect algebra to embed into an orthomodular lattice via sharp elements. METHODS.md Method 4 notes this is automatic for sharp-effect subspaces (`P_e^{0,1}` consists of sharp effects by construction), but the §S4 proof is stated for **all** effects `a, b ∈ eff(V)`, not just sharp ones. F-H applies directly to the **sharp** effects; the mixing function `f(0, x) = 0` then carries the non-sharp case.
- **Extra work:** Must state the F-H theorem in the revision text (or cite Kalmbach 1983) and verify the orthomodular-lattice embedding for the specific OUS framework used by Paper 5. Adds ~20 lines vs. Approach 1's ~5 lines of citation edits.
- **Risk:** F-H is in the METHODS.md method list but was not used in Phase 54; Phase 55 would be the first to invoke it. Independent verification load is higher.

**Decision criterion:** Approach 2 triggered only if secondary-source verification of Prop 7.43 fails AND Bryan confirms no physical A-S 2003 access is available within the phase window.

### Anti-Patterns to Avoid

- **Hanche-Olsen §2.6 Peirce decomposition at pre-S4 scope (R6 circularity):** H-O develops Peirce decomposition for **unital Jordan algebras**. Invoking it at §S4 is post-Jordan: the very axiom (S4) is what Paper 5 is proving in order to apply vdW Thm 1 and promote OUS to EJA. If §S4's proof of S4 invokes H-O Peirce, the derivation chain is circular.
  - _Example:_ "By Hanche-Olsen-Størmer Prop 2.6.3 the Peirce decomposition is respected..." — **DO NOT WRITE THIS.** Cite A-S 2003 Ch. 7 (compression-theoretic Peirce, pre-Jordan) or the Phase 54 Peirce-Preservation Lemma instead.

- **Bare `\cite{AlfsenShultz2003}` without chapter/prop:** R5 pitfall from PITFALLS.md. The referee will flag it. Worse, it leaves ambiguity between Ch. 1-8 (pre-Jordan-legal) and Ch. 9 (post-Jordan-illegal).
  - _Example:_ "(Alfsen-Shultz, facial structure)" — **MUST BE** "(Alfsen-Shultz 2003, Ch. 7, Prop. 7.43)".

- **Collapsing A-S 2001 + A-S 2003 into bare "Alfsen-Shultz":** The two volumes have different content; 2001 is C\*-algebraic, 2003 is geometric/compression-theoretic. Phase 54 already corrected "A-S 2001 Ch. 7-8 compression axioms" → "A-S 2003 Ch. 2/7/8". Do not re-introduce the misattribution.

- **"By facial structure..." without a theorem number:** R6 pitfall — hand-wave invocation of facial geometry is exactly where Jordan-structure can sneak in. Every facial-structure appeal needs either an A-S Prop/Thm or an S0 + compression derivation.

- **Invoking Thm 9.37 anywhere pre-S4:** Thm 9.37 lives in A-S 2003 Ch. 9 (Jordan state-space characterization) — post-Jordan-illegal per Phase 54 Flag 4.1. The current `axiom-verification.tex` line 125 citation to Thm 9.37 is exactly this pitfall and is the primary bug Phase 55 fixes.

- **Rederiving the Peirce-Preservation Lemma in §S4:** Phase 54 already proved it. Phase 55 cites `\ref{lem:peirce-preservation}` and `\ref{ax:S0}`; it does not reprove.

- **Editing `main-jmp-submitted.tex`:** The submitted file is frozen at git tag `paper5-jmp-submitted`. All edits go into `main.tex` + `sections/*.tex`. Verify zero diff on `main-jmp-submitted.tex` at close.

---

## Existing Results to Leverage

**This section is MANDATORY.** List results the executor should CITE rather than re-derive. Prevents wasting context budget on textbook results. The planner uses this to scope task effort.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
|--------|-----------|--------|------------|
| **S0 axiom (Peirce coherence, compression level)** | `C_{p_i} C_{p_j} = 0` for orthogonal projective units i ≠ j | Phase 54 main.tex lines 537-545 `\begin{axiom}[S0]` with `\label{ax:S0}` | Backs every "Peirce direct sum" and "facial orthogonality" step that previously invoked Thm 9.37 or unnamed facial theorems |
| **Peirce-Preservation Lemma** | Parts (i), (ii), (iii) giving V_2-invariance, V_1 on-support case, V_1 off-support R3 cross-term case | Phase 54 main.tex lines 590-612 `\begin{lemma}[Peirce-Preservation Lemma]\label{lem:peirce-preservation}` | Cited in §S4 Case B support-projection step (Part (iii) handles the off-support cross-term exactly) |
| **A-S idempotency + positivity** | `C_p^2 = C_p` and `C_p ≥ 0` | A-S 2003 Prop 7.23 (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Case A component-wise vanishing; Preliminary Lemma |
| **A-S projector fix** | `C_p(1) = p` | A-S 2003 Def 7.1 (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Support structure in Case B |
| **A-S compression composition for compatible pairs** | `C_p ∘ C_q = C_{p ∧ q}` | A-S 2003 Prop 7.50 (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) | Backs S0 (orthogonal pairs have trivial meet); alternative route to mutual annihilation |
| **A-S facial absorption theorem** | `C_p(b) = 0 ∧ b ≥ 0 ⟹ b ∈ face(p^⊥)` | A-S 2003 Prop 7.43 (VERIFICATION-DEFERRED; quoted in `appendix-proofs.tex` line 79-84) | Case B key step placing b in complementary face; must be verified in Phase 55 |
| **Peirce direct sum** (pre-Jordan form) | `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i, p_j)` as A-S compression-theoretic decomposition | Derivable from S0 + A-S compression additivity; currently miscited as A-S Thm 9.37 | Rewrite as derived from S0 + A-S Ch. 7 compression theory, not from Ch. 9 Thm 9.37 |
| **vdW 2019 Def 2 S4 statement** | "If `a ∘ b = 0` then `b ∘ a = 0`" (S4 verbatim) | vdW 2019 arXiv:1803.11139 Def 2 / cite `vandeWetering2019b`; Paper 5 main-jmp-submitted.tex line 283 | S4 statement source; never re-define S4 |
| **φ-independence of S4 (Corollary cor:S4-phi-indep)** | S4 holds for any mixing function f with f(0, x) = 0, not only for √(λ_i λ_j) | Paper 5 appendix-proofs.tex lines 121-137 | Keep verbatim; already correct and consistent with Phase 54 |
| **Phase 54 (C-i) outcome tag** | Allowed-axiom scope `{S0, S1, S3, linearity, A-S compression axioms, finite-dim spectrality}` | `.gpd/phases/54-.../54-RESULT.md` §1-3 | Every Phase 55 revision step must stay in this scope |

**Key insight:** The S4 proof is a specialized application of Peirce structure, which Phase 54 already formalized. Phase 55's work is **~90% citation surgery and ~10% new content** (the "new content" is the S0-termwise derivation in Step 4 of the recommended approach, which replaces the unnamed "facial orthogonality theorem"). Do not re-prove the Peirce direct sum, the compression axioms, or the Peirce-Preservation Lemma.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
|--------|-------------------|--------|------------|
| **Orthogonal pairs have trivial meet** | For orthogonal projective units p_i, p_j: `p_i ∧ p_j = 0` | Face-disjointness of orthogonal projective units; standard in A-S compression theory | Holds in any spectral OUS with projective-unit face lattice |
| **Mixing function vanishing** | `f(0, x) = 0` for the φ-independent S4 proof | Paper 5 `\eqref{eq:faithful-f}` specialized to λ_i = 0 | Holds for `f = √(λ_i λ_j)` and any f with f(0, x) = 0 |
| **Support projection** | `p_+ := Σ_{i ∈ I_+} p_i` with `p_+ ≤ 1` | Construction in Case B; uses orthogonality of {p_i} | In a spectral OUS with spectral decomposition |
| **Complementary face** | `face(p_+^⊥) = face(Σ_{i ∈ I_0} p_i)` | Complement-face fact; pre-Jordan-legal in A-S Ch. 7 | A-S Ch. 7 compression-face correspondence |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
|-------------|---------|------|-----------|------------------|
| **vdW 2019 JMP** (arXiv:1803.11139) | van de Wetering | 2019 | S4 statement source; Thm 1 (EJA classification) | S4 statement verbatim; cite key `vandeWetering2019b` |
| **A-S 2003** (Birkhäuser PM 190) | Alfsen, Shultz | 2003 | Compression theory Ch. 2/7/8; facial absorption Prop 7.43; Thm 9.37 ILLEGAL | Prop 7.43 statement (verify); Prop 7.23, Def 7.1, Prop 7.50 (already verified Phase 54) |
| **A-S 2001** (Birkhäuser PM 179) | Alfsen, Shultz | 2001 | Disambiguation anchor; NOT the source for compression theory | Confirm no Phase 55 citation routes to 2001 |
| **Hanche-Olsen & Størmer 1984** | Hanche-Olsen, Størmer | 1984 | Post-Jordan; §2.6 Peirce; §2.1 face-projection (JB-algebra context) | Do not invoke at pre-S4 scope; note in anti-patterns |
| **Niestegge 2009** (cite key `Niestegge2009`) | Niestegge | 2009 | Pre-Jordan U_e compression framework; secondary-source candidate for Prop 7.43 verification | If Prop 7.43 equivalent appears, cite as secondary verification |
| **Foulis-Holland theorem / Kalmbach 1983** | Foulis, Holland / Kalmbach | 1961-65 / 1983 | Pure order-theoretic S4 alternative (fallback) | Hold as Approach 2 fallback |
| **Jenčová-Pulmannová 2021** (arXiv:2102.01628) | Jenčová, Pulmannová | 2021 | Comparison paper for OUS spectrality; Phase 54 ADDENDUM Finding 2 confirms Peirce is post-Jordan in their treatment | Secondary verification candidate only |
| **Paper 5 submitted** at tag `paper5-jmp-submitted` | Ehrlich | 2026 | Frozen baseline for classification | Line numbers 483-712 + axiom-verification.tex §S4 + appendix-proofs.tex §S4-proof |

---

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
|------|----------------|---------|--------------|
| **grep / ripgrep** | any | Citation inventory, forbidden-token grep, line-range extraction | Standard; the Phase 54 exit gate already uses this pattern |
| **git** | any | Verify `main-jmp-submitted.tex` unchanged (`git diff --stat HEAD -- main-jmp-submitted.tex` → 0); track living edits in `main.tex` and `sections/*.tex` | Phase 54 uses this pattern |
| **LaTeX / pdflatex** (via blog repo Hugo build) | existing project toolchain | Compile revised Paper 5 to verify no broken cross-references (`\ref{ax:S0}`, `\ref{lem:peirce-preservation}`, `\ref{thm:S4}`, `\ref{thm:S4-full}`) | Standard |
| **SymPy (optional validation)** | 1.12+ | Spot-check the S4 claim numerically on `H_3(ℝ)` or `H_4(ℝ)` using Phase 54's `closeout-sympy.py` pattern | Phase 54 closeout-sympy.py establishes the template |

### Supporting Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Zotero / BibTeX** | Verify cite keys `AlfsenShultz2003`, `HancheOlsen1985`, `Niestegge2009`, `vandeWetering2019b` against refs.bib | Before committing revision text |
| **SymPy H_n(ℝ) spot-check** | Numerical verification of S4 on small matrix algebras | Optional validation if time permits |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| grep for citation audit | Full LaTeX parser (e.g., plasTeX) | Parser gives structured output but is overkill for 1-2 file audit |
| SymPy spot-check | Pure pen-and-paper verification | SymPy catches typos in lambda/p indices; Phase 54 precedent supports it |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
|-------------|----------------|------------|------------|
| Citation inventory (§S4 + §S4-proof) | < 30 sec | grep runtime (negligible) | — |
| Revision text drafting | ~1 hour | Manual; no computation | — |
| SymPy S4 spot-check | < 10 sec runtime | Already templated from Phase 54 | Reuse Phase 54 closeout-sympy pattern |
| LaTeX compile | < 30 sec | Blog repo toolchain | Standard |
| alfsen-shultz-notes.md extension | ~30 min | Manual row addition | Use Phase 54 row schema verbatim |

**Installation / Setup:**
```bash
# All tools already available in the project toolchain; no new installation required.
# Verify availability:
which grep git pdflatex python3
python3 -c "import sympy; print(sympy.__version__)"  # optional
```

---

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
|-------|-------------------|----------------|-----------------|
| **Forbidden-token grep** | No Jordan-structure leakage in pre-S4 revision text (R7) | `grep -E 'Jordan\|EJA\|Lüders\|L.ders\|pxp\|sqrt.?a.?b.?sqrt.?a' sections/axiom-verification.tex sections/appendix-proofs.tex \| grep -v '% BEGIN canonical-example.*% END'` after revision | Zero hits outside demarcated scopes |
| **Submitted-file frozen check** | `main-jmp-submitted.tex` unchanged | `git -C ~/repos/blog diff --stat HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` | Zero changes |
| **Thm 9.37 grep** | No remaining Thm 9.37 invocation at pre-S4 scope | `grep -n "Theorem.*9\.37\|Thm.*9\.37" sections/axiom-verification.tex sections/appendix-proofs.tex main.tex` | Zero hits in §3.3-§3.5 + §S4 + §S4-proof (Thm 9.37 may still appear in §S4-independent contexts only if they are post-Jordan; currently none expected) |
| **Bare AlfsenShultz2003 grep** | No bare citation without chapter/prop in §S4 + §S4-proof scope | `grep -n '\\\\cite{AlfsenShultz2003}' sections/axiom-verification.tex sections/appendix-proofs.tex \| grep -v 'Ch\\.\\|Prop\\.\\|Thm\\.\\|Def\\.'` | Zero bare cites |
| **Cross-reference resolution** | `\ref{ax:S0}`, `\ref{lem:peirce-preservation}`, `\ref{thm:S4}`, `\ref{thm:S4-full}` resolve | LaTeX compile log; `grep -E '\?\?\|undefined' main.log` | Zero undefined references |
| **alfsen-shultz-notes.md row count** | Phase 55 extension added new rows without modifying existing | Diff against pre-Phase-55 commit; count new rows | >= 4 new rows (Thm 9.37 REPLACE, Prop 7.43 VERIFY, "facial orthogonality" RESOLVE, Prop 7.49/7.50 duplicates) |
| **S0 + Peirce-Preservation Lemma usage** | Revision text cites `\ref{ax:S0}` and/or `\ref{lem:peirce-preservation}` at each site that previously invoked Thm 9.37 or unnamed facial structure | `grep -c 'ax:S0\\|lem:peirce-preservation' sections/axiom-verification.tex sections/appendix-proofs.tex` | >= 2 hits per file |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
|-------|------------------|--------------|--------|
| **Abelian OUS limit** (V_1 = {0}) | Commutative C(X) case | S4 is trivial: a ∘ b = a · b (pointwise), so a · b = 0 ⟹ b · a = 0 | Standard; METHODS.md Method 3 commentary |
| **M_n(ℂ)^sa limit** | Self-adjoint matrix algebra | S4 follows from Lüders product: `√a b √a = 0` ⟹ `supp(b) ⊆ ker(a)` ⟹ `√b a √b = 0`. The Phase 55 proof at pre-Jordan level should recover this as a special case | Standard; canonical-example defense scope only |
| **Spin factor case** | Clifford-generated OUS | S4 holds via facial orthogonality (two rank-1 projective units are either identical or disjoint) | Phase 54 s0-axiom.md canonical-example defense |
| **V_2-only case** (b ∈ V_2(p_i)) | When b is supported on a single Peirce 2-space | S4 reduces to Case A and is immediate | Paper 5 Case A |

**Sanity anchor:** The revised Phase 55 S4 proof must recover the M_n(ℂ)^sa standard result when specialized to that model. If not, something is wrong. Verify via Phase 54's closeout-sympy.py pattern extended to test S4 on `H_3(ℝ)` or `H_4(ℝ)`.

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
|------|--------|-----------|-----------------|
| **S4 spot-check on H_3(ℝ)** | Construct `a = diag(λ_1, λ_2, 0)` and `b` orthogonal to face(p_1 + p_2); verify `a ∘ b = 0 ⟹ b ∘ a = 0` | Exact (symbolic) | 0 |
| **S4 on H_4(ℝ) with rank-deficient a** | `a = diag(λ_1, λ_2, 0, 0)`, `b = diag(0, 0, μ_1, μ_2) + off-diagonal in V_1(p_3, p_4)`; verify both directions annihilate | Exact (symbolic) | 0 |
| **Case A full-rank** | `a = diag(λ_1, λ_2, λ_3)` all positive; verify `a ∘ b = 0 ⟹ b = 0 ⟹ b ∘ a = 0` trivially | Exact | 0 |
| **φ-independence** | Replace `f = √(λ_i λ_j)` with alternative `f` having `f(0, x) = 0` (e.g., `f = λ_i λ_j`); verify S4 still holds | Exact | 0 |

### Red Flags During Computation

- **A Thm 9.37 citation remains in the pre-S4 revision text** → R6 circularity violation; stop and replace.
- **A bare `\cite{AlfsenShultz2003}` appears without chapter/prop** → R5 violation; tighten citation.
- **Forbidden token (`Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`) appears outside demarcated canonical-example scope** → R7 violation; rewrap or rewrite.
- **`\ref{ax:S0}` or `\ref{lem:peirce-preservation}` unresolved at LaTeX compile** → Phase 54 integration broke or labels collided; investigate.
- **`main-jmp-submitted.tex` shows diff** → frozen-file discipline violated; revert immediately.
- **alfsen-shultz-notes.md row modified without change-log entry** → shared-artifact discipline violated; add dated entry.
- **SymPy H_n(ℝ) spot-check returns non-zero** → S4 revision has a bug; compare against Phase 54 closeout-sympy.py pattern.

---

## Common Pitfalls

### Pitfall 1: Invoking Hanche-Olsen facial structure at pre-S4 scope (R6 circularity)

**What goes wrong:** H-O §2.6 (Peirce) and §2.1 (face-projection correspondence) are Jordan-algebra theorems. The whole point of S4 is to promote OUS → EJA via vdW Thm 1 — so invoking JB-algebra structure at §S4 is circular.

**Why it happens:** METHODS.md Method 3 lists H-O facial symmetry as a Phase 55 method; a careless reader may reach for it without noticing the "CHECK phase ordering" caveat.

**How to avoid:** **Do not cite Hanche-Olsen anywhere in the §S4 revision text.** Use A-S 2003 Ch. 7 compression theory or the Phase 54 S0 axiom. Add `Hanche-Olsen` to the pre-S4 forbidden-token list for Phase 55's grep check.

**Warning signs:** Revision draft contains "Hanche-Olsen", "JB-algebra", "Jordan operator algebra" outside demarcated scope.

**Recovery:** Replace H-O invocation with either Phase 54 Peirce-Preservation Lemma (for Peirce structure) or A-S 2003 Prop 7.43 / Prop 7.50 (for facial structure).

### Pitfall 2: Bare `\cite{AlfsenShultz2003}` (R5)

**What goes wrong:** Without chapter/prop, the citation is ambiguous between pre-Jordan Ch. 1-8 and post-Jordan Ch. 9. Referee will flag it.

**Why it happens:** `main-jmp-submitted.tex` line 513 is exactly this pattern; easy to replicate.

**How to avoid:** Every A-S 2003 cite uses `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` or `\cite[Ch.~7]{AlfsenShultz2003}` at minimum.

**Warning signs:** grep for `\\cite{AlfsenShultz2003}` returning any hit without `[` before the `{`.

**Recovery:** Resolve chapter + prop via alfsen-shultz-notes.md or secondary-source verification; update inline.

### Pitfall 3: Invoking Thm 9.37 for Peirce direct sum (R6, primary Phase 55 bug)

**What goes wrong:** Thm 9.37 is in A-S 2003 Ch. 9 (Jordan state-space characterization). Invoking it at pre-S4 scope is pre-Jordan-illegal.

**Why it happens:** The Peirce direct sum `V = ⊕ V_2(p_i) ⊕ ⊕ V_1(p_i, p_j)` is stated in Ch. 9 of A-S 2003 for Jordan state spaces; the Paper 5 author (at submission time) may have reached for it without noticing the Ch. 9 boundary.

**How to avoid:** Cite the Phase 54 Peirce-Preservation Lemma (`\ref{lem:peirce-preservation}`) or derive from S0 + A-S Ch. 7 compression theory (Prop 7.23, Prop 7.50). The Peirce direct sum at pre-Jordan level is a compression-theoretic fact available in Ch. 2/7/8.

**Warning signs:** `grep -n "9\.37\|9\.33" sections/ main.tex` returning any hit in §S4 or §S4-proof.

**Recovery:** Replace `(Alfsen-Shultz\cite{AlfsenShultz2003}, Theorem~9.37)` at axiom-verification.tex line 125 with `(by Lemma~\ref{lem:peirce-preservation} and axiom~\ref{ax:S0})` or similar.

### Pitfall 4: Unnamed "facial orthogonality theorem" (R5 + R6)

**What goes wrong:** appendix-proofs.tex line 108 and axiom-verification.tex line 154 invoke a "facial orthogonality theorem" with no citation. Referee will demand a theorem number. If the intended source is Jordan-structured, it's also R6 circular.

**Why it happens:** The argument is informal — "effects in complementary faces have zero compression" is intuitively obvious from facial geometry, but informal invocations accumulate unstated assumptions.

**How to avoid:** Derive from S0 termwise (`q_j ≤ p_+^⊥` ∧ `p_i ≤ p_+` ⟹ `q_j ⊥ p_i` ⟹ `C_{q_j}(p_i) = 0` by S0). Or cite Prop 7.43 specialized to `(p, b) = (q_j, p_+)` with the role-swap.

**Warning signs:** "facial orthogonality" or "by facial structure" appears in revision text without a cross-reference.

**Recovery:** Rewrite with explicit derivation; cite `\ref{ax:S0}` or `\cite[Prop.~7.43]{AlfsenShultz2003}`.

### Pitfall 5: Peirce-Preservation Lemma Part (iii) role-swap confusion

**What goes wrong:** Part (iii) is stated for L_a acting on V_1(p_k, p_l) where `{p_k}` are orthogonal projective units and `a = Σ_i λ_i p_i`. In the S4 argument, the reverse product is L_b acting on V_1(q_j, q_k) where `b = Σ_j μ_j q_j`. The roles swap but the lemma applies; the revision text must state the swap explicitly or it reads as hand-waving.

**Why it happens:** The lemma is stated abstractly; the S4 specialization requires noticing that "a" in the lemma corresponds to "b" in the S4 proof and vice versa.

**How to avoid:** Add an explicit "`Applying Lemma~\ref{lem:peirce-preservation} Part (iii) with a ← b and {p_k, p_l} ← {q_j, q_k} (noting {q_j, q_k} ∩ supp(b) = ∅ since ...)`" transition.

**Warning signs:** Part (iii) invocation appears without explicit swap notation; referee would flag "which variable plays which role?"

**Recovery:** Rewrite the invocation step with swap annotation.

### Pitfall 6: Prop 7.43 verification deferred indefinitely

**What goes wrong:** If Phase 55 closes without resolving Prop 7.43's exact statement (leaves VERIFICATION-DEFERRED), the referee can still flag the citation as unverified.

**Why it happens:** Direct A-S 2003 access is not in Phase 55's toolkit; secondary-source routes (Niestegge 2009, Hanche-Olsen-Størmer 1984, Jenčová-Pulmannová 2021) are the path of least resistance but may not resolve Prop 7.43 specifically.

**How to avoid:** Phase 55 plan must include a secondary-source verification sub-task (modeled on Phase 54 NEW SCOPE item 2). If secondary sources do not resolve Prop 7.43, escalate to user for physical book access decision before Phase 55 closes.

**Warning signs:** alfsen-shultz-notes.md Prop 7.43 row still VERIFICATION-DEFERRED at phase close.

**Recovery:** Either (a) verify via secondary source (preferred), (b) escalate to user for book access, or (c) fall back to Approach 2 (Foulis-Holland) if neither is feasible.

---

## Level of Rigor

**Required for this phase:** Formal proof at the level of "pre-Jordan-legal chain of citations, each resolved to a specific A-S 2003 Prop/Thm number or a named Phase 54 axiom/lemma." No hand-waving; no bare `AlfsenShultz` citations; no Jordan-structure invocations.

**Justification:** Paper 5 is under JMP referee review. The Phase 54 Adversarial Review Fresh (PASSES-WITH-CAVEATS) established the bar: every citation must be volume + chapter + prop, every theorem invocation must be pre-Jordan-legal, and forbidden tokens must not leak outside demarcated scopes. Phase 55 inherits and extends this bar.

**What this means concretely:**

- Every A-S citation in §S4 + §S4-proof revision text is of the form `\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}` or `\cite[Ch.~7]{AlfsenShultz2003}` at minimum.
- No `\cite{AlfsenShultz2003}` without `[]` modifier in §3.3-§3.5 + §S4 + §S4-proof scope.
- No citation to A-S 2001 vol 179 for compression theory (always 2003 vol 190).
- No Thm 9.37 invocation (post-Jordan-illegal).
- No Hanche-Olsen citation in §S4 or §S4-proof (post-Jordan-circular at pre-S4 scope).
- No forbidden tokens (`Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`) outside demarcated canonical-example scopes.
- Every unnamed "facial structure" or "facial orthogonality" appeal replaced with either a specific A-S Prop/Thm cite or a derivation from S0 + compression axioms.
- Every pre-sealing "it follows from Peirce..." in the Phase 55 edit scope replaced with "by S0" or "by Lemma~\ref{lem:peirce-preservation}" as appropriate.
- Corollary `cor:S4-phi-indep` preserved verbatim (already correct post-Phase 54).
- SymPy H_n(ℝ) spot-check passes for at least one non-trivial case (recommended but not required).

---

## S0-Substitution Sites (Phase 54 C-i consistency map)

Per the phase_context "Consistency with Phase 54 (C-i)": every pre-sealing "it follows from Peirce..." must become "by S0, ..." in Phase 55's revision text. Catalog:

| File | Line(s) | Current Text | S0-Substituted Text |
|------|---------|--------------|---------------------|
| `sections/axiom-verification.tex` | 125 | `(Alfsen-Shultz\cite{AlfsenShultz2003}, Theorem~9.37)` | `(by Lemma~\ref{lem:peirce-preservation} and axiom~\ref{ax:S0}, §3.3)` |
| `sections/axiom-verification.tex` | 143-147 | "By the facial structure of spectral order unit spaces, the Peirce 1-space components V_1(p_i, p_j) connecting a face to its complement are excluded" | "By the Peirce-Preservation Lemma Part (iii) (R3 cross-term case, §3.3): since {i, j} with i ≤ m, j > m has j ∉ supp(b|_{face(p_+)}) (b is supported on face(p_+^⊥)), L_b annihilates V_1(p_i, p_j)." |
| `sections/axiom-verification.tex` | 154 | "the facial orthogonality theorem gives C_{q_j}(a) = 0" | "since p_i ≤ p_+ and q_j ≤ p_+^⊥ implies p_i ⊥ q_j, axiom~\ref{ax:S0} gives C_{q_j}(p_i) = 0 for each i, hence C_{q_j}(a) = Σ_i λ_i C_{q_j}(p_i) = 0" |
| `sections/axiom-verification.tex` | 155-157 | "The Peirce 1-space terms Q_{jk}(a) either vanish by facial structure..." | "The Peirce 1-space terms Q_{jk}(a) vanish by Lemma~\ref{lem:peirce-preservation} Part (iii) (R3 cross-term case): both q_j, q_k ≤ p_+^⊥ gives {q_j, q_k} ∩ supp(a) = ∅, so L_a(V_1(q_j, q_k)) = 0, in particular Q_{jk}(a) = 0." |
| `sections/appendix-proofs.tex` | 79 (Prop 7.43 quote) | Already cited as `Proposition~7.43 of~\cite{AlfsenShultz2003}` with blockquote | Tighten to `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`; verify prop number or mark VERIFICATION-DEFERRED inline |
| `sections/appendix-proofs.tex` | 85-89 ("compressions for orthogonal projective units act independently") | Currently "compressions for orthogonal projective units act independently on their respective faces" | Add explicit `\ref{ax:S0}` or `\cite[Prop.~7.50]{AlfsenShultz2003}` citation: "by axiom~\ref{ax:S0} (§3.3, mutual compressional annihilation for orthogonal projective units), compressions for orthogonal projective units act independently, giving C_{p_+}(b) = Σ_{i ∈ I_+} C_{p_i}(b) = 0" |
| `sections/appendix-proofs.tex` | 106-108 | "the facial orthogonality of complementary faces gives C_{q_j}(a) = 0" | Same S0-termwise pattern as axiom-verification.tex line 154 substitution |
| `sections/appendix-proofs.tex` | 109-113 | "The Peirce 1-space terms Q_{jk}(a) either vanish by facial structure..." | Same Part (iii) citation as axiom-verification.tex line 155-157 substitution |
| `sections/appendix-proofs.tex` | 37-49 (Peirce direct sum invocation) | Uses `\eqref{eq:peirce-proj}` without citing the decomposition's source | Add parenthetical: "(Peirce direct sum is established in §3.3 via Lemma~\ref{lem:peirce-preservation} and axiom~\ref{ax:S0}; see also \cite[Ch.~7]{AlfsenShultz2003} for the compression-theoretic underpinning)" |

**Count:** 8 substitution sites across the two files. Primary sites (bugs to fix) are `axiom-verification.tex` line 125 (Thm 9.37) and the unnamed "facial orthogonality" at both files. Secondary sites (tightening) are the support-projection step and the Q_{jk}(a) step.

**Not substitution sites (verify stays):**
- `sections/axiom-verification.tex` line 39 (`(Alfsen--Shultz\cite{AlfsenShultz2003}, Ch.~7)`) — already chapter-cited; OK as-is but could be tightened to specific prop.
- `sections/axiom-verification.tex` line 68 (`(Alfsen--Shultz\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37)`) — **WAIT:** this is a second Thm 9.37 citation outside §S4. Check context: line 68 is likely in §S1-S3 proof scaffolding. If so, this is also pre-Jordan-illegal and should be flagged. **Phase 55 TODO: verify context of line 68 Thm 9.37 invocation.**
- `sections/axiom-verification.tex` line 83 (`(Alfsen--Shultz\cite{AlfsenShultz2003}, Def.~7.1)`) — OK, Def 7.1 is pre-Jordan-legal (Phase 54 verified).
- `sections/axiom-verification.tex` line 180 (`(Alfsen--Shultz\cite{AlfsenShultz2003}, Prop.~7.49)`) — OK, Prop 7.49 is S5-scope, pre-Jordan in Ch. 7.
- `sections/axiom-verification.tex` lines 228, 232 (`Prop.~7.49` + `Prop.~7.50`) — OK; note Prop 7.50 was Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE.
- `sections/axiom-verification.tex` line 321 (`Prop.~7.50`) — OK, same.

**Scope adjustment:** The roadmap says "§3.3-§3.4 S4 argument." Strictly, the S4 **axiom** is declared in §3.2 (main-jmp-submitted.tex line 267-295 Definition 3.2) and the S4 **proof** lives in §4 (via `sections/axiom-verification.tex`) and Appendix A (via `sections/appendix-proofs.tex`). Phase 55's effective edit scope is §S4 of axiom-verification.tex + §S4-proof of appendix-proofs.tex. §3.3-§3.4 of main.tex is already Phase 54's scope (sealed C-i). §3.5 (Circularity Check) is out-of-scope but has "Alfsen-Shultz compressions" language at line 730 that should be kept as-is (it's a list of mathematical objects, not a theorem citation).

**Flag for planner:** The line 68 Thm 9.37 invocation in `axiom-verification.tex` is outside the strict §S4 scope but is the same R6 circularity bug. Recommend Phase 55 includes line 68 in its edit scope OR explicitly flags it for a follow-up phase.

---

## Forbidden-Token Discipline Checklist

Before committing to any proposed revision wording, ensure the pre-S4 revision text satisfies (R7):

- [ ] `grep -n "Jordan" sections/axiom-verification.tex sections/appendix-proofs.tex | grep -v '% BEGIN canonical-example' | grep -v '% END'` returns zero (or only demarcated hits).
- [ ] `grep -n "EJA" sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero in §S4 + §S4-proof scope.
- [ ] `grep -n "Lüders\|L.ders" sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero.
- [ ] `grep -n "pxp" sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero.
- [ ] `grep -nE "sqrt.?a.?b.?sqrt.?a|√.?a.?b.?√.?a" sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero.
- [ ] `grep -n "Hanche-Olsen\|HancheOlsen" sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero (Phase 55-specific forbidden token: H-O is post-Jordan-circular at pre-S4 scope).
- [ ] `grep -n "Theorem.*9\.37\|Thm.*9\.37\|9\.37" sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero (Thm 9.37 is PRE-JORDAN-ILLEGAL).
- [ ] `grep -n "\\cite{AlfsenShultz2003}" sections/axiom-verification.tex sections/appendix-proofs.tex | grep -v "\\cite\[.*\]{AlfsenShultz2003}"` returns zero (no bare cites).
- [ ] Canonical-example defenses (if any) wrapped in `% BEGIN canonical-example defense ... % END` markers.
- [ ] `\ref{ax:S0}` and `\ref{lem:peirce-preservation}` cross-references resolve at LaTeX compile.
- [ ] `main-jmp-submitted.tex` unchanged (`git diff --stat HEAD -- main-jmp-submitted.tex` → 0).

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Bare `\cite{AlfsenShultz2003}` at line 513 of main-jmp-submitted.tex | Tightened to `\cite[Prop.~7.23]{AlfsenShultz2003}` + explicit S0 axiom | Phase 54 (2026-04-16) | §3.3 now pre-Jordan-legal with named lemma |
| Thm 9.37 invocation for Peirce direct sum | S0 + Peirce-Preservation Lemma (Phase 54); Phase 55 propagates this through §S4 + §S4-proof | Phase 55 (2026-04-16) | §S4 revision replaces R6 circularity with S0-based derivation |
| Unnamed "facial orthogonality theorem" | S0 termwise (preferred) or A-S 2003 Prop 7.43 specialized to complementary face | Phase 55 | Referee-proofs the Case B reverse-product step |
| Hanche-Olsen Peirce at pre-S4 (never actually in Paper 5, but in METHODS.md Method 3 as "primary" with CHECK flag) | A-S 2003 Ch. 7 compression Peirce (pre-Jordan-legal) | Phase 54 + 55 (METHODS.md Method 3 is post-Jordan only; Method 4 F-H is pre-Jordan) | Avoids R6 circularity |

**Superseded approaches to avoid:**

- **H-O §2.6 Peirce decomposition at pre-S4 scope:** post-Jordan; replaced by A-S 2003 Ch. 7 compression-theoretic Peirce + S0.
- **H-O §2.1 face-projection correspondence at pre-S4 scope:** post-Jordan (JB-algebra); replaced by A-S 2003 Prop 7.43 (pre-Jordan-legal in Ch. 7).
- **Thm 9.37 citation for Peirce direct sum:** post-Jordan (Ch. 9); replaced by Phase 54 Peirce-Preservation Lemma.
- **Bare `AlfsenShultz` citations:** R5 violation; replaced by chapter+prop-specific cites.

---

## Open Questions

1. **Is line 68 of `axiom-verification.tex` (second Thm 9.37 invocation) in Phase 55 scope?**
   - What we know: Line 68 cites `(Alfsen--Shultz\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37)` — same Thm 9.37 as line 125 (§S4). Context: unknown (need to read surrounding lines).
   - What's unclear: Is this in §S1-S3 proof scaffolding, §3.x scaffolding, or §S5+? If §S1-S3, it's pre-S4 and also R6-illegal. If §S5+ (post-S4 proven), it's legal.
   - Impact on this phase: If pre-S4, Phase 55 should include it in edit scope. If post-S4, out of Phase 55 scope.
   - Recommendation: Phase 55 planner's first task reads lines 1-90 of axiom-verification.tex to classify context of line 68.

2. **Does secondary-source verification resolve Prop 7.43 statement?**
   - What we know: alfsen-shultz-notes.md Section 5A lists Niestegge 2010 (arXiv:1001.3633), Hanche-Olsen-Størmer 1984, Jenčová-Pulmannová 2021 as candidates. Phase 54 verified Prop 7.23, Def 7.1, Prop 7.50 via internal cross-references (`derivations/04-axiom-S4.md`, `derivations/04-axioms-S1-S3-S5-S7.md`). Prop 7.43 was not in Phase 54's scope.
   - What's unclear: Do any of those internal derivations cite Prop 7.43 explicitly?
   - Impact on this phase: If yes, VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (same as Prop 7.50). If no, VERIFICATION-DEFERRED remains and fallback (Approach 2 or book access) triggers.
   - Recommendation: Phase 55 planner includes a sub-task (modeled on Phase 54 NEW SCOPE item 2) that greps `derivations/` for "7.43" and "facial absorption" to see if an internal cross-reference already exists.

3. **Should Phase 55 also extend to §3.5 (Circularity Check, lines 714-740)?**
   - What we know: §3.5 is labeled out of Phase 54-01 scope in alfsen-shultz-notes.md Section 1. It contains an informal list at lines 727-737 of mathematical objects (including "Alfsen-Shultz compressions") but no theorem citations.
   - What's unclear: Does Phase 55's revision of §S4 introduce any change that propagates to §3.5 (e.g., if S0 is now axiomatic, should §3.5's list mention it)?
   - Impact on this phase: Minimal. §3.5 lists objects used; adding S0 to the list is a 1-line edit.
   - Recommendation: Add S0 to §3.5's list at line 729 (between "effect space" and "Alfsen-Shultz compressions"); low-cost consistency edit.

4. **Does line 68's Thm 9.37 citation invalidate Phase 54's claim of "zero Thm 9.37 invocations after sealing"?**
   - What we know: Phase 54's close checklist item (§5.1) says "no Ch.~9, Thm.~9.37 in main.tex §3.3". This only covered main.tex §3.3, not axiom-verification.tex.
   - What's unclear: Did Phase 54 intend to cover all of Paper 5 or just §3.3?
   - Impact on this phase: Scope-clarification; does not affect Phase 54's (C-i) seal.
   - Recommendation: Phase 55's deliverable 1 (classification) explicitly lists all Thm 9.37 invocations across the paper to clarify the full R6 exposure.

5. **Is the Lean axiom `orthogonal_face_sp_zero` (cited as Prop 7.36) affected by Phase 55's S4 revision?**
   - What we know: alfsen-shultz-notes.md Flag 4.2 tags Prop 7.36 as PROP-NUMBER-UNVERIFIED with a Lean statement-mismatch concern. Phase 54 deferred this to Phase 58.
   - What's unclear: Does Phase 55's paper-level S4 revision (using Prop 7.43 + S0) change the Lean axiom's intended content?
   - Impact on this phase: Phase 55 should not modify Lean; but should update alfsen-shultz-notes.md to note that Paper 5's S4 argument now uses Prop 7.43 + S0, not Prop 7.36 (so the Lean axiom's citation is potentially wrong).
   - Recommendation: Phase 55 adds a note to Flag 4.2 row: "Paper 5 §S4 no longer invokes Prop 7.36 at all (uses Prop 7.43 + S0); Phase 58 Lean audit should reconsider whether `orthogonal_face_sp_zero` should cite Prop 7.43 or S0 instead."

---

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
|---------------|------------|-----------|-------------------|
| Approach 1 (S0 + Prop 7.43) | Prop 7.43 cannot be verified via secondary sources AND physical book access unavailable | Approach 2 (Foulis-Holland fallback) | ~20 extra lines of revision text; extra H-O-free derivation of facial orthogonality |
| Approach 1 (S0 + Prop 7.43) | Prop 7.43 verified but specialized "facial orthogonality" direction unclear | Derive directly from S0 termwise without Prop 7.43 specialization | Near-zero; S0-termwise route is already the recommended step 4 |
| Approach 2 (Foulis-Holland) | F-H requires orthomodular-lattice embedding that cannot be established at §S4 scope | Escalate to user for scope decision (drop S4 claim or seek external theorem) | HIGH; triggers outcome (C) and milestone pause per backtracking rule |

**Decision criteria:**

- Abandon Approach 1 and switch to Approach 2 if: secondary-source Prop 7.43 verification fails (≥3 candidate sources checked, none resolves the prop number) AND user confirms no physical book access.
- Abandon both approaches and trigger outcome (C) if: both Prop 7.43 verification and F-H orthomodular-lattice embedding cannot be closed within Phase 55's time budget.
- Outcome (C) triggers milestone pause per roadmap backtracking rule.

---

## Sources

### Primary (HIGH confidence)

- **Alfsen, E. M., Shultz, F. W.**, *Geometry of State Spaces of Operator Algebras*, Birkhäuser PM 190, 2003. ISBN 978-0-8176-4319-8. Ch. 2 (Abstract characterization of compressions, p. 75), Ch. 7 (General Compressions, p. 211), Ch. 8 (Spectral Theory, p. 251), Ch. 9 (Jordan State-Space Characterization — **PRE-JORDAN-ILLEGAL at pre-S4 scope**).
- **van de Wetering, J.**, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019), arXiv:1803.11139. Def 2 (S1-S7 axioms including S4 verbatim); Thm 1 (EJA classification); Thm 3 (LT → C\*).
- **Paper 5 submitted**, `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` at git tag `paper5-jmp-submitted`. §3.3-§3.4 lines 483-712; Definition 3.2 (S1-S7) lines 267-295.
- **Paper 5 living**, `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main.tex` (integrates Phase 54 revision lines 524-663); `sections/axiom-verification.tex` lines 95-168 (§S4 proof sketch); `sections/appendix-proofs.tex` lines 9-138 (§S4-proof full).
- **Phase 54 `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md`** (256 lines, SHARED artifact with baseline + 2026-04-16 corrections). Sections 1-7 cover §3.3-§3.4 A-S citation inventory, Thm 9.37 PRE-JORDAN-ILLEGAL flag, Prop 7.36 PROP-NUMBER-UNVERIFIED flag, and Ch. 7 compression-axiom sub-table.
- **Phase 54 `derivations/paper5-peirce-preservation/s0-axiom.md`** — S0 axiom statement + canonical-example defenses + OUS-compatibility derivation of Peirce-Preservation Lemma.
- **Phase 54 RESULT.md** at `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-RESULT.md` — SEALED (C-i) 2026-04-17.

### Secondary (MEDIUM confidence)

- **Niestegge, G.**, "Conditional probability, three-slit experiments, and the Jordan algebra structure of quantum mechanics," Adv. Math. Phys. 2012, 156573 (published 2012; Phase 54 cites arXiv:1001.3633 2009 preprint as `Niestegge2009` via refs.bib). Pre-Jordan U_e compression framework; secondary-source verification candidate for Prop 7.43.
- **Hanche-Olsen, H., Størmer, E.**, *Jordan Operator Algebras*, Pitman Research Notes in Mathematics 21, 1984. §2.1 (face-projection correspondence, JB-algebra; **post-Jordan-circular at pre-S4 scope**). §2.6 (Peirce decomposition; **post-Jordan-circular at pre-S4 scope**).
- **Jenčová, A., Pulmannová, S.**, "Effect algebras and sequential products," arXiv:2102.01628 (2021). Phase 54 ADDENDUM Finding 2 confirms their Peirce treatment is post-Jordan (Section 5 "Spectrality for JB-algebras").
- **Phase 54 `derivations/paper5-peirce-preservation/secondary-source-verification.md`** — establishes the internal-cross-reference verification pattern used for Prop 7.23, Def 7.1, Prop 7.50; template for Phase 55's Prop 7.43 verification sub-task.
- **METHODS.md** `.gpd/research/METHODS.md` — Method 3 (Hanche-Olsen facial symmetry, Phase 55 primary but CHECK phase ordering), Method 4 (Foulis-Holland, Phase 55 fallback).
- **PITFALLS.md** `.gpd/research/PITFALLS.md` — R5 (A-S citation precision), R6 (facial orthogonality φ-independence), R7 (forbidden tokens in pre-Jordan context).

### Tertiary (LOW confidence)

- **Kalmbach, G.**, *Orthomodular Lattices*, Academic Press, 1983. Ch. 2 (Foulis-Holland theorem). METHODS.md Method 4 reference.
- **Beran, L.**, *Orthomodular Lattices: An Algebraic Approach*, Reidel, 1985. Alternative F-H treatment.
- **Gudder, S., Greechie, R.**, "Sequential products on effect algebras," Rep. Math. Phys. 49, 87-111 (2002). METHODS.md Method 2; Phase 54 (C-ii) feasibility check reference.

### Failed Lookups

- **Direct A-S 2003 book text for Prop 7.43 statement** — not accessed by Phase 54 or Phase 55 research; secondary-source verification path is the preferred route.
- **Physical A-S 2003 book** — not available in the project toolchain; requires user decision for purchase or library access (ISBN 978-0-8176-4319-8, ~$50 paperback).

---

## Caveats and Alternatives (Pre-Submission Self-Critique)

**1. What assumption am I making that might be wrong?**

I assume that the recommended S0-termwise derivation of "facial orthogonality" (axiom-verification.tex line 154 substitution) is pre-Jordan-legal. The chain is: `q_j ≤ p_+^⊥` and `p_i ≤ p_+` imply `p_i ⊥ q_j` (face-disjointness), so S0 gives `C_{q_j}(p_i) = 0`. But "`q_j ≤ p_+^⊥` implies `q_j ⊥ p_i` for `p_i ≤ p_+`" uses the complementary-face fact, which itself lives in A-S Ch. 7. If Ch. 7 does not state this directly (it may be a derived fact requiring Ch. 8 spectral theory), the chain is longer and requires another cite. The planner should verify this chain step-by-step, possibly via `derivations/04-axioms-S1-S3-S5-S7.md` or a new internal cross-reference.

**2. What alternative approach did I dismiss too quickly? Why?**

I dismissed **invoking A-S 2003 Prop 7.36** (the Lean axiom target in Flag 4.2 of alfsen-shultz-notes.md). Prop 7.36 is flagged PROP-NUMBER-UNVERIFIED with a potential Lean statement-mismatch; using it in Paper 5's §S4 revision would inherit the uncertainty. But if Prop 7.36 is in fact the "facial orthogonality of effects" result (correct Prop/Thm number, correct content), it is a direct hit for the step. I did not pursue this because Phase 54 deferred Prop 7.36 to Phase 58, and pulling it into Phase 55 expands scope. If Phase 55 has bandwidth, the planner may want to include a Prop 7.36 verification sub-task (same cost as Prop 7.43 verification) and use whichever pins faster.

**3. What limitation of my recommended method am I understating?**

The recommended method requires **verifying Prop 7.43** via secondary sources. Phase 54's internal cross-references (`derivations/04-axiom-S4.md`, `derivations/04-axioms-S1-S3-S5-S7.md`) verified Prop 7.23, Def 7.1, Prop 7.50 — but I have not personally checked whether they verify Prop 7.43. If they don't, Phase 55 must run a fresh secondary-source search (Niestegge 2009, Hanche-Olsen-Størmer 1984). That search may not succeed, in which case Approach 1 degrades to Approach 2 (F-H) or outcome (C). I am understating the risk that secondary-source verification of Prop 7.43 is harder than Prop 7.50 was.

**4. Is there a simpler method I overlooked because the complex one is more impressive?**

Yes: **drop the Case B argument entirely and use the mixing function `f(0, x) = 0` to extend Case A to the rank-deficient case via continuity.** The logic: in Case B, `a = Σ_{i ∈ I_+} λ_i p_i + 0 · (I_0 projectors)`. If the Case A proof goes through whenever `a ∘ b = 0` and a is full-rank on its support, the rank-deficient case reduces to the full-rank case on `face(p_+)`. The φ-independence Corollary already exploits `f(0, x) = 0`; it may be that a cleaner proof just observes `seqp{a}{b} = seqp{a|_{face(p_+)}}{b|_{face(p_+)}}` and reduces to Case A on the support face. This would eliminate the Prop 7.43 citation entirely.

I did not recommend this because (a) the current appendix-proofs.tex proof is already written with explicit Case B machinery and rewriting is a larger edit, (b) the reduction "`seqp{a}{b} = seqp{a|_{face(p_+)}}{b|_{face(p_+)}}`" may itself require a compression-theoretic lemma (possibly Prop 7.43 or equivalent), so I am not sure it actually saves citations. The planner should consider whether this reduction is worth exploring as a smaller-diff alternative to the full S0-termwise rewrite.

**5. Would a physicist specializing in this subfield disagree with my recommendation? Why?**

An operator-algebra specialist would likely disagree with my choice to keep A-S Prop 7.43 as the primary Case B citation. They would prefer **Niestegge 2009 §3 `U_e` compression framework**, which states facial absorption in a more operationally-motivated form (conditional-probability semantics), without invoking the geometric "face" primitive. Niestegge's formulation is pre-Jordan by construction and may be easier to verify than A-S 2003. The tradeoff: Niestegge's notation is different from A-S's (uses `U_e` instead of `C_p`), so the Paper 5 §S4 revision would need to translate. But if Niestegge 2009 §3 is the source already cited in refs.bib, using it directly avoids the A-S verification problem.

**Recommendation for planner:** Consider adding a sub-task to check whether Niestegge 2009 §3 has a statement equivalent to A-S Prop 7.43 but at pre-Jordan level. If yes, cite Niestegge directly and relegate Prop 7.43 to a footnote.

---

## Metadata

**Confidence breakdown:**

- **Mathematical framework:** HIGH. Pure algebra on finite-dim archimedean OUS; no numerical regime, no approximation, no model-dependence. All equations and techniques are Phase 54-proven or textbook-standard.
- **Standard approaches:** HIGH for Approach 1 (S0 + Prop 7.43); MEDIUM for Approach 2 (F-H) because it has not been used in Phase 54 and would be the first F-H invocation in the project. Fallback path is clear but untested.
- **Computational tools:** HIGH. grep + git + LaTeX + optional SymPy. All templated from Phase 54.
- **Validation strategies:** HIGH. Internal consistency checks (grep-based) are enumerable and automatable; forbidden-token discipline is mechanical. SymPy spot-check reuses Phase 54 pattern.
- **Citation-specific confidence:** HIGH for A-S 2003 cites already VERIFIED in Phase 54 (Prop 7.23, Def 7.1, Prop 7.50). MEDIUM for Prop 7.43 (VERIFICATION-DEFERRED; pending secondary-source check). HIGH for the forbidden-token list (Phase 54 R7 precedent). HIGH for the Thm 9.37 PRE-JORDAN-ILLEGAL flag (Phase 54 Flag 4.1 + ADDENDUM).
- **Prop 7.36 / Lean coupling:** LOW (deferred to Phase 58; Phase 55 only updates alfsen-shultz-notes.md row).

**Research date:** 2026-04-16

**Valid until:** Indefinite for the physics content (pure algebra; no tool-version dependence). The A-S book edition is stable (first-edition Birkhäuser PM 190, 2003); theorem numbering will not change. Valid until a referee report demands a different structural reorganization (in which case a new phase would be opened).

---

**Phase 55 research complete. Planner can now create 55-PLAN.md files.**
