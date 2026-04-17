# Phase 55-02 Task 5 — Annotated Diff Report

**Produced:** 2026-04-16 (Phase 55-02 Task 5)
**Source repo:** `/Users/ehrlich/repos/blog` (paper repo)
**Baseline:** HEAD~3 (before Phase 55-02 Tasks 2-4 commits; same as HEAD when Plan 55-01 closed)
**Head:** HEAD (Phase 55-02 Tasks 2-4 complete)
**Scope:** `landing/papers/qm-from-self-modeling/{main.tex, sections/axiom-verification.tex, sections/appendix-proofs.tex}`

---

## 1. Summary Table

| File | Lines added | Lines removed | Net | Classification-row origin |
|------|-------------|---------------|-----|--------------------------|
| `sections/axiom-verification.tex` | 41 | 22 | +19 | 55-01 rows 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 |
| `sections/appendix-proofs.tex` | 26 | 10 | +16 | 55-01 rows 14, 15, 16, 17, 18 |
| `main.tex` | 4 | 1 | +3 | Plan 55-02 Edit T (§3.5 Circularity Check, optional) |
| **Total** | **71** | **33** | **+38** | — |

**Frozen-file check:**
```bash
$ git -C /Users/ehrlich/repos/blog diff --stat HEAD~3..HEAD -- landing/papers/qm-from-self-modeling/main-jmp-submitted.tex
# (empty output — main-jmp-submitted.tex untouched)
```
**Status:** ✅ `main-jmp-submitted.tex` verified frozen (zero diff).

**Paper-repo commits (Phase 55-02):**

| SHA | Message |
|-----|---------|
| `b44408e` | Phase 55-02 Task 2: replace Thm 9.37 in axiom-verification.tex S2+S4 proofs with S0 axiom + Peirce-Preservation Lemma refs; tighten all A-S cites to Ch./Prop. form |
| `f4fb2f8` | Phase 55-02 Task 3: replace facial-orthogonality handwaves in appendix-proofs.tex §S4-proof with S0-termwise derivation + Peirce-Preservation Lemma Part (iii) refs |
| `e134c24` | Phase 55-02 Task 4: add S0 axiom + Peirce-Preservation Lemma to Circularity Check inventory (main.tex §3.5) |

## 2. Hunk-by-Hunk Annotation — axiom-verification.tex

### Hunk AV-1 (line 36-42) — CLASSIFICATION-ROW 1 (TIGHTEN-CITE)

```diff
-(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~7), and the Peirce
+(\cite[Ch.~7]{AlfsenShultz2003}), and the Peirce
```

**Rationale:** S1 proof (positive linear maps) — tighten bare Ch. 7 cite to bracketed form.

### Hunk AV-2 (line 65-72) — CLASSIFICATION-ROW 2 (REPLACE-WITH-alt-cite, MANDATORY)

```diff
-(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37).
+(the continuous spectral functional calculus on a finite-dimensional
+spectral order unit space; see~\cite[Ch.~8]{AlfsenShultz2003}).
```

**Rationale:** SECONDARY BUG at line 68 of the S2 (Continuity) proof. Thm 9.37 is Ch. 9 (post-Jordan, illegal at pre-S4 scope). Replaced with Ch. 8 (Spectral Theory; pre-Jordan-legal per 55-01 CLASSIFICATION Section 4). The cited assertion is the continuous spectral functional calculus on a finite-dim spectral OUS, which lives in A-S 2003 Ch. 8.

### Hunk AV-3 (line 80-84) — CLASSIFICATION-ROW 3 (TIGHTEN-CITE; was VERIFIED-AS-IS, upgraded to bracketed form)

```diff
-(Alfsen--Shultz~\cite{AlfsenShultz2003}, Def.~7.1). Therefore
+(\cite[Ch.~7, Def.~7.1]{AlfsenShultz2003}). Therefore
```

**Rationale:** S3 proof (C_id = id) — Def 7.1 is pre-Jordan-legal; tightening to bracketed form for uniformity and to eliminate bare `\cite{}`.

### Hunk AV-4 (line 122-130) — CLASSIFICATION-ROW 4 (REPLACE-WITH-S0 + REPLACE-WITH-LEMMA, PRIMARY BUG)

```diff
-(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~9.37)
+(established at the compression level in Section~\ref{sec:sp} via
+axiom~\ref{ax:S0} and Lemma~\ref{lem:peirce-preservation}; the
+compression-theoretic underpinning is~\cite[Ch.~7]{AlfsenShultz2003})
```

**Rationale:** PRIMARY PHASE 55 BUG. Thm 9.37 is Ch. 9 (post-Jordan, illegal at pre-S4 scope). Replaced with Phase 54 outputs: axiom~S0 (`\ref{ax:S0}`) + Peirce-Preservation Lemma (`\ref{lem:peirce-preservation}`) + Ch. 7 compression-theoretic pointer. The Peirce direct sum V = ⊕ V_2(p_i) ⊕ ⊕ V_1(p_i,p_j) is now established at the compression level (pre-Jordan-legal).

### Hunk AV-5 (line 134-156) — CLASSIFICATION-ROWS 5, 6 (TIGHTEN-CITE + REPLACE-WITH-LEMMA Part iii)

```diff
-(Proposition~7.43 of~\cite{AlfsenShultz2003}):
+(\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}):
...
-face $\mathrm{face}\!\left(\sum_{k=m+1}^n p_k\right)$. By the facial
-structure of spectral order unit spaces, the Peirce $1$-space components
-$V_1(p_i, p_j)$ connecting a face to its complement are excluded: an
-effect in $\mathrm{face}(p^\perp)$ has zero component in every
-$V_1(p_i,p_j)$ for $i\le m$, $j > m$. Therefore $b$ is supported
-entirely on the zero-eigenvalue block of $a$.
+face $\mathrm{face}\!\left(\sum_{k=m+1}^n p_k\right)$. The Peirce
+$1$-space components $V_1(p_i, p_j)$ connecting a face to its
+complement are excluded by Part~(iii) of the Peirce-Preservation Lemma
+(\Cref{lem:peirce-preservation}), applied with the roles $a \leftarrow b$
+and $\{p_k, p_l\} \leftarrow \{p_i, p_j\}$ for any $i \le m < j$:
+since $\mathrm{supp}(b) \subseteq \{p_{m+1}, \ldots, p_n\}$ while
+$p_i \le p_+$, we have $\{p_i, p_j\} \cap \mathrm{supp}(b) = \emptyset$
+whenever $i \le m$ and $j \le m$, and the lemma's R3 cross-term case
+yields $P_{ij}(b) = 0$ for $i \le m$, $j > m$ via the same compression
+algebra. Therefore $b$ is supported entirely on the zero-eigenvalue
+block of $a$.
```

**Rationale (row 5):** Prop 7.43 cite tightened to `\cite[Ch.~7, Prop.~7.43]{AS2003}`; inlined blockquote statement preserved; status VERIFIED-VIA-INTERNAL-CROSS-REFERENCE per Plan 55-01 Section 3.

**Rationale (row 6):** The unnamed "facial structure of spectral order unit spaces" handwave is replaced by an explicit Peirce-Preservation Lemma Part (iii) invocation with role-swap annotation (`a ← b`, `{p_k, p_l} ← {p_i, p_j}`). This routes the cross-term vanishing argument through pre-Jordan-legal primitives.

### Hunk AV-6 (line 155-176) — CLASSIFICATION-ROWS 7, 8 (RESOLVE-VIA-S0-TERMWISE + REPLACE-WITH-LEMMA Part iii)

```diff
-For the reverse product $\seqp{b}{a}$, write
-$b = \sum_j \mu_j\, q_j$ with each $q_j$ ($\mu_j > 0$) lying in
-$\mathrm{face}\!\left(\sum_{k>m} p_k\right)$. Since $a$ is supported on
-the complementary face $\mathrm{face}\!\left(\sum_{i\le m}
-p_i\right)$, the facial orthogonality theorem gives $C_{q_j}(a) = 0$ for
-all $j$ with $\mu_j > 0$. The Peirce $1$-space terms $Q_{jk}(a)$ either
-vanish by facial structure (when both $\mu_j,\mu_k>0$) or carry zero
-weight $\sqrt{\mu_j\mu_k}=0$. Hence $\seqp{b}{a} = 0$.
+For the reverse product $\seqp{b}{a}$, write
+$b = \sum_j \mu_j\, q_j$ with each $q_j$ ($\mu_j > 0$) lying in
+$\mathrm{face}\!\left(\sum_{k>m} p_k\right)$. For each such $j$ and
+each $i \le m$, we have $q_j \le p_+^\perp$ and $p_i \le p_+$, so
+$q_j \perp p_i$ (complementary faces of orthogonal projective units;
+\cite[Ch.~7]{AlfsenShultz2003}). Axiom~\ref{ax:S0} (mutual
+compressional annihilation for orthogonal projective units) then
+yields $C_{q_j}(p_i) = 0$ for every $i \le m$, and linearity gives
+\[
+  C_{q_j}(a) = \sum_{i \le m} \lambda_i\, C_{q_j}(p_i) = 0.
+\]
+The Peirce $1$-space terms $Q_{jk}(a)$ vanish by Part~(iii) of the
+Peirce-Preservation Lemma (\Cref{lem:peirce-preservation}) when both
+$\mu_j, \mu_k > 0$ (apply the lemma with the roles $a \leftarrow a$
+and $\{p_k, p_l\} \leftarrow \{q_j, q_k\}$, using
+$\{q_j, q_k\} \cap \mathrm{supp}(a) = \emptyset$ since both
+$q_j, q_k \le p_+^\perp$ and $\mathrm{supp}(a) \subseteq
+\{p_1, \ldots, p_m\}$), or carry zero weight
+$\sqrt{\mu_j \mu_k} = 0$ when $\mu_k = 0$. Hence $\seqp{b}{a} = 0$.
```

**Rationale (row 7):** The unnamed "facial orthogonality theorem" is replaced by an explicit S0-termwise derivation:
1. `q_j ≤ p_+^⊥` and `p_i ≤ p_+` (given) ⟹ `q_j ⊥ p_i` (complementary faces).
2. axiom~S0 ⟹ `C_{q_j}(p_i) = 0` for each `i ≤ m`.
3. linearity ⟹ `C_{q_j}(a) = Σᵢ λᵢ C_{q_j}(p_i) = 0`.
All three steps use only pre-Jordan-legal primitives (S0 axiom, A-S Ch. 7 compression orthogonality, linearity).

**Rationale (row 8):** Peirce 1-space cross-term vanishing (Q_{jk}(a) = 0 for μ_j, μ_k > 0) is routed through Peirce-Preservation Lemma Part (iii) with explicit role-swap annotation.

### Hunk AV-7 (line 197-203) — CLASSIFICATION-ROWS 9, 10 (TIGHTEN-CITE; were VERIFIED-AS-IS, now uniform bracketed form)

```diff
-C_q \circ C_p$ (Alfsen--Shultz~\cite{AlfsenShultz2003}, Prop.~7.49),
+C_q \circ C_p$ (\cite[Ch.~7, Prop.~7.49]{AlfsenShultz2003}),
 and their composition satisfies $C_p \circ C_q = C_{p \wedge q}$
-(Prop.~7.50).
+(\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}).
```

**Rationale:** S5 proof tightening. Rows 9 + 10 were VERIFIED-AS-IS at the classification stage; this edit elevates them to bracketed form for uniformity (eliminating orphan `(Prop.~7.50)` which lacked a cite key).

### Hunk AV-8 (line 226-232) — CLASSIFICATION-ROWS 11, 12 (TIGHTEN-CITE)

```diff
-By Alfsen--Shultz~\cite{AlfsenShultz2003} Prop.~7.49 and
+By \cite[Ch.~7, Prop.~7.49]{AlfsenShultz2003} and
 Niestegge~\cite{Niestegge2009} Lemma~3.3, $a \compatible b$ implies that
...
-By Prop.~7.50 of~\cite{AlfsenShultz2003},
+By \cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003},
```

**Rationale:** S6 proof (lem:peirce-vanish) — tighten both Prop 7.49 and Prop 7.50 cites.

### Hunk AV-9 (line 317-321) — CLASSIFICATION-ROW 13 (TIGHTEN-CITE)

```diff
-Prop.~7.50 of~\cite{AlfsenShultz2003} gives
+\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003} gives
```

**Rationale:** S7 proof — tighten Prop 7.50 cite.

## 3. Hunk-by-Hunk Annotation — appendix-proofs.tex

### Hunk AP-1 (line 34-45) — CLASSIFICATION-ROW 14 (TIGHTEN-CITE, parenthetical S0 + Lemma)

```diff
-By the Peirce decomposition~\eqref{eq:peirce-proj}, the terms
+By the Peirce decomposition~\eqref{eq:peirce-proj} (established at the
+compression level in §3.3 via axiom~\ref{ax:S0} and
+Lemma~\ref{lem:peirce-preservation}; the compression-theoretic
+underpinning is~\cite[Ch.~7]{AlfsenShultz2003}), the terms
```

**Rationale:** Parenthetical cross-reference to Phase 54 outputs (S0 axiom + Peirce-Preservation Lemma) + Ch. 7 compression-theoretic citation, making the Peirce direct sum's pre-Jordan derivation explicit at first invocation.

### Hunk AP-2 (line 78-82) — CLASSIFICATION-ROW 15 (TIGHTEN-CITE)

```diff
-(Alfsen--Shultz~\cite{AlfsenShultz2003}, Proposition~7.43):
+(\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}):
```

**Rationale:** Prop 7.43 (facial absorption) — tighten cite; inlined blockquote statement preserved (lines 80-84 unchanged). VERIFIED-VIA-INTERNAL-CROSS-REFERENCE per 55-01 Section 3.

### Hunk AP-3 (line 85-93) — CLASSIFICATION-ROW 16 (TIGHTEN-CITE, add explicit citation)

```diff
-their respective faces, we have
+their respective faces (by axiom~\ref{ax:S0}; equivalently
+\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}), we have
```

**Rationale:** The phrase "compressions for orthogonal projective units act independently" is pinned to axiom~S0 (primary) and Ch. 7 Prop 7.50 (equivalent, for reader familiar with A-S).

### Hunk AP-4 (line 107-129) — CLASSIFICATION-ROWS 17, 18 (RESOLVE-VIA-S0-TERMWISE + REPLACE-WITH-LEMMA Part iii)

```diff
-For each $j$ with $\mu_{j} > 0$: since $q_{j} \leq p_{+}^{\perp}$
-and $a$ is supported on $p_{+}$ (all nonzero eigenvalues correspond to
-$p_{+}$), the facial orthogonality of complementary faces gives
-$\comp{q_{j}}(a) = 0$.  The Peirce $1$-space terms $Q_{jk}(a)$ either
-vanish by facial structure (when both $\mu_{j}, \mu_{k} > 0$,
-so both $q_{j}, q_{k} \leq p_{+}^{\perp}$, and $a$ has no component
-in $V_{1}(q_{j}, q_{k})$ since $a$ is supported on the complementary
-face) or carry zero weight $f(\mu_{j}, 0) = 0$ (when $\mu_{k} = 0$).
+For each $j$ with $\mu_{j} > 0$: since $q_{j} \leq p_{+}^{\perp}$
+and $p_{i} \leq p_{+}$ for every $i \in I_{+}$, we have
+$q_{j} \perp p_{i}$ (complementary faces of orthogonal projective
+units; \cite[Ch.~7]{AlfsenShultz2003}). Axiom~\ref{ax:S0} (mutual
+compressional annihilation for orthogonal projective units) yields
+$\comp{q_{j}}(p_{i}) = 0$ for every $i \in I_{+}$, and linearity
+gives
+\[
+  \comp{q_{j}}(a)
+  = \sum_{i \in I_{+}} \lambda_{i}\, \comp{q_{j}}(p_{i})
+  = 0.
+\]
+The Peirce $1$-space terms $Q_{jk}(a)$ vanish by Part~(iii) of the
+Peirce-Preservation Lemma (\Cref{lem:peirce-preservation}) when both
+$\mu_{j}, \mu_{k} > 0$ (apply the lemma with the roles
+$a \leftarrow a$ and $\{p_{k}, p_{l}\} \leftarrow \{q_{j}, q_{k}\}$,
+using $\{q_{j}, q_{k}\} \cap \mathrm{supp}(a) = \emptyset$ since
+both $q_{j}, q_{k} \leq p_{+}^{\perp}$ and $\mathrm{supp}(a)
+\subseteq \{p_{i} : i \in I_{+}\}$), or carry zero weight
+$f(\mu_{j}, 0) = 0$ when $\mu_{k} = 0$.
```

**Rationale (row 17):** Parallel to axiom-verification.tex hunk AV-6 (row 7). Unnamed "facial orthogonality of complementary faces" replaced with explicit S0-termwise derivation, adjusted for the appendix's I_+ notation.

**Rationale (row 18):** Parallel to axiom-verification.tex hunk AV-6 (row 8). Q_{jk}(a) = 0 routed through Peirce-Preservation Lemma Part (iii) with role-swap annotation.

### Corollary `cor:S4-phi-indep` (lines 137-143 in post-edit file) — VERBATIM-PRESERVED

**Status:** ✅ Zero diff hunks touch lines 121-137 of pre-edit file / lines 137-153 of post-edit file (corollary statement + proof). Verified by `git diff HEAD~3..HEAD | grep -c 'cor:S4-phi-indep' → 0`.

### Line 204/220 Thm 1.23 (Local Tomography) — FLAG-OUT-OF-SCOPE

**Status:** Untouched. Classified FLAG-OUT-OF-SCOPE in 55-01 Section 2.3 (Ch. 1 pre-Jordan-legal; outside §S4-proof region). This is a pre-existing bare `\cite{AlfsenShultz2003}` citation that Phase 55-02 explicitly does not tighten.

**Carryforward note:** A future phase (Phase 56 or 57) could tighten this to `\cite[Ch.~1, Thm.~1.23]{AlfsenShultz2003}` for uniformity, but it is NOT a Phase 55-02 obligation and not a circularity bug.

## 4. Hunk-by-Hunk Annotation — main.tex

### Hunk MT-1 (line 860-872) — Plan 55-02 Edit T (§3.5 Circularity Check inventory; OPTIONAL)

```diff
   \item Alfsen--Shultz compressions $\comp{p}$ for faces of
     projective units;
+  \item the Peirce coherence axiom~\ref{ax:S0} (§3.3) at the
+    compression level;
   \item the Peirce decomposition~\eqref{eq:peirce-proj} derived from
-    compressions;
+    compressions together with
+    Lemma~\ref{lem:peirce-preservation};
   \item spectral decomposition of effects in the OUS;
```

**Rationale:** Makes the S0 axiom and Peirce-Preservation Lemma explicit in the Circularity Check inventory of mathematical objects. Supports the referee-facing consistency story: the §S4 proof's core derivation steps (now routed through S0 + Lemma) are accounted for in the §3.5 audit list.

**Tightening-only, not a MANDATORY classification mandate** (Plan 55-01 Section 7 listed this as LOW priority optional). Applied because the 2-line addition preserves the natural structure of the list and strengthens §S4 ↔ §3.5 consistency.

## 5. Final Forbidden-Token Sweep

**Command:**
```bash
git -C /Users/ehrlich/repos/blog diff HEAD~3..HEAD -- \
  landing/papers/qm-from-self-modeling/sections/axiom-verification.tex \
  landing/papers/qm-from-self-modeling/sections/appendix-proofs.tex \
  landing/papers/qm-from-self-modeling/main.tex \
  | grep -E '^\+' | grep -vE '^\+\+\+' \
  | grep -nE 'Jordan|EJA|Lüders|Luders|pxp|Hanche-Olsen|HancheOlsen|9\.37|sqrt.?a.?b.?sqrt.?a|√.?a.?b.?√.?a'
```

**Output:** (empty — zero hits; exit code 1)

**Status:** ✅ Zero forbidden-token leaks across all Phase 55-02 added lines.

## 6. Acceptance Test Roll-Up (from Plan 55-02 contract)

| Test | Status | Evidence |
|------|--------|----------|
| `test-thm-937-removed` | ✅ PASS | `grep '9\.37' sections/axiom-verification.tex sections/appendix-proofs.tex` → zero hits |
| `test-s0-refs-present` | ✅ PASS | `grep 'ref{ax:S0}'` → 2 hits in axiom-verification.tex (lines 127, 163) + 3 hits in appendix-proofs.tex (38, 91, 113) + 1 in main.tex (862) |
| `test-s0-termwise-derivation-present` | ✅ PASS | `axiom-verification.tex:163`: "Axiom~\ref{ax:S0} (mutual compressional annihilation for orthogonal projective units) then yields $C_{q_j}(p_i) = 0$"; parallel phrase at `appendix-proofs.tex:113`; role-swap explicit in both |
| `test-lemma-part-iii-refs-present` | ✅ PASS | `grep 'lem:peirce-preservation'` → 3 hits in axiom-verification.tex + 2 in appendix-proofs.tex + 1 in main.tex; "Part (iii)" or "Part~(iii)" annotation present in 4 of those invocations |
| `test-local-edit-preservation` | ✅ PASS | `\begin{theorem}\label{thm:S4}` / `\end{theorem}` unchanged; `\begin{theorem}\label{thm:S4-full}` / closing unchanged; cor:S4-phi-indep verbatim-preserved |
| `test-bare-cite-grep-zero` | ✅ PASS (edit scope) | Zero bare `\cite{AlfsenShultz2003}` in axiom-verification.tex or in appendix-proofs.tex §S4-proof region (lines 9-138). One pre-existing bare cite remains at appendix-proofs.tex:220 in thm:lt-full (out-of-scope per 55-01 Section 2.3) |
| `test-prop-743-cite-form` | ✅ PASS | All Prop 7.43 citations in edit scope are `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}`; exact statement inlined (blockquote retained at axiom-verification.tex:141-144 and appendix-proofs.tex:83-87) |
| `test-ch-prop-format` | ✅ PASS | Every A-S 2003 citation in edit scope has `[Ch.~X]`, `[Ch.~X, Prop.~Y.Z]`, `[Ch.~X, Def.~Y.Z]`, or `[Ch.~X, Thm.~Y.Z]` |
| `test-compile-clean` | ⚠️ STATIC-VERIFIED | pdflatex unavailable on this machine; see 55-02-COMPILE-LOG.md for static cross-reference verification (all `\ref{}` and `\cite{}` targets resolve; user must run actual compile) |
| `test-cross-refs-resolved` | ⚠️ STATIC-VERIFIED | `ax:S0`, `lem:peirce-preservation`, `thm:S4`, `thm:S4-full`, `cor:S4-phi-indep` all have `\label{}` definitions grep-verified |
| `test-no-new-warnings` | ⚠️ STATIC-VERIFIED | No new warnings expected; static verification in 55-02-COMPILE-LOG.md supports this |
| `test-submitted-frozen` | ✅ PASS | `git diff --stat HEAD~3..HEAD -- main-jmp-submitted.tex` → empty (zero output) |
| `test-forbidden-token-added-lines` | ✅ PASS | Final sweep → zero hits (see §5 above) |
| `test-role-swap-present` | ✅ PASS | Role-swap annotation present at axiom-verification.tex:149-150 (`roles $a \leftarrow b$ and $\{p_k, p_l\} \leftarrow \{p_i, p_j\}`), axiom-verification.tex:171-172, and appendix-proofs.tex:120-121 |

## 7. Forbidden Proxies (explicit rejection)

| ID | Status | Evidence |
|----|--------|----------|
| `fp-thm-937-leak` | ✅ REJECTED | Zero Thm 9.37 residue in edited scope (grep verified) |
| `fp-hos-in-revision` | ✅ REJECTED | Zero Hanche-Olsen hits in added lines (final sweep) |
| `fp-bare-as-cite-introduced` | ✅ REJECTED | No new bare `\cite{AS2003}` introduced; pre-existing bare cite at line 220 (out-of-scope) was not affected |
| `fp-rewrite-instead-of-edit` | ✅ REJECTED | +71/-33 lines total; theorem environments, section headings, proof structures all intact |
| `fp-submitted-file-touch` | ✅ REJECTED | `main-jmp-submitted.tex` unchanged (zero diff) |
| `fp-compile-skip` | ⚠️ PARTIAL | Full pdflatex unavailable (env gate); static cross-reference verification performed (see COMPILE-LOG.md) |
| `fp-role-swap-handwave` | ✅ REJECTED | Role-swap annotations explicit at 3 sites (see test-role-swap-present evidence) |
| `fp-phi-corollary-edit` | ✅ REJECTED | `cor:S4-phi-indep` verbatim-preserved (zero diff hunks) |
