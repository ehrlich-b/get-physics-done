# Phase 67: (c) Degree-2 Uniqueness — Research

**Researched:** 2026-05-26
**Domain:** Computational invariant theory of exceptional groups; representation theory of F_4 (Albert algebra h_3(O), the 27 = 1 ⊕ 26); exact rational linear algebra
**Confidence:** HIGH (rep-theory facts; method; engine reuse). MEDIUM only on "verbatim literature plethysm of Sym²(26)" — see Open Questions; the decisive route does not depend on it.

## Summary

Phase 67 (RING-03) proves c = Tr(X∘Y) is the UNIQUE degree-2 coupling generator modulo scale, products, and pointwise terms. This is a representation-theoretic statement about the degree-2 graded piece of R[27⊕27]^{F_4}, complementary to Phase 66's differential/Jacobian functional-independence result (66 proved c is a genuine new field generator; 67 proves it is the unique NEW degree-2 coupling). The mathematical content reduces to two convergent claims: (i) the F_4-branching arithmetic — 27 = 1 ⊕ 26, Sym²(26) = 1 ⊕ 26 ⊕ 324 (dim 351), Sym²(27) = 378, and trivial-multiplicity-in-(27⊗27) = dim End_{F_4}(1⊕26) = 1² + 1² = 2 by Schur — so the bidegree-(1,1) trivial part is exactly 2-dimensional = span{Tr(X)Tr(Y), Tr(X∘Y)}; and (ii) an EXACT f_4-infinitesimal-kernel nullspace over Q on degree-2 monomials of (X,Y) that reproduces the branching count (total degree-2 invariant dim = 6; the (1,1) block = 2). The "mod products" quotient then removes the single reducible product Tr(X)Tr(Y), leaving the 1-dimensional genuine-coupling space span{c}.

The recommended approach is a TWO-ROUTE proof exactly mirroring the established Phase 64–66 pattern: Route A = the rep-theory branching count (the clean conceptual proof, a LITERATURE anchor); Route B = the exact f_4-kernel nullspace over QQ on the 27⊗27 bilinear-form space (the self-certifying harness witness). The two must agree on dim = 2 for the (1,1) block and dim = 6 for the full degree-2 space. The genuinely NEW computational work is small: lift the 52 certified f_4 generators (27×27 matrices) to their derivation action on the 27⊗27 space (dim 729) via the Leibniz rule ρ(M)(v⊗w) = (Mv)⊗w + v⊗(Mw), then take the exact rational nullspace. Every prerequisite — the 52-generator f_4 basis, the row-major 729 flatten, the exact-QQ rank/nullspace machinery — already exists and is certified in `code/orbit_dimension_gate.py` and `code/ring_generating_set.py`.

**Primary recommendation:** Prove dim = 2 for the (1,1) block by the EXACT f_4-kernel nullspace over QQ on the 27⊗27 (729-dim) space (reuse `cached_L_matrices`/`inner_derivations`, `_flatten_729`, `exact_qq_rank` — the nullspace dim = 729 − rank of the stacked 52·729 constraint operator), cross-checked against the rep-theory branching count (Schur: 1²+1²=2). Then express the 2-dim nullspace explicitly in the {Tr(X)Tr(Y), Tr(X∘Y)} basis and quotient the single reducible product to land at the 1-dimensional genuine-coupling space. **Per the roadmap backtracking guidance, if the two disagree, TRUST THE EXACT NULLSPACE and re-derive the irrep arithmetic.**

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `code/orbit_dimension_gate.py` (`cached_L_matrices`, `inner_derivations`, `_select_independent_basis`, `_flatten_729`, `exact_qq_rank`, `span_rank_over_QQ`, `infinitesimal_action`) | Prior artifact / certified engine | The 52-generator f_4 basis (certified Phase 65), the 729-flatten convention, and exact-QQ rank/nullspace are all here | REUSE verbatim; the f_4 generators must NOT be re-derived | plan (Route B tasks), execution, verification |
| `code/ring_generating_set.py` (`_f4_basis` @227, `check_f4_invariance` @236, `check_bidegree` @318, `CANDIDATE_GRADS`, `candidate_jacobian_matrix_at`) | Prior artifact / certified engine | Shows the exact D_M f = 0 contraction recipe over Q and the diagonal-action split (gradient blocks [0:27], [27:54]); `Tr`, `Tr2`, `c`, `jordan` imported from frozen `ring_lemma_verification.py` | REUSE the invariance-test pattern and the named invariants Tr(X), Tr(Y), c=Tr(X∘Y) | execution (express nullspace in named-invariant basis), verification |
| `code/ring_lemma_verification.py` (frozen exact engine: `jordan`, `Tr`, `Tr2`, `c`, `det_3`, `polarize_d`, `Xsym`/`Ysym`, `xs`/`ys`) | Prior artifact / frozen substrate | EXACT octonion arithmetic over Q; the source of the convention asserts | USE as the exact substrate; do NOT modify | execution, verification |
| `.gpd/research/PITFALLS.md` Pitfall 9 (26-vs-27; reducible Tr(X)Tr(Y)) | Method / guard | Names the #1 forbidden-proxy risk and the exact target integers {2, 6, 351, 378, 1⊕26⊕324} | READ; encode each as a runnable assert | plan (forbidden-proxy guards), verification |
| `.gpd/research/METHODS.md` §(c) lines 105–118 | Method | Already derives the branching and the precise "mod products" statement with full reasoning | CITE; do NOT re-derive the conceptual chain | plan, execution |
| `.gpd/research/PRIOR-WORK.md` Open Q #3 (RING-(c)) | Prior work / scope | States RING-(c) is "PROVABLE-IN-HARNESS via dim Hom_{F_4}(27⊗27, triv) + symmetric part," not a single verbatim citation | Frame Route A as corroboration, Route B as the proof | plan |
| Garibaldi–Guralnick 2015 (Forum Math. Pi 3, e3) "Simple Groups Stabilizing Polynomials" | Benchmark / literature | F_4 = identity component of Stab(Tr, trace form, det); pins down WHY the trace form (= c) is the F_4-invariant (1,1) pairing not present for E_6 | CITE for the group identification and uniqueness-of-trace-form context | plan, write-up |
| Wikipedia "F4 (mathematics)" + Slansky tables | Benchmark / literature | Confirms F_4 small-irrep dimensions {1, 26, 52, 273, 324, 1053, 1274}; 26 = trace-free Albert part; 52 = adjoint | CITE for the dimension list backing the branching | plan, write-up |

**Missing or weak anchors:** The *verbatim* published plethysm "Sym²(26)_{F_4} = 1 ⊕ 26 ⊕ 324" was NOT retrievable as readable text from web sources this session (arXiv PDFs returned compressed/unreadable; no indexed LiE table). This is a MEDIUM-confidence literature gap, but it is NOT a planning blocker: (a) the dimension arithmetic is fully internally consistent (verified below), (b) the constituent facts (the irreps {1,26,52,273,324}, 27=1⊕26, self-duality) are textbook-standard, and (c) the DECISIVE route is the self-certifying exact-QQ nullspace, which proves dim=2 independently of any literature table. The roadmap's own backtracking guidance ("TRUST THE EXACT NULLSPACE") confirms this ordering. Recommend the planner schedule a cheap optional Route-A0 character/Molien sanity check (see Validation) if a fully independent confirmation of the 324 multiplicity is wanted; flag that this would naively want LiE/Sage (absent — see Pitfall "Sage-only").

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Jordan product | A∘B = ½(AB + BA) | (AB+BA) without ½ | `ring_lemma_verification.py` ASSERT_CONVENTION |
| Jordan trace Tr | sum of 3 real diagonal entries; **Tr(I) = 3** | — | frozen engine; affects linear-independence check |
| Coupling | c(X,Y) = Tr(X∘Y), bidegree (1,1), **c(X,X) = Tr(X²)** | — | spine_independence.py ASSERT_CONVENTION line 82 |
| Group rep | 27 = h_3(O) real-27 of F_4; **27 = 1 ⊕ 26** (trivial ⊕ trace-free irreducible) | treating 27 as irreducible (WRONG) | PITFALLS Pitfall 9; Wikipedia F4 |
| Arithmetic | EXACT SymPy over Q (QQ) | float64 (FORBIDDEN on decisive path) | all engine ASSERT_CONVENTION lines |
| Rank/nullspace | `exact_qq_rank` = DomainMatrix-over-QQ; `Matrix.rank()` for ≤27 cols | numpy.linalg.matrix_rank / SVD tolerance (FORBIDDEN) | orbit_dimension_gate.py lines 154–177 |
| 27×27 → vector | row-major `_flatten_729` (r outer, col inner); extend to 27⊗27 = 729 | any other order (must be consistent) | orbit_dimension_gate.py line 121 |
| Symmetry bookkeeping | c is SYMMETRIC under X↔Y; track symmetric (unordered) vs full ordered (1,1) tensor separately | conflating them | physics_research_focus item 1 |

**CRITICAL: All counts below use these conventions.** In particular Tr(I)=3 makes Tr(X)Tr(Y)|_{X=Y=I} = 9 while c|_{X=Y=I} = Tr(I) = 3, so the two (1,1) invariants are linearly independent (9 ≠ 3) — this is the explicit normalization-dependent witness the executor must compute. Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| 27 = 1 ⊕ 26 | F_4 branching of the Albert algebra | Wikipedia F4; PITFALLS P9 | The backbone; the "1" is the Tr/identity direction, the "26" the trace-free part |
| Sym²(26) = 1 ⊕ 26 ⊕ 324, dim 351 | symmetric square of the F_4 fundamental | METHODS §(c) line 112; dimension-verified | Source of one trivial in Sym²(27); 324 is a genuine F_4 irrep |
| Sym²(27) = 2·(1) ⊕ 2·(26) ⊕ 324, dim 378 | symmetric square of the 27 | METHODS §(c) line 112 | trivial mult 2 = {(Tr X)², Tr X²} |
| mult_1(27⊗27) = dim End_{F_4}(1⊕26) = 1²+1² = 2 | Schur's lemma count | METHODS §(c) line 113 | The bidegree-(1,1) trivial part is exactly 2-dim |
| ρ(M)(v⊗w) = (Mv)⊗w + v⊗(Mw) | Leibniz/derivation lift of f_4 to 27⊗27 | standard; physics_research_focus item 3 | THE new function: lifts the 52 generators to the 729-dim space |
| D_M f = grad_X(f)·(M·v_x) + grad_Y(f)·(M·v_y) = 0 | diagonal infinitesimal-invariance | ring_generating_set.py check_f4_invariance | The kernel condition defining invariants |
| c = (1,1)-polarization of Tr(X²) | trace-form polarization | METHODS line 64 | Identifies c with the genuine 26⊗26→1 contraction |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Complete reducibility (F_4 compact ⇒ all reps real, completely reducible) | Guarantees invariants = trivial isotypic component, multiplicity-counting is valid | Both routes | Fulton–Harris; standard |
| Schur's lemma for End_{F_4}(1⊕26) | dim of invariant pairings = Σ(mult)² over irreducibles | Route A bidegree-(1,1) count | METHODS line 113 |
| Plethysm / symmetric-square branching | Decompose Sym²(27), Sym²(26) into irreps | Route A | LiE/Slansky (cross-check only; see Open Questions) |
| Leibniz lift of a Lie-algebra action to a tensor product | Builds ρ(M) on 27⊗27 from M on 27 | Route B (NEW work) | standard derivation rule |
| Exact rational nullspace over QQ (DomainMatrix) | invariant space = kernel of stacked 52 derivation operators | Route B (the proof) | engine `exact_qq_rank` |
| Reynolds-operator / Haar averaging | Alternative projector onto invariants | Route B fallback only | METHODS line 118 (numerical Haar — AVOID, group-sampling) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| ------------- | --------------- | ------------------ | -------------- | ----------------------- |
| NONE — this phase is EXACT (rational arithmetic over Q, integer-dimensional rep theory) | — | — | zero (exact) | — |

There are no approximations. Every quantity is an exact integer (a representation dimension or a Q-vector-space dimension). Any appearance of float64 or an SVD rank tolerance on the decisive path is a forbidden proxy.

## Standard Approaches

### Approach 1: Two-Route — Branching count + Exact f_4-kernel nullspace (RECOMMENDED)

**What:** Prove the (1,1) trivial part is 2-dim and the genuine-coupling quotient is 1-dim by (A) the F_4 rep-theory branching/Schur count [conceptual proof, literature-anchored] and (B) an independent EXACT f_4-infinitesimal-kernel nullspace over QQ on the 27⊗27 (729-dim) bilinear-form space [self-certifying harness witness]. Cross-check they agree.

**Why standard:** This is the EXACT pattern that Phases 64–66 used and that the project's own METHODS.md §(c) (lines 107–118) and the roadmap success criteria both prescribe. The branching count is "the clean proof"; the infinitesimal-kernel projection is "the exact harness witness" (METHODS line 118, line 143). Two-route agreement is the project's established standard of rigor (Phase 66 SPINE was two-route).

**Track record:** The single-copy and pair f_4 actions are already built and CERTIFIED (Phase 65: pair orbit dim 44, certified against Garibaldi–Guralnick; Phase 66: two-route SPINE PASSED). The infinitesimal-kernel-over-Q route avoids the group-sampling fragility of numerical Haar averaging.

**Key steps:**

1. **Route A (branching, conceptual):** State and assert the integer facts — 27=1⊕26; dim Sym²(27)=378; dim Sym²(26)=351 = 1+26+324; trivial mult in Sym²(27)=2; trivial mult in 27⊗27 = dim End_{F_4}(1⊕26) = 1²+1² = 2 (Schur). Conclude bidegree-(1,1) trivial part = 2-dim. Cite Wikipedia/Slansky for the dimensions, Garibaldi–Guralnick 2015 for F_4 = Stab(Tr, trace form, det).
2. **Route B build (NEW work):** Lift each of the 52 certified f_4 generators M (27×27, from `inner_derivations`/`_select_independent_basis`) to ρ(M) on the 27⊗27 space (729-dim) by the Leibniz rule ρ(M)(v⊗w)=(Mv)⊗w+v⊗(Mw). In coordinates on the basis {E_a⊗E_b} this is ρ(M) = M⊗I + I⊗M (a 729×729 rational matrix, or — more cheaply — keep the action implicit and contract gradients as in `check_f4_invariance`).
3. **Route B invariance gate (BEFORE any dim count):** Verify D_M(Tr(X∘Y)) = 0 and D_M(Tr(X)Tr(Y)) = 0 over Q for ALL 52 generators at ≥3 genuinely octonionic rational points (reuse the `check_f4_invariance` recipe and `octonionic_points()`). A candidate that is not annihilated is not an invariant — STOP, do not compute any dim.
4. **Route B nullspace (the proof):** Stack the 52 derivation operators on the 729-dim space (or on the relevant degree-2 monomial space) into one tall exact-QQ matrix; the invariant space = its kernel. Compute dim = 729 − exact_qq_rank(stacked). Assert the (1,1) block dim = 2; also run the FULL degree-2 space and assert total invariant dim = 6 (blocks (2,0)=2, (0,2)=2, (1,1)=2).
5. **Identify the named basis:** Express the 2-dim (1,1) nullspace as a Q-span and show {coordinate-vector of Tr(X)Tr(Y), coordinate-vector of Tr(X∘Y)} is a basis of it (they lie in the kernel AND are linearly independent — witness Tr(I)Tr(I)=9 vs c(I,I)=3).
6. **Quotient (mod products):** The only degree-1 invariants are Tr(X) (1,0) and Tr(Y) (0,1); the only bidegree-(1,1) product of lower-degree invariants is Tr(X)·Tr(Y); hence the reducible part of the (1,1) space is span{Tr(X)Tr(Y)} (1-dim); quotient (2−1)=1 ⇒ c is the UNIQUE genuine (irreducible, non-product) degree-2 coupling generator, unique up to scale and additive multiples of Tr(X)Tr(Y).

**Known difficulties at each step:**
- Step 1: dropping the trivial summand of 27=1⊕26, or computing Sym²(26) where Sym²(27) is needed (Pitfall 9). Guard with explicit integer asserts {2, 6, 351, 378}.
- Step 2: getting the Leibniz lift wrong (e.g. M⊗M instead of M⊗I+I⊗M). Guard: ρ(M) must annihilate the KNOWN invariant Tr(X∘Y) (step 3 catches this).
- Step 3/4: the 729-dim explicit operator is large; prefer the implicit gradient-contraction approach already in `check_f4_invariance` (operates on the 54-variable symbolic gradient, splits into [0:27]/[27:54] blocks). The full nullspace, if done explicitly, is a 52·729-row by 729-col exact-QQ kernel — must use DomainMatrix (Matrix.rank is too slow at this width; see line 159).
- Step 5: a nullspace basis returned by the solver is in some arbitrary basis; must explicitly verify the named invariants span it, not just match the dimension.
- Step 6: the "mod products" qualifier is mandatory — omitting it makes the claim false (Pitfall 9.2).

### Approach 2: Branching-only (rep theory), no harness witness (FALLBACK)

**What:** Prove dim=2 purely by F_4 character theory / plethysm (Sym²(27⊕27) trivial multiplicity = 6, (1,1) block = 2), citing a literature plethysm table.

**When to switch:** Never as the primary — the project standard demands the exact harness witness, and the verbatim plethysm could not be located this session. Use Route A ONLY as corroboration of Route B, not as a standalone proof.

**Tradeoffs:** Conceptually clean and short, but (a) depends on a literature table not confirmed verbatim, and (b) violates the project's two-route / exact-witness standard. A pure character computation would naively want LiE/Sage (absent).

### Anti-Patterns to Avoid

- **Conflating Sym²(26) with Sym²(27):** the trivial summand of 27=1⊕26 is silently dropped, giving the wrong trivial multiplicity. *Example:* "Sym²(27) trivial mult = trivial mult of Sym²(26) = 1" — WRONG, it's 2.
- **Stating "c is the unique (1,1) invariant":** false — Tr(X)Tr(Y) is also a (1,1) invariant. Must say "unique modulo the reducible product Tr(X)Tr(Y) and pointwise terms." (Pitfall 9.2)
- **float64 / numpy.linalg.matrix_rank / SVD-tolerance rank on the decisive path:** rank is discontinuous; a tolerance fabricates the verdict (forbidden proxy `fp-float-rank`). Use `exact_qq_rank` only.
- **Numerical Haar/group-sampling Reynolds as the proof:** group-sampling is fragile and not exact; the infinitesimal-kernel-over-Q is the exact route (METHODS line 118).
- **Leibniz lift as M⊗M:** the derivation action is M⊗I + I⊗M, not M⊗M (which would be a group-like, not Lie-algebra-like, action).
- **Redefining "reducible"/"pointwise" to make c trivially in/out:** the definitional reward-hack (Pitfall 7). Freeze R_pt as the subalgebra generated by {Tr X, Tr X², det X, Tr Y, Tr Y², det Y}; Tr(X)Tr(Y) ∈ R_pt (it's a product of pointwise generators), c ∉ R_pt at degree 2.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| F_4 branching of Albert algebra | 27 = 1 ⊕ 26 (1 = identity/Tr direction; 26 = trace-free irreducible, self-dual) | Wikipedia F4; PITFALLS P9; standard | Backbone of Route A; assert as a fact, do not re-derive |
| F_4 small-irrep dimensions | {1, 26, 52, 273, 324, 1053, 1274} | Wikipedia F4; Slansky | Justifies 324 is a genuine irrep |
| Sym²(26) decomposition | 1 ⊕ 26 ⊕ 324, dim 351 | METHODS §(c) line 112 (dimension-verified; see Open Q for verbatim cite) | One trivial in Sym²(27) comes from here |
| ∧²(26) decomposition | 52 ⊕ 273, dim 325 | dimension-consistent (52+273=325); 52 = adjoint | Sanity: 26⊗26 = 351 + 325 = 676 ✓ |
| Trivial mult in 27⊗27 | 2 (Schur: dim End_{F_4}(1⊕26) = 1²+1²) | METHODS §(c) line 113 | The (1,1) block is exactly 2-dim |
| c = Tr(X∘Y) is the (1,1)-polarization of Tr(X²) | symmetric bilinear trace form T(X,Y)=Tr(X∘Y) | METHODS line 64; Faraut–Korányi 1994 | Identifies c with the genuine 26⊗26→1 contraction |
| F_4 = Stab(Tr, trace form, det) | identity-component characterization | Garibaldi–Guralnick 2015, Forum Math. Pi 3 e3 | WHY the trace form (=c) is the F_4-invariant (1,1) pairing |
| The 52-generator f_4 basis over Q | certified, bracket-closed, dim 52 | Phase 65/65.1; `orbit_dimension_gate.py` | REUSE verbatim for Route B; do NOT rebuild |
| Pair orbit dim = 44, trdeg = 10 | certified vs Garibaldi–Guralnick | Phase 65 | Context: 67 is degree-graded, not field-level |
| c functionally independent of 6 pointwise (SPINE_RANK=7) | two-route exact, PASSED | Phase 66 | Complementary; 67 adds the degree-2 uniqueness |

**Key insight:** Re-deriving the F_4 plethysm from scratch (e.g. a full Molien/Weyl-character integration) is wasteful AND naively wants LiE/Sage (absent). The decisive, self-certifying route is the exact f_4-kernel nullspace over Q, which the certified engine already supports. The branching is corroboration. Per the roadmap, if they disagree, the exact nullspace wins.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `_flatten_729` row-major convention | 27×27 → length-729 vector; directly the 27⊗27 coordinate order | orbit_dimension_gate.py line 121 | use consistently |
| `check_f4_invariance` gradient-split recipe | D_M f = grad_X·(M v_x) + grad_Y·(M v_y) over Q; blocks [0:27]/[27:54] | ring_generating_set.py line 236 | substitute point FIRST |
| `octonionic_points()` | ≥3 genuinely octonionic rational test points | engine | for the invariance gate |
| Total degree-2 invariant space = 6 | {(Tr X)², Tr X², (Tr Y)², Tr Y², Tr(X)Tr(Y), Tr(X∘Y)} | METHODS line 114 | the full cross-check target |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| "Simple Groups Stabilizing Polynomials" (Forum Math. Pi 3, e3) | Garibaldi, Guralnick | 2015 | F_4 = Stab(Tr, trace form, det); supports RING-(c) uniqueness | group identification; why trace form is F_4-invariant |
| "Generic Stabilizers for Simple Algebraic Groups" (arXiv:2105.09486) | Garibaldi, Guralnick | 2021 | s.g.p. of F_4 on 26 = Spin8; dim-counting for k[V]^G | context for trdeg (Phase 65 already used it) |
| C[2V]^{E6} = free on 4 det-polarizations (J. Lie Theory 21) | Blind | 2011 | CONTRAST case (E6, not F4); E6 does NOT preserve the trace form, so c is NOT an E6 invariant | sharpens why c is the genuinely F_4 (1,1) coupling |
| Iltyakov, Laplace operator & polynomial invariants (J. Algebra 207) | Iltyakov | 1998 | F_4 several-copy invariants = trace polynomials + Laplace invariants | c is a trace monomial; supports the named-basis identification |
| F4 small-irrep dimensions | Wikipedia / Slansky | — | {1,26,52,273,324,...}; 26=trace-free Albert; 52=adjoint | dimension list for Route A asserts |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| Python + SymPy | 3.x + SymPy 1.14.0 | exact rational arithmetic, symbolic gradients | the frozen project substrate |
| SymPy DomainMatrix over QQ | `sympy.polys.matrices.DomainMatrix`, `sympy.polys.domains.QQ` | EXACT fast rank/nullspace at large width (729) | `exact_qq_rank` already validated EXACT == Matrix.rank() on certified single-copy case |
| `code/orbit_dimension_gate.py` | — | f_4 basis, `_flatten_729`, `exact_qq_rank`, `span_rank_over_QQ`, `infinitesimal_action` | certified Phase 65 engine; ZERO re-derivation |
| `code/ring_generating_set.py` | — | `_f4_basis`, `check_f4_invariance`, `check_bidegree`, named invariants | certified invariance-test recipe |
| `code/ring_lemma_verification.py` | — | frozen `jordan`, `Tr`, `Tr2`, `c`, `det_3`, `polarize_d`, `Xsym`/`Ysym` | exact octonion substrate over Q |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| SymPy `Matrix.nullspace()` over QQ (small blocks ≤ ~54 cols) | explicit nullspace BASIS vectors for the named-invariant identification | step 5 of Approach 1; small blocks only |
| SymPy `.subs` + `simplify` | substitute octonionic points, verify D_M f == 0 | invariance gate |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| exact f_4-kernel nullspace | LiE/SageMath `WeylCharacterRing('F4').symmetric_power` | Sage/LiE ABSENT in env; would be the cleanest character route but cannot run here |
| infinitesimal-kernel (Lie) | numerical Haar/group-sampling Reynolds | sampling is fragile, not exact, group-element generation for F_4 nontrivial — AVOID on decisive path |
| explicit 729×729 ρ(M) = M⊗I+I⊗M | implicit gradient-contraction (check_f4_invariance style) | implicit is far cheaper and already coded; build explicit ρ(M) only if a direct nullspace basis is wanted |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| Invariance gate D_M f=0, 52 gens × ~5 points, on Tr(X∘Y), Tr(X)Tr(Y) | seconds–minutes | `simplify` over Q | substitute point FIRST (rationals, not symbols) — already the engine pattern |
| (1,1) block nullspace: stack ≤ 52 derivation ops on the relevant (1,1) monomial space, exact-QQ kernel | seconds with DomainMatrix | column width | use `exact_qq_rank` (DomainMatrix-QQ), NOT Matrix.rank at width >27 (line 159: Matrix.rank fails to return at width 54 in >5 min) |
| Full degree-2 space (the 6-dim total cross-check) | seconds–minutes | same | DomainMatrix-QQ |
| Full explicit 729-dim 27⊗27 nullspace (if built) | minutes | 52·729-row exact matrix | only if needed; prefer per-bidegree blocks (the (1,1) block alone is the contract target) |

**Installation / Setup:** No new packages required — SymPy 1.14.0 is present. SageMath is NOT installed (verified) and is NOT needed for the decisive route.
```bash
# Nothing to install. If a character cross-check via LiE/Sage were desired (NOT required):
#   it is unavailable in this environment — do not attempt; use the exact-QQ nullspace instead.
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| Dimension bookkeeping | branching arithmetic self-consistent | assert 1+26=27; 1+26+324=351; 52+273=325; 351+325=676; 1+(1·26)+351=378 | all True (verified this session) |
| Two-route agreement | rep-theory count == exact nullspace | compare Route A integer (2) vs Route B `729 − rank` on (1,1) block | both = 2 |
| Total degree-2 = 6 | full graded-piece count | exact-QQ nullspace on full degree-2 space; blocks (2,0)+(0,2)+(1,1)=2+2+2 | 6 |
| Invariance BEFORE dim | builder correctness | D_M(c)=0 AND D_M(Tr(X)Tr(Y))=0 for ALL 52 gens at ≥3 octonionic points | all annihilate (else STOP) |
| Leibniz-lift correctness | ρ(M) is a derivation | ρ(M) annihilates the KNOWN invariant c=Tr(X∘Y) | yes (catches M⊗M error) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| Restrict to E_6 (drop trace-form invariance) | larger group, smaller invariant ring | c = Tr(X∘Y) is NOT an E_6 invariant; the (1,1) E_6 invariants are fewer | Blind 2011; PRIOR-WORK line 151 |
| X = Y diagonal | c(X,X) = Tr(X²); Tr(X)Tr(X) = (Tr X)² | the (1,1) invariants restrict to the (2,0) pointwise quadratics | convention (c(X,X)=Tr X²) |
| Linear-independence witness | X = Y = I | Tr(I)Tr(I) = 9, c(I,I) = Tr(I) = 3, 9 ≠ 3 | Tr(I)=3 normalization |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| (1,1) trivial multiplicity | exact-QQ nullspace dim | EXACT (zero tolerance) | 2 |
| total degree-2 invariant dim | exact-QQ nullspace dim | EXACT | 6 |
| genuine-coupling quotient | (1,1) dim − reducible-product dim = 2 − 1 | EXACT | 1 |
| Sym² dimensions | integer arithmetic | EXACT | 378, 351 |

**Optional Route-A0 (character/Molien sanity, only if a fully independent confirmation of the 324 multiplicity is wanted):** A cheap character spot-check would evaluate the Sym² character at a few F_4 group elements and match the trivial multiplicity. This naively wants LiE/Sage (ABSENT). If pursued in pure SymPy it is heavier than the exact-QQ nullspace and is NOT recommended as part of the contract — the nullspace already gives an independent integer.

### Red Flags During Computation

- (1,1) block dim ≠ 2: recheck 27=1⊕26 split and whether Tr(X)Tr(Y) was double-counted or dropped (roadmap backtracking). If exact nullspace says ≠2, TRUST THE NULLSPACE and re-derive the irrep arithmetic.
- Total degree-2 dim ≠ 6: a block ((2,0)/(0,2)/(1,1)) is miscounted; isolate per-bidegree.
- ρ(M) does NOT annihilate Tr(X∘Y): the Leibniz lift is wrong (likely M⊗M) — STOP.
- Any `numpy`/float rank call on the decisive path: forbidden proxy — replace with `exact_qq_rank`.
- A nullspace dim matches 2 but the named invariants do NOT span it: the coordinate convention (729 flatten order) or the named-invariant coordinatization is inconsistent — recheck `_flatten_729` usage.

## Common Pitfalls

### Pitfall 1: 26-vs-27 confusion (forbidden proxy — Pitfall 9)

**What goes wrong:** Computing Sym²(26) where Sym²(27) is needed, or forgetting the trivial summand of 27=1⊕26, giving the wrong trivial multiplicity.
**Why it happens:** "the 27" and "the 26" are used interchangeably in physics prose; the Tr/identity direction is easy to drop.
**How to avoid:** Carry 27=1⊕26 explicitly everywhere. Encode runnable asserts: trivial mult in Sym²(27)=2, in 27⊗27=2; dim Sym²(27)=378, dim Sym²(26)=351=1+26+324.
**Warning signs:** a Sym² dimension that is not 378 or 351; a trivial multiplicity ≠ 2.
**Recovery:** re-split 27=1⊕26; recompute Sym²(1⊕26)=Sym²(1)⊕(1⊗26)⊕Sym²(26).

### Pitfall 2: Dropping the "mod products" qualifier (Pitfall 9.2)

**What goes wrong:** Claiming "c is the unique (1,1) invariant" — false, since Tr(X)Tr(Y) is also (1,1).
**Why it happens:** the reducible product Tr(X)Tr(Y) is easy to forget; the uniqueness is in the QUOTIENT, not the full (1,1) space.
**How to avoid:** State precisely: the (1,1) space is 2-dim {Tr(X)Tr(Y), Tr(X∘Y)}; modulo the reducible product Tr(X)Tr(Y) (a product of pointwise generators) the genuine-coupling space is 1-dim = span{c}. Assert `is_in_Rpt(Tr_X·Tr_Y) == True`.
**Warning signs:** a (c) statement with no "modulo Tr(X)Tr(Y)" clause.
**Recovery:** restate the quotient explicitly.

### Pitfall 3: Float/SVD rank on the decisive path (forbidden proxy `fp-float-rank`)

**What goes wrong:** `numpy.linalg.matrix_rank` or an SVD tolerance fabricates a dimension (rank is discontinuous).
**Why it happens:** float linear algebra is faster and habitual.
**How to avoid:** `exact_qq_rank` (DomainMatrix-over-QQ) only; the engine's exact-only source guard asserts zero numpy float-rank calls.
**Warning signs:** any `import numpy` on the nullspace path.
**Recovery:** swap to DomainMatrix-QQ; re-run the exact-only guard.

### Pitfall 4: Symmetric vs ordered (1,1) bookkeeping

**What goes wrong:** Confusing Sym²(27) (X↔Y unordered) with the ordered bidegree-(1,1) part 27⊗27. The coupling c=Tr(X∘Y) is SYMMETRIC under X↔Y.
**Why it happens:** the (1,1) graded piece of R[27⊕27] is the FULL 27_X⊗27_Y (ordered, two distinct copies), whose trivial mult is 2 by Schur; both basis invariants {Tr(X)Tr(Y), Tr(X∘Y)} happen to be X↔Y-symmetric, but the count is the End_{F_4}(1⊕26) count, not a Sym² count.
**How to avoid:** For the bidegree-(1,1) block use mult_1(27_X ⊗ 27_Y) = dim End_{F_4}(1⊕26) = 2 (Schur). For Sym²(27) (the (2,0)+(0,2) self-coupling combined as one symmetric square) use the 378 decomposition. Keep the two computations separate; the exact nullspace per-bidegree settles it.
**Warning signs:** trying to read the (1,1) count off Sym²(27) directly.
**Recovery:** compute the (1,1) block as its own exact nullspace (the 27_X⊗27_Y space).

### Pitfall 5: Sage-only reflex

**What goes wrong:** Reaching for SageMath `WeylCharacterRing('F4')` (cited in PITFALLS detection tests) — it is NOT installed.
**Why it happens:** the project research files reference Sage for the character cross-check.
**How to avoid:** the decisive route is the exact-QQ nullspace (pure SymPy); the branching integers are LITERATURE anchors, not things to recompute. Do NOT attempt Sage/LiE.
**Warning signs:** `import sage` (will fail); a plan task that requires a WeylCharacterRing.
**Recovery:** replace any Sage character step with the exact f_4-kernel nullspace.

## Level of Rigor

**Required for this phase:** EXACT computational proof (rational arithmetic over Q, integer rep-theory) with two-route agreement, matching the project's established standard.

**Justification:** The claim is a precise finite-dimensional statement (dim of a Q-vector space = 2; quotient = 1). It admits an exact answer and the project standard (Phases 64–66) is exact-over-Q with two-route corroboration. No approximation is acceptable.

**What this means concretely:**
- All ranks/dims via `exact_qq_rank` (DomainMatrix-over-QQ) or small-block `Matrix.rank()`/`nullspace()` over QQ — NEVER float.
- The invariance gate (D_M f = 0 for all 52 generators) must PASS before any dimension is reported.
- The 2-dim (1,1) nullspace must be shown to be SPANNED by the named invariants {Tr(X)Tr(Y), Tr(X∘Y)}, not merely have the right dimension.
- The "mod products" quotient must be stated precisely (the reducible part = span{Tr(X)Tr(Y)}, quotient = span{c}).
- Two routes (branching count + exact nullspace) must agree on dim=2; on disagreement, the exact nullspace is authoritative.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Numerical Haar/group-sampling Reynolds projection | Exact f_4-infinitesimal-kernel over Q | Phase 65 (engine certified) | exact, no sampling fragility; the decisive route |
| Matrix.rank() at pair width | DomainMatrix-over-QQ (`exact_qq_rank`) | Phase 65 (line 159) | ~0.01s vs >5min; same exact answer |
| Treating R[27⊕27]^{F_4} as "find generators from scratch" (Derksen) | "verify + cite": branching count + exact witness | METHODS / PRIOR-WORK | RING-(c) is provable-in-harness, not a from-scratch Gröbner computation |

**Superseded approaches to avoid:**
- Full Derksen algorithm / complete SFT syzygy ideal: OUT OF SCOPE for degree-2 uniqueness (that is Phase 68 generation, and even there only Hilbert-series matching is needed). People reach for it because it is "the general algorithm," but it is far heavier than needed.
- Numerical group averaging: superseded by the exact infinitesimal kernel; still tempting because it is conceptually simple, but it is not exact.

## Open Questions

1. **Verbatim literature plethysm of Sym²(26)_{F_4} = 1 ⊕ 26 ⊕ 324.**
   - What we know: the dimensions {1,26,52,273,324} are confirmed F_4 irreps (Wikipedia/Slansky); the arithmetic 1+26+324=351 and 52+273=325 (=∧²) is fully self-consistent; METHODS.md already states the decomposition with reasoning.
   - What's unclear: a single readable published table stating "Sym²(26)=1⊕26⊕324" was not retrievable from web text this session (arXiv PDFs returned compressed; no indexed LiE output). The relevant papers (Quantum diagrammatics for F4 arXiv:2204.11976; Casimir-operators hep-th/9312148) almost certainly contain it but could not be parsed here.
   - Impact on this phase: LOW. The decisive route is the self-certifying exact-QQ nullspace, which proves dim=2 independently. The branching is corroboration.
   - Recommendation: proceed with the exact nullspace as the proof; cite METHODS.md + Wikipedia/Slansky dimensions for Route A; if a fully independent literature confirmation of the 324 multiplicity is later wanted, retrieve Cvitanović/Cohen-de Man or a LiE table offline (NOT a blocker).

2. **Whether to build ρ(M) explicitly (729×729) or keep it implicit (gradient contraction).**
   - What we know: both are exact; the implicit contraction (check_f4_invariance style) is already coded and cheap; the explicit operator gives a direct nullspace basis.
   - What's unclear: which the planner/executor prefers for the named-basis identification (step 5).
   - Impact: implementation detail, not correctness.
   - Recommendation: Agent's discretion — default to the per-bidegree block nullspace (the (1,1) block alone is the contract target), build the explicit ρ(M) only if a direct basis is needed.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Exact nullspace on full 729 space | width too large / slow | Per-bidegree block nullspace (just the (1,1) = 27_X⊗27_Y block) | low — the (1,1) block is the contract target anyway |
| Implicit gradient contraction | hard to extract a basis | Explicit ρ(M)=M⊗I+I⊗M, then `Matrix.nullspace()` over QQ on the block | low–medium |
| Route B disagrees with Route A | irrep-arithmetic error | TRUST Route B (exact nullspace); re-derive Route A integers | low (roadmap-mandated) |
| Verbatim plethysm needed but unavailable | no Sage/LiE | Rely on exact nullspace + dimension-bookkeeping asserts | none for the proof; only weakens the corroboration citation |

**Decision criteria:** If the full 729-space nullspace is slow, drop immediately to the per-bidegree (1,1) block (the contract only requires the (1,1) count = 2 plus the total degree-2 = 6 cross-check, both of which decompose by bidegree). If Routes A and B ever disagree, the exact nullspace is authoritative (roadmap backtracking guidance).

## Sources

### Primary (HIGH confidence)

- `.gpd/research/METHODS.md` §(c) lines 105–118 — the branching derivation and precise "mod products" statement (project-internal, derived & cross-checked).
- `.gpd/research/PITFALLS.md` Pitfall 9 (lines 278–306) — the 26-vs-27 forbidden proxy and the exact target integers {2, 6, 351, 378, 1⊕26⊕324}; runnable detection asserts.
- `.gpd/research/PRIOR-WORK.md` Open Q #3, refs Garibaldi–Guralnick 2015/2021, Blind 2011, Iltyakov 1998 — framing RING-(c) as provable-in-harness.
- `code/orbit_dimension_gate.py`, `code/ring_generating_set.py`, `code/ring_lemma_verification.py` — the certified exact engine (f_4 basis, `_flatten_729`, `exact_qq_rank`, `check_f4_invariance`).
- Wikipedia "F4 (mathematics)" (https://en.wikipedia.org/wiki/F4_(mathematics)) — F_4 irrep dimensions {1,26,52,273,324,1053,1274}; 26 = trace-free Albert part; 52 = adjoint. (verified this session)
- Garibaldi–Guralnick, "Simple Groups Stabilizing Polynomials," Forum Math. Pi 3 (2015) e3 — F_4 = Stab(Tr, trace form, det). (cited via PRIOR-WORK)

### Secondary (MEDIUM confidence)

- "Quantum diagrammatics for F4," arXiv:2204.11976 — likely contains 26⊗26 decomposition (PDF unreadable this session; for offline verification of the 324 multiplicity).
- "Casimir operators of the exceptional group F4," arXiv:hep-th/9312148 — likely tabulates Sym²/∧² of 26 (abstract only readable this session).
- Slansky, "Group Theory for Unified Model Building," Phys. Rep. 79 (1981) — standard branching/plethysm tables for F_4 (not re-pulled this session; cited via project research).

### Tertiary (LOW confidence)

- Internal dimension-bookkeeping script (this session) — confirms arithmetic self-consistency (1+26=27; 1+26+324=351; 52+273=325; 351+325=676; 1+26+351=378; Tr(I)=3 ⇒ 9≠3). Not a rep-theory proof, only a consistency witness.

## Metadata

**Confidence breakdown:**
- Mathematical framework (branching, Schur count, "mod products"): HIGH — textbook-standard facts, fully self-consistent arithmetic, already derived in project METHODS.md.
- Standard approaches (two-route, exact nullspace): HIGH — exact replica of the certified Phase 64–66 pattern; engine confirmed present.
- Computational tools (SymPy exact-QQ engine): HIGH — `exact_qq_rank`, `_flatten_729`, `check_f4_invariance`, f_4 basis all verified present and certified; no Sage needed.
- Validation strategies (two-route agreement, total-degree-6 cross-check, named-basis identification): HIGH.
- Verbatim literature plethysm of Sym²(26): MEDIUM — facts standard and arithmetic-consistent, but a single readable published table was not retrieved this session; immaterial to the decisive route.

**Research date:** 2026-05-26
**Valid until:** Indefinite for the rep-theory facts (stable mathematics). SymPy 1.14.0 / engine-API specifics may drift faster; the named engine functions are the current certified API.

## Caveats and Alternatives (Pre-Submission Self-Critique)

1. **What assumption might be wrong?** That the (1,1) graded piece is the full ordered 27_X⊗27_Y (mult 2), not a symmetric square. Mitigation: this is settled by the exact per-bidegree nullspace, which does not assume the count.
2. **What alternative did I dismiss too quickly?** A pure-character (LiE/Sage) proof. Dismissed because Sage is absent and the project standard demands the exact harness witness. Reasonable: the exact nullspace is strictly more authoritative here per the roadmap.
3. **What limitation am I understating?** The verbatim literature confirmation of "324 appears with multiplicity 1 in Sym²(26)" is not pinned to a single readable citation this session. Understated risk is LOW because the decisive route is self-certifying; flagged as Open Q #1.
4. **Simpler method overlooked?** The implicit gradient-contraction (already in `check_f4_invariance`) is simpler than building a 729×729 operator; recommended as default. The explicit operator is only for extracting a basis.
5. **Would a specialist disagree?** A rep-theorist might prefer the one-line Schur argument (dim End_{F_4}(1⊕26)=2) and consider the harness redundant. But the project's standard of rigor (exact, two-route, no forbidden proxies) makes the harness witness mandatory, and the roadmap explicitly elevates the exact nullspace above the irrep arithmetic on disagreement. The two-route presentation satisfies both audiences.

## RESEARCH COMPLETE
