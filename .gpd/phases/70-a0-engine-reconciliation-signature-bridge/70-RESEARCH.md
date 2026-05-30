# Phase 70: A0 — Engine Reconciliation & Signature Bridge - Research

**Researched:** 2026-05-30
**Domain:** Mathematical physics — exact-over-Q certification of the cubic norm (generic norm) of the Albert algebra h_3(O); Riemannian-cone-Hessian (Faraut–Koranyi) to Lorentzian-slice signature bridge on the Peirce V_0 = h_2(O) sub-slice; constant-curvature cross-check of H^3 = SL(2,C)/SU(2) via Totaro.
**Confidence:** HIGH. Every load-bearing object (the SSOT `det_3`, the three cross-term orderings, the three benchmarks `diag(9,9,18,18)` / det 26244 / slice det form, the Minkowski reduction) was reproduced empirically this session against the in-repo warm engine, exact over Q. MEDIUM only on the signature-bridge being a *modeling choice this phase FIXES* (construction (ii)), not a discovery — but the gate it must pass (exact Minkowski at M=0, center) is verified to hold.

## Summary

Phase 70 is a **prerequisite gate**, not a discovery phase. Two plans: (70-01) stand up a single certified cubic-norm engine; (70-02) fix the signature bridge and prove it reduces to EXACT Minkowski. Because every downstream v17.0 curvature is built from derivatives of `det`, a wrong det cross-term association or a contaminated Minkowski background silently corrupts the entire milestone. The work is **exact symbolic certification over Q**, not perturbative physics: the deliverables are (a) `code/bulk_geometry_verification.py` whose `det_3` is certified the single source of truth on genuinely non-associative octonionic data, and (b) a stated construction-(ii) signature bridge with a machine-checked zero-residual Minkowski reduction.

The decisive ground truth is **`code/ring_lemma_verification.py`** (the warm exact-SymPy engine, ALL_PASS, dated Phase 64.1). I verified empirically this session: its `det_3` uses cross-term `2*Re((x2 x1) x3)` (x2 BEFORE x1), equals the Cayley–Hamilton generic norm on octonionic points, and is annihilated by all 324 inner derivations (= f_4). The buggy `octonion_algebra.py` ordering `2*Re((x1 x2) x3)` gives the WRONG sign (−4 vs +4 at the test point; det differs by 16) and is NOT the F_4-invariant norm — confirming the contract's `fp-wrong-cross-term` and the `do-not-import-octonion_algebra.py` instruction.

I also reproduced all three Phase-70 benchmarks from this SSOT engine, exact over Q: on the 4 spacetime sub-slice coordinates the bare slice det form is `b*g/3 − p²/3 − q²/3`; the cone-metric Hessian `Hess(−log det)` at the center I/3 is exactly `diag(9,9,18,18)` with `det = 26244`; and the slice metric at (M=0, center) equals exact Minkowski with zero residual. The H^3 sub-slice cross-check is anchored to Totaro's constant-curvature result (−d²/4 = −1 for the rank-1 complex line, d=2).

**Primary recommendation:** Build `code/bulk_geometry_verification.py` by COPYING (not importing) the Section-1–3 exact octonion/Jordan/`det_3` engine of `ring_lemma_verification.py` verbatim, re-run its ALL_PASS locks (especially LOCK 7a Cayley–Hamilton and LOCK 7b 324/324 inner-derivation annihilation) on the new module, add an explicit three-ordering reconciliation pre-flight on non-associative e_4..e_7 data, and use construction (ii) for the signature bridge with the machine-checked zero-residual Minkowski gate. Fix the potential as `−log det` and the spacetime sub-slice index set `{17,18,19,26}` (≡ engine-native `{beta, gamma, x1·e_0, x1·e_7}`) at the very start.

## User Constraints

No phase CONTEXT.md exists (no `/gpd:discuss-phase` was run). The binding spec is the roadmap Phase-70 section + the v17.0 contract slice + the frozen conventions block, all reproduced as anchors below. Treat every item in "Active Anchor References" as a locked constraint, not optional reading.

Key locked decisions affecting this research:
- **Engine SSOT = `code/ring_lemma_verification.py`'s `det_3`** (cross `2Re((x2 x1) x3)`). COPY/extend into `code/bulk_geometry_verification.py`. Do NOT import `code/octonion_algebra.py` (FORBIDDEN — buggy cross-term, see reconciliation below).
- **Signature bridge = construction (ii)** (eta from h_2(C_u)'s own det; cone-Hessian supplies only h_mu_nu). Construction (i) (Wick-rotate via u=e_7) is the *rejected alternative*; the phase must report which is used and why.
- **Potential FIXED as `−log det`** (not `det`) at the start.
- **Spacetime sub-slice = `{17,18,19,26}`** (h_2(C_u), u=e_7); signature mostly-minus (1,3).
- **Arithmetic EXACT over Q**; ranks via `sympy.Matrix.rank()`, NEVER `numpy.linalg.matrix_rank`; no decisive verdict in float (`fp-float-decisive` forbidden).
- This phase is statement + certification only. It does NOT compute curvature (Phase 71+), does NOT decide homogeneity, does NOT touch supergravity/SUSY/GST-action inputs.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `code/ring_lemma_verification.py` (960 ln, ALL_PASS, Phase 64.1) | in-repo warm engine (SSOT) | Decisive `det_3` (cross `2Re((x2 x1) x3)`), `jordan`, `Tr/Tr2`, `polarize_d`, `cayley_hamilton_norm`, `inner_derivations`, `jordan_L_matrix`, the LOCK harness | COPY Sections 1–3 verbatim into `bulk_geometry_verification.py`; re-run LOCKs 1–7b | plan 70-01 (engine), 70-02 (det for the slice), verification (ALL_PASS) |
| `code/octonion_algebra.py` (FORBIDDEN, buggy) | forbidden proxy | Its `det_3` (line 2152) uses `2Re((x1 x2) x3)` — NOT F_4-invariant; differs from CH norm by 16 at the octonionic test point | Read lines 2134–2181 ONLY to quote the buggy ordering for the reconciliation contrast; never import on the decisive path | plan 70-01 (three-ordering pre-flight; contrast row) |
| `/Users/ehrlich/repos/blog/research/qualia-fixed-point/h3o_tower.py` (796 ln, float64) | corrected-formula reference (float) | Cross-term `2Re(x2* x0* x1)` in its OWN index naming (x0,x1,x2); structurally = the SSOT ordering. Float64 — formula reference only | Cite as a third (conjugated) labeling that reconciles to the SSOT; do NOT put on the decisive path | plan 70-01 (reconciliation table) |
| `derivations/52-kkt-spacetime.tex` (231 ln) | prior result (HIGH) | det_2(X) = x0²−x1²−x2²−x3², signature (1,3) mostly-minus, forward cone, det=1 hyperboloid = H^3 = SL(2,C)/SU(2); KKT = so(4,2) | Use as the source of eta for construction (ii) and the H^3 identification | plan 70-02 (eta; VALD-03) |
| `code/embedding_under_E_verification.py` (1071 ln, warm) | companion exact engine | `proj_u_exact(a,u=7)`, `cu_to_complex`, `slice_to_complex`, `E(X)` Peirce projector, positional Peirce-grade split | Reuse for the h_2(C_u) projection and the Peirce V_0 split (copy or import the slice helpers) | plan 70-02 (sub-slice projection) |
| `code/octonion_algebra.py::det3_quadratic_expansion_50` + ASSERT blocks (ln 3603–3722, 3890) | benchmark provenance + index convention | Source of `{17,18,19,26}` spacetime / `{20..25}` internal split, the V_0 O(eps²) = det_2 Gram (massless) result, and the Peirce basis ordering `I0_V1_I1to16_Vhalf_I17to26_V0` | Read the ASSERT/VERIFIED comments to lift the index convention; do NOT call the float function on the decisive path | plan 70-02 (index assignment; sub-slice form) |
| Totaro, "The curvature of a Hessian metric," arXiv:math/0401381 | literature (HIGH) | Constant sectional curvature `−d²/4` for the rank-1 cone slice; d=2 (complex line) → −1; warped-product cone↔hypersurface | Cite Cor. for the H^3 = −1 cross-check (VALD-03); full curvature engine is Phase 71 | plan 70-02 (VALD-03 statement) |
| Faraut & Koranyi, *Analysis on Symmetric Cones* (1994), Ch. II–IV | literature (HIGH) | g_X = Hess(−log det) is THE canonical cone metric; positive-definite (hence a bridge is needed) | Cite Ch. II–IV (NOT Ch. V — citation_correction convention) for the cone metric | plan 70-01/70-02 (potential definition) |
| Visser, "How to Wick rotate generic curved spacetime," arXiv:1702.05572 | literature (MEDIUM, contrast) | Naive coordinate Wick rotation is a complex deformation of the metric, not the coordinate; coordinate version is chart-dependent on curved metrics | Cite to JUSTIFY rejecting construction (i); not load-bearing for (ii) | plan 70-02 (why (i) rejected) |

**Missing or weak anchors:**
- **CRITICAL — stale project research.** `.gpd/research/METHODS.md` (TL;DR #4, "What NOT to Use") and `.gpd/research/PITFALLS.md` (Pitfall 2) BOTH assert that `code/octonion_algebra.py`'s `det_3` is the *corrected* single source of truth (left-to-right `(x1·x2)·x3`). **This is WRONG and contradicts the actual code.** `ring_lemma_verification.py`'s header and my empirical check this session confirm `octonion_algebra.py` carries the SAME `(x1 x2) x3` factor-order bug that caused the Phase-64.1 defect; it is NOT F_4-invariant (annihilated by only 30 of 324 inner derivations). The phase brief and the contract (`fp-wrong-cross-term`, "do NOT import octonion_algebra.py") are correct; the project METHODS/PITFALLS files are stale on this single point. **The planner MUST follow the contract/brief (SSOT = ring_lemma_verification.py), not the stale METHODS/PITFALLS claim.** (Flagged so it can be corrected in those files later.)
- `rho_directional_derivatives.py`, `h3o_tower.py`, `peirce_coupling.py` are named in the brief but live OUTSIDE `code/` (h3o_tower.py is in `/Users/ehrlich/repos/blog/...`; the other two are repo-root / absent from `code/`). Their functionality is fully covered by `ring_lemma_verification.py` + `embedding_under_E_verification.py`. The planner should not assume the brief's filenames exist verbatim under `code/`.
- The benchmark `Hess(−log det)|_{I/3} = diag(9,9,18,18)`, det 26244, is NOT pre-computed in any in-repo file — but I reproduced it exactly this session (see Key Equations). The planner should wire it as a NEW computed gate, with the value as the expected result.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Arithmetic field | EXACT over Q (Q-adjoin-surds if needed) | float64 | engine convention; contract `fp-float-decisive` |
| Ranks | `sympy.Matrix.rank()` / `DomainMatrix` over QQ | `numpy.linalg.matrix_rank` (FORBIDDEN) | ring_lemma RANK_ROUTING_CONVENTION |
| Jordan product | a∘b = (1/2)(ab+ba) | matrix product (off by 1/2) | conventions_frozen; ring_lemma `jordan` |
| Octonion basis | Fano, e_1 e_2 = e_4 | — | conventions_frozen; matches Paper 7 |
| Cubic norm cross-term | **`2*Re((x2 x1) x3)`** (x2 BEFORE x1) ≡ `2Re(x2* x1* x3)` | `(x1 x2) x3` (BUGGY) | ring_lemma `det_3` ln 308–336; Phase-64.1 fix |
| det normalization | det(diag(a,b,c))=abc, det(I)=1, d(X,X,X)=6·det_3 | — | ring_lemma LOCKs 1,4,5 |
| Complex structure | u = e_7 (C_u = span{1,e_7}) | other imaginary units | conventions_frozen |
| Potential | **−log det** (FIXED at start) | det (differs by radial term) | roadmap SC #5; Faraut–Koranyi |
| Cone metric | g_X(A,B) = −∂_s∂_t log det(X+sA+tB)\|_0 = Hess(−log det) | — | conventions_frozen; Faraut–Koranyi |
| Center | I/3 (F_4-symmetric, rho_J = 0) | E_11 (rank-1, det=0) | conventions_frozen |
| Spacetime sub-slice | `{17,18,19,26}` = h_2(C_u) ≡ engine-native `{beta, gamma, x1·e_0, x1·e_7}` | other 4 of the 10 V_0 dirs | octonion_algebra.py ln 3611; verified this session |
| Internal V_0 | `{20,...,25}` (W-sector, killed by pi_u) | — | octonion_algebra.py ln 3612 |
| Signature | mostly-minus (1,3); eta = diag(+1,−1,−1,−1) | mostly-plus | `52-kkt-spacetime` Eq. det_2; `metric_on_h2Cu=mostly_minus_via_det2` |
| Field theory / units | N/A — pure algebra/geometry, dimensionless | — | conventions_frozen |

**CRITICAL: All equations below use these conventions.** The cross-term factor order and the `−log det` (vs `det`) potential are the two most error-prone choices; both are pinned here and verified reproducible.

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `N(X) = αβγ − α\|x1\|² − β\|x2\|² − γ\|x3\|² + 2Re((x2 x1) x3)` | Cubic norm / generic norm (SSOT) | ring_lemma `det_3` ln 308–336 | 70-01: the engine's det; certified single source of truth |
| `X^∘3 − Tr(X)X^∘2 + S(X)X − N(X)I = 0`, `S=(1/2)(Tr²−Tr(X∘X))` | Cayley–Hamilton (degree-3) for `jordan` | ring_lemma `cayley_hamilton_norm` ln 663 | 70-01: certifies `det_3` IS the unique F_4-invariant norm (LOCK 7a) |
| `[L_a,L_b]·N = 0` for all 324 brackets (span = f_4, dim 52) | inner-derivation annihilation | ring_lemma `inner_derivations` ln 699, LOCK 7b | 70-01: F_4-invariance certificate (the discriminating test) |
| `g_X = Hess(−log det)` | Faraut–Koranyi canonical cone metric | conventions_frozen; FK Ch. II–IV | 70-02: the bulk Riemannian metric; supplies h_mu_nu |
| `det_2(X) = x0²−x1²−x2²−x3²`, eta = diag(+1,−1,−1,−1) | Minkowski form on h_2(C_u) | `52-kkt-spacetime` | 70-02: the background eta for construction (ii) |
| `det_3 slice = b·g/3 − p²/3 − q²/3` (alpha=1/3) | bare det on the 4-dir spacetime sub-slice | reproduced this session | 70-02: benchmark; with b=x0+x3, g=x0−x3 → Minkowski |
| `Hess(−log det)\|_{I/3} = diag(9,9,18,18)`, det 26244 | cone metric at center, spacetime sub-slice | reproduced this session | 70-02: nondegeneracy + reduce-to-Minkowski benchmark |
| `R_{1212}/(g_11 g_22 − g_12²) = −d²/4`, d=2 → −1 | Totaro constant sectional curvature, rank-1 line | Totaro arXiv:math/0401381 | 70-02: VALD-03 H^3 = SL(2,C)/SU(2) cross-check |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Exact octonion arithmetic via Fano table | Non-associative product over Q | every `det_3`/`jordan` eval | ring_lemma Section 1 |
| Full 3×3 octonion matmul (no assoc assumed) | Computes (XY)Z and X(YZ) independently | cross-term, Cayley–Hamilton | ring_lemma `h3o_matmul` |
| Polarization of the cubic norm | symmetric trilinear d(X,Y,Z), d(X,X,X)=6N | LOCK 1; third-derivative tensor later | ring_lemma `polarize_d` |
| Symbolic Hessian over Q (`sympy.diff` ×2) | Hess(−log det) at a point, exact | 70-02 benchmark + reduction gate | SymPy |
| Conditional expectation E onto h_2(C_u), proj_u | restrict to the complex sub-slice | 70-02 sub-slice projection | embedding engine `E`, `proj_u_exact` |
| Source-token guard (regex) | forbid float-rank / forbidden imports on decisive path | new module's exact-only guard | ring_lemma `exact_only_guard` |

### Approximation Schemes

None. This phase is exact algebra/geometry; there is no small parameter and no truncation. The only "expansion" is the finite, terminating Taylor jet of `−log det` around a point (det is cubic, so `det_ijkl ≡ 0`), which is exact. (Float finite-difference is allowed ONLY as a non-decisive cross-check, never as a verdict.)

## Standard Approaches

### Approach 1: Copy-and-certify the warm engine (RECOMMENDED for 70-01)

**What:** Create `code/bulk_geometry_verification.py` by copying Sections 1–3 of `ring_lemma_verification.py` (exact octonion arithmetic, 3×3 octonion matmul, `jordan`, `Tr`, `Tr2`, `det_3`, `polarize_d`, `cayley_hamilton_norm`, `_standard_basis_27`, `jordan_L_matrix`, `inner_derivations`, the exact-only guard) VERBATIM, then re-run the ALL_PASS lock harness on the new module.

**Why standard:** This is the established repo pattern (the ring_lemma engine was itself copied verbatim from `embedding_under_E_verification.py`; copying decouples the decisive module and pins conventions in one place — see ring_lemma PROVENANCE). The contract explicitly requires standing up `bulk_geometry_verification.py` by "copying/extending that engine."

**Track record:** `ring_lemma_verification.py` is ALL_PASS, has gated the entire v16.0 milestone (Phases 65–69), and caught two plan typos via its locks. Its `det_3` survived the Phase-64.1 audit that killed the buggy ordering.

**Key steps:**
1. Copy Sections 1–3 verbatim (octonion arithmetic → `inner_derivations`). Keep the `# ASSERT_CONVENTION` header line.
2. Re-run LOCKs 1–5 (d=6N headline, c(X,X)=Tr2, Fano e1e2=e4, det(diag)=abc, det(I)=1).
3. Re-run LOCK 7a (`det_3 == cayley_hamilton_norm` at ≥3 octonionic points) and LOCK 7b (324/324 inner derivations annihilate `det_3`). **These two are the certification that `det_3` is the single source of truth.**
4. Add the explicit three-ordering reconciliation pre-flight (Approach below) on non-associative e_4..e_7 data.
5. Keep the exact-only source guard (forbid `octonion_algebra` import + `numpy.linalg.matrix_rank` on the decisive path). The new module may drop ring_lemma's single sanctioned oracle-fence touch of `octonion_algebra.py` entirely (cleaner: no touch at all), OR keep it as an informational blast-radius readout — planner's call, but the guard must still forbid decisive-path use.

**Known difficulties at each step:**
- Step 1: the engine-native coordinate layout (`X_from_symbols`: x0,x1,x2=diag; x3..10=oct x1→X[2][1]; x11..18=oct x2→X[0][2]; x19..26=oct x3→X[1][0]) must be carried verbatim or the index map breaks. Do not "tidy" it.
- Step 3: LOCK 7b is the slow one (constructs 324 brackets as 27×27 rational matrices, ~tens of seconds). It is the decisive F_4 certificate — do not skip or downgrade.

### Approach 2: Three-ordering reconciliation pre-flight (RECOMMENDED, the SETU-01 heart)

**What:** On genuinely non-associative octonionic data (off-diagonals with nonzero e_4..e_7 components), evaluate the three in-repo cross-term orderings and the discriminating norm, and tabulate which equals the Cayley–Hamilton norm.

| Ordering | Code expression | Source | Re(cross) at the test pt | = CH norm? |
| -------- | --------------- | ------ | ------------------------ | ---------- |
| `(x2 x1) x3` | `oct_mul(oct_mul(x2,x1),x3)` | `ring_lemma.det_3` (SSOT) | **+4** | **YES** |
| `x2* x1* x3` | `oct_mul(oct_conj(x2),oct_mul(oct_conj(x1),x3))` | h3o_tower-style (conjugated) | +4 | YES (≡ SSOT) |
| `(x1 x2) x3` | `oct_mul(oct_mul(x1,x2),x3)` | `octonion_algebra.det_3` (BUGGY) | −4 | NO (off by 16 in det) |

(Values are at ring_lemma's octonionic point `octonionic_points()[1]`, verified this session.)

**Why this is non-vacuous:** On diagonal or e_0..e_3 (quaternionic) data the three orderings AGREE (those subalgebras are associative), so a check there is vacuous and hides the bug. The association-invariance pre-flight MUST be on e_4..e_7 data; the difference `Re((x1·x2)·x3) − Re(x1·(x2·x3))` must be NONZERO (it equals twice the associator's real part) or the test inputs are accidentally associative.

**Why standard:** This is exactly the Phase-64.1 lock that caught the original bug. The contract test `test-cross-term-association` demands it BEFORE any geometry.

### Anti-Patterns to Avoid

- **Importing `octonion_algebra.py`'s `det_3`** — buggy `(x1 x2) x3`; not F_4-invariant. Contract `fp-wrong-cross-term`. Use the copied SSOT.
- **Verifying the cross-term on diagonal / e_0..e_3 data** — vacuous (associative subalgebra). Use e_4..e_7.
- **Trusting LOCKs 1–5 alone** — the buggy ordering passes ALL of them. Only LOCK 7a+7b discriminate.
- **Float verdict** — any "= 0?" / rank decision in float. Contract `fp-float-decisive`. Exact over Q only.
- **Mixing `det` and `−log det` potentials** — they differ by the radial (det=const) direction. Fix `−log det` at the start.
- **Using the stale METHODS/PITFALLS claim that octonion_algebra.py is corrected** — it is not (see Missing Anchors). Follow the contract/brief.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| `det_3` is the unique F_4-invariant cubic norm | `2Re((x2 x1) x3)` cross; passes CH + 324/324 inner-deriv | ring_lemma Phase-64.1, ALL_PASS | COPY; re-certify, don't re-derive uniqueness |
| Single-state ring R[h_3(O)]^{F_4} = R[Tr,Tr²,det] | free, trdeg 3, degrees 1/2/3 | Faraut–Koranyi Ch. II–IV; Springer 1962/73 | cite; no Reynolds/Jacobian re-derivation |
| h_2(C_u) ≅ R^{3,1}, det_2 = Minkowski form, sig (1,3) | `det_2 = x0²−x1²−x2²−x3²` | `52-kkt-spacetime` (Phase 46/52) | the eta for construction (ii); cite |
| det=1 hyperboloid in h_2(C_u) = H^3 = SL(2,C)/SU(2) | constant negative curvature | `52-kkt-spacetime`; standard | VALD-03 identification; cite |
| Totaro constant sectional curvature of {f=1} | `−d²/4`; d=2 (complex line) → −1 | Totaro arXiv:math/0401381 | VALD-03 expected value −1; cite |
| g_X = Hess(−log det) is the canonical cone metric, positive-definite | — | Faraut–Koranyi Ch. II–IV | WHY a Riemannian→Lorentzian bridge is needed |
| V_0 O(eps²) expansion of det_3 around E_11 = det_2 Gram (massless) | M_{ab} = det_2 Gram, exact | octonion_algebra `det3_quadratic_expansion_50` (VERIFIED 50-01) | leading-order homogeneity signal; provenance of the index split (read the comment, don't call the float fn) |

**Key insight:** The cross-term uniqueness and the F_4-invariance are ALREADY certified in the warm engine; 70-01 RE-CERTIFIES on a fresh module (cheap insurance against a copy error), it does not discover. Re-deriving the single-state ring or the H^3 curvature from scratch wastes budget and risks error in something certain — cite.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `polarize_d(X,Y,Z)`, d(X,X,X)=6 det_3 | the symmetric trilinear = third-derivative tensor of det (needed Phase 71) | ring_lemma `polarize_d` | exact over Q |
| `jordan_L_matrix(A, basis)` 27×27 | left-multiplication matrices; building block for f_4 | ring_lemma | exact over Q |
| `proj_u_exact`, `cu_to_complex`, `slice_to_complex`, `E(X)` | restrict h_3(O) → h_2(C_u), map C_u→C | embedding engine | u=e_7 |
| `_compute_sharp`, `_polarized_sharp` (X#) | Freudenthal adjugate; X∘X# = det·I | octonion_algebra (float — formula ref only) | re-port to exact if needed |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| *Analysis on Symmetric Cones* Ch. II–IV | Faraut, Koranyi | 1994 | THE cone metric g_X=Hess(−log det); positive-definite | metric definition; cite (NOT Ch. V) |
| "The curvature of a Hessian metric" math/0401381 | Totaro | 2004 | constant curvature −d²/4 of {f=1}; warped-product cone↔hypersurface | the −1 value for VALD-03; full curvature formula is Phase 71 |
| "How to Wick rotate generic curved spacetime" 1702.05572 | Visser | 2017 | Wick rotation = complex deformation of the METRIC, not the coordinate; coordinate version chart-dependent | the argument to reject construction (i) |
| Springer, *Jordan Algebras and Algebraic Groups* | Springer | 1973 | cubic-norm uniqueness; F_4 = Aut(h_3(O)) | citation for det_3 uniqueness |
| `52-kkt-spacetime` | (in-repo) | — | h_2(C_u)≅R^{3,1}, det_2, so(4,2), H^3 | eta source + VALD-03 |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (confirmed in env) | exact octonion arithmetic, `det_3`, `Matrix.rank()` over QQ, `diff`, `simplify`, `log` | exact-over-Q; the engine's native arithmetic |
| Python | 3.14.2 | runtime | ring_lemma reproducibility pin |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| NumPy | 2.4.2 | float spot-checks (signature eigenvalues, triage) ONLY | NEVER on a decisive rank/zero-test |
| `sympy.diffgeom` | curvature of an explicit metric (verified: 2D sphere → sin²θ) | Phase 71 (4-dim slice cross-check), NOT this phase |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| copy the engine | import `ring_lemma_verification` | import is import-safe (main guarded) but couples the decisive module to a v16.0 file; repo precedent is COPY |
| `Matrix.rank()` | `DomainMatrix` over QQ | DomainMatrix is faster for large exact ranks (used in `orbit_dimension_gate.py`); either is exact |
| exact-square / registry sqrt | `sympy` eigenvects sqrt | the diagonal-projected fast path avoids casus-irreducibilis cubic-radical blowup (embedding engine) — only relevant if a slice sqrt is needed |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| LOCKs 1–5 (exact) | < 5 s | symbolic simplify | hardcoded rational test points |
| LOCK 7a (CH norm at 3 pts) | seconds | octonion simplify | fixed octonionic points |
| LOCK 7b (324 inner derivations) | tens of seconds | 324 × (27×27 matmul over Q) + grad·(M·v) simplify | the slowest; it is the F_4 certificate, keep it |
| Hess(−log det) at I/3 (4-var) | < 2 s | `diff` ×2 of −log of a cubic | restrict to the 4 spacetime vars (done this session) |
| Minkowski reduction gate | < 2 s | exact subtraction g − eta | exact over Q |

All comfortably within a single session. No HPC, no sign problem, no undecidability.

**Installation / Setup:**
```bash
# Already satisfied in the executor venv (confirmed): sympy 1.14.0, numpy 2.4.2.
python3 -c "import sympy, numpy; print(sympy.__version__, numpy.__version__)"
# No new packages. NO Sage/GAP/Singular/Magma (not available, not needed).
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| LOCK 1 (headline) | polarization normalization | `polarize_d(X,X,X) − 6·det_3(X)` over Q | 0 |
| LOCK 7a | `det_3` = the unique F_4-invariant norm | `det_3(P) − cayley_hamilton_norm(P)` at ≥3 octonionic P | 0 each |
| LOCK 7b | F_4-invariance (the discriminator) | every `[L_a,L_b]` annihilates `det_3` at an octonionic point | **324/324** (dim f_4 = 52) |
| Three-ordering pre-flight | association is load-bearing & correct | tabulate Re(cross) for the 3 orderings vs CH norm | SSOT/+4 match CH; buggy/−4 does not; difference nonzero |
| Minkowski reduction gate | bridge not contaminated | `g_mu_nu(center, M=0) − eta_mu_nu` over Q (4×4) | exact zero, zero residual h_mu_nu |
| Hessian nondegeneracy | slice metric well-defined at center | `det(Hess(−log det)|_{I/3})` | **26244** (≠ 0) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| center, M=0 | X = I/3, no matter | g = eta, exact Minkowski (1,3) | reproduced this session |
| cone metric at center | I/3, spacetime sub-slice | `diag(9,9,18,18)`, det 26244 | reproduced this session |
| bare det on sub-slice | alpha=1/3 | `b·g/3 − p²/3 − q²/3` (Minkowski with b=x0+x3,g=x0−x3) | reproduced this session |
| h_2(C_u) det=1 hyperboloid | rank-1 complex line, d=2 | H^3 = SL(2,C)/SU(2), curvature −d²/4 = −1 | Totaro; `52-kkt-spacetime` |
| diagonal cone diag(a,b,c) | off-diagonals 0 | −log(abc) factorizes (flat-in-log check) | standard |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| float det cross-check | one isolated float eval vs CH norm | 1e-12 | informational only; NOT a verdict |
| eigenvalues of g at center | `numpy.linalg.eigvalsh` | triage only | {9,9,18,18} → positive-definite Riemannian (before signature bridge) |

(Both float; allowed only as cross-checks. The decisive verdicts are exact over Q.)

### Red Flags During Computation

- LOCK 7b returns anything other than 324/324 → the copied `det_3` cross-term order is wrong (a port error, NOT a new result). STOP, diff against ring_lemma line by line.
- The three-ordering difference `Re((x1·x2)·x3) − Re(x1·(x2·x3))` is 0 → test inputs are accidentally associative; pick e_4..e_7 data.
- `Hess(−log det)|_{I/3}` is not `diag(9,9,18,18)` → wrong sub-slice coordinates, wrong potential (`det` vs `−log det`), or a det cross-term error.
- Nonzero residual `h_mu_nu` at (M=0, center) → contaminated bridge (double-counted background, or wrong index identification). Per the backtracking trigger: switch to construction (i) or STOP.
- `det(Hess) = 0` at center → degenerate metric; wrong coordinates or potential.

## Common Pitfalls

### Pitfall 1: Wrong cross-term association (silently corrupts everything)

**What goes wrong:** Using `(x1 x2) x3` (octonion_algebra.py order) instead of `(x2 x1) x3`. Returns a plausible number that passes LOCKs 1–5 but is NOT the F_4-invariant norm; every downstream Hessian/curvature is silently wrong.
**Why it happens:** Octonion non-associativity — `Re((x1 x2) x3) ≠ Re((x2 x1) x3)` (they differ by the associator). Three different labelings coexist in-repo (`(x2 x1) x3`, `x2* x1* x3`, `(x1 x2) x3`) and look interchangeable.
**How to avoid:** Copy the SSOT `det_3`; run LOCK 7a (CH norm) + LOCK 7b (324/324 inner derivations) on e_4..e_7 data. NEVER import `octonion_algebra.py`.
**Warning signs:** LOCK 7b < 324; det differs by an even integer from the CH norm at an octonionic point.
**Recovery:** Recompute `det_3` with the corrected order; everything built on the wrong norm must be redone (HIGH cost — which is why this is a gate).

### Pitfall 2: Vacuous association test on associative data

**What goes wrong:** "Verifying" the cross-term on diagonal or e_0..e_3 data — those subalgebras are associative, so all orderings agree and the bug is invisible.
**Why it happens:** Diagonal/quaternionic data is the easy hand-check.
**How to avoid:** Use off-diagonals with nonzero e_4..e_7 components; assert `Re((x1·x2)·x3) − Re(x1·(x2·x3)) ≠ 0` as a pre-flight.
**Warning signs:** the associator real part is 0 on your test inputs.
**Recovery:** swap in genuinely octonionic points (e.g. ring_lemma's `octonionic_points()`).

### Pitfall 3: Contaminated signature bridge (nonzero h_mu_nu at center)

**What goes wrong:** The chosen bridge gives g ≠ eta at (M=0, center); the constant offset masquerades as a cosmological constant (Phase B false positive) or position dependence (Phase A false positive). Or: double-counting Minkowski by taking eta from det_2 AND keeping the eta-like part of the restricted cone-Hessian.
**Why it happens:** Construction (i) and (ii) both have a Minkowski piece; mixing them double-counts. The reduction check is easy to skip.
**How to avoid:** Use construction (ii); DEFINE `h_mu_nu := [g_X restricted to V_0, in h_2(C_u) coords] − [its value at (M=0, center)]`, so h=0 at center BY CONSTRUCTION; then verify the residual is exact-Q zero. Fix the V_0-direction ↔ Minkowski-index frame ONCE at the center (a fixed linear map), not per-point.
**Warning signs:** nonzero 4×4 residual; signature ≠ (1,3).
**Recovery:** re-fix the bridge (construction (ii) or, per the backtracking trigger, fall back to (i)), re-run the gate.

### Pitfall 4: Wrong 4 of the 10 V_0 directions

**What goes wrong:** Picking the wrong 4 spacetime coords (e.g. internal `{20..25}`) gives a metric that is not the Minkowski slice and fails the reduction.
**Why it happens:** Two coordinate layouts coexist — the octonion_algebra.py Peirce index set `{17,18,19,26}` and the ring_lemma engine-native layout. I verified this session that `{17,18,19,26}` ≡ engine-native `{beta, gamma, x1·e_0, x1·e_7}` (the C_u part of the (2,1)/(1,2) octonion entry).
**How to avoid:** Pin the sub-slice to `{beta, gamma, x1·e_0, x1·e_7}` in engine-native coords (= `{17,18,19,26}` in Peirce coords); verify `det_3` on it equals `b·g/3 − p²/3 − q²/3`.
**Warning signs:** slice det form has the wrong sign pattern or extra terms.
**Recovery:** re-map the index set; recompute.

## Level of Rigor

**Required for this phase:** Exact symbolic certification over Q (the strongest computational rigor; equivalent to a machine-checked proof of each algebraic identity). No physicist's-proof hand-waving on the decisive path; no float verdict.

**Justification:** This is a prerequisite gate — a wrong det or contaminated background corrupts the whole milestone, and the decisive quantities (rank, "= 0?", F_4-invariance) are discontinuous and float-fragile. The contract forbids `fp-float-decisive`.

**What this means concretely:**
- Every LOCK and gate must be `simplify(... ) == 0` (or `.rank()`) over Q, exact, with hardcoded rational/octonionic test points (deterministic, no random seeds).
- LOCK 7b must report the full 324/324 count, not a sample.
- The Minkowski reduction must show zero residual over Q (machine-zero is insufficient).
- Float is permitted only as an explicitly-labeled, non-decisive cross-check (e.g. an isolated `det_3` float vs CH norm, or eigenvalue triage).

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| `octonion_algebra.py` `det_3` cross `(x1 x2) x3` | ring_lemma `det_3` cross `(x2 x1) x3` (CH + 324/324 certified) | Phase 64.1 (2026-05-25) | the buggy order is NOT F_4-invariant; do not regress |
| `trip_tracking.py` `2Re(x0(x1 x2))` | corrected `2Re((x2 x1) x3)` | Phase 64.1 | the original bug of record |
| float64 octonion engines (h3o_tower, octonion_algebra) | exact-SymPy-over-Q engines | v15.0+ | decisive verdicts must be exact |

**Superseded approaches to avoid:**
- `octonion_algebra.py`'s `det_3` on any decisive path — buggy cross-term; people still cite it because its ASSERT comment *claims* "corrected" (it is not, for F_4-invariance). The stale `.gpd/research/METHODS.md`/`PITFALLS.md` repeat that claim — do not follow them on this point.

## Open Questions

1. **Does construction (ii) capture the V_0↔matter coupling that Phase B needs?**
   - What we know: (ii) reduces to exact Minkowski at (M=0, center) — verified. It supplies ONLY h_mu_nu.
   - What's unclear: whether restricting g_X to V_0 then projecting to h_2(C_u) preserves the V_1/V_{1/2} cross-term channel that sources curvature (a Phase-71/B concern, not 70).
   - Impact on this phase: none for the gate; (ii) is the correct A0 choice. Flagged for Phase 71.
   - Recommendation: proceed with (ii); if Phase B finds the coupling is projected away, revisit the bridge then.

2. **Keep or drop the single `octonion_algebra.py` oracle-fence touch in the new module?**
   - What we know: ring_lemma keeps one sanctioned, fenced, non-decisive float cross-check.
   - What's unclear: whether the planner wants `bulk_geometry_verification.py` to be 100% touch-free of the forbidden file.
   - Impact: cosmetic/safety. A touch-free module is cleaner and removes any temptation.
   - Recommendation: prefer NO touch at all (drop the oracle); rely on LOCK 7a's CH-norm cross-check, which is float-free.

3. **The H^3 curvature value −1 — assert by citation or compute now?**
   - What we know: Totaro gives −d²/4 = −1 (d=2); `52-kkt-spacetime` identifies the hyperboloid as H^3.
   - What's unclear: whether 70-02 should COMPUTE the constant curvature (needs the Phase-71 curvature engine) or STATE it by citation as a target.
   - Impact: scope. The roadmap lists VALD-03 as a "limiting case verified" cross-check.
   - Recommendation: STATE the target (−1) by citation in 70-02 and wire the actual constant-curvature computation as a Phase-71 deliverable, OR do a lightweight 3-metric curvature on the det_2 hyperboloid here (feasible: 3-dim, the det_2 form `b·g − p² − q²` is reproduced). Planner's call; the cheap version is a small `sympy.diffgeom` run on the 3-dim slice.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| construction (ii) Minkowski reduction | nonzero residual h_mu_nu at center | construction (i): restrict g_X + Wick-rotate via u=e_7 | HIGH — (i) carries the unproven C*-bottleneck signature-flip conjecture and the Visser chart-dependence hazard; report honestly |
| copy-the-engine | a copied lock fails | diff line-by-line vs ring_lemma; fix the port | LOW — it is a port error, not a new result |
| `Matrix.rank()` too slow on 324 brackets | symbolic blowup | `DomainMatrix` over QQ (orbit_dimension_gate pattern) | LOW |
| exact simplify of a slice expression non-terminating | heavy octonionic rationals | evaluate at a generic integer point (zero is generic), confirm the decisive instance exactly | LOW |

**Decision criteria:** Abandon construction (ii) ONLY if the exact-Q residual at (M=0, center) is provably nonzero AND cannot be removed by re-fixing the V_0↔Minkowski frame. Per the backtracking trigger, that is the documented condition to switch to (i) or STOP. Abandon the engine copy never — a failing lock is always a port error to fix, not a result.

## Sources

### Primary (HIGH confidence)

- **`code/ring_lemma_verification.py`** (in-repo, 960 ln, ALL_PASS, Phase 64.1) — SSOT `det_3` (cross `2Re((x2 x1) x3)`), `jordan`, `cayley_hamilton_norm`, `inner_derivations`, LOCK harness. Empirically re-verified this session (LOCK values, cross-term reconciliation, all three benchmarks).
- **Faraut, J. & Koranyi, A., *Analysis on Symmetric Cones*, OUP (1994), Ch. II–IV** — g_X = Hess(−log det), positive-definite cone metric, symmetric-space structure. (Cite Ch. II–IV, NOT Ch. V — citation_correction.)
- **Totaro, B., "The curvature of a Hessian metric," arXiv:math/0401381 (Int. J. Math. 15 (2004) 369–391)** — constant sectional curvature −d²/4 of {f=1}; warped-product cone↔hypersurface. https://arxiv.org/abs/math/0401381
- **`derivations/52-kkt-spacetime.tex`** (in-repo) — h_2(C_u) ≅ R^{3,1}, det_2 = Minkowski form, sig (1,3) mostly-minus, forward cone, det=1 hyperboloid = H^3 = SL(2,C)/SU(2), KKT = so(4,2).
- **Springer, T.A., *Jordan Algebras and Algebraic Groups*, Springer (1973)** — cubic-norm uniqueness, F_4 = Aut(h_3(O)), det normalization.

### Secondary (MEDIUM confidence)

- **`code/embedding_under_E_verification.py`** (in-repo, 1071 ln) — `proj_u_exact`, `cu_to_complex`, `slice_to_complex`, `E(X)`, positional Peirce split. Verified import-safe.
- **`code/octonion_algebra.py`** lines 2134–2181 (buggy `det_3`), 3603–3722 (the `{17,18,19,26}`/`{20..25}` index convention + Peirce ordering), `det3_quadratic_expansion_50` (V_0 O(eps²)=det_2 Gram). Read for convention provenance and the buggy-ordering contrast ONLY.
- **Visser, M., "How to Wick rotate generic curved spacetime," arXiv:1702.05572 (2017)** — Wick rotation = complex deformation of the METRIC, not the coordinate; the coordinate version is chart-dependent on curved metrics. Cited to justify rejecting construction (i). https://arxiv.org/abs/1702.05572

### Tertiary (LOW confidence)

- `/Users/ehrlich/repos/blog/research/qualia-fixed-point/h3o_tower.py` (float64) — corrected cross-term `2Re(x2* x0* x1)` in its own index naming; structurally = the SSOT ordering. Float reference only.
- `.gpd/research/METHODS.md` / `PITFALLS.md` — rich and mostly current, BUT carry a stale claim that `octonion_algebra.py` is the corrected SSOT (it is not). Use for everything EXCEPT that one point; follow the contract/brief for the engine SSOT.

## Metadata

**Confidence breakdown:**
- Mathematical framework: HIGH — every object reproduced empirically against the warm engine, exact over Q.
- Standard approaches: HIGH — copy-and-certify is the established repo pattern; the reconciliation pre-flight is the proven Phase-64.1 lock.
- Computational tools: HIGH — SymPy 1.14.0 confirmed in env; all computations done this session in seconds.
- Validation strategies: HIGH — three benchmarks (`diag(9,9,18,18)`, det 26244, slice det form) and the Minkowski reduction all verified exact this session; H^3 = −1 anchored to Totaro.
- Signature-bridge choice: MEDIUM — (ii) is the correct A0 choice and passes its gate, but it is a modeling FIX, not a discovery; whether it preserves the matter coupling is a Phase-71 question.

**Research date:** 2026-05-30
**Valid until:** Indefinite for the algebra/geometry (stable mathematics); the in-repo engine paths/line numbers are valid as of this session and should be re-confirmed if the repo is refactored.

## Caveats and Alternatives (Pre-Submission Self-Critique)

1. **What assumption might be wrong?** That `{17,18,19,26}` ≡ engine-native `{beta, gamma, x1·e_0, x1·e_7}`. I derived this from the lower-right h_2(O) block being rows/cols {1,2} and the C_u part being comps {0,7}, and confirmed the slice det form `b·g/3 − p²/3 − q²/3` matches — but the explicit Peirce-index↔engine-index dictionary is reconstructed, not read from a single in-repo line. **The planner should have 70-02 assert this mapping explicitly** (e.g. by checking the restricted det_2 on those 4 engine-native coords equals the Minkowski form) rather than trusting my reconstruction.
2. **What alternative did I dismiss too quickly?** Construction (i) (Wick via u=e_7). I dismissed it because it bundles an unproven conjecture and fails the "exact Minkowski" gate without an ad-hoc continuation — consistent with the project METHODS Method-1 comparison. If Phase B later shows (ii) projects away the matter coupling, (i) must be revisited; I flagged this as Open Question 1.
3. **What limitation am I understating?** That this phase does NOT establish anything physical — it certifies the engine and fixes a background. The "reduces to Minkowski" success is a consistency requirement, not evidence for the gravity claim. I have tried to state this plainly (it is a gate).
4. **Simpler method overlooked?** Possibly: import `ring_lemma_verification` instead of copying. I recommended COPY (repo precedent, decoupling), but noted import is import-safe — the planner may choose import if they prefer a single source. Either is defensible; copy is the established pattern.
5. **Would a specialist disagree?** A Jordan-algebra specialist would want the F_4-invariance certified by the inner-derivation annihilation (LOCK 7b), not just Cayley–Hamilton (LOCK 7a) — both are in the SSOT and I require both. A relativist would insist the signature bridge be stated as an explicit fixed frame (linear identification), not an analytic continuation — construction (ii) does exactly that, and I flagged fixing the frame ONCE at the center as Pitfall 3's mitigation.
