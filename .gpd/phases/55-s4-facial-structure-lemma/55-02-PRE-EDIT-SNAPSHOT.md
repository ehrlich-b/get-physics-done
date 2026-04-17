# Phase 55-02 Task 1 — Pre-Edit Snapshot (Line-Number Reconciliation)

**Produced:** 2026-04-16 (Phase 55-02 Task 1)
**Scope:** Reconcile line numbers in 55-01-CLASSIFICATION.md Section 2 against the CURRENT state of
`sections/axiom-verification.tex` and `sections/appendix-proofs.tex` (in `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/`).
**Purpose:** Provide authoritative line targets for the Task 2-3 edit passes; verify Phase 54 labels are still present in `main.tex`; record the Approach 1 vs Approach 2 gate verdict.

---

## 1. Line-Number Delta Table

All line numbers in 55-01-CLASSIFICATION.md Section 2 match the current file state (verified by grep against verbatim quotes). **Zero drift.**

### axiom-verification.tex (file currently 378 lines)

| Row | Description | Expected (55-01) | Actual | Delta |
|-----|-------------|-------------------|--------|-------|
| 1 | `Ch.~7` bare cite (S1 proof) | 39 | 39 | 0 |
| 2 | Ch.~9 Thm.~9.37 (S2 Continuity proof) | 68 | 68 | 0 |
| 3 | Def.~7.1 (S3 proof) | 83 | 83 | 0 |
| 4 | Theorem~9.37 (S4 Case A Peirce direct sum) — PRIMARY BUG | 125 | 125 | 0 |
| 5 | Proposition~7.43 (S4 facial absorption) | 136-137 | 136-137 | 0 |
| 6 | "By the facial structure of spectral order unit spaces, the Peirce $1$-space components..." | 143-147 | 143-147 | 0 |
| 7 | "the facial orthogonality theorem gives $C_{q_j}(a) = 0$" | 154 | 154 | 0 |
| 8 | "vanish by facial structure" (Q_{jk}(a)) | 155-157 | 155-157 | 0 |
| 9 | Prop.~7.49 (S5 proof) | 180 | 180 | 0 |
| 10 | Prop.~7.50 parenthetical (S5 proof) | 182 | 182 | 0 |
| 11 | Prop.~7.49 (S6 proof) | 228 | 228 | 0 |
| 12 | Prop.~7.50 (S6 proof) | 232 | 232 | 0 |
| 13 | Prop.~7.50 (S7 proof) | 321 | 321 | 0 |

### appendix-proofs.tex (file currently 238 lines)

| Row | Description | Expected (55-01) | Actual | Delta |
|-----|-------------|-------------------|--------|-------|
| 14 | Peirce direct sum via `\eqref{eq:peirce-proj}` | 37-49 | 37-49 | 0 |
| 15 | Prop 7.43 facial absorption | 78-79 | 78-79 | 0 |
| 16 | "compressions for orthogonal projective units act independently" | 85-89 | 85-89 | 0 |
| 17 | "facial orthogonality of complementary faces" | 106-108 | 106-108 | 0 |
| 18 | "vanish by facial structure" (Q_{jk}(a)) | 109-113 | 109-113 | 0 |
| 19 | Thm 1.23 (Local Tomography proof, OUT-OF-SCOPE) | 204 | 204 | 0 |

**Verification grep evidence:**

```
axiom-verification.tex:
  68:(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37).
  125:(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~9.37)
  137:(Proposition~7.43 of~\cite{AlfsenShultz2003}):
  154:p_i\right)$, the facial orthogonality theorem gives $C_{q_j}(a) = 0$ for
  156:vanish by facial structure (when both $\mu_j,\mu_k>0$) or carry zero

appendix-proofs.tex:
  78: The key step is the \emph{facial absorption theorem}
  79:(Alfsen--Shultz~\cite{AlfsenShultz2003}, Proposition~7.43):
  108:$p_{+}$), the facial orthogonality of complementary faces gives
  110:vanish by facial structure (when both $\mu_{j}, \mu_{k} > 0$,
```

## 2. Phase 54 Label Confirmation (main.tex)

Both Phase 54 labels resolve successfully in `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main.tex`:

| Label | Line | Definition |
|-------|------|-----------|
| `ax:S0` | 537 | `\begin{axiom}[S0, Peirce Coherence (compression level)]\label{ax:S0}` |
| `lem:peirce-preservation` | 590 | `\begin{lemma}[Peirce-Preservation Lemma]\label{lem:peirce-preservation}` |

Both are in the post-Phase-54 `§3.3` integration (preamble.sty adds `\newtheorem{axiom}` declaration). Cross-references from sections/axiom-verification.tex and sections/appendix-proofs.tex via `\ref{ax:S0}` and `\ref{lem:peirce-preservation}` will resolve.

**Circularity Check section (§3.5) location:** `main.tex:845` (`\subsection{Circularity Check}\label{sec:circularity}`). Bullet list at lines 858-868 (order unit space, effect space, Alfsen-Shultz compressions, Peirce decomposition, spectral decomposition, scalar sqrt).

## 3. Approach Gate Verdict

**Verdict extracted from 55-01-CLASSIFICATION.md Section 5:** **Approach 1 CONFIRMED** (S0 + Prop 7.43).

- Prop 7.43 status: VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (not VERIFICATION-DEFERRED).
- Approach 2 (Foulis-Holland) fallback NOT triggered — both conjuncts of the trigger `(Prop 7.43 FAILS) AND (no internal-cross-reference salvage)` are FALSE.
- **Proceed with Task 2-3 (edit application).**

## 4. Read-Only Discipline

This task produces ONLY `55-02-PRE-EDIT-SNAPSHOT.md`. Zero modifications to paper files in Task 1.

- `sections/axiom-verification.tex` untouched (verified: no pending diff in blog repo for this file).
- `sections/appendix-proofs.tex` untouched.
- `main.tex` untouched.
- `main-jmp-submitted.tex` untouched.

## 5. Edit Plan (authoritative targets for Tasks 2-3)

### axiom-verification.tex

| Edit | Line | Action |
|------|------|--------|
| A (PRIMARY) | 125 | Replace `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~9.37)` with `(by Lemma~\ref{lem:peirce-preservation} together with axiom~\ref{ax:S0}; see also \cite[Ch.~7]{AlfsenShultz2003} for the compression-theoretic Peirce direct sum)` |
| B | 154 | Replace "the facial orthogonality theorem gives $C_{q_j}(a) = 0$" with explicit S0-termwise derivation |
| C | 155-157 | Replace "vanish by facial structure" with Lemma Part (iii) cite + role-swap annotation |
| D | 143-147 | Replace "By the facial structure of spectral order unit spaces..." with Lemma Part (iii) cite + role-swap |
| E (MANDATORY) | 68 | Replace Ch.~9 Thm.~9.37 with `\cite[Ch.~8]{AlfsenShultz2003}` (pre-Jordan-legal substitute for continuous spectral functional calculus) |
| F | 136-137 | Tighten Prop 7.43 to `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}` |
| G | 39 | LOW priority — leave `Ch.~7` as-is (pre-Jordan-legal; S1 scope). Skip unless trivial. |
| H | 180 | Tighten Prop 7.49 to `\cite[Ch.~7, Prop.~7.49]{AlfsenShultz2003}` |
| I | 228 | Tighten Prop 7.49 to `\cite[Ch.~7, Prop.~7.49]{AlfsenShultz2003}` |
| J | 232 | Tighten Prop 7.50 to `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` |
| K | 321 | Tighten Prop 7.50 to `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` |
| L | 83 | VERIFIED-AS-IS (Def.~7.1, pre-Jordan-legal; no change) |
| M | 182 | Parenthetical "(Prop.~7.50)" - tighten to `(\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003})` |

### appendix-proofs.tex

| Edit | Line | Action |
|------|------|--------|
| N | 37-49 | Add parenthetical S0 + Lemma cross-reference alongside `\eqref{eq:peirce-proj}` |
| O | 78-79 | Tighten Prop 7.43 to `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}` |
| P | 85-89 | Add `\ref{ax:S0}` or `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` citation |
| Q | 106-108 | Replace "facial orthogonality of complementary faces" with S0-termwise derivation |
| R | 109-113 | Replace "vanish by facial structure" with Lemma Part (iii) cite + role-swap |
| S | 204 | OUT-OF-SCOPE (Local Tomography, Ch. 1 pre-Jordan-legal; no edit) |

### main.tex (optional §3.5 edit)

| Edit | Line | Action |
|------|------|--------|
| T | 858-868 | Add S0 to Circularity Check bullet list (between "effect space" at line 860 and "Alfsen-Shultz compressions" at 861) |

**Corollary `cor:S4-phi-indep` at appendix-proofs.tex:121-137 — DO NOT TOUCH (verbatim preservation per plan).**

## 6. Sanity Check

- [x] All 19 rows of classification Section 2 grep-verify at stated line numbers (zero drift).
- [x] `\ref{ax:S0}` resolves to `main.tex:537` (axiom env declared in preamble.sty).
- [x] `\ref{lem:peirce-preservation}` resolves to `main.tex:590` (lemma env standard).
- [x] Approach 1 confirmed; no halt.
- [x] Zero paper-file modifications in Task 1 (read-only discipline maintained).
- [x] `main-jmp-submitted.tex` untouched throughout (no git diff).

**Task 1 COMPLETE.** Task 2 (edit `axiom-verification.tex`) may proceed.
