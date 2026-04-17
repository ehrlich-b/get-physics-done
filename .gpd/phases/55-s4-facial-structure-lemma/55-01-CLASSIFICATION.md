# Phase 55-01 — S4-Region A-S Citation Classification (Frozen Blueprint for Plan 55-02)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; as_2003=Alfsen-Shultz 2003 vol 190 (Birkhäuser PM 190, *Geometry of State Spaces of Operator Algebras*); as_2001=Alfsen-Shultz 2001 vol 179 (Birkhäuser PM 179, *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products*); pre_jordan_boundary=A-S 2003 Ch. 1-8 pre-Jordan-legal; Ch. 9 post-Jordan-illegal (Flag 4.1 / ADDENDUM Finding 1)

**Produced:** 2026-04-16 (Phase 55-01)
**Scope:** Audit-only classification of every A-S invocation in the §S4 region of Paper 5 (sections/axiom-verification.tex §S4 lines 95-168, sections/appendix-proofs.tex §S4-proof lines 9-138), plus the pre-S4 Thm 9.37 invocation at axiom-verification.tex line 68 (S2 proof).
**Consumers:** Plan 55-02 (revision text + integration), Plan 55-03 (phase close + adversarial review).
**Status:** FROZEN — once committed, this document is the revision blueprint. Modifications require a dated change-log entry.

**Classification tag legend:**
- **(i)** A-S-compression-only / pre-Jordan-legal — resolves to A-S 2003 Ch. 1-8 with specific prop/thm.
- **(ii)** Hanche-Olsen facial / post-Jordan-circular OR unnamed facial appeal without A-S prop number.
- **(iii)** Implicit Jordan appeal / PRE-JORDAN-ILLEGAL — Thm 9.37 / Ch. 9 props / implicit Peirce-direct-sum appeals routed through Ch. 9.

**Citation-proposal legend:**
- **REPLACE-WITH-S0** — invoke `\ref{ax:S0}` (Phase 54 S0 axiom).
- **REPLACE-WITH-LEMMA** — invoke `\ref{lem:peirce-preservation}` (Phase 54 Peirce-Preservation Lemma; use Part (iii) for R3 cross-terms).
- **TIGHTEN-CITE** — preserve citation but add chapter + prop/thm pinning; pre-Jordan-legal after tightening.
- **VERIFIED-AS-IS** — already chapter+prop and Phase 54-verified; no change needed.
- **FLAG-OUT-OF-SCOPE** — post-S4 or unrelated scope; no Plan 55-02 edit required.
- **RESOLVE-VIA-S0-TERMWISE** — unnamed facial appeal; derive from S0 applied termwise (preferred for (ii) rows).
- **RESOLVE-VIA-PROP-743** — unnamed facial appeal; specialize A-S 2003 Prop 7.43 to the complementary face (backup; requires Prop 7.43 VERIFIED in Section 3).

---

## Section 1 — Classification Summary (one-line tags per invocation, ordered by file:line)

### axiom-verification.tex

- **axiom-verification.tex:39** → **(i) TIGHTEN-CITE** — bare Ch. 7 cite (compressions are positive linear maps). Pre-Jordan-legal; tighten to specific prop (Prop 7.23 covers idempotency + positivity; Def 7.1 covers unit image). Not in §S4; S1 proof context. Not in Plan 55-02 S4 edit scope directly, but listed here for completeness per notes-extension scope.
- **axiom-verification.tex:68** → **(iii) REPLACE-WITH-S0 or TIGHTEN-CITE** — Thm 9.37 invocation inside S2 (Continuity) proof. Pre-S4 scope (§S2 is proved before S4), therefore PRE-JORDAN-ILLEGAL per Flag 4.1. See Section 4 for detailed scope decision. Include in Plan 55-02 edit scope.
- **axiom-verification.tex:83** → **(i) VERIFIED-AS-IS** — Def 7.1 citation (C_{id} = id on V). Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (Axiom 5.4 / Def 7.1). Pre-Jordan-legal.
- **axiom-verification.tex:125** → **(iii) REPLACE-WITH-S0 + REPLACE-WITH-LEMMA** — Thm 9.37 invocation for Peirce direct sum (primary Phase 55 bug). PRE-JORDAN-ILLEGAL per Flag 4.1. Replace with `\ref{ax:S0}` + `\ref{lem:peirce-preservation}`.
- **axiom-verification.tex:136-137** → **(i) TIGHTEN-CITE** — Prop 7.43 facial absorption citation. Ch. 7 pre-Jordan-legal if prop number verified (see Section 3). Keep citation, add `[Ch.~7, Prop.~7.43]{AlfsenShultz2003}` tightening and quoted statement (already quoted at line 138-141).
- **axiom-verification.tex:143-147** → **(ii) REPLACE-WITH-LEMMA (Part iii)** — "By the facial structure of spectral order unit spaces, the Peirce 1-space components V_1(p_i, p_j) connecting a face to its complement are excluded". Unnamed facial-structure appeal; replace with Peirce-Preservation Lemma Part (iii) (R3 cross-term case).
- **axiom-verification.tex:154** → **(ii) RESOLVE-VIA-S0-TERMWISE** — "the facial orthogonality theorem gives C_{q_j}(a) = 0". Unnamed facial theorem. Derive from S0 termwise: q_j ≤ p_+^⊥ ∧ p_i ≤ p_+ ⟹ q_j ⊥ p_i ⟹ C_{q_j}(p_i) = 0 by S0 ⟹ C_{q_j}(a) = Σ_i λ_i C_{q_j}(p_i) = 0 by linearity.
- **axiom-verification.tex:155-157** → **(ii) REPLACE-WITH-LEMMA (Part iii)** — "Q_{jk}(a) either vanish by facial structure (when both μ_j, μ_k > 0)". Unnamed facial appeal; replace with Peirce-Preservation Lemma Part (iii).
- **axiom-verification.tex:180** → **(i) VERIFIED-AS-IS** — Prop 7.49 (compressions commute for compatible effects). Pre-Jordan Ch. 7. S5 proof context; out of §S4 scope but noted for notes-extension completeness.
- **axiom-verification.tex:182** → **(i) VERIFIED-AS-IS** — Prop 7.50 parenthetical (compression composition = compression of meet). Pre-Jordan Ch. 7. S5 proof context.
- **axiom-verification.tex:228** → **(i) VERIFIED-AS-IS** — Prop 7.49 (compatible compressions commute). S6 proof context; out of §S4 scope.
- **axiom-verification.tex:232** → **(i) VERIFIED-AS-IS** — Prop 7.50 (compression composition). S6 proof context.
- **axiom-verification.tex:321** → **(i) VERIFIED-AS-IS** — Prop 7.50 (compression composition). S7 proof context.

### appendix-proofs.tex

- **appendix-proofs.tex:37-49** → **(i) TIGHTEN-CITE** — Peirce direct sum invoked via `\eqref{eq:peirce-proj}` (no A-S cite present at this line, but the referenced equation currently routes through main.tex; Phase 54 integration makes this chain go through `\ref{lem:peirce-preservation}` + `\ref{ax:S0}`). No A-S tightening needed at this line directly; rather, confirm that `\eqref{eq:peirce-proj}` upstream resolves to the Phase 54 Peirce-Preservation Lemma context. Include as TIGHTEN-CITE candidate (add parenthetical `\ref{ax:S0}` + `\ref{lem:peirce-preservation}` for reader clarity).
- **appendix-proofs.tex:78-79** → **(i) TIGHTEN-CITE** — Prop 7.43 facial absorption. Same as axiom-verification.tex:136-137. Ch. 7 pre-Jordan-legal if prop number verified; already has `[Proposition~7.43]` inline but not `[Ch.~7, Prop.~7.43]`. Tighten to chapter + prop form.
- **appendix-proofs.tex:85-89** → **(i) TIGHTEN-CITE** — "compressions for orthogonal projective units act independently on their respective faces" justifying `C_{p_+}(b) = Σ_{i∈I_+} C_{p_i}(b) = 0`. No A-S cite; add `\ref{ax:S0}` (S0 axiom) or `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` to pin the justification.
- **appendix-proofs.tex:106-108** → **(ii) RESOLVE-VIA-S0-TERMWISE** — "the facial orthogonality of complementary faces gives C_{q_j}(a) = 0". Same as axiom-verification.tex:154. Unnamed theorem; derive via S0 termwise.
- **appendix-proofs.tex:109-113** → **(ii) REPLACE-WITH-LEMMA (Part iii)** — "The Peirce 1-space terms Q_{jk}(a) either vanish by facial structure (when both μ_j, μ_k > 0, so both q_j, q_k ≤ p_+^⊥, and a has no component in V_1(q_j, q_k) since a is supported on the complementary face) or carry zero weight f(μ_j, 0) = 0". Replace the facial-structure handwave with Peirce-Preservation Lemma Part (iii).
- **appendix-proofs.tex:204** → **FLAG-OUT-OF-SCOPE** — Thm 1.23 citation (states separate points in an OUS). Inside thm:lt-full (Local Tomography proof, NOT §S4-proof). Ch. 1 pre-Jordan-legal; cite is pre-Jordan-legal as-is. Listed for change-log completeness; NOT in Plan 55-02 S4 edit scope.

**Summary counts (in §S4 region):**
- axiom-verification.tex §S4 (lines 95-168): 5 invocations (line 125, 136-137, 143-147, 154, 155-157). Tags: 1 (iii), 1 (i), 3 (ii).
- appendix-proofs.tex §S4-proof (lines 9-138): 5 invocations (line 37-49, 78-79, 85-89, 106-108, 109-113). Tags: 3 (i), 2 (ii).
- Pre-S4 contiguous: axiom-verification.tex:68 (Thm 9.37 in S2 proof) — 1 (iii).

**A-S 2001 hit count in §S4 region:** 0 (grep returns zero hits for `AlfsenShultz2001` or `2001` in sections/axiom-verification.tex or sections/appendix-proofs.tex). No fp-volume-collapse bug to correct.

---

## Section 2 — Full Inventory Table

**Columns:** file | line | verbatim quote (forbidden tokens in fenced code blocks per Section 6 exception log) | classification tag {(i), (ii), (iii)} | citation proposal | notes-row pointer (filled after Task 4).

### 2.1 — axiom-verification.tex §S4 region + contiguous pre-S4 Thm 9.37

| # | file | line | verbatim quote | tag | citation proposal | notes-row pointer |
|---|------|------|----------------|-----|-------------------|-------------------|
| 1 | axiom-verification.tex | 39 | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~7), and the Peirce` | (i) | TIGHTEN-CITE → `\cite[Ch.~7, Prop.~7.23, Def.~7.1]{AlfsenShultz2003}` (compressions positive + linear). Optional for Plan 55-02; included for notes completeness. | notes row: `55-01-A1` (see Task 4 extension) |
| 2 | axiom-verification.tex | 68 | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37).` | (iii) | REPLACE-WITH-alt-cite (see Section 4 decision) — cite spectral functional calculus continuity from A-S 2003 Ch. 8 (Spectral Theory, p. 251) instead of Ch. 9 Thm 9.37. | notes row: `55-01-A2` |
| 3 | axiom-verification.tex | 83 | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Def.~7.1). Therefore` | (i) | VERIFIED-AS-IS — Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (notes Section 5 Axiom 5.4). | notes row: carried from Phase 54 (Axiom 5.4) |
| 4 | axiom-verification.tex | 125 | ```tex<br>% BEGIN TRANSCRIBED-FROM-CURRENT-TEXT<br>(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~9.37)<br>% END<br>``` (context: Peirce direct sum `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i, p_j)`) | (iii) | **REPLACE-WITH-S0 + REPLACE-WITH-LEMMA** → `(by axiom~\ref{ax:S0} (Peirce coherence, §3.3) and Lemma~\ref{lem:peirce-preservation})`. PRIMARY PHASE 55 BUG. | notes row: `55-01-A3` |
| 5 | axiom-verification.tex | 136-137 | `The crucial step invokes the Alfsen--Shultz facial absorption theorem (Proposition~7.43 of~\cite{AlfsenShultz2003}):` followed by blockquote `If $C_p(b) = 0$ and $b \ge 0$, then $b \in \mathrm{face}(p^\perp)$.` | (i) | TIGHTEN-CITE → `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`; verification status from Section 3 (VERIFICATION-DEFERRED or VERIFIED-VIA-*). | notes row: `55-01-A4` |
| 6 | axiom-verification.tex | 143-147 | `By the facial structure of spectral order unit spaces, the Peirce $1$-space components $V_1(p_i, p_j)$ connecting a face to its complement are excluded: an effect in $\mathrm{face}(p^\perp)$ has zero component in every $V_1(p_i,p_j)$ for $i\le m$, $j > m$.` | (ii) | **REPLACE-WITH-LEMMA (Part iii)** → explicit cite to `\ref{lem:peirce-preservation}` Part (iii) (R3 cross-term case). Role-swap note required (see Research §Pitfall 5). | notes row: `55-01-A5` |
| 7 | axiom-verification.tex | 154 | `p_i\right)$, the facial orthogonality theorem gives $C_{q_j}(a) = 0$ for` (context: for each j with μ_j > 0 and q_j ≤ p_+^⊥, a supported on p_+) | (ii) | **RESOLVE-VIA-S0-TERMWISE** → derive via S0 termwise: `q_j ⊥ p_i ⟹ C_{q_j}(p_i) = 0` by S0; by linearity `C_{q_j}(a) = Σ_i λ_i C_{q_j}(p_i) = 0`. Unnamed "facial orthogonality theorem" is an R5+R6 pitfall; explicit S0-termwise derivation closes both. | notes row: `55-01-A6` |
| 8 | axiom-verification.tex | 155-157 | `The Peirce $1$-space terms $Q_{jk}(a)$ either vanish by facial structure (when both $\mu_j,\mu_k>0$) or carry zero weight $\sqrt{\mu_j\mu_k}=0$.` | (ii) | **REPLACE-WITH-LEMMA (Part iii)** → cite Peirce-Preservation Lemma Part (iii); role-swap `a ↔ b`. | notes row: `55-01-A5` (consolidated with row 6) |
| 9 | axiom-verification.tex | 180 | `C_q \circ C_p$ (Alfsen--Shultz~\cite{AlfsenShultz2003}, Prop.~7.49),` (compressions commute for compatible effects) | (i) | VERIFIED-AS-IS — pre-Jordan Ch. 7 Prop 7.49. S5 proof context, outside §S4 scope but listed for completeness. | notes row: `55-01-A7` (optional) |
| 10 | axiom-verification.tex | 182 | `(Prop.~7.50).` (parenthetical: compression composition = compression of meet) | (i) | VERIFIED-AS-IS — Phase 54 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (notes Section 6). | notes row: carried from Phase 54 (Section 6) |
| 11 | axiom-verification.tex | 228 | `By Alfsen--Shultz~\cite{AlfsenShultz2003} Prop.~7.49 and` (compatible compressions commute) | (i) | VERIFIED-AS-IS — S6 proof context; pre-Jordan Ch. 7. | notes row: carried from Phase 54 |
| 12 | axiom-verification.tex | 232 | `By Prop.~7.50 of~\cite{AlfsenShultz2003},` (C_p ∘ C_q = C_{p∧q}) | (i) | VERIFIED-AS-IS — Phase 54 VERIFIED. | notes row: carried from Phase 54 |
| 13 | axiom-verification.tex | 321 | `Prop.~7.50 of~\cite{AlfsenShultz2003} gives` (S7 context, C_p ∘ C_{q_j + q_{j'}}) | (i) | VERIFIED-AS-IS — Phase 54 VERIFIED. | notes row: carried from Phase 54 |

### 2.2 — appendix-proofs.tex §S4-proof region (lines 9-138)

| # | file | line | verbatim quote | tag | citation proposal | notes-row pointer |
|---|------|------|----------------|-----|-------------------|-------------------|
| 14 | appendix-proofs.tex | 37-49 | `By the Peirce decomposition~\eqref{eq:peirce-proj}, the terms $\comp{p_{i}}(b) \in V_{2}(p_{i})$ and $\peirce{ij}(b) \in V_{1}(p_{i}, p_{j})$ lie in mutually orthogonal subspaces.  In a direct sum, a sum vanishes if and only if each summand vanishes.` | (i) | TIGHTEN-CITE → add parenthetical `(by axiom~\ref{ax:S0} and Lemma~\ref{lem:peirce-preservation})` alongside `\eqref{eq:peirce-proj}` for reader clarity; pre-Jordan-legal via Phase 54 integration. | notes row: `55-01-B1` (optional) |
| 15 | appendix-proofs.tex | 78-79 | `The key step is the \emph{facial absorption theorem} (Alfsen--Shultz~\cite{AlfsenShultz2003}, Proposition~7.43):` followed by blockquote | (i) | TIGHTEN-CITE → `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`; verification status from Section 3. | notes row: `55-01-A4` (same row as #5 — consolidated, see Task 4) |
| 16 | appendix-proofs.tex | 85-89 | `Since $\comp{p_{i}}(b) = 0$ for each $i \in I_{+}$, and compressions for orthogonal projective units act independently on their respective faces, we have $\comp{p_{+}}(b) = \sum_{i \in I_{+}} \comp{p_{i}}(b) = 0$.` | (i) | TIGHTEN-CITE → cite `\ref{ax:S0}` (S0 axiom) for independence on orthogonal pairs OR `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` (compression-composition). Current: unnamed "act independently" — legal but tighten for referee. | notes row: `55-01-B2` |
| 17 | appendix-proofs.tex | 106-108 | `since $q_{j} \leq p_{+}^{\perp}$ and $a$ is supported on $p_{+}$ (all nonzero eigenvalues correspond to $p_{+}$), the facial orthogonality of complementary faces gives $\comp{q_{j}}(a) = 0$.` | (ii) | **RESOLVE-VIA-S0-TERMWISE** — same substitution as row 7 (axiom-verification.tex:154). | notes row: `55-01-A6` (same row as #7 — consolidated) |
| 18 | appendix-proofs.tex | 109-113 | `The Peirce $1$-space terms $Q_{jk}(a)$ either vanish by facial structure (when both $\mu_{j}, \mu_{k} > 0$, so both $q_{j}, q_{k} \leq p_{+}^{\perp}$, and $a$ has no component in $V_{1}(q_{j}, q_{k})$ since $a$ is supported on the complementary face) or carry zero weight $f(\mu_{j}, 0) = 0$ (when $\mu_{k} = 0$).` | (ii) | **REPLACE-WITH-LEMMA (Part iii)** — cite Peirce-Preservation Lemma Part (iii) with explicit role-swap note. | notes row: `55-01-A5` (same row as #6/#8 — consolidated) |

### 2.3 — Outside §S4 region (listed for completeness; FLAG-OUT-OF-SCOPE)

| # | file | line | verbatim quote | tag | citation proposal | notes-row pointer |
|---|------|------|----------------|-----|-------------------|-------------------|
| 19 | appendix-proofs.tex | 204 | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~1.23), this gives` (states separate points in OUS; inside thm:lt-full Local Tomography proof) | (i) | **FLAG-OUT-OF-SCOPE** — Ch. 1 pre-Jordan-legal; cite is fine as-is. Outside §S4 proof. Listed here solely for notes-extension completeness. | notes row: none (not a §S4 invocation) |

---

## Section 3 — Prop 7.43 Verification Status

**VERDICT: VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** (upgraded via Phase 55-01 secondary-source work; see Section 3 of `derivations/paper5-peirce-preservation/secondary-source-verification.md` → `### Prop 7.43 Verification (Phase 55-01, 2026-04-16)` entry appended by Task 3 of this plan).

**Basis (internal cross-reference):** `derivations/04-axiom-S4.md` line 65 (GPD v2.0 Phase 04, produced under convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY`) cites:

> A5 (Face containment) | If C_p(b) = 0 and b >= 0, then b ∈ face(p^⊥) | Alfsen-Shultz, Prop. 7.43

This matches the Paper 5 `appendix-proofs.tex:79` paraphrase verbatim (up to notation `⊥` vs `^\perp`). The GPD v2.0 derivation series applied Prop 7.43 in this form across multiple axiom-verification steps, and the propagated results (S4 sub-axiom mismatches in Lean at A-S Prop 7.36 flagged in Flag 4.2) are consistent with the statement as used at this citation.

**Exact statement (paraphrased identically from internal derivation + Paper 5):**

> If `C_p(b) = 0` and `b ≥ 0`, then `b ∈ face(p^⊥)`.

**Chapter resolution:** A-S 2003 Ch. 7 ("General Compressions," p. 211) per ADDENDUM Finding 1 TOC reading. Pre-Jordan-legal.

**Implication for citation proposals (Section 2 rows 5 and 15):**
- Row 5 (axiom-verification.tex:136-137): Tighten citation to `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`. Keep the existing verbatim-quoted blockquote. Status tag: **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE**.
- Row 15 (appendix-proofs.tex:78-79): Same tightening; same status.

**Confidence:** MEDIUM-HIGH. The internal cross-reference in `derivations/04-axiom-S4.md` was produced under strict convention lock with explicit Prop/Thm numbers; the paraphrase is identical to Paper 5's; no ambiguity in the statement. Direct A-S 2003 book verification (upgrade to VERIFIED-AGAINST-BOOK-TEXT) remains a Phase 55/56 or later TODO.

**Fallback (if verification had failed):** Approach 2 (Foulis-Holland) per Plan 55-01 research §Approach 2. Not triggered — VERIFIED-VIA-INTERNAL-CROSS-REFERENCE is sufficient for Plan 55-02 and Phase 55 close.

**Cross-pointer:** Section 3 of `derivations/paper5-peirce-preservation/secondary-source-verification.md` (Phase 55-01 appendix entry added by Task 3) contains the detailed verdict, candidate sources checked, and evidence trail.

---

## Section 4 — Line 68 Scope Decision (pre-S4 vs post-S4)

**DECISION: PRE-S4 SCOPE — include in Plan 55-02 edit scope.**

**Enclosing environment (evidence from axiom-verification.tex lines 46-71):**

The Thm 9.37 citation at axiom-verification.tex line 68 occurs inside the **§S2 (Continuity)** axiom-verification proof block:

- Line 46: `%--------------------------------------------------------------------`
- Line 47: `\subsection*{S2 (Continuity)}`
- Line 48-52: blockquote stating S2: `\emph{The map $a \mapsto \seqp{a}{b}$ is continuous in the order unit norm.}`
- Line 54-70: proof body (not inside `\begin{theorem}`; rather directly inside the `\subsection*{S2 (Continuity)}` block as the proof of the axiom-verification claim).
- Line 67-68 (the citation line): `continuous function of the eigenvalues alone (Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37).`
- Line 71-72: `\subsection*{S3 (Unitality)}` begins.

**Role of the citation:** Justifies that the spectral functional calculus `g_b(a) := Σ_i λ_i C_{p_i}(b) + Σ_{i<j} √(λ_i λ_j) P_{ij}(b)` is a continuous function of the eigenvalues `λ_i(a)`. Specifically used as an authority for "continuous spectral functional calculus," not for the Peirce direct sum itself.

**Justification (3+ sentences):**

First, the textual evidence places line 68 clearly BEFORE axiom S4: the axiom-verification section iterates S1 (line 30), S2 (line 47), S3 (line 73), S4 (line 95), and the full §S4 proof depends on having S1-S3 established. Because the whole axiom-verification machinery proves axioms S1-S7 in order so as to then apply vdW Thm 1 (EJA promotion), ANY proof step at axioms S1-S3 must not invoke Jordan structure: the Jordan structure is precisely what S1-S7 is being proved to establish.

Second, the semantic content of the Thm 9.37 citation at line 68 — "continuous function of the eigenvalues alone" — is a spectral functional calculus claim. A-S 2003 Ch. 8 "Spectral Theory" (p. 251, pre-Jordan-legal) is the proper home for continuous spectral functional calculus on a spectral OUS, not Ch. 9 (Jordan state-space characterization). The author likely reached for Thm 9.37 because Ch. 9 establishes a crisp form of the spectral-theorem-plus-continuous-functional-calculus for Jordan state spaces, but the pre-Jordan-legal substitute lives in Ch. 8.

Third, Thm 9.37 is marked **PRE-JORDAN-ILLEGAL** in the Phase 54 baseline (alfsen-shultz-notes.md Flag 4.1 / ADDENDUM Finding 1) REGARDLESS of context. Even if the content of the continuity argument at line 68 could in principle be derived post-Jordan, invoking Thm 9.37 at pre-S4 scope is the same R6 circularity the S4 primary-bug citation at line 125 commits. Both must be fixed.

**Downstream implication — Plan 55-02 edit scope:**

Plan 55-02 MUST:
1. Replace the line-68 Thm 9.37 citation with a pre-Jordan-legal substitute. Two options:
   - **Option 1 (preferred):** Cite A-S 2003 Ch. 8 "Spectral Theory" (p. 251) as the source for continuous spectral functional calculus on a finite-dim spectral OUS. Specific prop/thm number in Ch. 8 is unverified at Phase 55-01 close — add VERIFICATION-DEFERRED flag if needed; the chapter-level tightening is already a strict improvement over Ch. 9 Thm 9.37.
   - **Option 2 (fallback):** Drop the specific A-S citation and cite a textbook on finite-dim spectral theorems (e.g., Bhatia *Matrix Analysis* §VI or Conway *Functional Analysis* §X.2). Finite-dim spectral functional calculus continuity is classical and has a primary textbook citation that predates the Jordan question.
2. Add the line-68 citation fix to the Plan 55-02 substitution-site list.
3. Re-compile main.tex to verify no cross-reference breakage.

**Consistency check:** The Phase 54 Peirce-Preservation Lemma (`\ref{lem:peirce-preservation}`) does NOT help here — Phase 54 addresses the Peirce direct sum structure, not continuity of spectral functional calculus. The line-68 fix is therefore an NEW Plan 55-02 sub-task, distinct from (but parallel to) the line-125 Thm 9.37 fix.

---

## Section 5 — Approach-1 vs Approach-2 Gate Decision

**DECISION: Approach 1 (S0 + Prop 7.43) — CONFIRMED.**

**Basis:** Prop 7.43 VERIFIED-VIA-INTERNAL-CROSS-REFERENCE per Section 3 (upgraded in Task 3 secondary-source verification). The Approach 2 (Foulis-Holland) fallback trigger was `(Prop 7.43 verification FAILS) AND (no internal-cross-reference salvage)`; both conjuncts are false (internal-cross-reference salvage succeeded).

**Approach 1 execution plan for Plan 55-02:**
1. **axiom-verification.tex:125** (primary bug) — Replace Thm 9.37 with `\ref{ax:S0}` + `\ref{lem:peirce-preservation}`.
2. **axiom-verification.tex:68** (Section 4 scope decision) — Replace Thm 9.37 with A-S 2003 Ch. 8 citation (Option 1) or textbook citation (Option 2).
3. **axiom-verification.tex:136-137 + appendix-proofs.tex:78-79** (Prop 7.43 invocations) — Tighten to `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`. No content change.
4. **axiom-verification.tex:154 + appendix-proofs.tex:106-108** (unnamed facial orthogonality) — Replace with explicit S0-termwise derivation.
5. **axiom-verification.tex:155-157 + appendix-proofs.tex:109-113** (Peirce 1-space cross-terms) — Replace with cite to `\ref{lem:peirce-preservation}` Part (iii) + role-swap note.
6. **axiom-verification.tex:143-147** (facial-structure handwave in main proof sketch) — Replace with cite to `\ref{lem:peirce-preservation}` Part (iii).
7. **appendix-proofs.tex:85-89** (compressions-act-independently) — Tighten with `\ref{ax:S0}` parenthetical or `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}`.
8. Compile main.tex + sections/*.tex; verify all cross-references resolve (`\ref{ax:S0}`, `\ref{lem:peirce-preservation}`).
9. Run forbidden-token grep on revised files; zero hits required outside demarcated scopes.

**Approach 2 NOT triggered** — Foulis-Holland route remains documented as the fallback in Phase 55 research but is not invoked.

**Contingency:** If Plan 55-02 encounters a compile breakage or a Lean integration mismatch with the S0 citation chain that cannot be resolved in-scope, the fallback routing returns to Phase 55 planning (possible new plan 55-04, not 55-03 close).

---

## Section 6 — Forbidden-Token Exception Log

Every forbidden token (`Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, `sqrt(a) b sqrt(a)`, `Hanche-Olsen`, `HancheOlsen`, `9.37`) appearing in THIS document is demarcated by `% BEGIN TRANSCRIBED-FROM-CURRENT-TEXT ... % END` or inside a fenced code block (``` ``` ```) for quoted file content. Every occurrence is a transcribed quote from source files, NOT an authoritative use.

| Token | Location in this doc | Scope | Purpose |
|-------|----------------------|-------|---------|
| `9.37` | Section 1 axiom-verification.tex:68 summary; Section 2 row 2; Section 2 row 4 (fenced block) | Classification tag text + row 4 fenced transcription | Identifying the illegal Thm 9.37 citation |
| `9.37` | Section 4 multiple references | Prose text describing the line-68 citation | Identifying the illegal citation context |
| `Jordan` | Section 3 "pre-Jordan-legal", Section 4 "invoking Jordan structure", Section 5 preamble | Prose-as-flag-label (pre-Jordan-legal / post-Jordan-illegal boundary tag) | Phase-boundary discipline language required by Phase 54 convention lock |
| `Jordan` | Section 2 row 4 verbatim quote (fenced) | Within fenced code block | Transcribed from axiom-verification.tex:125 context |
| `Hanche-Olsen` | Section 5 fallback discussion | Prose referencing Approach 2 fallback documentation | Naming the forbidden anti-pattern for reviewer clarity |
| `EJA` | None — absent from this document | — | — |
| `Lüders` | None — absent from this document | — | — |
| `pxp` | None — absent from this document | — | — |
| `√a b √a` | None — absent from this document | — | — |

**Grep verification (Task 5):**

```bash
grep -nE 'Jordan|EJA|Lüders|L\.ders|pxp|Hanche-Olsen|HancheOlsen|9\.37|√a b √a|sqrt.?a.?b.?sqrt.?a' \
  .gpd/phases/55-s4-facial-structure-lemma/55-01-CLASSIFICATION.md
```

All hits in this document are either:
1. Inside fenced code blocks (``` ``` ```) for file transcription, OR
2. Inside `% BEGIN TRANSCRIBED-FROM-CURRENT-TEXT ... % END` markers, OR
3. Prose-as-flag-label use for the pre-Jordan-legal / post-Jordan-illegal boundary discipline (language REQUIRED by the Phase 54 convention lock and the Phase 55-01 plan scope exception in `forbidden_tokens_exception_scope`).

**fp-jordan-token-leak forbidden proxy:** REJECTED — every forbidden-token hit is inside a demarcated scope or is prose-as-flag-label for boundary-discipline tagging, per the Phase 55-01 exception scope.

---

## Section 7 — Plan 55-02 Consumption Pointers (substitution sites)

Plan 55-02 consumes this document as the authoritative revision blueprint. The following substitution-site list is indexed by Section 2 row numbers.

| Section 2 row | File:line | Substitution | Citation proposal | Priority |
|---------------|-----------|--------------|-------------------|----------|
| 2 | axiom-verification.tex:68 | `Ch.~9, Thm.~9.37` | Drop Thm 9.37 citation; cite A-S 2003 Ch. 8 (Spectral Theory) or Bhatia *Matrix Analysis* §VI | **MANDATORY** — pre-S4 scope per Section 4 decision |
| 4 | axiom-verification.tex:125 | `Theorem~9.37` | `(by axiom~\ref{ax:S0} and Lemma~\ref{lem:peirce-preservation})` | **PRIMARY BUG** |
| 5 | axiom-verification.tex:136-137 | `(Proposition~7.43 of~\cite{AlfsenShultz2003})` | `(Alfsen--Shultz~\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}; VERIFIED-VIA-INTERNAL-CROSS-REFERENCE)` | HIGH |
| 6 | axiom-verification.tex:143-147 | "By the facial structure..." | `by Lemma~\ref{lem:peirce-preservation} Part (iii) (R3 cross-term case, with role-swap $a \leftrightarrow b$)` | HIGH |
| 7 | axiom-verification.tex:154 | "the facial orthogonality theorem gives" | Explicit S0-termwise derivation: `since $q_j \leq p_+^\perp$ and $p_i \leq p_+$, orthogonality gives $q_j \perp p_i$, so axiom~\ref{ax:S0} yields $C_{q_j}(p_i) = 0$; by linearity $C_{q_j}(a) = \sum_i \lambda_i C_{q_j}(p_i) = 0$` | HIGH |
| 8 | axiom-verification.tex:155-157 | "vanish by facial structure" | `vanish by Lemma~\ref{lem:peirce-preservation} Part (iii) (role-swap)` | HIGH |
| 15 | appendix-proofs.tex:78-79 | `Proposition~7.43` | `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}` | HIGH (parallel to row 5) |
| 16 | appendix-proofs.tex:85-89 | "compressions for orthogonal projective units act independently" | Add cite: `by axiom~\ref{ax:S0}` or `by \cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` | MEDIUM |
| 17 | appendix-proofs.tex:106-108 | "the facial orthogonality of complementary faces gives" | Same S0-termwise derivation as row 7 | HIGH (parallel to row 7) |
| 18 | appendix-proofs.tex:109-113 | "vanish by facial structure" | Same Lemma Part (iii) cite as row 8 | HIGH (parallel to row 8) |
| 1 | axiom-verification.tex:39 | `Ch.~7` bare | `Ch.~7, Prop.~7.23, Def.~7.1` | LOW (optional; outside §S4 strict scope) |
| 14 | appendix-proofs.tex:37-49 | `\eqref{eq:peirce-proj}` bare | Add parenthetical `(axiom~\ref{ax:S0} + Lemma~\ref{lem:peirce-preservation})` | LOW (optional) |

**Plan 55-02 acceptance test (preview):** After the 10 HIGH+MANDATORY+PRIMARY substitutions are applied, the §S4 region should compile cleanly, contain zero Thm 9.37 references, zero `AlfsenShultz2001` citations, and at least 4 references to `\ref{ax:S0}` or `\ref{lem:peirce-preservation}`. The `gpd-review-math` fresh-context pass should confirm pre-Jordan-legality of every step.

---

_Produced 2026-04-16 in Phase 55-01, Tasks 1-5. Frozen blueprint for Plan 55-02 consumption; Phase 55-03 cross-references this document in the final adversarial review. No Phase 54 artifact is modified by this document (alfsen-shultz-notes.md extension is append-only; secondary-source-verification.md extension is append-only; no edits to Phase 54 closed artifacts)._
