---
artifact: thm-5-8-identity-verbatim
phase: 56
plan: 01
task: 1
status: COMPLETE
conventions:
  allowed_axiom_scope: "{S0, S1-S7, linearity of L_a, A-S 2003 Ch. 2/7/8, finite-dim spectrality}"
  as_citation_form: bracketed "\\cite[Ch.~X, Prop.~Y.Z]{AlfsenShultz2003}" with X <= 8
  frozen_file: main-jmp-submitted.tex (git tag paper5-jmp-submitted; ZERO-DIFF preserved)
  W_definition: "W := span_R{a_i (x) b_j : a_i basis V_B, b_j basis V_M} <= V_{BM}"
---

# Thm 5.8 Upper-Bound Identity — Verbatim Extraction

## Section 1 — Roadmap 'Thm 5.8' → LaTeX label mapping

The roadmap token "Thm 5.8" does **not** correspond to a `\label{thm:5.8}` anywhere in Paper 5.
It is an informal shorthand, internal to the v14.0 roadmap, for the upper-bound step of the
Local Tomography theorem. The canonical LaTeX locations are:

| Roadmap term            | Living LaTeX label / file:line                                        |
| ----------------------- | --------------------------------------------------------------------- |
| "Thm 5.8" (full)        | `thm:local-tomo` in `sections/composite-lt.tex:162`                   |
| "Thm 5.8 upper bound"   | upper-bound step of `thm:local-tomo`, `composite-lt.tex:203-221`      |
| "Thm 5.8" (detailed)    | `thm:lt-full` in `sections/appendix-proofs.tex:164`                   |
| "Thm 5.8 upper bound"   | upper-bound step of `thm:lt-full`, `appendix-proofs.tex:228-238`      |

The living composite-lt.tex body is the primary target of Plan 56-02's sense-(b) verification;
the appendix proof is the companion detailed statement.

## Section 2 — Verbatim composite-lt.tex L203–221 (upper-bound step)

```latex
% FILE: composite-lt.tex:203-221
\emph{Upper bound.}
Let $W \subseteq V_{BM}$ be the $d^2$-dimensional span of the product
effects $\{a_i \otimes b_j\}$.  The subspace $W$ inherits OUS
structure from $V_{BM}$: it contains the order unit
$\id_B \otimes \id_M$ (since $\id_B \in \spn\{a_i\}$ and
$\id_M \in \spn\{b_j\}$), and the induced cone
$W^+ = W \cap V_{BM}^+$ is proper (the product cone is contained
in $W^+$ and generates~$W$).  We check that $W$, equipped with this
induced order and the product-form sequential product, satisfies
(C1)--(C4): product effects lie in $W$ by construction (C2);
product states are positive functionals on $W$ (C3, by restriction);
non-signaling holds because marginals factor through $V_B$ and $V_M$
(C4); and the product-form SP maps $W$ into $W$ since
$\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes
(\seqp{b}{d})$ is again a product effect (C1).
By minimality (Definition~\ref{def:self-modeling-system}\ref{sms:minimal}),
$V_{BM}$ is the smallest OUS satisfying these axioms.  Since $W$
satisfies them and has dimension $d^2$,
we have $\dim(V_{BM}) \le d^2$.
```

**Cite:** `composite-lt.tex:203-221` (living).

## Section 3 — Verbatim appendix-proofs.tex L228–238 (upper-bound step)

```latex
% FILE: appendix-proofs.tex:228-238
\textbf{Step 4: Upper bound via minimality.}
The product effects $\{a_{i} \otimes b_{j}\}$ span a
$(\dim V_{B} \cdot \dim V_{M})$-dimensional subspace of $V_{BM}$.
The product-form sequential product~\eqref{eq:product-sp} preserves
this subspace: $\seqp{(a \otimes b)}{(c \otimes d)} =
(\seqp{a}{c}) \otimes (\seqp{b}{d})$, which is again a product effect.
The non-signaling constraints (C4) are satisfied by the
product-effect subspace.  By
minimality (\Cref{ass:minimal}), $V_{BM}$ contains no
structure beyond what is forced by (C1)--(C4) and the product-form SP.
Therefore $\dim(V_{BM}) \leq \dim(V_{B}) \cdot \dim(V_{M})$.
```

**Cite:** `appendix-proofs.tex:228-238` (living).

## Section 4 — Full `thm:local-tomo` context (composite-lt.tex L162–222)

```latex
% FILE: composite-lt.tex:162-222
\begin{theorem}[Local tomography]\label{thm:local-tomo}
Under conditions~\ref{sms:minimal} and~\ref{sms:simple} of
Definition~\ref{def:self-modeling-system},
\[
  \dim(V_{BM}) \;=\; \dim(V_B)\cdot\dim(V_M).
\]
\end{theorem}

\begin{proof}
\emph{Lower bound.}
Let $\{a_1,\ldots,a_d\}$ and $\{b_1,\ldots,b_d\}$ be bases for
$V_B$ and $V_M$ respectively ($d = \dim V_B = \dim V_M$).
We show that the $d^2$ product effects
$\{a_i \otimes b_j\}$ are linearly independent in~$V_{BM}$.

Suppose $\sum_{i,j} \alpha_{ij}\, a_i \otimes b_j = 0$ in $V_{BM}$.
By axiom~(C3), every product state $\omega_B \otimes \omega_M$
belongs to the state space of~$V_{BM}$.  Evaluating:
\[
  0 = (\omega_B \otimes \omega_M)\!\Bigl(\sum_{i,j} \alpha_{ij}\,
  a_i \otimes b_j\Bigr)
  = \sum_{i,j} \alpha_{ij}\, \omega_B(a_i)\, \omega_M(b_j)
\]
for all states $\omega_B$ on $V_B$ and $\omega_M$ on $V_M$.
Fix~$\omega_B$.  Then for all~$\omega_M$:
\[
  \omega_M\!\Bigl(\sum_j c_j\, b_j\Bigr) = 0,
  \qquad c_j \coloneqq \sum_i \alpha_{ij}\, \omega_B(a_i).
\]
States separate points in finite-dimensional order unit
spaces~\cite{AlfsenShultz2003}, so $\sum_j c_j\, b_j = 0$.
Since $\{b_j\}$ is a basis, $c_j = 0$ for every~$j$, i.e.,
\[
  \omega_B\!\Bigl(\sum_i \alpha_{ij}\, a_i\Bigr) = 0
  \qquad \text{for all } \omega_B \text{ and all } j.
\]
State separation again gives $\sum_i \alpha_{ij}\, a_i = 0$ for
every~$j$, and since $\{a_i\}$ is a basis, $\alpha_{ij} = 0$ for
all~$i, j$.  Hence the product effects are linearly independent and
$\dim(V_{BM}) \ge d^2$.

\emph{Upper bound.}
Let $W \subseteq V_{BM}$ be the $d^2$-dimensional span of the product
effects $\{a_i \otimes b_j\}$.  The subspace $W$ inherits OUS
structure from $V_{BM}$: it contains the order unit
$\id_B \otimes \id_M$ (since $\id_B \in \spn\{a_i\}$ and
$\id_M \in \spn\{b_j\}$), and the induced cone
$W^+ = W \cap V_{BM}^+$ is proper (the product cone is contained
in $W^+$ and generates~$W$).  We check that $W$, equipped with this
induced order and the product-form sequential product, satisfies
(C1)--(C4): product effects lie in $W$ by construction (C2);
product states are positive functionals on $W$ (C3, by restriction);
non-signaling holds because marginals factor through $V_B$ and $V_M$
(C4); and the product-form SP maps $W$ into $W$ since
$\seqp{(a \otimes b)}{(c \otimes d)} = (\seqp{a}{c}) \otimes
(\seqp{b}{d})$ is again a product effect (C1).
By minimality (Definition~\ref{def:self-modeling-system}\ref{sms:minimal}),
$V_{BM}$ is the smallest OUS satisfying these axioms.  Since $W$
satisfies them and has dimension $d^2$,
we have $\dim(V_{BM}) \le d^2$.
\end{proof}
```

**Cite:** `composite-lt.tex:162-222` (living).

## Section 5 — Full `thm:lt-full` context (appendix-proofs.tex L164–243)

```latex
% FILE: appendix-proofs.tex:164-243
\begin{theorem}[Local tomography, detailed version]\label{thm:lt-full}
Let $V$ be a finite-dimensional simple Euclidean Jordan algebra
equipped with the self-modeling sequential
product~\eqref{eq:corrected-product}.  Let $V_{BM}$ be the minimal
composite (\Cref{ass:minimal}) of two copies $V_{B} \cong V_{M}
\cong V$ with the product-form sequential product.  Then
\[
  \dim(V_{BM}) = \dim(V_{B}) \cdot \dim(V_{M}).
\]
\end{theorem}

\begin{proof}
\textbf{Step 1: Lower bound.}
The product effects $\{a_{i} \otimes b_{j}\}$, where $\{a_{i}\}$ and
$\{b_{j}\}$ are bases for $V_{B}$ and $V_{M}$ respectively, belong to
$V_{BM}$ by construction (C1).  If these are linearly independent in
$V_{BM}$, then $\dim(V_{BM}) \geq \dim(V_{B}) \cdot \dim(V_{M})$.

\medskip
\textbf{Step 2: Non-degeneracy of the correlation form.}
Define the correlation bilinear form
\[
  B(a, b) = \tau\!\left(a \circ \varphi^{-1}(b)\right),
\]
where $\tau$ is the normalized trace functional on the EJA $V$
(Faraut--Kor\'anyi~\cite{FarautKoranyi1994}, Chapter~III), $\circ$
denotes the Jordan product, and $\varphi^{-1}: V_{M} \to V_{B}$ is
the inverse of the tracking isomorphism.

On a simple EJA, the trace form $(a, c) \mapsto \tau(a \circ c)$ is
non-degenerate (Faraut--Kor\'anyi~\cite{FarautKoranyi1994},
Proposition~III.4.2): if $\tau(a \circ c) = 0$ for all $a \in V$,
then $c = 0$.  Since $\varphi: V_{B} \to V_{M}$ is an order
isomorphism (Definition~\ref{def:self-modeling-system}\ref{sms:faithful}), its inverse
$\varphi^{-1}$ is a bijection.  Therefore, if $B(a, b) = 0$ for all
$a \in V_{B}$, then $\tau(a \circ \varphi^{-1}(b)) = 0$ for all $a$,
which gives $\varphi^{-1}(b) = 0$ by non-degeneracy, hence $b = 0$.
So $B$ is non-degenerate.

\medskip
\textbf{Step 3: Linear independence of product effects.}
Suppose $\sum_{i,j} \alpha_{ij}\, a_{i} \otimes b_{j} = 0$ in
$V_{BM}$, where $\{a_{i}\}$ and $\{b_{j}\}$ are bases.  For any
state $\omega$ on $V_{BM}$, evaluating on this zero element gives
$\sum_{i,j} \alpha_{ij}\, \omega(a_{i} \otimes b_{j}) = 0$.
In particular, for product states
$\omega = \omega_{B} \otimes \omega_{M}$:
\[
  \sum_{i,j} \alpha_{ij}\, \omega_{B}(a_{i})\, \omega_{M}(b_{j}) = 0
  \quad \text{for all } \omega_{B}, \omega_{M}.
\]
The non-degeneracy of $B$ (which is defined via the Jordan product and
trace, both available on the EJA) ensures that the matrix
$(\alpha_{ij})$ must be zero: fix $j$ and vary $\omega_{B}$ to obtain
$\sum_{i} \alpha_{ij}\, \omega_{B}(a_{i}) = 0$ for all
$\omega_{B}$; since states separate points in an OUS
(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~1.23), this gives
$\sum_{i} \alpha_{ij}\, a_{i} = 0$ for each $j$, hence
$\alpha_{ij} = 0$ (since $\{a_{i}\}$ is a basis).

This establishes the lower bound:
$\dim(V_{BM}) \geq \dim(V_{B}) \cdot \dim(V_{M})$.

\medskip
\textbf{Step 4: Upper bound via minimality.}
The product effects $\{a_{i} \otimes b_{j}\}$ span a
$(\dim V_{B} \cdot \dim V_{M})$-dimensional subspace of $V_{BM}$.
The product-form sequential product~\eqref{eq:product-sp} preserves
this subspace: $\seqp{(a \otimes b)}{(c \otimes d)} =
(\seqp{a}{c}) \otimes (\seqp{b}{d})$, which is again a product effect.
The non-signaling constraints (C4) are satisfied by the
product-effect subspace.  By
minimality (\Cref{ass:minimal}), $V_{BM}$ contains no
structure beyond what is forced by (C1)--(C4) and the product-form SP.
Therefore $\dim(V_{BM}) \leq \dim(V_{B}) \cdot \dim(V_{M})$.

\medskip
Combining the lower and upper bounds:
$\dim(V_{BM}) = \dim(V_{B}) \cdot \dim(V_{M})$.
\end{proof}
```

**Cite:** `appendix-proofs.tex:164-243` (living).

## Section 6 — Ambiguity note: no `\label{thm:5.8}` in Paper 5

Executed:

```bash
grep -n 'label{thm:5.8}' \
  /Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex \
  /Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/sections/*.tex
```

**Result:** zero hits.

**Statement:** Paper 5 contains no `\label{thm:5.8}` in either the FROZEN
`main-jmp-submitted.tex` or any of the living `sections/*.tex` files. The roadmap token
"Thm 5.8" is informal shorthand internal to the v14.0 roadmap for the upper-bound step of
`thm:local-tomo` (composite-lt.tex:162) and, equivalently, the upper-bound step of
`thm:lt-full` (appendix-proofs.tex:164). All Phase 56 artifacts MUST use the
`\ref{thm:local-tomo}` / `\ref{thm:lt-full}` labels when the label-level identity is
needed.

## Section 7 — Token inventory: 'carries' / 'inherits' / 'closed' / 'respects' / 'extends' / 'restricts' / 'maps into'

This is the R7-equivocation inventory. Each site is a candidate for the three-sense
disambiguation in `carries-senses.md`; every downstream invocation must tag (a)/(b)/(c).

| # | Token            | file:line             | Verbatim phrase (quoted)                                         | Candidate sense      |
|---|------------------|-----------------------|------------------------------------------------------------------|----------------------|
| 1 | `inherits`       | composite-lt.tex:205  | "The subspace $W$ inherits OUS structure from $V_{BM}$"          | sense (b)            |
| 2 | `satisfies`      | composite-lt.tex:211  | "satisfies (C1)--(C4)"                                           | sense (b)            |
| 3 | `maps $W$ into $W$` | composite-lt.tex:215 | "the product-form SP maps $W$ into $W$"                          | sense (a)            |
| 4 | `is again a product effect` | composite-lt.tex:216-217 | "$(\seqp{a}{c}) \otimes (\seqp{b}{d})$ is again a product effect (C1)" | sense (a)            |
| 5 | `carries`        | composite-lt.tex:14    | "isomorphically the model $M$) carries EJA structure"            | sense (c) (not Phase 56 scope; pre-composite) |
| 6 | `carries`        | composite-lt.tex:101   | "this product carries EJA structure" (tensor product context)    | sense (b)/(c) (Remark `rem:bootstrap`) |
| 7 | `preserves`      | appendix-proofs.tex:231 | "The product-form sequential product preserves this subspace"    | sense (a)            |
| 8 | `is again a product effect` | appendix-proofs.tex:233 | "which is again a product effect"                                | sense (a)            |
| 9 | `contains no structure beyond` | appendix-proofs.tex:236-237 | "$V_{BM}$ contains no structure beyond what is forced by (C1)--(C4) and the product-form SP" | sense (b) (minimality semantics) |
| 10| `inherits`       | type-exclusion.tex:245-248 | "The composite $V_{BM}$ with the product-form SP inherits"  | sense (b)            |
| 11| `inherits`       | discussion.tex:253     | "the product-form sequential product inherits"                   | sense (b)            |
| 12| `carries`        | discussion.tex:182     | "composite carries no structure beyond what product measurements can" | sense (b) (minimality) |
| 13| `carries`        | main.tex:308           | "that also carries a sequential product"                         | sense (c) (morphism) |

**R7 flag:** Item (1) ('W inherits OUS structure') is THE central equivocation. In the
upper-bound proof, "inherits" must mean sense (b) — `(W, <=|_W, 1_W, \circ|_W)` is
itself an OUS satisfying the axioms — because the minimality clause requires W to be
a full OUS competitor, not merely a subspace closed under \circ. Plan 56-02 will prove
sense (b) directly via vdW 2019 Def. 4 + Thm 1. The proof text at L211-217 currently
conflates (a) (the "maps into" closure) with (b) (the full "satisfies (C1)-(C4)"
assertion). Plan 56-03 may want to audit this phrasing in the revision text.

**R7 flag:** Item (3) 'maps $W$ into $W$' is the weakest sense-(a) claim, and the
closure identity `(a \otimes b) \circ (c \otimes d) = (a \circ c) \otimes (b \circ d)`
(composite-lt.tex:216-217 and appendix-proofs.tex:232-233) gives sense (a) immediately
by construction. Sense (b) requires the additional S1-S7 verification, which is the
substance of Plan 56-02.

**Frozen-file zero-diff check:**

```
$ git -C /Users/ehrlich/repos/blog diff --stat HEAD -- \
    landing/papers/qm-from-self-modeling/main-jmp-submitted.tex
(empty output — no changes)
```

Confirmed: main-jmp-submitted.tex is unchanged at HEAD. Task 1 is read-only.

## Forbidden-proxy rejections

- **fp-identity-paraphrase** — REJECTED. Every identity statement in Sections 2–5 is a
  direct verbatim quote with a `file:line-range` citation.
- **fp-frozen-file-edit** — REJECTED. No write operation on main-jmp-submitted.tex; zero
  diff verified above.
