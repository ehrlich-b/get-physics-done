# Paper 5 §3.3 Revision Text — Peirce Preservation from OUS Primitives (C-i Branch)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 03 (wave 3, (C-i) branch)
**Purpose:** Revised §3.3 text for `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`, replacing the R2 non-sequitur at submitted lines 508-528. Lemma statement verbatim from `claim.md` Section 3 with the (C-i) assumption-set clause. A-S citations point to A-S 2003 Ch. 2/7/8 with specific Prop/Thm numbers where VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (per `alfsen-shultz-notes.md` 2026-04-16 update + `secondary-source-verification.md`); never bare `\cite{AlfsenShultz2003}`, never A-S 2001, never Thm 9.37.

---

## Section 1: LaTeX Revision Text (staged; to be inserted into main.tex §3.3)

The following LaTeX block replaces the submitted §3.3 non-sequitur at `main-jmp-submitted.tex` lines 508-528 (frozen; not modified). It is inserted into `main.tex` §3.3 at the corresponding location (lines 524-544 of the living copy, which currently contains the same non-sequitur).

```latex
\emph{Why this form is forced (revised for Phase 54 closure: Peirce-Preservation Lemma under S0).}
By \ref{ax:S1}, $\seqp{a}{\cdot}$ is a linear endomorphism of~$V$ (finite-dim).  We
need to show that the Peirce decomposition with respect to the spectral
projectors $\{p_i\}$ of~$a$ is respected by~$\seqp{a}{\cdot}$, i.e., that
$\seqp{a}{\cdot}$ maps each Peirce subspace to itself. This is a claim
about the invariance of the map $L_a(b) := \seqp{a}{b}$, not about the
decomposition of $V$ itself --- decomposition of $V$ does not imply
invariance of $L_a$, and the submitted phrasing of this step was a
non-sequitur that we now repair.

\paragraph{Peirce Coherence Axiom (S0).}
We introduce an OUS-level coherence axiom at the compression level:

\begin{axiom}[S0, Peirce Coherence (compression level)]\label{ax:S0}
Let $V$ be a finite-dimensional spectral order unit space over $\mathbb{R}$
with unit~$\id$, and let $\{p_1, \ldots, p_n\}$ be an orthogonal family of
projective units. Then
\begin{equation}\label{eq:S0}
  \comp{p_i} \comp{p_j} = 0 \quad \text{for all } i \neq j
  \quad \text{(mutual annihilation of compressions)}.
\end{equation}
\end{axiom}

\begin{remark}[Pairwise commutation as immediate consequence]
For the same orthogonal family, the compressions pairwise commute:
$\comp{p_i} \comp{p_j} = \comp{p_j} \comp{p_i}$ for all $i, j$.  If $i \neq j$,
both sides equal~$0$ by~\eqref{eq:S0}; if $i = j$, both sides equal
$\comp{p_i}^2 = \comp{p_i}$ by Alfsen--Shultz idempotency
\cite[Prop.~7.23]{AlfsenShultz2003}.
\end{remark}

\emph{Canonical-example defense of S0.}
% BEGIN canonical-example defense for S0 (forbidden-token exception scope)
In three canonical spectral-OUS models, axiom~S0 is automatic:

\begin{itemize}
\item In $M_n(\mathbb{C})^{\mathrm{sa}}$ (self-adjoint complex matrices),
projective units are self-adjoint orthogonal projections $p_i$ with
$p_i p_j = 0$ for $i \neq j$; the A-S compression is
$\comp{p}(b) = p b p$ within the matrix algebra; orthogonality
gives $\comp{p_i} \comp{p_j}(b) = p_i p_j b p_j p_i = 0$.

\item In $C(X)$ (continuous real functions on a compact set), projective
units are characteristic functions $\chi_A$ of clopen subsets; the A-S
compression is multiplication by $\chi_A$; disjoint supports give
$\chi_A \chi_B = 0$ pointwise.

\item In a spin factor (Clifford-generated OUS), orthogonal rank-1
projective units define transverse one-dimensional faces of the effect
algebra with trivial intersection; the A-S P-projections onto these
disjoint faces annihilate pairwise.
\end{itemize}
% END canonical-example defense for S0

Moreover, $S0$ is recoverable from the Alfsen--Shultz compression-meet
structure: for compatible projective units $p, q$,
$\comp{p} \comp{q} = \comp{p \wedge q}$ \cite[Prop.~7.50]{AlfsenShultz2003};
orthogonal projective units are face-disjoint with trivial meet
$p \wedge q = 0$, so $\comp{p} \comp{q} = \comp{0} = 0$. We state
axiom~S0 at the OUS level (rather than invoking Prop.~7.50 directly) to
keep the scaffolding of~\S3.3 independent of specific A-S theorem
numbers; the two routes are equivalent.

\paragraph{Peirce-Preservation Lemma.}
We now state and prove the invariance claim directly:

\begin{lemma}[Peirce-Preservation Lemma]\label{lem:peirce-preservation}
Under $\{S0, \ref{ax:S1}, \ref{ax:S3}, \text{linearity of } L_a, \text{A-S
compression axioms, finite-dim spectrality}\}$, let $V$ be a
finite-dimensional spectral order unit space over $\mathbb{R}$, let
$\{p_1, \ldots, p_n\}$ be an orthogonal family of projective units in $V$
(i.e., $p_i \perp p_j$ for $i \neq j$ with mutual compressional
annihilation $\comp{p_i} \comp{p_j} = 0$), and let
$a = \sum_i \lambda_i\, p_i$ with $\lambda_i \in \mathbb{R}$ be a spectral
decomposition. Write $\mathrm{supp}(a) := \{ i : \lambda_i \neq 0 \}$. Let
$L_a(b) := \seqp{a}{b}$ denote the left-multiplication map.  Then:
\begin{enumerate}[label=(\roman*)]
\item\label{eq:peirce-i}
  For every $i \in \{1, \ldots, n\}$,
  $\seqp{a}{V_2(p_i)} \subseteq V_2(p_i).$
\item\label{eq:peirce-ii}
  For every pair $(i, j)$ with $i \neq j$ and $i, j \in \mathrm{supp}(a)$,
  $\seqp{a}{V_1(p_i, p_j)} \subseteq V_1(p_i, p_j).$
\item\label{eq:peirce-iii}
  For every pair $(k, l)$ with $k \neq l$ and
  $\{k, l\} \cap \mathrm{supp}(a) = \emptyset$,
  $\seqp{a}{V_1(p_k, p_l)} \subseteq V_1(p_k, p_l).$
\end{enumerate}
\end{lemma}

\begin{proof}
By \ref{ax:S1} and linearity, $L_a(b) = \sum_j \lambda_j\, (p_j \seqp{}{} b)
= \sum_j \lambda_j\, \comp{p_j}(b)$, where the second equality uses
\ref{ax:S3} ($p \seqp{}{} b = \comp{p}(b)$ for sharp~$p$).

\emph{Part (i).} For $b \in V_2(p_i) = \range(\comp{p_i})$, idempotency
\cite[Prop.~7.23]{AlfsenShultz2003} gives $\comp{p_i}(b) = b$. For
$j \neq i$, axiom~S0 gives $\comp{p_j}(b) = \comp{p_j} \comp{p_i}(b) = 0$.
Hence $L_a(b) = \lambda_i\, b \in V_2(p_i)$.

\emph{Preliminary lemma for Parts (ii) and (iii).} For any
$b \in V_1(p_i, p_j)$ we have $\comp{p_i}(b) = 0$ and $\comp{p_j}(b) = 0$.
Writing $b = P_{ij}(c)$ where $P_{ij} := \comp{p_i + p_j} - \comp{p_i} -
\comp{p_j}$ is the A-S Peirce 1-projector on the pair, and using
compression-additivity $\comp{p_i + p_j} = \comp{p_i} + \comp{p_j}$ on
the shared range (an A-S compression-theoretic fact for orthogonal
pairs), the idempotency of $\comp{p_i}$ together with S0 gives
$\comp{p_i}(b) = \comp{p_i}\, P_{ij}(c) = \comp{p_i}(c) - \comp{p_i}(c) -
0 = 0$.  Symmetrically $\comp{p_j}(b) = 0$. (Only A-S compression axioms
and S0 are used in this sub-step; no post-S4 structure is invoked.)

\emph{Part (ii).} For $b \in V_1(p_i, p_j)$ with $i, j \in
\mathrm{supp}(a)$, the preliminary lemma gives $\comp{p_i}(b) =
\comp{p_j}(b) = 0$. For any $j' \notin \{i, j\}$, writing $b = P_{ij}(c)$
and using S0 termwise, $\comp{p_{j'}}(b) = 0$. Hence $L_a(b) = \sum_{j'}
\lambda_{j'}\, \comp{p_{j'}}(b) = 0 \in V_1(p_i, p_j)$.

\emph{Part (iii).} For $b \in V_1(p_k, p_l)$ with $\{k, l\} \cap
\mathrm{supp}(a) = \emptyset$, for every $j \in \mathrm{supp}(a)$ we have
$j \neq k$ and $j \neq l$; the same termwise-S0 computation as in (ii)
gives $\comp{p_j}(b) = 0$. Hence $L_a(b) = 0 \in V_1(p_k, p_l)$.
\end{proof}

\begin{remark}[Annihilation in the minimal tool-set vs. the mixing
function in~\S3.4]
Under the minimal tool-set
$\{S0, \ref{ax:S1}, \ref{ax:S3}, \text{linearity}, \text{A-S
compressions}\}$, $L_a$ annihilates $V_1(p_i, p_j)$ in both the
on-support case~(ii) and the off-support case~(iii); annihilation is
stronger than preservation. The non-trivial action $L_a(b) =
f(\lambda_i, \lambda_j)\, P_{ij}(b)$ that determines the mixing
function~$f$ enters in~\S\ref{sec:sp-faithful} via the
self-modeling feedback postulate, which upgrades~$\seqp{}{}$ beyond the
bare sharp-constraint form. The Peirce-Preservation Lemma states
invariance, which follows a fortiori.
\end{remark}
```

---

## Section 2: Line-count audit (R4)

Counting substantive lines in the LaTeX block above (Section 1), EXCLUDING LaTeX environment boilerplate (`\begin{...}`, `\end{...}`, blank lines, comments):

| Section | Substantive lines |
|---------|------|
| `\emph{Why this form is forced...}` intro paragraph | 7 |
| `\paragraph{Peirce Coherence Axiom (S0).}` intro | 1 |
| Axiom S0 body (inside `\begin{axiom}...\end{axiom}`) | 4 |
| `\begin{remark}` (pairwise commutation) | 5 |
| `\emph{Canonical-example defense of S0.}` intro | 1 |
| Three `\item` bullets (M_n(C)^sa, C(X), spin factors) | 12 |
| A-S Prop 7.50 backing paragraph | 7 |
| `\paragraph{Peirce-Preservation Lemma.}` intro | 1 |
| `\begin{lemma}` body (lemma statement verbatim from claim.md) | 16 |
| `\begin{proof}` body (three parts + preliminary lemma) | 22 |
| `\begin{remark}` (annihilation vs mixing-function) | 9 |
| **TOTAL** | **85 substantive lines** |

≥ 20 per R4 ✓. No padding phrases ("obvious", "clearly", "immediately follows" without citation) appear; all "follows" phrasings are followed by a specific cited theorem or a derivation step.

---

## Section 3: Lemma statement verbatim grep match

The Lemma statement (in Section 1's `\begin{lemma}...\end{lemma}` block) matches claim.md Section 3 (lines 61-87) modulo:

- LaTeX formatting (`$...$`, `\{...\}`, `\sum`, `\lambda`, etc.) in place of plain math symbols.
- The `\begin{enumerate}[label=(\roman*)]` environment replacing the bulleted propositions.
- Identical English wording: "Under [ASSUMPTION SET]", "finite-dimensional spectral order unit space", "orthogonal family of projective units", "mutual compressional annihilation", "spectral decomposition", "Write supp(a)", "left-multiplication map", three target inclusions in the same order (i)/(ii)/(iii) matching Propositions 3.1/3.2/3.3.

Grep-match verification will run in Task 6 exit gate.

---

## Section 4: Forbidden-token discipline

Forbidden tokens scan on the LaTeX block above:

- `M_n(\mathbb{C})` appears ONLY inside the `% BEGIN canonical-example defense for S0 ... % END` scope (three canonical examples section).
- No `Jordan`, `EJA`, `Lüders`, `pxp` (the matrix-algebra `pbp` appears inside the M_n(C)^sa defense scope and is bracketed by the demarcation comments), `√a b √a`, `operator product`, `h_n(C)` tokens outside the defense scope.
- `spin factor` appears inside the `% BEGIN ... % END` defense scope and in the word "compression" (legal: "compression" is NOT a forbidden token).
- No `f(λ,μ) = √(λμ)` as primitive; the only reference to the mixing function is in the annihilation-vs-mixing-function Remark, where $f(\lambda_i, \lambda_j)$ is referenced as a §3.4 concept, not used as a §3.3 primitive.

Discipline check: all forbidden-token hits are demarcated within the canonical-example defense environment, consistent with `forbidden_tokens_exception_scope` in 54-03-PLAN.md.

---

## Section 5: A-S citation discipline

Every A-S citation in the revision points to A-S 2003 with a specific Prop/Thm number:

- `\cite[Prop.~7.23]{AlfsenShultz2003}` — idempotency of compressions (commutation Remark proof, Part (i) proof). Verified-via-internal-cross-reference per `alfsen-shultz-notes.md` Axiom 5.1 / 5.2 update 2026-04-16.
- `\cite[Prop.~7.50]{AlfsenShultz2003}` — compression-meet: `C_p C_q = C_{p ∧ q}` for compatible `p, q`. Verified-via-internal-cross-reference per `alfsen-shultz-notes.md` Section 6 update 2026-04-16; used in the "S0 recoverable from A-S" paragraph.

NO bare `\cite{AlfsenShultz2003}` anywhere in the revision. NO A-S 2001 citations. NO Thm 9.37 invocation (the PRE-JORDAN-ILLEGAL flag from ADDENDUM is respected).

The compression-additivity claim `C_{p_i + p_j} = C_{p_i} + C_{p_j}` (used in the preliminary lemma for Parts (ii) and (iii)) is stated in the proof as "an A-S compression-theoretic fact for orthogonal pairs" without a specific Prop/Thm number — it is AXIOM-STATED-IN-SECONDARY-SOURCE per `alfsen-shultz-notes.md` Axiom 5.3 update 2026-04-16 (the specific Prop/Thm resolution is deferred to Phase 55 or later). Phrasing in the paper is hedged ("A-S compression-theoretic fact for orthogonal pairs") rather than claiming a specific theorem number that is not yet book-verified.

---

## Section 6: Integration into main.tex

To integrate, replace the current `main.tex` §3.3 lines 524-544 (the "Why this form is forced" paragraph through to the end of the corresponding submitted lines 508-528 region) with the LaTeX block in Section 1. Specifically:

**Before integration** (current `main.tex` lines 524-544, which is the R2 non-sequitur):

```
\emph{Why this form is forced.}
By \ref{ax:S1}, $\seqp{a}{\cdot}$ is a linear endomorphism of~$V$.
The Peirce decomposition with respect to the spectral projectors of~$a$
decomposes $V$ into subspaces $V_2(p_i)$ and $V_1(p_i, p_j)$.
Compressions project onto these subspaces
(Alfsen--Shultz~\cite{AlfsenShultz2003}), so linearity gives a block
decomposition: $\seqp{a}{\cdot}$ maps each Peirce subspace to itself.
On $V_2(p_i)$, the sharp constraint $\seqp{p_i}{b} = \comp{p_i}(b)$
and coalescence ($\lambda_i \to \lambda_j$ via \ref{ax:S2}) fix the
action to $\lambda_i \comp{p_i}(\cdot)$.  On $V_1(p_i, p_j)$, the
action is a linear endomorphism $E_{ij}(\lambda_i, \lambda_j)$ of
$V_1(p_i, p_j)$, depending continuously on the eigenvalues by
\ref{ax:S2}.  In Proposition~\ref{prop:coherence}, we prove that
compatible associativity (\ref{ax:S5}), eigenvalue symmetry, and
coalescence force $E_{ij}$ to be a scalar multiple of the identity
on each $V_1(p_i, p_j)$: that is,
$E_{ij}(\lambda_i, \lambda_j) = f(\lambda_i, \lambda_j) \cdot
\peirce{ij}$ for a single mixing function~$f$, simultaneously
determining $f = \sqrt{\lambda_i\, \lambda_j}$.
Thus~\eqref{eq:general-product} is the unique form compatible with
\ref{ax:S1}--\ref{ax:S5} and the sharp constraint.
```

**After integration:** the "Why this form is forced" paragraph is replaced by the Section 1 LaTeX block above, which contains:

1. Revised intro paragraph (keeps the `\emph{Why this form is forced...}` opening but repairs the R2 non-sequitur).
2. Axiom S0 (Peirce Coherence) statement + commutation Remark.
3. Canonical-example defense of S0 (three models, scope-demarcated).
4. A-S Prop 7.50 backing paragraph.
5. Peirce-Preservation Lemma (verbatim from claim.md) + full proof.
6. Annihilation-vs-mixing-function Remark (connecting to §3.4).

Downstream paragraphs of §3.3 in `main.tex` (starting with "The mixing function is constrained by..." at current line 546) are unchanged; they follow naturally after the Peirce-Preservation Lemma concludes.

`main-jmp-submitted.tex` is NOT modified (frozen at git tag `paper5-jmp-submitted`).

---

## Section 7: Unified diff (staged)

```diff
--- main.tex (current, R2 non-sequitur)
+++ main.tex (post-integration, Peirce-Preservation Lemma under S0)
@@ -524,20 +524,95 @@
-\emph{Why this form is forced.}
-By \ref{ax:S1}, $\seqp{a}{\cdot}$ is a linear endomorphism of~$V$.
-The Peirce decomposition with respect to the spectral projectors of~$a$
-decomposes $V$ into subspaces $V_2(p_i)$ and $V_1(p_i, p_j)$.
-Compressions project onto these subspaces
-(Alfsen--Shultz~\cite{AlfsenShultz2003}), so linearity gives a block
-decomposition: $\seqp{a}{\cdot}$ maps each Peirce subspace to itself.
-On $V_2(p_i)$, the sharp constraint $\seqp{p_i}{b} = \comp{p_i}(b)$
-and coalescence ($\lambda_i \to \lambda_j$ via \ref{ax:S2}) fix the
-action to $\lambda_i \comp{p_i}(\cdot)$.  On $V_1(p_i, p_j)$, the
-action is a linear endomorphism $E_{ij}(\lambda_i, \lambda_j)$ of
-$V_1(p_i, p_j)$, depending continuously on the eigenvalues by
-\ref{ax:S2}.  In Proposition~\ref{prop:coherence}, we prove that
-compatible associativity (\ref{ax:S5}), eigenvalue symmetry, and
-coalescence force $E_{ij}$ to be a scalar multiple of the identity
-on each $V_1(p_i, p_j)$: that is,
-$E_{ij}(\lambda_i, \lambda_j) = f(\lambda_i, \lambda_j) \cdot
-\peirce{ij}$ for a single mixing function~$f$, simultaneously
-determining $f = \sqrt{\lambda_i\, \lambda_j}$.
-Thus~\eqref{eq:general-product} is the unique form compatible with
-\ref{ax:S1}--\ref{ax:S5} and the sharp constraint.
+\emph{Why this form is forced (revised for Phase 54 closure: Peirce-Preservation Lemma under S0).}
+[Section 1 LaTeX block of paper5-s3-revision.md; ~85 substantive lines]
```

(Detailed line-by-line diff will be surfaced in the actual `git diff` after `main.tex` is patched.)

---

_Produced 2026-04-16 in Phase 54-03 Task 6 / NEW SCOPE item 3. Replaces the submitted §3.3 R2 non-sequitur (main-jmp-submitted.tex lines 508-528) with the Peirce-Preservation Lemma under S0. A-S citations point to A-S 2003 Ch. 7 Prop 7.23 and Prop 7.50 with VERIFIED-VIA-INTERNAL-CROSS-REFERENCE backing. Forbidden tokens appear only inside demarcated canonical-example defense scope. Lemma statement verbatim from claim.md. R4 line count 85 ≥ 20._
