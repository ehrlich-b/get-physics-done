# Phase 74: Phase 0 — Engine Recovery, Tangent Identity & Calibration - Research

**Researched:** 2026-06-01
**Domain:** Mathematical physics — exceptional Jordan algebra h_3(O); the Cayley plane OP^2 = F_4/Spin(9) as the primitive-idempotent variety; Peirce decomposition; exact-over-Q symbolic computation (SymPy/QQ); re-certification of the inherited v16.0/v17.0 engine.
**Confidence:** HIGH

## Summary

Phase 74 is a re-certification + calibration phase, not a discovery phase. Three requirements (DERV-01, DERV-02, VALD-01) establish the computational foundation and the single load-bearing geometric fact — that the soldering form `dE` is `V_{1/2}(E_11)`-valued, EXACTLY over Q — before any geometry is built on it in Phases 75-78. Two of the three requirements (DERV-01 engine recovery; VALD-01 calibration) are *re-pass* gates over warm, byte-identical v17.0 engines and carry HIGH confidence. The genuinely research-bearing piece is the **second half of DERV-02**: proving EXACTLY over Q that the tangent space to the primitive-idempotent variety of h_3(O) at `E_11` equals `V_{1/2}(E_11)`, of dimension 16.

That novel piece is fully de-risked. The primitive-idempotent variety (= affine cone over OP^2, = rank-1 locus) is cut out by the single quadratic Jordan equation `X∘X = Tr(X)·X` (Manivel; cp4space); with the trace-1 normalization this is `X∘X = X`. Linearizing `F(X) = X∘X − X` at `X = E_11` and taking the kernel of the Jacobian (the Zariski tangent space) over Q gives **exactly 16 dimensions, equal to V_{1/2}(E_11)** — I verified this end-to-end against the live engine this session (Jacobian rank 11 = 27 − 16; `rank[ker | V_half basis] = 16`; the engine's own `peirce_indices_under_E11()` independently puts `V_{1/2}` at engine indices {11..26} with `L_{E_11}` diagonal). The first half of DERV-02 (`E_11∘δ = (1/2)δ` for `δ ∈ V_{1/2}`) is just the Peirce half-eigenspace definition and reads directly off the same diagonal `L_{E_11}`.

A critical *planning* fact the prior research did not surface explicitly: the VALD-01 calibration anchors are **split across three engines**, not one. DERV-01 lives in `ring_lemma_verification.py` (CH + 324/324 + source guard; runs in ~1.5 s, confirmed ALL_PASS exit 0 this session). The single-copy anchor (orbit 24 / Spin(8)=28 / trdeg 3) lives in `orbit_dimension_gate.py`. The `e_6=78`, `orbit(E_11)=17`, `Stab_{E_6}(E_11)=61`, `Stab_{V_0}=45=Spin(9,1)` anchors AND the `K=−1/2` cone-Hessian sign benchmark live in `bulk_geometry_verification.py`. The latter two engines are slow (exact-QQ ranks on 27×78 / 52×27 matrices — minutes each) and buffer stdout when not a TTY.

**Primary recommendation:** Inherit the warm SSOT engines verbatim. DERV-01 = re-run `ring_lemma_verification.py` (assert exit 0 + the `exact_only_guard()` "0 outside-fence octonion_algebra imports" line). DERV-02 = (a) read the half-eigenvalue split off `peirce_indices_under_E11()` and check `E_11∘δ=(1/2)δ` per basis element; (b) build the 27×27 Jacobian of `X∘X − X` at `E_11`, take `sympy` nullspace over Q, assert `dim = 16` AND that the kernel equals `span(V_HALF_IDX)`. VALD-01 = re-run the single-copy gate in `orbit_dimension_gate.py` and the e_6/stabilizer/K=−1/2 gates in `bulk_geometry_verification.py`, asserting the exact integer anchors. Everything exact over Q (`sympy.Matrix.rank`/`.nullspace`/`.eigenvals`); `octonion_algebra.py` BANNED on every decisive path; no float.

## User Constraints

No phase CONTEXT.md exists (no `/gpd:discuss-phase` was run). The locked scope is the contract slice + requirements (`DERV-01`, `DERV-02`, `VALD-01`) and the milestone spec `paper6-cartan-tetrad-prompt.md`. Constraints binding this research:

- **Scope is Phase 0 ONLY.** Re-certification + calibration + the tangent identity. This phase does NOT perform the C_u/π_u coframe reduction (Phase 75), the Berry curvature (Phase 76), the Cartan connection (Phase 77), or the circularity audit (Phase 78). Do not research those here.
- **Exact over Q on every decisive path.** `sympy.Matrix.rank`/`.nullspace`/`.eigenvals` only — NEVER numpy/float (forbidden proxy `fp-float-decisive`: float tolerance fabricates rank/signature verdicts via derivative cancellations).
- **`octonion_algebra.py` is BANNED on any decisive path** (forbidden proxy `fp-octonion-algebra`: buggy `(x1 x2) x3` association, ~0.67 associator gap, corrupts det). The det SSOT is `ring_lemma_verification.py` det_3. The phase MUST include a source-guard confirming `octonion_algebra.py` is not imported on the decisive path.
- **Conventions LOCKED for v18.0** (inherit the v17.0 lock): octonion mul = Fano `e1 e2 = e4`; complex structure `u = e7`; `E_11 = diag(1,0,0)`; det SSOT cross-term `2Re(x2* x0* x1)`; metric signature mostly-minus `(−,+,+,+)` on the `h_2(C_u)` det_2 Lorentzian slice; bulk cone Riemannian positive-definite; natural units `ħ=k_B=1`.
- **`code/peirce_coupling.py` does NOT exist** (cited in the milestone prompt's build-on list, but absent from the repo). Use `bulk_geometry_verification.py:peirce_indices_under_E11` (it exists, at line 1753) and/or `embedding_under_E_verification.py`, or build Peirce-under-E_11 fresh. The machine-readable contract reference has already been corrected.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `code/ring_lemma_verification.py` det_3 SSOT (`ref-ring-lemma-engine`) | prior_artifact / benchmark | DERV-01: the det SSOT (F_4-invariant cubic norm, CH + 324/324 inner-derivation annihilation = dim f_4 = 52); the warm exact-Q h_3(O) engine to inherit | USE (re-run); assert ALL_PASS exit 0 + guard | plan, execution |
| `code/orbit_dimension_gate.py` (`ref-orbit-gate`) | prior_artifact / benchmark | VALD-01: single-copy orbit 24 / Spin(8)=28 / trdeg 3 calibration | USE (re-run); assert the anchors | plan, execution |
| `code/bulk_geometry_verification.py` (`ref-bulk-geometry-prior`, `ref-peirce-coupling`) | prior_artifact / benchmark | VALD-01: `e_6=78=52+26`, `orbit(E_11)=17`, `Stab_{E_6}(E_11)=61`, `Stab_{V_0}=45=Spin(9,1)`, and the `K=−1/2` cone-Hessian sign benchmark; DERV-02: `peirce_indices_under_E11()` (the V_{1/2} basis + half-eigenvalue) | USE (re-run + extend with the Jacobian-kernel tangent check) | plan, execution, verification |
| `code/embedding_under_E_verification.py` | prior_artifact | DERV-02 alternative Peirce-under-E_11 route; `proj_u_exact`/`slice_to_complex` (needed Phase 75, not here) | USE if a second Peirce route is wanted | plan, execution |
| Baez, *The Octonions* (Bull. AMS 39, 2002), §3.4 (`ref-baez-octonions`) | paper / definition | Canonical reference: `OP^2 = F_4/Spin(9)` (16-dim) and `T_E OP^2 = V_{1/2}(E)` | READ, CITE | plan, execution |
| McCrimmon, *A Taste of Jordan Algebras* (Springer 2004) (`ref-mccrimmon`) | paper / definition | The load-bearing tangent identity `E∘δ = (1/2)δ`; the Peirce decomposition backbone | READ, CITE | plan, execution |
| Manivel, *On the derived category of the Cayley plane* (arXiv:0907.2784) | paper / definition | The Cayley plane / rank-1 locus is cut out by `X² = Tr(X)·X`; E_6 orbit structure (rank 3/2/1 strata) | CITE (defining equations of the variety) | plan, execution |
| `paper6-cartan-tetrad-prompt.md` (`ref-prompt`) | spec | Authoritative milestone spec; the Phase 0 deliverables, conventions, forbidden proxies | READ | plan, execution |
| H^3 sign benchmark `K=−1/2` (Baseline) | benchmark | Pin sign conventions BEFORE any downstream curvature verdict; `g_slice|_apex = 2·g_round`, so `K=−1/2` vs round `K=−1` differ by an exact factor 2 | USE (re-pass) | plan, execution, verification |

**Missing or weak anchors:**

- **`code/peirce_coupling.py` is ABSENT** (named in the prompt). RESOLVED: use `bulk_geometry_verification.py:peirce_indices_under_E11` (confirmed present, line 1753) and/or `embedding_under_E_verification.py`. No blocker.
- **The Zariski-tangent-of-the-idempotent-variety computation is NOT yet in any engine** — it is the one piece of new code Phase 74 must add (~15 lines; prototyped and validated this session — see Mathematical Framework). The `peirce_indices_under_E11()` routine gives the half-eigenvalue split but NOT the variety-tangent statement; those are two distinct (and both required) clauses of DERV-02.
- **Live PDF fetches of Manivel (0907.2784) and the cp4space blog were thin/compressed** — but the defining equation `X²=Tr(X)·X` and the dimensions (cone 17, projective OP^2 16) are independently confirmed by the project's own engine comment (`bulk_geometry_verification.py:2981`: "orbit of E_11 = 17 = cone over Cayley plane OP^2") and by my exact-over-Q spot-check. Confidence HIGH despite thin fetches.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Octonion multiplication | Fano `e1 e2 = e4` (documented orientation) | other Fano labelings | v17.0 lock; `ring_lemma_verification.py` LOCK 3/3b |
| Complex structure | `u = e7` | any imaginary octonion | v17.0 lock |
| Primitive idempotent | `E_11 = diag(1,0,0)` | `E_22`, `E_33` (F_4-conjugate) | v17.0 lock |
| det_3 cross-term | `2 Re(x2* x0* x1)` (F_4-invariant) | buggy `2Re((x1 x2)x3)` (off by 16, REJECTED) | `ring_lemma_verification.py` det_3 |
| Engine coord layout (27-dim) | `V_1={0}` (alpha); `V_0={1,2}∪{3..10}` (beta,gamma,oct-x1); `V_{1/2}={11..26}` (oct-x2,oct-x3) | — | `bulk_geometry_verification.py:1058-1066`; `V_HALF_IDX = list(range(11,27))` |
| Metric signature | mostly-minus `(−,+,+,+)` on the det_2 Lorentzian slice | mostly-plus | v18.0 lock; CONVENTIONS §6 |
| Bulk cone metric | Riemannian (positive-definite) | — | v18.0 lock |
| H^3 curvature normalization | cone-Hessian `K=−1/2`; `g_slice|_apex = 2·g_round`; round-H^3 `K=−1` | — | `bulk_geometry_verification.py:1358-1370` |
| Units | natural `ħ=k_B=1` | SI | v18.0 lock |

**CRITICAL: All results below use these conventions.** The det_3 cross-term order `2Re(x2* x0* x1)` is load-bearing — the cyclic-rotation variant is the documented buggy form (annihilated by only 30 of 324 inner derivations) and is REJECTED. The `K=−1/2` magnitude is the cone-Hessian/round factor-of-2 normalization, not an error; the load-bearing fact is the negative-constant SIGN.

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `X∘X = X`, `Tr(X) = 1` | primitive-idempotent (rank-1) variety = OP^2 (trace-1 normalization) | McCrimmon; Baez §3.4 | DERV-02: the variety whose tangent at `E_11` we compute |
| `X∘X = Tr(X)·X` | rank-1 / affine cone over OP^2 (un-normalized) | Manivel 0907.2784; cp4space | DERV-02: the cone (dim 17 = `orbit(E_11)`); homogenize ↔ projective OP^2 (dim 16) |
| `X#  = 0` (adjoint/sharp vanishes) | the rank ≤ 1 condition (all 2×2 "minors" vanish) | Springer-Veldkamp; KMRT | DERV-02 ALTERNATIVE: cuts out the rank-1 component explicitly (referee-proof) |
| `E_11 ∘ δ = λ δ`, `λ ∈ {0, 1/2, 1}` | Peirce eigenvalue equation for `L_{E_11}` | McCrimmon; Baez | DERV-02 first half: `δ ∈ V_{1/2}` ⟺ `λ = 1/2` |
| `D F_{E_11}(b) = 2·jordan(E_11, b) − b` | linearization of `F(X)=X∘X−X` at `E_11` | derived (jordan symmetric) | DERV-02: the 27×27 Jacobian; kernel = Zariski tangent |
| `N(X) = X^∘3 − Tr(X)X^∘2 + S(X)X − N·I` | Cayley-Hamilton cubic for `jordan` (`S=(1/2)(Tr²−Tr(X∘X))`) | `ring_lemma_verification.py:316` | DERV-01: det_3 = the unique CH generic norm (LOCK 7a) |
| `D_ξ det_3 = 0` ∀ `ξ ∈ {[L_a,L_b]}` (324 brackets, span f_4 = 52) | inner-derivation annihilation = F_4-invariance | `ring_lemma_verification.py:699` | DERV-01: LOCK 7b (324/324) |
| `g_ij = Hess(−log det_2)` on `{det_2=1}` → `K=−1/2` | cone-Hessian sectional curvature on the H^3 hyperboloid | `bulk_geometry_verification.py:1503-1582` | VALD-01: sign benchmark |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Peirce decomposition via `L_E` spectrum | `L_{E_11}` is diagonal in the engine-native basis; eigenvalues {0,1/2,1} give `V_0`/`V_{1/2}`/`V_1` as coordinate index sets | DERV-02 first half | McCrimmon; `peirce_indices_under_E11()` |
| Zariski tangent space = kernel of the defining-map Jacobian | linearize `F(X)=X∘X−X` at `E_11`; the nullspace over Q is the tangent space; `dim = 27 − rank(J)` | DERV-02 second half | standard algebraic geometry; Manivel for the variety |
| Exact rational rank/nullspace over QQ | `sympy.Matrix.rank`/`.nullspace` (or `DomainMatrix(...).rank()`); generic-point sampling over Z for orbit dims (rank is lower-semicontinuous) | DERV-02, VALD-01 | `orbit_dimension_gate.py` `exact_qq_rank`/`span_rank_over_QQ` |
| Source-import AST/text guard | `exact_only_guard()` greps the file for real `octonion_algebra` imports outside the single sanctioned fence and for float-rank calls | DERV-01 | `ring_lemma_verification.py:541` |
| Closed-form Totaro + hand-rolled Levi-Civita Riemann; sectional curvature | curvature of the cone-Hessian metric on the det_2=1 slice; `K=−1/2` | VALD-01 sign benchmark | `bulk_geometry_verification.py` |

### The DERV-02 second-half method (validated this session, exact over Q)

This is the one genuinely new computation. The recipe:

```python
# Engine-native 27-dim coords. F(X) = X∘X − X (the idempotent / trace-1 OP^2 equation).
# Linearization at E_11: DF(b_k) = 2*jordan(E_11, b_k) − b_k   (jordan symmetric).
basis = BG._standard_basis_27()
E11   = BG.h3o_from_coords(1,0,0, BG.oct_zero(), BG.oct_zero(), BG.oct_zero())
cols  = [BG._flat27(BG.octmat_sub(BG.octmat_scal(Rational(2), BG.jordan(E11, basis[k])), basis[k]))
         for k in range(27)]
J     = Matrix(27, 27, lambda r, c: cols[c][r])     # Jacobian; column k = DF(b_k)
ker   = J.nullspace()                                # Zariski tangent space, exact over Q
assert J.rank() == 11                                # 27 − 16
assert len(ker) == 16                                # dim T_{E_11} OP^2 = 16
# Identity with V_{1/2}: kernel == span(engine indices 11..26).
Khalf = Matrix.hstack(*[Matrix([1 if i==j else 0 for i in range(27)]) for j in range(11,27)])
assert Matrix.hstack(*ker, Khalf).rank() == 16       # ker ⊆ and ⊇ V_half  ⇒  equal
```

**Result (confirmed live):** `J.rank() = 11`, `dim ker = 16`, `rank[ker | V_half] = 16`. The Zariski tangent space of `{X∘X = X}` at `E_11` is **exactly the 16-dim `V_{1/2}(E_11)`**. The trace-1 constraint `Tr(X)=1` is automatically tangent (the kernel has no `V_1`/alpha component, and Tr is constant along it), so it need not be imposed separately — but the executor MAY add `d Tr = 0` as a defensive 28th row (it does not change the kernel).

**Subtlety to document (not a blocker):** the bare equation `X∘X = X` cuts out *all* idempotents (ranks 0,1,2,3). The Zariski tangent at `E_11` could in principle include directions toward higher-rank strata — but it does not: the computed tangent is exactly 16-dim = `V_{1/2}` = `T_{E_11} OP^2`, because `E_11` is a *smooth* point of the rank-1 component and the strata do not meet it tangentially at first order. For a referee-proof statement that the rank-1 *component* (not the whole idempotent scheme) is what is tangent, the executor can additionally cut the variety with the sharp equations `X# = 0` (rank ≤ 1) and re-confirm the same 16-dim kernel; the `orbit(E_11) = 17` anchor (the affine cone) is the independent cross-check that the projective tangent is `17 − 1 = 16`.

### Approximation Schemes

None. This phase is exact over Q end-to-end; there are no controlled approximations, small parameters, or truncations. Any appearance of a float on a decisive path is a defect (`fp-float-decisive`), not an approximation.

## Standard Approaches

### Approach 1: Inherit-and-re-run the warm SSOT engines + add the one Jacobian-kernel check (RECOMMENDED)

**What:** DERV-01 and VALD-01 are re-pass gates over byte-identical v16.0/v17.0 engines. Re-run them, assert the exact anchors, and assert the source guard. DERV-02 reuses `peirce_indices_under_E11()` for the half-eigenvalue split and adds the ~15-line Jacobian-kernel tangent computation above.
**Why standard:** the engines are validated across v16.0/v17.0; the det_3 SSOT is the project's single source of truth; re-deriving any of it wastes context and risks introducing the very `octonion_algebra.py` association bug the guard exists to catch.
**Track record:** `ring_lemma_verification.py` ALL_PASS confirmed this session (exit 0, ~1.5 s); the calibration anchors are the same numbers v17.0 Phase 70-73 relied on; the Zariski-tangent method validated live this session.
**Key steps:**

1. **DERV-01:** run `python3 code/ring_lemma_verification.py`; assert exit 0 and ALL_PASS; capture the LOCK 7a (CH norm), LOCK 7b (324/324, dim f_4=52), and `exact-only guard` lines (the guard reports "octonion_algebra imports: 1 in-fence (expect 1), 0 outside (expect 0); float-rank calls: 0").
2. **DERV-02(a):** call `peirce_indices_under_E11()`; assert `V_{1/2}` = indices {11..26} (16 elements) and `L_{E_11}` diagonal; for each `δ` in the V_{1/2} basis, assert `jordan(E_11, δ) == (1/2)·δ` exactly over Q.
3. **DERV-02(b):** build the 27×27 Jacobian of `X∘X − X` at `E_11`; assert `nullspace` dim = 16 AND kernel = `span(V_HALF_IDX)`; record both the dimension and the index-set identity.
4. **VALD-01(single-copy):** run `python3 code/orbit_dimension_gate.py`; assert orbit 24 / Spin(8)=28 / trdeg 3 (the multi-point MAX = 24 gate).
5. **VALD-01(e_6/stab/K):** run `python3 code/bulk_geometry_verification.py`; assert `e_6 = 78 = 52+26`, `orbit(E_11)=17`, `Stab_{E_6}(E_11)=61`, `Stab_{V_0}=45=Spin(9,1)`, and `K_value = −1/2` (with the round-metric `K=−1` factor-2 cross-check).
6. Write `derivations/` deliverable + supporting exact-SymPy code stating the three results with the convention lock.

**Known difficulties at each step:**

- Step 1: none expected (fast, confirmed passing). If it fails, the engine has drifted — STOP and diff against the v17.0 commit.
- Step 3: the kernel must be checked for *equality* with `V_{1/2}`, not just dimension 16 — a 16-dim kernel that is not coordinate-aligned to {11..26} would be a (very surprising) red flag. The `rank[ker | V_half]` test is the clean equality check.
- Steps 4-5: SLOW (minutes) and stdout is buffered when not a TTY. Run with `python -u` (unbuffered) so progress is visible and the long-symbolic-run watchdog does not mistake silence for a stall. Budget for the exact-QQ ranks on 27×78 (e_6) and 52×27 (single-copy) matrices.

### Approach 2: Build Peirce-under-E_11 and the tangent check fresh, in a new `code/cartan_curvature_verification.py` (FALLBACK / forward-looking)

**What:** verbatim-copy the SSOT engine (det_3, jordan, Tr, `_standard_basis_27`, `_flat27`) into a fresh Phase-0 file (matching the v17.0 precedent of one self-contained verification file per milestone), and implement Peirce-under-E_11 + the Jacobian-kernel tangent there.
**When to switch:** if the planner wants a single self-contained Phase-0 artifact that Phases 75-78 extend (likely, since the V_{1/2} basis and the engine are reused downstream), rather than spreading the Phase-0 checks across three existing files.
**Tradeoffs:** + one clean inheritable artifact and one `exact_only_guard()` to enforce; − must re-assert byte-identity of the copied det_3 against `ring_lemma_verification.py` (the v17.0 `verbatim_copy_integrity()` / "LOCK 0 byte-identical" pattern at `bulk_geometry_verification.py:807,2537` is the template). The calibration anchors (single-copy, e_6/stab) are expensive to re-implement, so even with this approach VALD-01 should *call into* `orbit_dimension_gate.py` / `bulk_geometry_verification.py` rather than re-derive.

### Anti-Patterns to Avoid

- **Re-deriving the det_3 cross-term or the octonion product.** The correct association is `2Re(x2* x0* x1)`; the "obvious" `2Re((x1 x2)x3)` is the documented bug (off by 16, annihilated by only 30/324 derivations). Inherit, never re-derive. *Example:* importing `octonion_algebra.py` "just for the product" silently corrupts det_3 and every downstream curvature.
- **Checking only `dim = 16` for the tangent, not the identity with `V_{1/2}`.** A dimension match is necessary but not sufficient; DERV-02 claims the tangent *equals* `V_{1/2}(E_11)`, which requires the index-set / span identity. *Example:* a kernel that happened to be 16-dim but mixed `V_0` directions would satisfy a naive dim check yet falsify the geometric claim the soldering form rests on.
- **Using a float rank/eigenvalue anywhere on the decisive path.** `numpy.linalg.matrix_rank` is `fp-float-decisive` — derivative cancellations in the Jacobian/Gram can fabricate or destroy a rank. SymPy/QQ only. mpmath is allowed for a *triage* spot-check, never a verdict.
- **Treating `orbit(E_11)=17` as the tangent dimension.** 17 is the *affine cone* (rank-1 locus including scale) / E_6-orbit dimension; the projective OP^2 tangent is `17 − 1 = 16`. Conflating them would mis-state DERV-02.
- **Skipping the `K=−1/2` sign benchmark "because it's downstream."** The sign convention must be pinned in Phase 0; an unfixed sign poisons every curvature verdict in Phases 76-77. It is cheap relative to the stabilizer ranks — keep it.

## Existing Results to Leverage

**This section is MANDATORY.** These are CITE-don't-re-derive results. The whole phase is re-certification, so almost everything here is "inherit, assert, move on."

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Cayley plane = primitive-idempotent variety | `OP^2 = F_4/Spin(9)`, 16-dim; trace-1 idempotents of h_3(O) | Borel 1950; Baez 2002 §3.4 | DERV-02: the variety; its dim 16 is the target |
| Tangent = Peirce half-eigenspace | `T_E OP^2 = V_{1/2}(E)` via `E∘δ=(1/2)δ` | McCrimmon; Baez 2002 | DERV-02: the identification to verify exactly |
| Defining equation of the rank-1 locus | `X² = Tr(X)·X` (single quadratic Jordan eqn); rank ≤ 1 ⟺ `X# = 0` | Manivel 0907.2784; cp4space; Springer-Veldkamp | DERV-02: linearize this at `E_11` for the Zariski tangent |
| det_3 = unique CH generic norm of `jordan` | `N(X)` from `X^∘3 − Tr X·X^∘2 + S·X − N·I` | `ring_lemma_verification.py` (SSOT) | DERV-01: LOCK 7a — assert, don't re-derive |
| `Der(h_3(O)) = f_4`, dim 52 | spanned by the 324 inner derivations `[L_a,L_b]`; all annihilate det_3 | `ring_lemma_verification.py:699`; Baez | DERV-01: LOCK 7b (324/324) |
| `e_6 = f_4 ⊕ L(h_3(O)_traceless)`, dim 78 = 52+26 | Koecher-Tits | `bulk_geometry_verification.py:1735`; Baez | VALD-01: assert dim 78 |
| `orbit(E_11) = 17`, `Stab_{E_6}(E_11)=61` | 17 = dim of the cone over OP^2; `61 = 78 − 17` | `bulk_geometry_verification.py:2981`; Manivel | VALD-01: assert; also the 16 = 17−1 cross-check for DERV-02 |
| `Stab_{V_0} = 45 = dim Spin(9,1)` | the slice-preserving Levi | `bulk_geometry_verification.py:2995`; v17.0 | VALD-01: assert |
| single-copy orbit 24 / Spin(8)=28 / trdeg 3 | Garibaldi-Guralnick / Lawther anchor, COMPUTED in-engine | `orbit_dimension_gate.py` | VALD-01: assert |
| `h_2(C_u) ≅ R^{3,1}`, det_2 = Minkowski, signature (1,3) | 2×2 Hermitian-over-C determinant IS the Minkowski form | `derivations/52-kkt-spacetime.tex`; nLab | context only (the Phase-75 precedent); not computed here |
| cone-Hessian on `{det_2=1}` has `K=−1/2` | constant, negative; round-H^3 `K=−1` differs by exact factor 2 (`g_slice|_apex=2 g_round`) | `bulk_geometry_verification.py:1358-1582` | VALD-01: sign benchmark — assert `K=−1/2` |

**Key insight:** This is a re-certification phase. Re-deriving any of the above is wasted context AND a risk — the SSOT engine exists precisely so that the correct (non-associative-bug-free) det_3 is reused byte-identically. The only *new* derivation is the ~15-line Jacobian-kernel tangent check, and it is already validated.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `peirce_indices_under_E11()` returns `{0:[1..10], 1/2:[11..26], 1:[0]}`, `L_{E_11}` diagonal | the V_{1/2} basis as coordinate indices + the half-eigenvalue, for free | `bulk_geometry_verification.py:1753` | exact over Q; native engine layout |
| `_standard_basis_27()`, `_flat27`, `jordan`, `octmat_scal/sub` | the building blocks for the Jacobian-kernel computation | `bulk_geometry_verification.py` | exact over Q |
| `exact_qq_rank`, `span_rank_over_QQ`, `infinitesimal_action` | fast exact-QQ rank / orbit-dimension machinery | `orbit_dimension_gate.py` | char-0; generic-point sampling |
| `verbatim_copy_integrity()` / "LOCK 0 byte-identical" pattern | the template for asserting a copied det_3 matches the SSOT | `bulk_geometry_verification.py:807,2537` | if Approach 2 is taken |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| *The Octonions*, Bull. AMS 39:145, §3.4 (math/0105155) | Baez | 2002 | canonical OP^2=F_4/Spin(9), `T_E OP^2 = V_{1/2}` | the identification (cite) |
| *A Taste of Jordan Algebras* | McCrimmon | 2004 | Peirce decomposition; `E∘δ=(1/2)δ`; primitive idempotents | the tangent identity (cite) |
| *On the derived category of the Cayley plane* (arXiv:0907.2784) | Manivel | 2011 | OP^2 / rank-1 locus cut by `X²=Tr(X)X`; E_6 orbits rank 3/2/1 | the defining equation + the 16/17 dimensions (cite) |
| *Composition Algebras, Exceptional Jordan Algebra and Related Groups* (JGSP 46:59) | — | 2017 | h_3(O) rank-3 simple Euclidean Jordan algebra, F_4 transitive on rank-1 idempotents, Stab = Spin(9) | corroboration (cite if useful) |
| `derivations/52-kkt-spacetime.tex`, `52-observer-uniqueness.tex` | (in-program) | — | `h_2(C_u) ≅ R^{3,1}`; the Phase-46 π_u bottleneck | context for Phase 75 (NOT computed here) |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (confirmed in env) | exact symbolic algebra over QQ: `Matrix.rank`/`.nullspace`/`.eigenvals`, `jordan`, det_3, `cancel`/`simplify` | the whole program runs exact over Q; `DomainMatrix` over QQ is the fast exact-rank path |
| Python | 3.14.2 (confirmed) | run the engines | — |
| `ring_lemma_verification.py` | in-repo (SSOT) | DERV-01: det_3, CH norm, 324/324, `exact_only_guard()` | the det single-source-of-truth |
| `bulk_geometry_verification.py` | in-repo | DERV-02 (`peirce_indices_under_E11`); VALD-01 (e_6/stab/`K=−1/2`) | the calibration + curvature harness |
| `orbit_dimension_gate.py` | in-repo | VALD-01 single-copy (orbit 24/Spin(8)=28/trdeg 3); `exact_qq_rank` | the orbit/stabilizer engine |
| `embedding_under_E_verification.py` | in-repo | DERV-02 alt Peirce route; `proj_u_exact` (Phase 75) | second Peirce-under-E_11 route |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| NumPy | 2.4.2 — float spot-checks ONLY (signature/zero triage) | NEVER on a decisive rank/eigenvalue/zero-test (`fp-float-decisive`) |
| mpmath | high-precision triage of which components are nonzero | cross-check only, never a verdict |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| three existing engines | one fresh `cartan_curvature_verification.py` (Approach 2) | cleaner single inheritable artifact for Phases 75-78, but must re-assert byte-identity and still call into the slow calibration engines |
| `peirce_indices_under_E11()` | `embedding_under_E_verification.py` Peirce route | redundant second route (good for cross-check, not required) |
| `sympy.Matrix.rank` | `DomainMatrix(...).rank()` over QQ | faster for the 27×78 / 52×27 ranks; the engines already use it via `exact_qq_rank` |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| DERV-01 (`ring_lemma_verification.py`) | ~1.5 s (measured this session) | none | — |
| DERV-02 Jacobian-kernel + half-eigenvalue | seconds | trivial (27×27 over Q) | — (validated live) |
| VALD-01 single-copy (`orbit_dimension_gate.py`) | ~1-2 min (single-copy ranks ~55-110 s per the project COMPUTATIONAL.md) | exact-QQ rank on 52×27 | run unbuffered (`python -u`); generic-point sampling already used |
| VALD-01 e_6 + stabilizers + K (`bulk_geometry_verification.py`) | several minutes (e_6 78-dim span rank + two stabilizer kernels + curvature benchmark) | exact-QQ ranks on 27×78; nullspaces; symbolic Riemann | run unbuffered; the long-symbolic-run watchdog can mistake buffered silence for a stall — see Pitfalls |

**Installation / Setup:**
```bash
# Environment already provisioned (confirmed): Python 3.14.2, SymPy 1.14.0, NumPy 2.4.2.
# No new packages on the decisive path. Run unbuffered so progress is visible:
python -u code/ring_lemma_verification.py        # DERV-01 (~1.5s)
python -u code/orbit_dimension_gate.py           # VALD-01 single-copy (~1-2 min)
python -u code/bulk_geometry_verification.py     # VALD-01 e_6/stab/K + DERV-02 peirce (several min)
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| det_3 = CH generic norm (LOCK 7a) | det_3 is the unique cubic norm of `jordan` | `simplify(det_3(P) − cayley_hamilton_norm(P)) == 0` at ≥3 octonionic points | 0 (exact) |
| 324/324 inner-derivation annihilation (LOCK 7b) | det_3 is F_4-invariant (dim f_4 = 52) | `D_ξ det_3 = 0` for all 324 brackets at an octonionic point | 324/324 killed |
| source guard | no `octonion_algebra.py` on the decisive path | `exact_only_guard()` text/AST scan | "0 outside (expect 0); float-rank calls: 0" |
| `E_11∘δ=(1/2)δ` per basis element | the half-eigenspace identity | `jordan(E_11, δ) == Rational(1,2)*δ` for each `δ ∈ V_{1/2}` | exact equality, all 16 |
| tangent dim AND identity | `T_{E_11}OP^2 = V_{1/2}(16)` | `nullspace(J)` dim = 16 AND `rank[ker | V_half] = 16` | 16 and 16 |
| 16 = 17 − 1 cross-check | projective tangent vs affine cone | compare DERV-02 (16) with VALD-01 `orbit(E_11)=17` | consistent |
| e_6 = f_4 ⊕ L(traceless) | dim 78 = 52 + 26 | `span_rank_over_QQ` | 78 |
| stabilizer arithmetic | `61 = 78 − 17`; `45 = dim Spin(9,1)` | exact kernels | 61, 45 |
| `K=−1/2` with round-`K=−1` factor 2 | sign convention pinned | `sectional_curvature` on `{det_2=1}` at the rational point | `K_value = −1/2`, `round_K = −1` |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| cone-Hessian on H^3 | det_2 = 1 hyperboloid | constant `K = −1/2` (round metric `−1`, factor 2) | `bulk_geometry_verification.py`; SL(2,C)/SU(2) |
| F_4 transitive on rank-1 idempotents, Stab = Spin(9) | — | `OP^2 = F_4/Spin(9)`, dim 16 | Baez 2002; JGSP 46 |
| matrices over h_3(O) rank strata | E_6 orbits | rank 3 (open) / 2 (det hypersurface) / 1 (closed orbit = OP^2) | Manivel 0907.2784 |

### Numerical Validation

Not applicable in the float sense — every check is exact over Q. The only "numerical" element is the high-precision mpmath spot-check, allowed solely to triage which components are nonzero before a symbolic simplify, never as a verdict.

### Red Flags During Computation

- `ring_lemma_verification.py` exits nonzero or prints "FAILURES PRESENT" → the engine has drifted from the v17.0 SSOT; STOP and diff against the warm commit. Do NOT patch around it.
- The Jacobian nullspace is 16-dim but NOT equal to `span(V_HALF_IDX)` → a basis/layout bug or a wrong `E_11`; the geometric claim is false as stated until resolved.
- The 324/324 count comes back < 324 (e.g. 30) → the buggy `(x1 x2)x3` association has crept in; the det is corrupted. This is exactly what the guard exists to prevent.
- `orbit(E_11)` ≠ 17 or `Stab_{V_0}` ≠ 45 → a regression in the e_6/stabilizer machinery; the v17.0 anchors must reproduce byte-for-byte.
- `K_value` comes back `+1/2` or `−1` (instead of `−1/2`) → a sign/normalization slip; pin it before any downstream phase reads a curvature sign.
- A float appears in any rank/eigenvalue on the decisive path → `fp-float-decisive`; remove it.

## Common Pitfalls

### Pitfall 1: Re-deriving (and re-breaking) the octonion product / det_3 cross-term

**What goes wrong:** writing a fresh octonion multiplication or det_3 with the "natural" association `2Re((x1 x2)x3)` instead of the F_4-invariant `2Re(x2* x0* x1)`.
**Why it happens:** the buggy order looks symmetric and passes naive sanity checks (it still gives `N(I)=1` and matches the float-det oracle), but it is annihilated by only 30 of 324 inner derivations — it is NOT F_4-invariant and corrupts every downstream curvature.
**How to avoid:** inherit `det_3`/`jordan` from `ring_lemma_verification.py` verbatim; if copying into a fresh file (Approach 2), assert byte-identity (the `verbatim_copy_integrity()` / LOCK 0 pattern). Run `exact_only_guard()`.
**Warning signs:** 324/324 → some smaller number; `octonion_algebra` import outside the sanctioned fence; an associator gap ≈ 0.67.
**Recovery:** revert to the SSOT engine; never patch the cross-term by hand.

### Pitfall 2: Verifying tangent *dimension* but not the *identity* with V_{1/2}

**What goes wrong:** asserting `dim ker = 16` and declaring DERV-02 done, without confirming the kernel equals `V_{1/2}(E_11)`.
**Why it happens:** the dimension is the headline number; the index-set identity is easy to skip.
**How to avoid:** always run the `rank[ker | V_half] == 16` equality check; report the kernel as a coordinate index set, not just its dimension.
**Warning signs:** a 16-dim kernel with nonzero components in `V_0` indices {1..10} or the `V_1` index {0}.
**Recovery:** re-examine the Jacobian construction and `E_11`; check the engine layout (`V_HALF_IDX = range(11,27)`).

### Pitfall 3: Watchdog mistaking buffered silence on the slow calibration runs for a stall

**What goes wrong:** `orbit_dimension_gate.py` / `bulk_geometry_verification.py` produce no stdout for minutes (Python buffers when not a TTY), and a stream-watchdog or the agent kills the run as a "stall."
**Why it happens:** the exact-QQ ranks on 27×78 / 52×27 matrices are genuinely slow and the `print`/`_report` output is buffered until flush. (This is a known repo failure mode — long no-output symbolic runs get killed around the harness timeout.)
**How to avoid:** run with `python -u` (unbuffered); for very long runs, run in the background and poll the log, or have the orchestrator commit + write SUMMARY on stall (the work is deterministic and re-runnable). Budget minutes, not seconds, for VALD-01.
**Warning signs:** empty log file while the process is still alive (`pgrep` shows it running).
**Recovery:** the computations are pure/deterministic — just re-run unbuffered; nothing is lost.

### Pitfall 4: Skipping or mis-signing the K=−1/2 benchmark

**What goes wrong:** treating the sign benchmark as "downstream curvature" and deferring it, or accepting `−1` (the round-metric value) as the cone-Hessian value.
**Why it happens:** `K=−1/2` looks like it belongs to Phase 76/77; the factor-2 vs the round `−1` is easy to fumble.
**How to avoid:** pin the sign in Phase 0; assert `K_value = −1/2` AND `round_K = −1` (the factor-2 cross-check). The load-bearing fact is the negative-constant SIGN; the magnitude `1/2` is the documented `g_slice|_apex = 2 g_round` normalization.
**Warning signs:** `K_value` is `+1/2` or `−1`.
**Recovery:** re-derive nothing — re-read `bulk_geometry_verification.py:1358-1370`'s normalization note and confirm the slice point lies on `det_2=1`.

## Level of Rigor

**Required for this phase:** EXACT computational proof over Q (the strongest tier in this program). Every decisive statement is an exact rational equality / rank / eigenvalue, machine-checked, with the source guard certifying no banned engine and no float on the decisive path.

**Justification:** Phase 0 is the foundation the entire milestone (Phases 75-78) stands on. The soldering form being `V_{1/2}`-valued (DERV-02) is the geometric premise of the coframe reduction, the Berry curvature, and the Cartan connection. The det SSOT (DERV-01) underlies every downstream curvature. A weaker rigor here would propagate silently into every later verdict.

**What this means concretely:**

- All ranks/eigenvalues/zero-tests via `sympy` over QQ (or QQ(I) where complex — not needed in Phase 74). NEVER numpy/float on a decisive path.
- DERV-02 must report BOTH the tangent dimension (16) AND the index-set identity (kernel = `V_{1/2}` = {11..26}), plus the `16 = 17 − 1` cross-check against `orbit(E_11)`.
- DERV-01 must report engine exit 0 + ALL_PASS + the explicit guard line ("0 outside-fence octonion_algebra imports; 0 float-rank calls").
- VALD-01 must report every anchor as an exact integer / exact rational (`24, 28, 3, 78, 17, 61, 45` and `K=−1/2`), each from its named engine.
- Established math (`OP^2=F_4/Spin(9)`, `T_E OP^2=V_{1/2}`, the `X²=Tr(X)X` defining equation, the QGT split) is CITED, not re-derived.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| `octonion_algebra.py` det_3 (float, `(x1 x2)x3` association) | `ring_lemma_verification.py` det_3 (exact Q, `2Re(x2* x0* x1)`, 324/324 verified) | v16.0 | DERV-01: the SSOT; the old engine is BANNED on decisive paths |
| naive Spin(8)-triality "back-of-envelope" orbit count | computed exact-QQ orbit/stabilizer ranks | v16.0 (the GATE surprise) | VALD-01: trust the rank, not the hand count |
| `peirce_coupling.py` (named in the prompt) | `peirce_indices_under_E11()` (real, in `bulk_geometry_verification.py`) | — (the named file never existed) | DERV-02: use the real routine |

**Superseded approaches to avoid:**

- `octonion_algebra.py` on any decisive path — buggy associator (~0.67 gap); replaced by the exact SSOT. People still reach for it because it has a convenient API; the guard exists to catch that.
- Hand-counting stabilizer dimensions from coset arithmetic — the v16.0 "7" surprise showed a back-of-envelope count can be wrong; the orbit-rank method is decisive.

## Open Questions

1. **Should DERV-02 cut the variety with `X∘X=X` alone, or also impose `X#=0` (rank-1 component)?**
   - What we know: `X∘X=X` linearized at `E_11` already gives exactly the 16-dim `V_{1/2}` tangent (validated live); the trace-1 constraint is automatically tangent.
   - What's unclear: whether a referee demands the rank-1 *component* be cut out explicitly (via the sharp equations `X#=0`) rather than relying on `E_11` being a smooth point of the rank-1 stratum of the full idempotent scheme.
   - Impact on this phase: cosmetic/rigor-presentation only — both routes give the same 16-dim kernel; the `orbit(E_11)=17` anchor independently certifies the projective tangent is `17−1=16`.
   - Recommendation: lead with `X∘X=X` (simplest, validated); have the executor add the `X#=0` confirmation as a defensive cross-check if the deliverable is to be referee-proof. NOT a blocker.

2. **One self-contained Phase-0 file vs three existing engines?**
   - What we know: the v17.0 precedent is one verification file per milestone; Phases 75-78 will reuse the V_{1/2} basis + engine.
   - What's unclear: planner's preference.
   - Impact: organizational; affects whether DERV-01/VALD-01 are re-run-in-place or wrapped.
   - Recommendation: a thin Phase-0 driver that (a) adds the Jacobian-kernel tangent check and (b) *calls into* the three existing engines for the re-pass anchors (don't re-implement the slow ranks). Forward-compatible with a fresh `cartan_curvature_verification.py` for Phase 75+.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| `ring_lemma_verification.py` re-pass | engine drift / env change | diff against the v17.0 commit, restore the warm file | low (git) |
| `peirce_indices_under_E11()` half-eigenvalue split | unexpected layout change | `embedding_under_E_verification.py` Peirce route, or build from `L_{E_11}` spectrum fresh | low |
| `X∘X=X` Jacobian-kernel tangent | (very unlikely — validated) referee wants the rank-1 component explicit | add `X#=0` (sharp) equations and re-confirm 16-dim kernel | low (~20 lines) |
| in-place re-run of the three engines | planner wants one artifact | Approach 2: fresh self-contained file with byte-identity assert + calls into the slow engines | medium |

**Decision criteria:** Phase 74 has no genuine failure mode that should HALT the milestone — it is re-certification of validated machinery plus one already-validated new check. If `ring_lemma_verification.py` does NOT re-pass, that is an environment/engine-integrity problem to fix (restore the warm file), not a physics dead-end.

## Caveats and Alternatives (pre-submission self-critique)

1. **What assumption might be wrong?** That the warm engines still pass in the current env. Mitigation: I re-ran `ring_lemma_verification.py` this session (exit 0, ALL_PASS, ~1.5 s) and validated the DERV-02 Jacobian-kernel live; the two slow calibration engines were launched and were still running at write-time (deterministic, byte-identical to v17.0 anchors — expected to pass, but the planner should treat the VALD-01 re-pass as a "run-and-assert" task, not a foregone print).
2. **What did I dismiss too quickly?** The `X#=0` (sharp/rank-1) defining-equation route — I lead with `X∘X=X` because it is simplest and already gives the right 16-dim tangent. If a referee insists on cutting out the rank-1 *component* (not the whole idempotent scheme), the sharp equations are the rigorous answer; I flagged this as Open Question 1 rather than burying it.
3. **What limitation am I understating?** The live PDF fetches of Manivel/cp4space were thin (compressed PDF; blog lacked the dimension details). I lean on the project's own engine comment (`orbit(E_11)=17 = cone over Cayley plane OP^2`) and my exact spot-check to backstop the `X²=Tr(X)X` / 16 / 17 claims — these are standard, multiply-attested facts, so confidence stays HIGH, but the *primary-source equation numbers* are not pinned (the math is not in doubt).
4. **Simpler method overlooked?** For DERV-02 first half, no — reading the half-eigenvalue off the already-diagonal `L_{E_11}` via `peirce_indices_under_E11()` is the simplest possible route. For the tangent, the 27×27 Jacobian nullspace is about as simple as it gets.
5. **Would a specialist disagree?** A Jordan-algebra specialist might prefer the intrinsic statement (`T_E OP^2 = V_{1/2}(E)` is *definitional* via `E∘δ=(1/2)δ`, so "the tangent is the half-eigenspace" is almost a tautology once you know OP^2 is the idempotent variety) over the extrinsic Jacobian-kernel computation. Both are correct; the contract (DERV-02 / `test-tangent-identity`) explicitly asks for the *variety* tangent computed exactly over Q, so the Jacobian-kernel route is the right deliverable, with the half-eigenvalue identity as the conceptual cross-check. They agree exactly (validated live).

## Sources

### Primary (HIGH confidence)

- **J. C. Baez, "The Octonions," Bull. Amer. Math. Soc. 39 (2002) 145-205, arXiv:math/0105155, §3.4 (Cayley plane).** `OP^2 = F_4/Spin(9)` (16-dim); `T_E OP^2 = V_{1/2}(E)`; `F_4 = Aut(h_3(O))`.
- **K. McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004).** Peirce decomposition; primitive idempotents; the `E∘δ = (1/2)δ` tangent identity.
- **L. Manivel, "On the derived category of the Cayley plane," J. Algebra (arXiv:0907.2784, 2011).** The Cayley plane / rank-1 locus cut out by `X² = Tr(X)·X`; the E_6 orbit stratification (rank 3 / 2 / 1) of `P(J_3(O))`.
- **In-repo SSOT engines (validated v16.0/v17.0, exact over Q):** `ring_lemma_verification.py` (det_3, CH norm LOCK 7a, 324/324 LOCK 7b, `exact_only_guard()`); `orbit_dimension_gate.py` (single-copy orbit 24 / Spin(8) 28 / trdeg 3; `exact_qq_rank`); `bulk_geometry_verification.py` (`peirce_indices_under_E11`, `e6_dimension`=78, `stab_E6_E11`=61 with `orbit(E_11)=17`, `stab_preserving_V0`=45, the `K=−1/2` sectional-curvature benchmark). DERV-01 re-confirmed ALL_PASS exit 0 this session; the DERV-02 Jacobian-kernel tangent (rank 11, ker 16 = `V_{1/2}`) validated live this session.
- **Project-level research (2026-06-01): `.gpd/research/SUMMARY.md`, `METHODS.md`, `PITFALLS.md`, `COMPUTATIONAL.md`.** The Phase-74 entry, the five phase-mapped methods, the arithmetic-hygiene pitfalls, and the env pin (Python 3.14.2 / SymPy 1.14.0).

### Secondary (MEDIUM confidence)

- **"Composition Algebras, Exceptional Jordan Algebra and Related Groups," JGSP 46 (2017) 59-93.** h_3(O) rank-3 simple Euclidean Jordan algebra; F_4 transitive on rank-1 idempotents with stabilizer Spin(9).
- **cp4space, "The exceptional Jordan algebra" (2020).** `A∘A=A` idempotents = rank-1 projections = OP^2 points; E_6 determinant; F_4 fixes det-1. (Confirms the qualitative picture; lacked the dimension/codimension details on fetch.)

### Tertiary (LOW confidence)

- **WebFetch of Manivel arXiv:0907.2784 PDF and the cp4space blog returned compressed/thin extractions** — the defining equation and dimensions are backstopped by the in-repo engine comment (`orbit(E_11)=17 = cone over Cayley plane OP^2`) and the live exact spot-check, so the underlying math is HIGH confidence even though the primary-source equation numbers were not legibly extracted.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH — DERV-02 method validated end-to-end over Q live this session; the variety/tangent facts are standard (Baez, McCrimmon, Manivel) and corroborated by the engine's own `orbit(E_11)=17` comment.
- Standard approaches: HIGH — "inherit + re-run + add one validated check" over byte-identical v17.0 engines; DERV-01 re-confirmed passing.
- Computational tools: HIGH — all engines in-repo and validated; env pinned; only caveat is the slow calibration runs (mitigated by `python -u`).
- Validation strategies: HIGH — every check is an exact rational equality/rank with a named engine and expected value; the `16 = 17−1` and round-`K=−1` factor-2 cross-checks add independent corroboration.

**Research date:** 2026-06-01
**Valid until:** physics/math results are stable indefinitely; tool versions (SymPy 1.14.0, Python 3.14.2) and the in-repo engine APIs are the faster-moving dependency — re-confirm the engine function names if the codebase is refactored.
