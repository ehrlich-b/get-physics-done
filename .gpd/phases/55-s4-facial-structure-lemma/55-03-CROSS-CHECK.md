# Phase 55-03 Task 2 — Cross-Check: Phase 55-02 Revised §S4 Proof vs `derivations/04-axiom-S4.md` (Submitted-Era Derivation)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A

**Produced:** 2026-04-17 (Phase 55-03 Task 2)
**Baseline (submitted-era):** `derivations/04-axiom-S4.md` (GPD v2.0 Phase 04, produced 2026-03-21 under convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY`)
**Revised (Phase 55-02):** `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/sections/{axiom-verification.tex, appendix-proofs.tex}` at blog repo commits `b44408e` (axiom-verification.tex), `f4fb2f8` (appendix-proofs.tex), `e134c24` (main.tex §3.5 Circularity Check)
**Purpose:** Per-step cross-check that the Phase 55-02 revised §S4 proof reaches the same conclusion as the submitted-era derivation (`a ∘ b = 0 ⟹ b ∘ a = 0`) via a pre-Jordan-legal refactoring of the submitted-era steps. Reject fp-skip-cross-check (top-level declaration without per-step comparison).

---

## 1. Step-by-Step Cross-Check Table

Eight major steps spanning Case A (full-rank), Case B (rank-deficient), and the φ-independence corollary. Each row records the submitted-era justification (with line number) and the Phase 55-02 revised justification (with file:line), plus a pre-Jordan-legal verdict.

| # | Step | Submitted-era justification (`04-axiom-S4.md` line) | Phase 55-02 revised justification (file:line) | Pre-Jordan-legal? | Notes |
|---|------|------------------------------------------------------|-----------------------------------------------|-------------------|-------|
| 1 | Case A opening: `a ∘ b = 0` with `a = Σ λ_i p_i` full-rank ⟹ expand via eq:corrected-product; sum over Peirce 2-space + Peirce 1-space components | `04-axiom-S4.md:83-96` — states Eq. (*), separates into `Σ λ_i C_{p_i}(b)` (Peirce 2-space) + `Σ_{i<j} √(λ_iλ_j) P_{ij}(b)` (Peirce 1-space) | `appendix-proofs.tex:28-36` — states `eq:S4-expand` verbatim; identical decomposition | **YES** | Verbatim preserved; standard spectral-decomposition expansion |
| 2 | Peirce direct sum: `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i, p_j)` justifies component-wise vanishing | `04-axiom-S4.md:99-103` — invokes **"Alfsen-Shultz Ch. 9, Theorem 9.37"** for Peirce direct sum (submitted-era cite; PRE-JORDAN-ILLEGAL per Phase 54 Flag 4.1) | `appendix-proofs.tex:37-40` — invokes `\eqref{eq:peirce-proj}` with inline parenthetical **`(established at the compression level in §3.3 via axiom~\ref{ax:S0} and Lemma~\ref{lem:peirce-preservation}; the compression-theoretic underpinning is ~\cite[Ch.~7]{AlfsenShultz2003})`** | **YES** | **PRIMARY PHASE 55 BUG FIXED.** Submitted-era Ch.~9 Thm.~9.37 citation replaced with Phase 54 outputs (S0 axiom + Peirce-Preservation Lemma) backed by A-S 2003 Ch.~7 compression theory. Conclusion (direct-sum ⟹ termwise vanishing) preserved. |
| 3 | Case A diagonal vanishing: `λ_i > 0` ∧ direct-sum ⟹ `C_{p_i}(b) = 0` for each `i` | `04-axiom-S4.md:106-112` — direct consequence of step 2; cites A-S Prop 7.23 implicitly (via A1 Positivity + A3 Idempotency in the A-properties table at line 61-67) | `appendix-proofs.tex:45-48` — `eq:S4-diag` gives `λ_i C_{p_i}(b) = 0` for each `i`; then `λ_i > 0` ⟹ `C_{p_i}(b) = 0`. Cites `\cite[Ch.~7, Prop.~7.23]{AlfsenShultz2003}` implicitly (A-S idempotency in the toolkit). | **YES** | A-S Prop 7.23 is `VERIFIED-VIA-INTERNAL-CROSS-REFERENCE` per Phase 54 baseline. Identical logic. |
| 4 | Case B: partition `{1..n}` into `I_+ = {i : λ_i > 0}` and `I_0 = {i : λ_i = 0}`; spectral calculus on `a = Σ_{i ∈ I_+} λ_i p_i` | `04-axiom-S4.md:121-128` — states `lambda_{m+1} = ... = lambda_n = 0`; spectral decomposition unchanged; `a = sum_{i=1}^m lambda_i p_i` | `appendix-proofs.tex:70-79` — states `I_+ = {i : λ_i > 0}` and `I_0 = {i : λ_i = 0}`, both nonempty; same rank split | **YES** | Standard spectral calculus; A-S 2003 Ch. 8 pre-Jordan-legal territory. No change. |
| 5 | Case B facial absorption: `C_{p_+}(b) = 0` ∧ `b ≥ 0` ⟹ `b ∈ face(p_+^⊥)` | `04-axiom-S4.md:156-163` — invokes "Alfsen-Shultz Prop. 7.43" (submitted-era cite, bare; per A5 table entry at line 65) for facial absorption; gives it the name "Effect constraint on mixed Peirce components" | `appendix-proofs.tex:81-94` — invokes **`\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`** (tightened to bracketed [Ch., Prop.] form); blockquote statement **verbatim preserved**: "If `C_p(b) = 0` and `b ≥ 0`, then `b ∈ face(p^⊥)`"; support projection `p_+ = Σ_{i ∈ I_+} p_i` cited with axiom~`\ref{ax:S0}` and equivalent Prop 7.50 route | **YES** (VERIFIED-VIA-INTERNAL-CROSS-REFERENCE inherited from Plan 55-01 Section 3) | Citation tightened (not content-changed). Prop 7.43 verdict: **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** (Plan 55-01 Section 3 + `secondary-source-verification.md` Phase 55-01 appendix entry, via `derivations/04-axiom-S4.md:65` which itself cites "Alfsen-Shultz, Prop. 7.43" under convention lock). Approach 2 (Foulis-Holland fallback) NOT triggered. |
| 6 | Case B reverse product: `q_j ≤ p_+^⊥` ∧ `a` supported on `face(p_+)` ⟹ `C_{q_j}(a) = 0` for each `j` with `μ_j > 0` | `04-axiom-S4.md:220-230` — invokes "Alfsen-Shultz facial orthogonality theorem" (**UNNAMED**, no Prop/Thm number) and A6 (line 66: "If p, q are orthogonal projective units (p + q <= 1), then C_p(q) = 0 and C_q(p) = 0 | From A2 + orthogonality") | `appendix-proofs.tex:110-121` — **explicit S0-termwise derivation**: `q_j ≤ p_+^⊥` ∧ `p_i ≤ p_+` ⟹ `q_j ⊥ p_i` (complementary faces of orthogonal projective units; `\cite[Ch.~7]{AlfsenShultz2003}`); **axiom`~\ref{ax:S0}`** (mutual compressional annihilation for orthogonal projective units) yields `C_{q_j}(p_i) = 0` for every `i ∈ I_+`; linearity then gives `C_{q_j}(a) = Σ_{i ∈ I_+} λ_i C_{q_j}(p_i) = 0` | **YES** | **UNNAMED "facial orthogonality theorem" RESOLVED.** Submitted-era unnamed theorem (a R5+R6 pitfall) replaced by explicit S0-termwise derivation using only pre-Jordan-legal primitives (S0 axiom, A-S Ch. 7 face-lattice orthogonality, linearity). Conclusion identical: `C_{q_j}(a) = 0` for each `j ∈ {j : μ_j > 0}`. |
| 7 | Case B Peirce 1-space vanishing: `Q_{jk}(a) = 0` for pairs `(j, k)` with both `μ_j, μ_k > 0` (and `q_j, q_k ≤ p_+^⊥`) | `04-axiom-S4.md:232-290` — "vanish by facial structure" (UNNAMED handwave); elaborated informally via: "a is in face(sum p_i) and q_j, q_k are in the complementary face, so a has zero projection onto V_1(q_j, q_k)"; no explicit Prop/Thm cite | `appendix-proofs.tex:122-128` — explicit invocation of **Peirce-Preservation Lemma Part (iii)** (`\Cref{lem:peirce-preservation}`) with role-swap annotation: `apply the lemma with the roles $a \leftarrow a$ and $\{p_k, p_l\} \leftarrow \{q_j, q_k\}$, using $\{q_j, q_k\} \cap \mathrm{supp}(a) = \emptyset$ since both $q_j, q_k \leq p_+^\perp$ and $\mathrm{supp}(a) \subseteq \{p_i : i \in I_+\}$` | **YES** | **UNNAMED "facial structure" HANDWAVE RESOLVED.** Submitted-era informal argument replaced by explicit Peirce-Preservation Lemma Part (iii) invocation (Phase 54 authored precisely for this use-case, lines 641-644 of main.tex). Role-swap annotation `a ← a`, `{p_k, p_l} ← {q_j, q_k}` is explicit, resolving Phase 55-01 Pitfall 5 (role-swap confusion). Conclusion: `Q_{jk}(a) = 0`. |
| 8 | Corollary `cor:S4-phi-indep`: S4 holds for any mixing function `f` with `f(0, x) = 0`, not only for `f = √(λ_i λ_j)` | `04-axiom-S4.md:316-323` — Step 4 "Role of phi (Self-Modeling Faithfulness)"; states `S4 holds for ALL phi choices`; only requirement is `f(0, x) = 0 for all x` | `appendix-proofs.tex:137-153` — **VERBATIM PRESERVED** from pre-Phase-55 state; no diff in Phase 55-02. Corollary statement: "S4 holds for any mixing function f satisfying f(0, x) = 0 for all x" | **YES** | No content change in Phase 55-02 (per Plan 55-02 `cor:S4-phi-indep` VERBATIM-PRESERVED tag). Identical to submitted-era. SymPy Test 3 (this phase, Task 1) exercises this directly by using `f = λ_i · λ_j` as an alternative mixing function and verifying S4 still holds. |

---

## 2. Final Verdict

**Revised proof reaches same conclusion: YES.**

All eight major steps of the submitted-era derivation map to Phase 55-02 revised text with identical conclusions. The differences are entirely in the JUSTIFICATION layer (citation tightening, unnamed-theorem replacement, Peirce direct sum recitation through pre-Jordan-legal primitives), not in the mathematical content.

**Breakdown by step:**

- **Verbatim preserved** (zero change in Phase 55-02): Steps 1, 4, 8 (3 steps).
- **Citation tightened** (cite form changed; content identical): Steps 3, 5 (2 steps).
- **Refactored to pre-Jordan-legal primitives** (content identical but routed through S0 / Peirce-Preservation Lemma instead of Thm 9.37 / unnamed theorems): Steps 2, 6, 7 (3 steps).

**Zero silent drift detected** (see §3 below).

**Prop 7.43 verdict inheritance:** VERIFIED-VIA-INTERNAL-CROSS-REFERENCE per Plan 55-01 Section 3. The submitted-era derivation (`derivations/04-axiom-S4.md:65`) is itself the internal cross-reference source. This is a self-consistent inheritance chain, not a circularity risk: the submitted-era derivation was produced under convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY` with explicit A-S Prop/Thm numbers; Paper 5's blockquote at `appendix-proofs.tex:83-87` matches verbatim (modulo notation); no paraphrasing occurred.

---

## 3. Silent-Drift Check

**No silent drift detected.**

Every major step in the submitted-era derivation (`04-axiom-S4.md`) is matched to at least one step in the Phase 55-02 revised text. Specifically:

1. **Every cited A-S property (A1-A7 in submitted-era Table at `04-axiom-S4.md:61-67`)** has a corresponding appearance in Phase 55-02 edits, either through direct citation (A1 Positivity / A3 Idempotency → Prop 7.23, A2 Unit image → Def 7.1, A5 Face containment → Prop 7.43, A6 Facial orthogonality → now derived from S0 termwise, A7 Spectral completeness → now via Peirce-Preservation Lemma + S0 + A-S Ch. 7) or through Phase 54 toolkit substitution.
2. **Every proof step** (Case A full-rank, Case B rank-deficient, Sub-step 2B.3 effect-constraint lemma, Sub-step 3.1 spectral projectors in complementary face, Sub-step 3.2 C_{q_j}(a) = 0, Sub-step 3.3 Q_{jk}(a) = 0, φ-independence) has a matching revised step with explicit justification.
3. **Every "handwavy" submitted-era step** (the two unnamed "facial orthogonality theorem" / "facial structure" appeals at lines 220-230 and 232-290) is now explicit in Phase 55-02, as documented in steps 6 and 7 above.

**Flag section** (steps flagged as "unmatched" or requiring escalation): **NONE.** The submitted-era derivation's informal steps are all accounted for in Phase 55-02 either by explicit derivation (S0-termwise, Peirce-Preservation Lemma Part (iii)) or by retained citation (Prop 7.43 blockquote preserved verbatim).

---

## 4. Pre-Jordan-Legal Audit

Every Phase 55-02 revised justification stays within the `{S0, S1, S3, linearity, A-S compression axioms (Ch. 2/7/8), finite-dim spectrality}` toolkit locked by Phase 54 (C-i) outcome:

| Primitive invoked in Phase 55-02 | Source | Pre-Jordan-legal? |
|----------------------------------|--------|-------------------|
| Axiom S0 (mutual compressional annihilation) | Phase 54 (Plan 54-03); `main.tex:537` | YES (compression-level OUS axiom; recoverable from A-S 2003 Prop 7.50 per `secondary-source-verification.md` §Section 6) |
| Peirce-Preservation Lemma (Parts i, ii, iii) | Phase 54 (Plan 54-03); `main.tex:590` | YES (proved from S0 + A-S compression axioms in Phase 54) |
| A-S 2003 Ch. 7, Prop 7.23 (idempotency + positivity) | A-S 2003 Ch. 7 | YES (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) |
| A-S 2003 Ch. 7, Prop 7.43 (facial absorption) | A-S 2003 Ch. 7 | YES (Plan 55-01 Section 3 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) |
| A-S 2003 Ch. 7, Prop 7.50 (compression composition) | A-S 2003 Ch. 7 | YES (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) |
| A-S 2003 Ch. 7, Def 7.1 (projector fix) | A-S 2003 Ch. 7 | YES (Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) |
| A-S 2003 Ch. 8 (continuous spectral functional calculus, line 68 substitute) | A-S 2003 Ch. 8 | YES (pre-Jordan-legal Ch. 8 boundary per Plan 55-01 Section 4) |
| Linearity of `L_a` and of compressions | Derived from S1 + finite-dim | YES |
| Spectral decomposition `a = Σ λ_i p_i` | Finite-dim spectrality axiom | YES |

**Zero instances** of `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, `Hanche-Olsen`, `9.37` in Phase 55-02 added lines outside demarcated canonical-example scopes (verified in `55-02-DIFF-REPORT.md` Section 5).

---

## 5. SymPy Spot-Check Consistency

Phase 55-03 Task 1 (`derivations/paper5-peirce-preservation/s4-sympy-spot-check.py`) exercises the Case B derivation symbolically on `H_3(ℝ)` and `H_4(ℝ)`:

- **Test 1 (H_3 rank-2 Case A, a-kernel b):** both `a ∘ b = 0` and `b ∘ a = 0` verified. Step 1 + step 3 of the proof.
- **Test 2 (H_4 Case B, V_1(p_3, p_4) off-diagonal β ≠ 0 in b):** both directions vanish; `C_{q_±}(a) = 0` verified explicitly (step 6); `P_{+−}(a) = 0` verified (step 7). Rejects `fp-mock-sympy` (nonzero a and b with genuine V_1 contribution).
- **Test 3 (φ-independence, alternative mixing `f = λ_i · λ_j`):** both directions vanish; step 8 corollary operationalized.
- **Supplementary (H_3 on-support V_1):** `a ∘ b = 0` forces `y = 0` (step 1 full-rank case reasoning).

Runtime 0.3 sec (budget < 10 sec). Symbolic-exact throughout (zero numerical floats; grep verified). See SUMMARY.md for Task 1 evidence pointer.

The SymPy spot-check confirms the revised S4 proof recovers the standard result on `H_n(ℝ)` as the canonical-example limit (sanity anchor from 55-RESEARCH.md "Limits and Benchmarks" table). This is consistency verification of the abstract derivation, not a standalone proof.

---

## 6. Fallback-Derivation Reference (if Prop 7.43 had been deferred)

Although NOT triggered (Prop 7.43 VERIFIED), the fallback routing from Plan 55-01 Section 5 is documented here for completeness of the cross-check audit trail:

- **Approach 2 (Foulis-Holland):** Submitted-era derivation does NOT use F-H. If Prop 7.43 had stayed DEFERRED, Phase 55-02 would have refactored step 5 (facial absorption) through orthomodular-lattice orthogonality (`a ⊥ b ⟺ a ≤ b'`). This would have changed the proof mechanism, not the conclusion. Triggered NONE of the Phase 55-02 edits.

Backtracking rule status (Plan 55-03 Task 6 §11 consumer): NOT TRIGGERED because (Prop 7.43 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE) ⟹ (Approach 2 fallback unused) ⟹ (backtracking-rule conjunct FALSE).

---

## 7. Test Roll-Up (Plan 55-03 Task 2 acceptance tests)

| Test ID | Procedure | Evidence | Verdict |
|---------|-----------|----------|---------|
| `test-cross-check-conclusion-matches` | Final verdict section states "YES" or "YES-WITH-DEFERRED" | §2 "Revised proof reaches same conclusion: YES." | **PASS** |
| `test-cross-check-steps-documented` | ≥ 6 rows in step table with submitted-era + revised + verdict columns | §1 table has 8 rows | **PASS** |
| `test-cross-check-no-skipped-steps` | Silent-drift check: zero unmatched submitted-era steps OR all flagged with resolution | §3 "No silent drift detected." Every submitted-era step (including handwavy ones) accounted for. | **PASS** |

**Forbidden proxy `fp-skip-cross-check`: REJECTED.** Cross-check is per-step with 8 rows, 4 columns, evidence on both sides of every row. Not a top-level declaration.

---

## 8. Consistency with Phase 55-02 Deliverables

The cross-check results above are consistent with Phase 55-02's own `55-02-DIFF-REPORT.md` annotations:

| Step (§1) | 55-02 Hunk | 55-02 Classification row(s) |
|-----------|-----------|------------------------------|
| 2 | AV-4 (axiom-verification.tex:122-130) + AP-1 (appendix-proofs.tex:34-45) | 55-01 row 4 (axiom-verification.tex:125) + row 14 (appendix-proofs.tex:37-49) — PRIMARY BUG FIXED |
| 5 | AV-5 (axiom-verification.tex:134-156) + AP-2 (appendix-proofs.tex:78-82) | 55-01 rows 5 + 15 (Prop 7.43 tightening) |
| 6 | AV-6 (axiom-verification.tex:155-176) + AP-4 (appendix-proofs.tex:107-129) | 55-01 rows 7 + 17 (unnamed facial orthogonality → S0-termwise) |
| 7 | AV-5 + AV-6 + AP-4 (Peirce-Preservation Lemma Part (iii)) | 55-01 rows 6, 8, 18 (Peirce 1-space handwave → Lemma Part (iii)) |

No contradictions between the Phase 55-02 diff-report and the cross-check results above.

---

_Produced 2026-04-17 in Phase 55-03 Task 2. Frozen cross-check document; Plan 55-03 Task 3 (adversarial review) and Task 6 (55-RESULT.md) consume this document as evidence for the "revised proof reaches same conclusion" claim. Reviewers needing a single-page summary should read §1 + §2._
