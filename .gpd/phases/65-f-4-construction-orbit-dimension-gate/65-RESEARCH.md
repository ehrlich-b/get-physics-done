# Phase 65: f_4 Construction + Orbit-Dimension GATE - Research

**Researched:** 2026-05-25
**Domain:** Computational invariant theory; f_4 = Der(h_3(O)) = Lie(Aut(h_3(O))); generic orbit dimension of F_4 on 27 (+) 27
**Confidence:** HIGH on the construction route (inner-derivation builder, verified to reproduce the orbit-24 / Spin(8) anchor), the basis-consistency, the anchor, AND the root-cause of a Phase-64 norm bug now fixed in Phase 64.1.

> **CORRECTION NOTICE (2026-05-25, supersedes the first draft of this file).**
> An earlier draft of this RESEARCH concluded the inner-derivation builder
> `f_4 = span{[L_a,L_b]}` was WRONG and recommended rebuilding f_4 as
> `stab(det_3)`. **That diagnosis was inverted.** Exact-SymPy + Cayley-Hamilton
> verification (orchestrator, 2026-05-25) established:
> - the inner-derivation builder is **CORRECT** — `span{[L_a,L_b]}` has dim 52
>   and reproduces the single-copy orbit dim **24** (= Spin(8) stabilizer, dim 28),
>   i.e. it IS `f_4 = Der(h_3(O)) = Lie(Aut)`;
> - the FROZEN `det_3` was the wrong object: its cubic-norm **cross term had the
>   first two octonion factors transposed** (`2Re((x1 x2) x3)` instead of the
>   generic norm's `2Re((x2 x1) x3)`), so it was NOT `Aut(h_3(O))`-invariant.
> This norm bug is **fixed in Phase 64.1** (cross term corrected; a permanent
> generic-norm-consistency lock added to the harness). The rest of this file is
> rewritten to the corrected diagnosis and route. The `Der(o) != stab(det_3)`
> observation the first draft made was a real *detection* of the bug — but the
> fault was in `det_3`, not in the builder.

## Summary

This phase builds `f_4 = Der(h_3(O))` explicitly as 52 derivations (27x27 rational
matrices), verifies infinitesimal `F_4`-invariance of the (now-correct) base
invariants, and computes the **generic orbit dimension** of the diagonal `F_4`
action on `h_3(O) (+) h_3(O)` as the exact rank over `Q` of the `52x54`
infinitesimal-action matrix at a generic rational point. The consistency anchor
`54 - orbit_dim = 7` is the milestone's early go/no-go.

**Construction route (VERIFIED CORRECT): inner derivations.**
`f_4 = span{ [L_a, L_b] : a,b in h_3(O) }`, where `L_A(Z) = jordan(A, Z)` is
Jordan left-multiplication as a 27x27 matrix. Facts established by exact spike
(orchestrator):
- `(h_3(O), jordan)` satisfies the Jordan identity (genuine Jordan algebra);
- each `[L_a, L_b]` is a genuine derivation (Leibniz holds as an identity);
- `span{[L_a,L_b]}` has dim **52** over Q (= dim f_4);
- it reproduces the single-copy orbit dim **24** (stabilizer Spin(8), dim 28) —
  the Garibaldi-Guralnick anchor — confirming the builder is `Der(h_3(O)) = f_4`;
- after the Phase-64.1 norm fix, all `324` nonzero brackets annihilate the
  corrected `det_3` (and `Tr`, `Tr2`); pre-fix only 30/324 did, which is how the
  bug was caught.

**The corrected norm (Phase 64.1):** the `F_4`-invariant cubic norm is the
generic norm `N` of `(h_3(O), jordan)`, characterized by Cayley-Hamilton
`X^o3 - Tr(X) X^o2 + S(X) X - N(X) I = 0`, `S(X) = (1/2)(Tr(X)^2 - Tr(X o X))`.
Concretely `N(X) = abc - a|x1|^2 - b|x2|^2 - g|x3|^2 + 2Re((x2 x1) x3)` (cross
term `(x2 x1) x3`, NOT `(x1 x2) x3`). Phase 64.1's frozen `det_3` equals this N.

**Why this matters for the GATE:** the seven base invariants
`{Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c=Tr(X o Y)}` must all be invariants
of the SAME group (`F_4 = Der(jordan)`) acting the SAME way. With the corrected
`det_3`, they are. The orbit-dim rank then measures the true `F_4`-orbit and
`54 - orbit_dim` is the true transcendence degree.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| `code/ring_lemma_verification.py` (Phase 64.1 frozen engine) | prior artifact (foundation) | `oct_mul`, `h3o_from_coords`, `h3o_matmul`, `jordan`=(1/2)(AB+BA), `_coord_from_octmat`, `Tr`/`Tr2`/`det_3`(CORRECTED)/`c`/`polarize_d`, 54-symbol layout, `X_from_symbols`, FROZEN R_pt, EXACT-ONLY guard, NEW generic-norm-consistency lock | REUSE verbatim; build f_4 (inner derivations) on top of `jordan`; use the corrected `det_3` | plan, execution, verification |
| `code/octonion_algebra.py` (FLOAT64 — FORBIDDEN on decisive path) | method spec ONLY | `_g2_derivation_matrix` (Schafer @2349); Spin(9) construction in `verify_f4_invariance_det3` (@2545); `to_vector`/`from_vector` (@268/276). NOTE its `det_3` (@2178) has the SAME cross-term bug — do NOT copy it; use the Phase-64.1 corrected norm | EXTRACT g_2/Spin(9) formulas only IF a cross-check is wanted; NEVER call on a decisive line | plan (optional cross-check) |
| Schafer 1966, *Nonassociative Algebras* | method (textbook) | inner derivations `[L_a,L_b]` span `Der(J)=f_4` (all derivations inner, simple char-0 Jordan algebra); each preserves the generic norm | CITE for the builder | plan, verification |
| Jacobson, *Structure & Repr. of Jordan Algebras* | method (textbook) | `[L_a,L_b] in Der(J)` for any Jordan algebra; `Der(Albert)=f_4` dim 52 | CITE for builder correctness | plan, verification |
| Garibaldi-Guralnick arXiv:2308.08214 / Lawther arXiv:1508.02918 | benchmark (single-copy anchor) | F_4 on 26 -> Spin(8) (28), orbit 24, trdeg 3 | CITE; reproduce as the single-27 builder GATE (already verified to match) | execution (sanity), verification |
| Derksen-Kemper 2002 *Computational Invariant Theory* §4 | method | orbit dim = rank of infinitesimal action at generic pt (char 0); = trdeg of invariant field | CITE for the orbit-dim GATE | execution, verification |
| Faraut-Koranyi Ch. II-IV (Thm IV.2.5) + Springer 1962 | benchmark (single-state ring) | R[h_3(O)]^{F_4}=R[Tr,Tr^2,det], trdeg 3 -> single-27 orbit 24 | CITE (Ch. II-IV, NOT Ch. V — Phase-64 correction) | verification |
| `.gpd/research/COMPUTATIONAL.md` (survey, 2026-05-24) | prior artifact (algorithm) | orbit-dim algorithm, exact-rank discipline, random-point hygiene, substitute-before-rank — ALL valid | CITE; its "all-inner route gives f_4" claim is CONFIRMED correct here (the survey was right; the first draft of THIS file wrongly doubted it) | plan |

**Missing or weak anchors:** Direct PDF quote of Garibaldi-Guralnick failed (arXiv
PDF rendered as compressed binary); MITIGATED by web_search snippet quoting the
statement, by the fact being standard (Springer-Veldkamp; Igusa 1970), and — most
decisively — by the in-engine reproduction of orbit 24 with the verified builder.

## Conventions

| Choice | Convention | Source |
| --- | --- | --- |
| Arithmetic | EXACT over Q (`sympy.Rational`); NO floats on decisive path | Phase 64; EXACT-ONLY GUARD |
| Rank | `sympy.Matrix(...).rank()` over QQ; `numpy.linalg.matrix_rank` FORBIDDEN on decisive path | Phase 64; survey anti-approach |
| Jordan product | `jordan(A,B)=(1/2)(AB+BA)` | ring_lemma_verification.py:260 |
| Octonion mult | Fano e1*e2=e4, e_i*e_i=-1 | engine block |
| Cubic norm cross term | `2*Re((x2*x1)*x3)` (CORRECTED in Phase 64.1; was `(x1*x2)*x3`) | Phase 64.1; Cayley-Hamilton generic norm |
| 54-symbol layout | engine-native: 3 diag reals + 3 octonions x 8; x1->[2][1], x2->[0][2], x3->[1][0] | ring_lemma_verification.py:380-395 |
| f_4 builder (USE THIS) | `f_4 = span{[L_a,L_b]}`, `L_A(Z)=jordan(A,Z)`, dim 52, all derivations inner | Schafer/Jacobson; spike-confirmed (orbit 24) |
| f_4 definition (equivalent cross-check) | `f_4 = {M in gl_27 : D_M is a Jordan derivation}` = `{M : D_M(jordan(X,Y)) = jordan(D_M X,Y)+jordan(X,D_M Y)}` | standard; equals the inner span |

**CRITICAL (lesson from the Phase-64 bug):** a candidate norm being a cubic form
with `polarize_d=6N`, `N(diag)=abc`, `N(I)=1` is NOT sufficient to certify it is
the `F_4`-invariant generic norm — those hold for the wrong cross-term ordering
too. The decisive certificate is: `N` equals the Cayley-Hamilton norm of `jordan`
AND `D_xi N = 0` for all 52 inner derivations, tested on **genuinely octonionic**
points (non-real off-diagonals). Phase 64.1 installs this as a permanent lock.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name | Source | Role |
| --- | --- | --- | --- |
| `L_A(Z) = jordan(A,Z)`; `D_{A,B} = [L_A,L_B] = L_A L_B - L_B L_A` | inner derivation | Schafer/Jacobson | the f_4 builder |
| `span{[L_a,L_b]}` over a basis of h_3(O), dim 52 | f_4 = Der(h_3(O)) | Jacobson (all derivations inner) | the 52 generators |
| `D_M f := (grad f) . (M . v)` | infinitesimal action of M on invariant f | Derksen-Kemper §4 | annihilation test AND orbit-rank |
| `X^o3 - Tr X^o2 + S X - N I = 0`, `S=(1/2)(Tr^2 - Tr2)` | Cayley-Hamilton / generic norm | Springer-Veldkamp | DEFINES the correct N (= corrected det_3) |
| `orbit_dim = rank(J_orbit)` at generic pt | orbit dim = rank of infinitesimal action | Derksen-Kemper §4 | the GATE |
| F_4 on 26 -> Spin(8), orbit 24 | Garibaldi-Guralnick generic stabilizer | arXiv:2308.08214 | single-27 builder GATE (verified to match) |

### Required Techniques

| Technique | What It Does | Where Applied | Reference |
| --- | --- | --- | --- |
| Jordan left-mult matrices `L_A` | 27x27 matrix, column j = `vec(jordan(A, E_j))` | build inner derivations | this RESEARCH (spike-verified) |
| Inner-derivation span | stack flattened `[L_a,L_b]` (729-vectors), `.rank()` over QQ == 52 | dim(f_4) check + select 52 independent | Jacobson; spike |
| Derivation identity test | `D_M(jordan(X,Y)) == jordan(D_M X,Y)+jordan(X,D_M Y)` at >=3 octonionic pts | confirm each generator is in Der | this RESEARCH |
| Infinitesimal invariance | `D_xi f := (grad f).(M_xi . v)` -> 0 over Q for f in {Tr,Tr2,det_3} | the F_4-invariance certificate | Derksen-Kemper |
| Substitute-then-rank, matrix-VECTOR tangents | substitute INTEGER point FIRST; `D.x = M.x` is matrix*vector | orbit-dim, Jacobian | survey + this RESEARCH (perf) |

### Approximation Schemes

NONE. Exact finite linear algebra over Q throughout. No small parameter, no
truncation; only termination (and SymPy expression swell, controlled by
substituting integer points first).

## Standard Approaches

### Route (PRIMARY, verified): inner derivations `f_4 = span{[L_a,L_b]}`

**What:** For a basis `E_0..E_26` of h_3(O), build `L_k = L_matrix(E_k)` (27x27,
column j = `vec(jordan(E_k, E_j))`). Form all `[L_a, L_b] = L_a L_b - L_b L_a`
(a<b). Stack the nonzero ones (324 of them), take `.rank()` over QQ -> 52. Select
52 independent generators (rref pivots on the 324x729 flattened stack, OR — to
avoid the heavy 729-col rref — orthogonalize incrementally / accept the full
spanning set, since the orbit-rank of a spanning set equals that of a basis).

**Why correct (spike-verified):** Jordan identity holds, so each `[L_a,L_b]` is a
derivation (Leibniz, exact identity); for the simple char-0 Albert algebra all
derivations are inner, so the span IS `Der(h_3(O)) = f_4`, dim 52; and it
reproduces the literature single-27 orbit dim 24 (= Spin(8) stabilizer). Reuses
ONLY the frozen `jordan`.

**Key steps (executor recipe):**
1. `E_basis[k] = X_from_symbols(unit_vector_k)`; `L_matrix(A)` columns `= vec(jordan(A, E_basis[j]))` (vec = `[a,b,g]+x1+x2+x3` flattening of `_coord_from_octmat`).
2. Build the 324 nonzero `[L_a,L_b]`; assert `span rank == 52` over QQ.
3. Select/keep generators so the 52-dim algebra is represented (basis or full span).
4. Lie-closure check: a sample of `[[L_a,L_b],[L_c,L_d]]` stays in the span (rank stays 52).

### Equivalent cross-check (optional): derivation-condition nullspace

`f_4 = { M in gl_27 : D_M(jordan(X,Y)) - jordan(D_M X,Y) - jordan(X,D_M Y) = 0 }`
as a linear system in the 729 entries of M (impose on a basis of pairs (X,Y) /
random octonionic points). Its nullspace is exactly `Der(jordan) = f_4`, dim 52.
Use ONLY as an independent confirmation that the inner span is complete — it is
heavier (729-wide nullspace) and not needed for the primary route.

> **Do NOT** build `f_4 = stab(det_3)` of the *uncorrected* det_3 (the first draft's
> route). With the corrected Phase-64.1 norm, `stab(det_3) ∩ stab(Tr)` and the
> inner span coincide (both = f_4); the inner span is the cheaper, directly-correct
> builder.

### Anti-Patterns to Avoid

- **Re-introducing the cross-term bug:** any copy of `octonion_algebra.py`'s
  `det_3` (cross `(x1 x2) x3`) re-imports the bug. Use the Phase-64.1 corrected
  `det_3` (`(x2 x1) x3`). The permanent norm-consistency lock will catch a regression.
- **Certifying a norm by `polarize=6N` / diagonal values only:** insufficient
  (the bug passed all of these). Certify by Cayley-Hamilton + `D_xi N = 0` on
  octonionic points.
- **Single-point invariance test:** `D_M f = 0` at one point has false positives;
  test at >=3 independent points (better: as a polynomial identity / nullspace).
- **Float rank (`np.linalg.matrix_rank`, `lstsq`, SVD tol):** FORBIDDEN on the
  decisive path. `Matrix.rank()` over QQ. (numpy is fine for non-decisive sanity.)
- **Spin(8)-triality back-of-envelope for the PAIR (HARD-forbidden proxy):** the
  single-copy Spin(8) does NOT give the pair principal isotropy (triality permutes
  the three 8's). COMPUTE the 52x54 rank.
- **Looking up the pair orbit dimension (HARD-forbidden proxy):** COMPUTE it.
- **Symbolic det_3 Jacobian in 54 vars then `simplify()`:** expression swell.
  Substitute an INTEGER point FIRST. Avoid fraction-heavy points (denominator blowup).

## Generic orbit dimension on 27 (+) 27 (the GATE)

The diagonal `F_4` action: `D_xi` acts on `X` and on `Y` by the SAME 27x27 matrix
`M_xi`. Build the `52 x 54` infinitesimal-action matrix `J_orbit` whose `xi`-th
row is `(M_xi . x*, M_xi . y*)` (a 54-vector) at a random rational pair
`(x*, y*)`. Then:

```
generic_orbit_dim = J_orbit.rank()          # rank over Q, EXACT, substitute point FIRST
generic_stabilizer_dim = 52 - generic_orbit_dim
transcendence_degree = 54 - generic_orbit_dim
```

Random-point hygiene: recompute at >=3 independent INTEGER points, take the MAX
(rank is lower-semicontinuous — it can only drop on special loci). Consistency
anchor: expect `54 - orbit_dim == 7` (orbit 47), with pair-stabilizer dim >= 5.

## Existing Results to Leverage

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| `[L_a,L_b] in Der(J)`; all derivations of Albert algebra inner | `Der(h_3(O)) = span{[L_a,L_b]}`, dim 52 | Jacobson; Schafer 1966 | the builder |
| g_2 derivation formula | `[L,L]+[L,R]+[R,R]`, dim 14, in the inner span, preserves the (corrected) norm | Schafer; octonion_algebra.py:2349 | optional seed / cross-check |
| F_4 on 26 generic stabilizer | Spin(8) (28); orbit 24; trdeg 3 | Garibaldi-Guralnick arXiv:2308.08214 | single-27 builder GATE (verified to match) |
| Single-state invariant ring | R[h_3(O)]^{F_4}=R[Tr,Tr^2,det] | Faraut-Koranyi Ch. II-IV; Springer 1962 | confirms single-27 trdeg=3 / orbit 24 |
| Jacobian criterion (char 0) | rank(infinitesimal-action at generic pt) = orbit dim = trdeg | Derksen-Kemper §4 | orbit-dim GATE + downstream (b) test |
| dim f_4 | 52 = 36 (so(9)) + 16 (spinor) = 14 (g_2) + 38 | standard | dim sanity |

**Key insight:** the builder (`Der(jordan)`) and the invariant norm (`det_3`) must
be the SAME-structure pair. The Phase-64 bug was a *mismatched* pair (correct
builder, wrong-cross-term norm); Phase 64.1 matches them. With the corrected norm,
`{Tr, Tr2, det_3, c}` are jointly `f_4`-invariant.

### Verified intermediate results (orchestrator spikes, 2026-05-25)

| Result | What It Gives You | Conditions |
| --- | --- | --- |
| `to_vector` == frozen 54-layout; symbolic round-trip OK | NO change-of-basis for f_4 matrices | exact |
| Jordan identity holds for `jordan` | genuine Jordan algebra; `[L_a,L_b] in Der` | exact, 3 pts |
| `span{[L_a,L_b]}` dim 52; single-27 orbit dim 24 | the inner builder IS f_4 = Der(h_3(O)) | exact dim; numpy orbit sanity (exact is Phase-65's deliverable) |
| corrected `det_3` (cross `(x2 x1)x3`) == Cayley-Hamilton N | the correct F_4-invariant norm | exact, rational + integer pts |
| pre-fix det_3 killed by 30/324 brackets; corrected by 324/324 | the bug, and the fix | exact |

## Computational Tools

| Tool | Version | Purpose | Notes |
| --- | --- | --- | --- |
| SymPy | 1.14.0 (present) | EXACT octonion/h_3(O) algebra, f_4 build, all rank/nullspace over QQ | the decisive path |
| `code/ring_lemma_verification.py` | Phase-64.1 frozen | warm exact engine (jordan, corrected det_3, Tr, layout, X_from_symbols, norm-consistency lock) | reuse verbatim |
| NumPy | 2.4.2 | float SCAFFOLD only (orbit-dim pre-screen, random points) — NEVER the verdict | optional |

**Computational feasibility:** building 27 L-ops + 324 brackets ~ 1-2 min;
`span rank == 52` over QQ ~ minutes (729-wide — sub-sample or incremental if slow);
single-27 orbit rank (52x27, integer pt) seconds-minutes; pair orbit rank
(52x54, integer pt) seconds-minutes (substitute integer point FIRST; the exact
rank of a 324x54 spanning-set action matrix can be heavy with large rational
entries — use small integer points, and prefer a selected 52-row basis if the
full-span rank stalls). SageMath NOT needed for Phase 65.

## Validation Strategies

| Check | What It Validates | How | Expected |
| --- | --- | --- | --- |
| dim(f_4) = 52 | the inner span is f_4 | span rank over QQ | EXACTLY 52 |
| derivation identity | each generator is in Der(jordan) | `D_M(jordan(X,Y))=...` at >=3 octonionic pts | EXACT identity |
| det/Tr/Tr2 annihilation | invariants are F_4-invariant (corrected norm) | `D_xi f` at >=3 octonionic pts, all 52 xi | EXACT 0 over Q |
| norm-consistency (inherited from 64.1) | det_3 == Cayley-Hamilton norm | the permanent lock | passes |
| single-27 GATE | builder correctness | rank of (52 x 27) action at integer pt | orbit 24; stab 28; trdeg 3 |
| pair orbit dim | the GATE value | rank of (52 x 54) action at >=3 integer pts, take MAX | `54 - orbit_dim == 7` expected |

### Red Flags During Computation

- dim(f_4) != 52 -> builder/layout bug. STOP.
- any generator with `D_xi det_3 != 0` (corrected norm, identity) -> NOT in f_4, OR
  the norm regressed (the 64.1 lock should have caught it). STOP.
- single-27 orbit != 24 -> builder broken. Do NOT compute the pair value.
- `54 - orbit_dim != 7` -> the "six pointwise + c" generating-set picture is wrong.
  STOP (milestone backtrack).
- any float on the decisive path -> EXACT-ONLY GUARD violation; verdict void.

## Common Pitfalls

### Pitfall 1 (the Phase-64 bug, now fixed — do not regress): norm/product mismatch
A cubic form passing `polarize=6N`, `N(diag)=abc`, `N(I)=1` need NOT be the
`F_4`-invariant generic norm — the wrong cross-term ordering `(x1 x2)x3` passes
all of those yet is killed by only 30/324 inner derivations. **Avoidance:** use
the Cayley-Hamilton norm (= corrected det_3, cross `(x2 x1)x3`); the permanent
norm-consistency lock (Phase 64.1) enforces it on octonionic inputs.

### Pitfall 2: real-only / commutative-subalgebra test points hide octonion bugs
The Phase-64 checks passed partly because some exercised the commutative real
subalgebra (diagonal / real off-diagonals), where the cross-term bug is invisible.
ALL invariance/norm tests must use **genuinely octonionic** points (non-real
off-diagonal octonion components).

### Pitfall 3: single-point invariance test gives false positives
Test at >=3 independent octonionic points (better: as an identity / nullspace).

### Pitfall 4: float rank / float closure (FORBIDDEN on decisive path)
`Matrix.rank()` / exact `linsolve` over QQ. numpy only for non-decisive sanity.

### Pitfall 5: expression swell + denominator blowup
Substitute the random point FIRST; use SMALL INTEGER coordinates; tangents as
matrix*vector (`M.x`), not matrix*matrix.

### Pitfall 6: basis mismatch (RESOLVED)
`to_vector` == frozen 54-layout (verified, symbolic round-trip OK). NO
change-of-basis. Defensive: assert `vec(X_from_symbols(v)) == v` round-trip at module top.

### Pitfall 7: Spin(8)-triality back-of-envelope for the PAIR (HARD-forbidden proxy)
COMPUTE the 52x54 rank.

## Level of Rigor

**Required:** EXACT computer-algebra proof over Q (decisive go/no-go). Phase 65 is
a GATE — `54 - orbit_dim == 7` is the milestone go/no-go. As the Phase-64 bug
showed, even the choice of *which* cubic form is "the norm" must be pinned exactly
(Cayley-Hamilton + inner-derivation annihilation on octonionic points), not by a
plausible-looking formula.

## Open Questions

1. **Exact generic orbit dimension of F_4 on 27 (+) 27 (the GATE value).**
   Single-27 is 24 (verified); the pair breaks more stabilizer; the value is NOT a
   textbook number and is forbidden to look up. COMPUTE via `52x54` exact rank at
   >=3 integer points (substitute first). Expect `54 - orbit_dim == 7` (orbit 47).
2. **Full-span vs selected-basis orbit rank (perf, non-gating).** The exact rank
   of the full 324-row action matrix can stall on large rational entries; selecting
   52 independent generators (or small integer points) resolves it. Either gives
   the same orbit dimension.

## Sources

### Primary (HIGH confidence)
- Schafer, R.D., *An Introduction to Nonassociative Algebras* (1966) — inner
  derivations `[L_a,L_b]` span `Der(J)`; `Der(h_3(O))=f_4`; g_2 derivation formula.
- Jacobson, N., *Structure and Representations of Jordan Algebras* (1968) —
  `[L_a,L_b] in Der(J)`; derivations of the simple Albert algebra are all inner, dim 52.
- Springer, T.A. & Veldkamp, F.D., *Octonions, Jordan Algebras and Exceptional
  Groups* — generic norm / Cayley-Hamilton for cubic Jordan algebras; F_4 = Aut.
- Derksen, H. & Kemper, G., *Computational Invariant Theory* §4 — orbit dim =
  rank of infinitesimal action at a generic point (char 0).
- Garibaldi, S. & Guralnick, R., arXiv:2308.08214 — F_4 on 26 -> Spin(8) (28),
  orbit 24. (Reproduced in-engine with the verified builder.)
- Faraut, J. & Koranyi, A., *Analysis on Symmetric Cones*, Ch. II-IV — single-state
  ring R[Tr,Tr^2,det], trdeg 3 (Phase-64 correction: Ch. II-IV, NOT Ch. V).
- Orchestrator exact-SymPy + Cayley-Hamilton verification (2026-05-25): Jordan
  identity; inner span dim 52 & orbit 24; corrected det_3 == CH norm; 324/324
  invariance post-fix. (`/tmp/f4_diag2..4.py`, `f4_confirm2.py`, `f4_orbit_sanity.py`.)

### Secondary (MEDIUM confidence)
- Lawther, R., arXiv:1508.02918 — corroborates Spin(8)/orbit-24.
- `.gpd/research/COMPUTATIONAL.md` (survey, 2026-05-24) — algorithm/discipline;
  its all-inner-route recommendation is CORRECT (confirmed here).

## Metadata
**Confidence breakdown:**
- Construction route (inner derivations): HIGH — Jordan identity, span dim 52, orbit 24 all exact/verified.
- Corrected norm (Cayley-Hamilton, cross `(x2 x1)x3`): HIGH — exact match to CH norm, 324/324 invariance.
- Basis consistency: HIGH — symbolic round-trip.
- Single-copy anchor (orbit 24 / Spin(8)): HIGH — literature + in-engine reproduction.
- Pair orbit dimension (the GATE value): METHOD HIGH; VALUE to be COMPUTED (forbidden to look up).

**Research date:** 2026-05-25 (rewritten after the Phase-64 norm-bug discovery + Phase-64.1 fix)
**Valid until:** Mathematical content stable; engine API pinned by Phase 64.1.
