# Phase 64: Setup, Conventions, and Exact Engine - Research

**Researched:** 2026-05-25
**Domain:** Computational invariant theory of F_4 = Aut(h_3(O)); exact-SymPy octonion/Albert-algebra arithmetic over Q (engine port + convention freeze)
**Confidence:** HIGH (this is a port + freeze phase grounded in a verified, on-disk warm engine and a fresh 2026-05-24 milestone survey)

## Summary

Phase 64 lays the frozen algebraic foundation for the (RING) milestone: it ports the **exact-SymPy h_3(O) engine** out of `code/embedding_under_E_verification.py` into a new `code/ring_lemma_verification.py`, builds the **54-symbol pair coordinatization** (x0..x26, y0..y26), constructs the **seven base invariants** {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c = Tr(X∘Y)} as SymPy expressions over Q, **freezes the pointwise subring R_pt**, and verifies a small set of **convention locks exactly over Q**. Nothing here is a discovery; the risk is entirely convention/port error. The milestone survey (`.gpd/research/SUMMARY.md`, `COMPUTATIONAL.md`, `PITFALLS.md`) is fresh (one day old) and already resolved the two reconciliations that matter here: (R2) use the exact-SymPy engine, NEVER the float64 `octonion_algebra.py`; and the citation correction that the single-state ring fact lives in Faraut-Korányi Ch. II-IV, not Ch. V.

The single most important port finding (verified by direct inspection this session): the exact engine has the full octonion + h_3(O) matrix algebra (`oct_mul`, `h3o_from_coords`, `h3o_matmul`, `jordan`, `_coord_from_octmat`, `_oct_normsq`) **but does NOT expose a standalone `det_3`, `Tr`, `Tr(X^2)`, or `polarize_d`**. The det_3 formula exists only *inlined* inside `reduced_charpoly_roots` (as the T3 term, lines 567-580). The float64 `code/octonion_algebra.py` carries the canonical standalone `det_3` and the 3-argument full-polarization `polarize_d` as the **formula spec** to re-port to exact SymPy. So the port is: (a) lift/import the exact octonion+matmul+jordan block as-is, (b) extract T1/T2/T3 from `reduced_charpoly_roots` into standalone `Tr`/`Tr2`/`det_3`, (c) re-port the `octonion_algebra.py` `polarize_d` body verbatim onto the exact `det_3`.

**Primary recommendation:** Build `code/ring_lemma_verification.py` by **importing** the exact octonion/h_3(O) block from `embedding_under_E_verification.py` (or copying it verbatim with a provenance header), then add four small standalone functions — `Tr(X)`, `Tr2(X)=Tr(jordan(X,X))`, `det_3(X)` (the inlined T3 formula, lifted out), `polarize_d(X,Y,Z)` (the `octonion_algebra.py` body re-ported) — plus the 54-symbol pair layout and the seven invariants. Gate everything behind the assert-based `_report`/`ALL_PASS`/`sys.exit` harness pattern. Verify all five convention locks exactly over Q before any downstream phase touches these objects.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `code/embedding_under_E_verification.py` (exact-SymPy octonion/h_3(O) block, 1071 lines) | prior artifact (THE thing being ported) | exact `oct_mul`/`h3o_matmul`/`jordan`/coord-layout over Q; the det_3 formula lives inlined in `reduced_charpoly_roots` | IMPORT or copy-with-header the octonion+matmul+jordan block; LIFT det_3/Tr/Tr2 out of `reduced_charpoly_roots` | execution (the new module's foundation), verification (locks) |
| `code/octonion_algebra.py` (float64) | reference spec ONLY (the thing to GUARD AGAINST) | canonical standalone `det_3` (line 2152) and 3-arg `polarize_d` (line 2184) formula bodies; the Fano table + layout match | RE-PORT the `det_3`/`polarize_d` formula bodies to exact SymPy; NEVER call its float functions on any decisive path | execution (formula spec), exact-only guard (the import to forbid) |
| `code/slice_clause_iii_verification.py` | pattern artifact | the assert-based `_report` / `ALL_PASS` / `sys.exit(0/1)` harness pattern (no pytest; executor venv = sympy/numpy only) | REUSE the harness skeleton verbatim | execution (module structure) |
| Faraut-Korányi, *Analysis on Symmetric Cones* (OUP 1994), Ch. II-IV (Thm IV.2.5 region) | benchmark / citation | the single-state ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det], trdeg 3, degrees 1/2/3 ("Observable" ring) | CITE for the single-state ring confirmation; RECORD the "Ch. V" citation correction | plan (Success Criterion 3), verification |
| Springer 1962/1973 (cubic norm) | benchmark / citation | uniqueness of the cubic norm N = det_3 on h_3(O); the det_3 reference | CITE as the det_3/cubic-norm anchor | plan, verification |
| `.gpd/research/PITFALLS.md` (Pitfall 7, convention traps) | prior research | the FROZEN R_pt definition; det-normalization / Jordan-½ / sharp-vs-d traps | HONOR the frozen R_pt phrasing; encode the convention locks | plan (R_pt freeze), verification |

**Missing or weak anchors:** None that block this phase. Two notes: (1) The exact engine has **no standalone det_3/Tr/polarize_d** — these are derivable from material already on disk (the inlined T3 formula + the `octonion_algebra.py` body), so this is a gap to *fill by porting*, not a missing anchor. (2) The exact `polarize_d`'s `d(X,X,X) == 6·det_3` lock was previously VERIFIED only in float64 (`octonion_algebra.py:2299`, "max rel err 1.4e-13"); Phase 64 must re-establish it **exactly over Q** — that is the headline convention lock, not a re-confirmation.

## Conventions

These are the BINDING conventions for the milestone (from `.gpd/research/SUMMARY.md` "Unified Notation"). Phase 64 freezes them in the new module header and verifies the ones marked "lock".

| Choice | Convention | Alternatives (rejected) | Source |
| ------ | ---------- | ----------------------- | ------ |
| Arithmetic field | Exact over **Q** (and Q-adjoin-surds) | float64 (FORBIDDEN on decisive path) | R2 / PITFALLS Pitfall 3 |
| Rank operator | `sympy.Matrix.rank()` over Q | `numpy.linalg.matrix_rank` (FORBIDDEN) | R2 / PITFALLS Pitfall 3 |
| Group | F_4 = Aut(h_3(O)) (compact, 52-dim; fixes Tr, trace form, det) | E_6 = Stab(det) (WRONG group; lacks c-invariance) | SUMMARY |
| F_4-rep on the 27 | 27 = 1 (trivial/Tr direction) ⊕ 26 (trace-free irreducible) | treating 27 as irreducible | SUMMARY / PITFALLS Pitfall 9 |
| Octonion mult | Fano `e_1 e_2 = e_4` (FANO_TRIPLES); `e_i e_i = -1` | other Fano orientations | `embedding...py:93-116` |
| Jordan product | **X∘Y = ½(XY + YX)** (the ½ is load-bearing) | matrix product XY (off-by-½ in c) | `embedding...py:280` |
| Trace Tr X | α + β + γ (degree 1) | — | `embedding...py:571` (T1) |
| Quadratic trace Tr X^2 | Tr(X∘X) (degree 2) | "Tr(X)^2" (a DIFFERENT invariant) | `embedding...py` T1/jordan |
| Cubic norm det X = N(X) | LEFT-assoc cross term `2·Re((x1·x2)·x3)`; det(diag(a,b,c))=abc; det(I)=1 | right-assoc cross term; naive octonionic "det" | `embedding...py:573-576`, `octonion_algebra.py:2152` |
| Polarization d(X,Y,Z) | `N(X+Y+Z) − N(X+Y) − N(X+Z) − N(Y+Z) + N(X)+N(Y)+N(Z)`; **locked d(X,X,X) = 6·det X** | `polarized_sharp` / Freudenthal × (sharp-vs-d trap) | `octonion_algebra.py:2184` |
| Coupling c(X,Y) | **c = Tr(X∘Y)**, bidegree (1,1); c(X,X) = Tr X^2 | Tr(XY) without ½; −Tr(X∘Y) | SUMMARY |
| R_pt (pointwise subring) | R-subalgebra generated by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y} = R[..X] ⊗ R[..Y]; FROZEN | "{Tr X, Tr Y} only"; "any smooth-function closure" | PITFALLS Pitfall 7 |

**CRITICAL: All equations below use these conventions.** The single non-negotiable: exact over Q, ranks via `sympy.Matrix.rank()`, never floats on any decisive path. The Jordan ½ and the left-association of the cubic cross term are the two most error-prone choices — both are already fixed in the warm engine and must be carried verbatim.

Convention loading: see agent-infrastructure.md Convention Loading Protocol. The new module MUST carry an `# ASSERT_CONVENTION:` header line (matching the `embedding...py:31-35` pattern) recording: `jordan=½(AB+BA); fano e1e2=e4; det3 left-assoc Re((x1x2)x3); det3_normalization d(X,X,X)=6·det_3; arithmetic=exact-SymPy-over-Q; NEVER float64 on decisive path`.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name / Description | Source | Role in This Phase |
| -------- | ------------------ | ------ | ------------------ |
| `(AB)_{ij} = Σ_k A_{ik} B_{kj}` (octonionic, non-associative) | 3×3 octonion matmul | `embedding...py:262` `h3o_matmul` | base op; reuse as-is |
| `X∘Y = ½(h3o_matmul(X,Y) + h3o_matmul(Y,X))` | Jordan product | `embedding...py:280` `jordan` | base op; reuse as-is |
| `Tr X = α + β + γ` | linear trace (T1) | `embedding...py:571` (inside `reduced_charpoly_roots`) | LIFT into standalone `Tr(X)` |
| `Tr X^2 = Tr(X∘X)` | quadratic trace | derive from `jordan` + `Tr` | NEW standalone `Tr2(X)` |
| `det X = αβγ − α·\|x1\|^2 − β·\|x2\|^2 − γ·\|x3\|^2 + 2·Re((x1·x2)·x3)` | cubic norm (T3); LEFT-assoc | `embedding...py:573-576`; `octonion_algebra.py:2152` | LIFT T3 into standalone `det_3(X)` |
| `d(X,Y,Z) = N(X+Y+Z) − N(X+Y) − N(X+Z) − N(Y+Z) + N(X)+N(Y)+N(Z)` | full polarization of det_3 | `octonion_algebra.py:2184` | RE-PORT `polarize_d` body onto exact `det_3` |
| `c(X,Y) = Tr(X∘Y)` | coupling generator (1,1) | SUMMARY | NEW; from `Tr`+`jordan` |
| `R[h_3(O)]^{F_4} = R[Tr, Tr^2, det]`, trdeg 3, degrees 1/2/3 | single-state ("Observable") ring | Faraut-Korányi Ch. II-IV (Thm IV.2.5); Springer | CITE (Success Criterion 3) |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Exact octonion 8-tuple arithmetic over Q | non-associative multiplication via Fano table | every algebra op | `embedding...py` (verified) |
| Coordinate ↔ 3×3-matrix bijection | maps (α,β,γ,x1,x2,x3) to/from the Hermitian octonion matrix | the 54-symbol layout, all invariants | `embedding...py:213,551` |
| Symbolic-then-substitute evaluation | build expression symbolically, substitute rational point, then evaluate/rank | convention-lock checks at a random rational point | `COMPUTATIONAL.md` |
| Assert-based PASS/FAIL harness | `_report`/`ALL_PASS`/`sys.exit(0/1)`, no pytest | module structure | `slice_clause_iii_verification.py` |

### Approximation Schemes

None. This phase is exact-symbolic over Q end to end. There is no small parameter, no truncation, no convergence — only correctness of the port and the convention locks. Any appearance of float64 on the decisive path is a defect, not an approximation.

## Standard Approaches

### Approach 1: Import-the-exact-block + lift-the-missing-functions (RECOMMENDED)

**What:** Reuse the verified exact-SymPy octonion/h_3(O) block from `embedding_under_E_verification.py`, then add the four standalone functions it is missing (`Tr`, `Tr2`, `det_3`, `polarize_d`), the 54-symbol pair layout, and the seven invariants.

**Why standard:** The contract says "importing/porting the exact-SymPy octonion block." The engine is already verified (it underpins the v15.0 Phase 62 result). Reusing it eliminates the dominant risk (convention drift in octonion multiplication, Jordan ½, det left-association). The four additions are mechanical lifts of formulas already on disk.

**Key steps (concrete, ready to encode):**

1. **Import or copy the exact octonion + matmul + jordan block.** From `embedding_under_E_verification.py`: `FANO_TRIPLES`, `_MUL_TABLE`, `oct_zero/oct/oct_real/oct_add/oct_sub/oct_neg/oct_scal/oct_mul/oct_conj/oct_is_zero/oct_equal`, `_oct_normsq`, `h3o_from_coords`, `h3o_identity`, `octmat_*`, `h3o_matmul`, `jordan`, `_coord_from_octmat`. RECOMMENDATION: prefer a clean `from code.embedding_under_E_verification import ...` if import hygiene allows; otherwise copy the block verbatim with a provenance header (`# Ported verbatim from code/embedding_under_E_verification.py §1-2`). Either satisfies "importing/porting." Copy is acceptable and arguably safer (decouples from a file whose primary purpose was Phase 62).
2. **Lift `det_3` out of `reduced_charpoly_roots`.** The T3 term (`embedding...py:573-576`) IS det_3:
   ```python
   def det_3(X):
       a, b, g, x1, x2, x3 = _coord_from_octmat(X)
       n1, n2, n3 = _oct_normsq(x1), _oct_normsq(x2), _oct_normsq(x3)
       cross = oct_mul(oct_mul(x1, x2), x3)   # LEFT-assoc: (x1 x2) x3
       return a*b*g - a*n1 - b*n2 - g*n3 + 2*cross[0]
   ```
   (Cross-check vs `octonion_algebra.py:2152` body — identical formula, left-association preserved.)
3. **Add `Tr` and `Tr2`.** `Tr(X) = X[0][0][0] + X[1][1][0] + X[2][2][0]` (= α+β+γ, the T1 term). `Tr2(X) = Tr(jordan(X, X))`.
4. **Re-port `polarize_d`.** Copy the `octonion_algebra.py:2184` body verbatim, calling the exact `det_3` and exact octmat `+`:
   ```python
   def polarize_d(X, Y, Z):
       XpY, XpZ, YpZ = octmat_add(X, Y), octmat_add(X, Z), octmat_add(Y, Z)
       XpYpZ = octmat_add(XpY, Z)
       return (det_3(XpYpZ) - det_3(XpY) - det_3(XpZ) - det_3(YpZ)
               + det_3(X) + det_3(Y) + det_3(Z))
   ```
5. **Build the 54-symbol pair layout** (see Mathematical Framework / the dedicated section below).
6. **Build the seven base invariants** as SymPy expressions on the layout.
7. **Freeze R_pt** (documented predicate; see R_pt section).
8. **Verify the five convention locks** exactly over Q via the assert harness.

**Known difficulties at each step:**

- Step 2/4: SymPy expression swell. `det_3` of a fully symbolic 54-variable matrix is a degree-3 polynomial with octonion cross-terms; `polarize_d` triples that. For the *convention locks*, this is fine — evaluate at concrete rational/symbolic test elements (diag(a,b,c), I, a single generic X), not the full 54-symbol X. Substitute the point FIRST when checking numeric locks. (For Phase 64 the locks use small explicit elements, so swell is a non-issue; the swell warning is mainly for downstream Jacobian phases.)
- Step 1: if importing, beware that `embedding_under_E_verification.py` runs its `main()` at import unless guarded by `if __name__ == "__main__":` — verify it is guarded (it defines `main()` at line 1051; confirm the module body does not execute self-checks on import) or prefer the copy route.
- Step 3: `Tr2 = Tr(jordan(X,X))` not `Tr(h3o_matmul(X,X))` — they agree for Hermitian X (the ½(XX+XX)=XX), but use `jordan` for convention consistency and to keep the c(X,X)=Tr2 lock manifest.

### Approach 2: Copy-verbatim-block instead of import (acceptable variant, not a fallback)

**What:** Identical to Approach 1 but physically copies the exact octonion block into `ring_lemma_verification.py` rather than importing it.
**When to prefer:** If `embedding_under_E_verification.py` is not import-safe (runs work at import), or to make `ring_lemma_verification.py` a self-contained decisive artifact (the survey's stated preference: "keep the executor self-contained"). This is a style choice, not a degradation — both are exact and both satisfy the contract.
**Tradeoffs:** Copy duplicates ~150 lines but decouples from a Phase-62 file; import is DRY but couples. Recommend copy for the decisive module (matches the `slice_clause_iii_verification.py` self-contained precedent).

### Anti-Patterns to Avoid

- **Calling any `octonion_algebra.py` function on the decisive path.** It is float64 (399 numpy sites, 0 sympy). Use it ONLY as a formula spec to read. *Example:* `from octonion_algebra import det_3` would silently put float64 on the path — the exact-only guard (Success Criterion 4) must forbid this import.
- **Re-deriving octonion arithmetic from scratch.** Risks Fano-sign / Jordan-½ / det-left-association drift. Reuse the verified exact block. *Example:* hand-writing a new multiplication table with `e_1 e_2 = e_3` (wrong orientation) would silently break det_3 and every invariant.
- **Defining `Tr2` as `Tr(X)**2`.** `Tr(X^2) = Tr(X∘X)` is a genuinely different invariant from `(Tr X)^2`. Both are degree-2 and both live in R_pt, but they are distinct generators/members. The base invariant is `Tr(X∘X)`.
- **Using `_polarized_sharp` / Freudenthal cross `X×Y` instead of `polarize_d`.** The sharp-vs-d trap (PITFALLS convention table). `polarize_d` is the trilinear locked to `6·det`; the sharp polarization differs by trace-term shifts. Pick `polarize_d` and document it.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE — CITE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Single-state ("Observable") invariant ring | R[h_3(O)]^{F_4} = R[Tr, Tr^2, det]; trdeg 3; generator degrees 1, 2, 3 | Faraut-Korányi Ch. II-IV (Thm IV.2.5 region); Springer 1962/1973 | CITE for Success Criterion 3; this IS the "Observable" ring = the pointwise single-copy subring R[Tr_X, Tr_X^2, det_X] |
| Uniqueness of the cubic norm | det_3 = N is the unique (up to scale) F_4-invariant cubic; det(diag(a,b,c))=abc, det(I)=1 | Springer, Indag. Math. 24 (1962) 259-265 | CITE as the det_3 anchor; justifies the lock det(diag)=abc |
| Polarization normalization | d(X,X,X) = 6·det X; det(aX+bY) = a^3 det X + (a^2 b/2) f(X,X,Y) + (ab^2/2) f(X,Y,Y) + b^3 det Y | Blind 2011 §3; Springer 1973 | the locked normalization; the (2,1)/(1,2) mixed cubics are downstream (Phase 68/69), not this phase |
| Octonion engine correctness | e_1·e_2 = e_4 (Fano); det_3(diag(a,b,c))=abc; det_3(I)=1; nonassociativity (e1·e2)·e3 ≠ e1·(e2·e3) | `embedding...py` / `octonion_algebra.py` headers (VERIFIED) | reproduce these EXACTLY over Q as port-correctness benchmarks |

**Key insight:** The single-state ring fact is the entire content of Success Criterion 3 and it is a *citation*, not a computation. Do NOT attempt to re-derive R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] in Phase 64 (that is established 1962-1994 mathematics). The phase's job is to *state* it correctly, with the corrected citation (II-IV, not V), and to *identify* the "Observable" ring of the Chalmers-gap framing with this exact pointwise single-copy subring. The Faraut-Korányi attribution correction is HIGH-confidence and verified twice (the project survey + this session's TOC check).

### Useful Intermediate Results (the port spec, already on disk)

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| Inlined T1/T2/T3 in `reduced_charpoly_roots` | Tr (=T1) and det_3 (=T3) formulas, exact over Q | `embedding...py:567-580` | lift T1→Tr, T3→det_3 |
| Standalone `det_3` body | the canonical cubic-norm formula (float, but the FORMULA is the spec) | `octonion_algebra.py:2152` | re-port to exact (already matches the inlined T3) |
| Standalone `polarize_d` body | the 3-arg full polarization formula | `octonion_algebra.py:2184` | re-port verbatim onto exact det_3 |
| Coordinate↔matrix maps | `h3o_from_coords` (build) and `_coord_from_octmat` (recover) | `embedding...py:213,551` | the exact layout; reuse as-is |
| Assert harness skeleton | `_report`/`ALL_PASS`/`sys.exit` | `slice_clause_iii_verification.py`, `embedding...py:77` | reuse verbatim |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| *Analysis on Symmetric Cones*, Ch. II-IV | Faraut, Korányi | 1994 | the single-state ring R[Tr,Tr^2,det] (Observable ring) | the citation + the corrected chapter (II-IV, Thm IV.2.5; NOT Ch. V = conical/spherical polynomials) |
| *Jordan Algebras and Algebraic Groups* | Springer | 1973 | cubic norm structure, F_4 = Aut, det normalization | det_3 / cubic-norm anchor |
| Cubic norm uniqueness, Indag. Math. 24 | Springer | 1962 | uniqueness of the cubic norm on h_3(O) | the det_3 reference (harness already cites it) |

## Computational Tools

### Core Tools

| Tool | Version / Module | Purpose | Why Standard |
| ---- | ---------------- | ------- | ------------ |
| **SymPy** | **1.14.0** (verified present) | exact arithmetic over Q: octonion/h_3(O) algebra, det_3, Tr, polarize_d, all the convention-lock checks | exact, tolerance-free; the entire decisive path runs here |
| **Python** | 3.x (3.14.2 per engine header) | runs the assert harness | — |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| **NumPy** | 2.4.2 (present) | NONE on the decisive path | only for non-decisive scaffolding (random rational generation is better done with `sympy.Rational`); its presence is the thing the exact-only guard polices |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| import exact block | copy exact block verbatim | DRY vs self-contained (recommend copy for the decisive module) |
| `sympy.Rational` random point | `numpy` random + cast | numpy cast reintroduces float risk; use Rational |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| Port + the four standalone fns | dev-minutes; < 1 s runtime | none | — |
| Five convention locks over Q (on small explicit elements) | seconds total | none (small elements, not the 54-symbol matrix) | use explicit diag(a,b,c)/I/single generic X, not full symbolic X |
| Building the 54 symbols + 7 invariants as expressions | seconds (construction); do NOT `simplify()` the full det_3 in 54 vars eagerly | SymPy swell IF eagerly expanded | construct lazily; substitution/expansion is a DOWNSTREAM (Phase 66+) concern, not Phase 64 |

**Installation / Setup:** Nothing to install — SymPy 1.14.0 + NumPy 2.4.2 are present. No Sage/GAP/Singular needed for this phase (those are a Phase-68 (a)-completeness concern only).
```bash
python3 -c "import sympy; print(sympy.__version__)"   # expect 1.14.0
python3 code/ring_lemma_verification.py               # assert harness; exits 0 on all-pass
```

## Validation Strategies

### Internal Consistency Checks (the five convention locks — Success Criterion 1)

All exact over Q. These are the deliverable of the phase's verification.

| Lock | What It Validates | How to Perform (exact over Q) | Expected Result |
| ---- | ----------------- | ----------------------------- | --------------- |
| `polarize_d(X,X,X) == 6*det_3(X)` | the cubic-norm polarization normalization (THE headline lock) | pick a generic rational X (e.g. `generic_ambient_element()` from the engine, or diag(2,3,5) with rational octonion off-diagonals); assert `simplify(polarize_d(X,X,X) - 6*det_3(X)) == 0` | exact 0 |
| `c(X,X) == Tr(X^2)` | the coupling reduces to the quadratic trace on the diagonal | with `c(X,Y) := Tr(jordan(X,Y))`, assert `simplify(c(X,X) - Tr2(X)) == 0` | exact 0 |
| octonion table `e1*e2 == e4` (Fano) | octonion multiplication orientation; cross-check vs Paper 7's table | `oct_mul(oct with comp1=1, oct with comp2=1)` has comp4 == 1, all else 0; cross-check the FANO_TRIPLES list matches `octonion_algebra.py` and Paper 7 | e_4 exactly |
| `det_3(diag(a,b,c)) == a*b*c` | cubic-norm diagonal normalization | symbolic a,b,c: assert `simplify(det_3(h3o_from_coords(a,b,c,0,0,0)) - a*b*c) == 0` | exact `a*b*c` |
| `det_3(I) == 1` | identity normalization | assert `det_3(h3o_identity()) == 1` | exact 1 |

### Known Limits and Benchmarks (port-correctness, from the engine headers)

| Benchmark | Regime | Known Result | Source |
| --------- | ------ | ------------ | ------ |
| Octonion nonassociativity | generic triple | `(e1·e2)·e3 ≠ e1·(e2·e3)` (associator nonzero) | `embedding...py` associator checks |
| det_3 of a rank-deficient element | `det_3(E_ii)` (single diagonal idempotent) | 0 | `octonion_algebra.py:2296` |
| Hermitian Jordan = matrix square | `jordan(X,X)` vs `h3o_matmul(X,X)` for Hermitian X | equal (½(XX+XX)=XX) | convention sanity |

### Numerical Validation

Not applicable in the float sense. The "numerical" validation is exact: every lock is a `simplify(...) == 0` or `== <exact value>` over Q. There is no tolerance anywhere.

### Red Flags During Computation

- Any `simplify(polarize_d(X,X,X) - 6*det_3(X))` that is **nonzero** → STOP (per contract Backtracking). This is a port error (wrong det_3 left-association, wrong polarize_d sign pattern, or a Jordan-½ slip), NOT a new result. Reconcile against the engine header before building anything downstream.
- `det_3(diag(a,b,c)) ≠ a*b*c` → the cubic-norm diagonal term is wrong (likely a sign on the quadratic correction).
- `det_3(I) ≠ 1` → identity/normalization error.
- `e1*e2 ≠ e4` → the Fano table was transcribed with the wrong orientation; cross-check against Paper 7 and `octonion_algebra.py`.
- A passing run that turns out to have imported anything from `octonion_algebra` → the exact-only guard failed; the result is float-contaminated even if the locks "passed."

## Common Pitfalls

### Pitfall 1: float64 contamination on the decisive path (the survey's Reconciliation 2)

**What goes wrong:** `octonion_algebra.py` is float64. If the new module imports any of its functions (`det_3`, `polarize_d`, `jordan`, ...), the decisive path silently runs in floats, and downstream rank verdicts (Phases 65-67) become tolerance artifacts.
**Why it happens:** The spawn-context and an earlier METHODS draft mislabeled `octonion_algebra.py` as the "warm exact-SymPy harness." It is NOT (verified: 399 numpy / 0 sympy). The exact engine is `embedding_under_E_verification.py`.
**How to avoid:** Port FROM `embedding_under_E_verification.py` (exact) using `octonion_algebra.py` only as a read-only formula spec. Implement the exact-only guard (Success Criterion 4): assert no `numpy.linalg.matrix_rank` and no float arithmetic is reachable from any rank-bearing path; a static grep/import check is sufficient at this phase (no ranks are computed yet, but the guard must be in place for downstream reuse).
**Warning signs:** `import numpy` used for anything beyond non-decisive scaffolding; any `from octonion_algebra import ...`.
**Recovery:** Remove the offending import; re-port the formula body to exact SymPy.

### Pitfall 2: R_pt definitional drift (PITFALLS Pitfall 7)

**What goes wrong:** "Pointwise"/"reducible" gets used loosely so c trivially lands in or out of R_pt. If R_pt is silently read as "{Tr X, Tr Y} only," c is trivially "not pointwise"; if stretched to arbitrary closures, c can be argued either way.
**Why it happens:** The narrative words "pointwise," "single-frame Observable," "reducible" are loose without a frozen algebraic definition.
**How to avoid:** Freeze ONE definition in Phase 64 and document it as the predicate used identically by Phases 66/67/68: **R_pt := the R-subalgebra of R[27⊕27]^{F_4} generated by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}** = R[Tr_X, Tr_X^2, det_X] ⊗ R[Tr_Y, Tr_Y^2, det_Y]. Record explicitly: Tr(X)·Tr(Y) ∈ R_pt (a product of two single-state generators); claim (b) is precisely "c ∉ R_pt."
**Warning signs:** the membership predicate differs between phases; "pointwise" used without pointing back to the six-generator definition.
**Recovery:** restore the frozen definition; re-audit any phase that used a different one.

### Pitfall 3: convention traps — Jordan ½, det left-association, sharp-vs-d (PITFALLS convention table)

**What goes wrong:** (a) Using XY where X∘Y=½(XY+YX) is meant → off-by-½ in c and Tr2. (b) Right-associating the cubic cross term `2·Re(x1·(x2·x3))` instead of left `2·Re((x1·x2)·x3)` → wrong det_3 (octonions are non-associative, so this genuinely differs). (c) Using the Freudenthal/sharp cross `X×Y` instead of `polarize_d` → a trilinear that differs from the `6·det`-locked one.
**Why it happens:** All three are silent: the code runs, the numbers are just wrong.
**How to avoid:** Reuse the engine's `jordan` (has the ½) and the inlined det_3 (has the left-association `oct_mul(oct_mul(x1,x2),x3)`). Pick `polarize_d`, never `_polarized_sharp`. The five convention locks catch (a) [via c(X,X)=Tr2] and (b)/(c) [via d(X,X,X)=6·det and det(diag)=abc].
**Warning signs:** any lock fails (see Red Flags).
**Recovery:** re-pin the convention; re-verify all five locks; propagate the fix.

### Pitfall 4: confusing the 27 with the 26; Tr2 vs (Tr)^2 (PITFALLS Pitfall 9, partial)

**What goes wrong:** Treating the 27 as irreducible (it is 27 = 1 ⊕ 26), or conflating Tr(X^2)=Tr(X∘X) with (Tr X)^2.
**Why it happens:** physics-side prose uses "the 27" and "the 26" interchangeably; the trivial Tr direction is easy to drop.
**How to avoid:** This phase only needs to (i) build Tr2 = Tr(X∘X) correctly (NOT (Tr X)^2) and (ii) document 27 = 1 ⊕ 26 in the header for downstream (c). The full Sym^2 branching is a Phase-67 concern.
**Warning signs:** Tr2 coded as `Tr(X)**2`; the header omits 27 = 1 ⊕ 26.
**Recovery:** fix the definition; re-state.

## Level of Rigor

**Required for this phase:** Exact symbolic verification over Q (the strongest computational rigor; BASE-01 validation profile = "Exact (symbolic over Q)"). The single-state-ring claim is a *literature citation* (no computation needed — it is established mathematics).

**Justification:** This is a foundation-freeze phase. Every downstream decisive verdict (orbit dimension, c-independence, c-uniqueness) inherits these objects and conventions verbatim. A convention error here silently corrupts all of Phases 65-69. Exact-over-Q is non-negotiable because rank (the downstream decisive quantity) is discontinuous and float-fragile.

**What this means concretely:**
- All five convention locks must pass as exact equalities (`simplify(...) == 0` or `== <exact value>`) over Q — no tolerances, no floats.
- The single-state ring is *stated with a citation* (Faraut-Korányi II-IV, Thm IV.2.5; Springer), NOT re-derived; the citation correction (II-IV not V) is recorded.
- The R_pt definition is *frozen and documented* as a predicate, not just described in prose.
- The exact-only guard is *in place* (even though no ranks run yet) so downstream phases inherit the float-free guarantee.
- The module runs as an assert-based harness exiting nonzero on any lock failure (the `embedding...py`/`slice_clause_iii` pattern).

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| "reuse the warm `octonion_algebra.py` exact harness" (spawn-context / early METHODS) | use `embedding_under_E_verification.py` (the actual exact engine); `octonion_algebra.py` is float64 reference only | Reconciliation 2 (2026-05-24, verified) | the port source and the exact-only guard both hinge on this; getting it wrong float-contaminates the milestone |
| cite "Faraut-Korányi Ch. V" for the single-state ring | cite Ch. II-IV (Thm IV.2.5 region) | survey citation correction (verified this session: Ch. V = conical/spherical polynomials) | the contract requires recording this correction |

**Superseded approaches to avoid:**
- `octonion_algebra.py` on the decisive path: superseded by the exact engine; people still reach for it because the spawn-context mislabeled it. Use it only to *read* formula bodies.

## Open Questions

1. **Import vs copy of the exact octonion block**
   - What we know: both satisfy "importing/porting"; the engine defines `main()` (line 1051) so import-safety depends on a `__name__` guard.
   - What's unclear: whether `embedding_under_E_verification.py` executes work at import (planner should have the executor check, or just copy).
   - Impact: trivial — both routes are exact and contract-compliant.
   - Recommendation: COPY the block verbatim with a provenance header (matches the self-contained `slice_clause_iii` precedent; decouples the decisive module from a Phase-62 file). If import is chosen, confirm the `__name__ == "__main__"` guard first.

2. **Exact `d(X,X,X) == 6·det_3` was only float-verified before**
   - What we know: `octonion_algebra.py:2299` recorded it at float tolerance 1.4e-13; the exact engine never exposed a standalone `polarize_d`.
   - What's unclear: nothing fundamental — it is expected to hold exactly; this phase establishes it over Q for the first time.
   - Impact: it is THE headline lock; if it fails exactly, it is a port error (per Backtracking).
   - Recommendation: make this the first lock the harness runs; treat failure as a hard stop.

3. **27-symbol basis choice for the layout (standard-basis vs Peirce-adapted)**
   - What we know: the survey suggests `E_i = peirce_basis_27()` OR "the simpler standard basis"; the *coordinate* layout (α,β,γ,x1,x2,x3) is the engine's native one.
   - What's unclear: whether downstream (Phase 65 f_4 build) prefers the Peirce-adapted basis (the Spin(9) route uses Peirce sectors).
   - Impact: low for Phase 64 (the seven invariants are basis-agnostic functions of the coordinates); matters more for the f_4 generators in Phase 65.
   - Recommendation: use the **engine-native coordinate layout** (α,β,γ + 3 octonions = 3 + 24 = 27) for the 54 symbols; this is unambiguous and matches `h3o_from_coords`. Defer any Peirce-adapted re-coordinatization to Phase 65 if needed. (See the 54-symbol section.)

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| import the exact block | engine not import-safe | copy the block verbatim | minutes (the recommended route anyway) |
| `d(X,X,X)==6·det_3` lock fails | port error in det_3 or polarize_d | re-derive det_3 from the inlined T3 char-recipe; re-check left-association of `oct_mul(oct_mul(x1,x2),x3)`; re-check polarize_d sign pattern vs `octonion_algebra.py:2184` | LOW (per Backtracking: STOP, reconcile against header) |
| ported engine disagrees with v15.0 harness benchmarks | port error | treat as port error, NOT a new result; diff against `embedding...py` line by line | LOW-MEDIUM |

**Decision criteria:** Any convention lock failing → STOP and reconcile against the harness header before building anything (contract Backtracking, verbatim). Never "tune" a lock to pass.

## The 54-Symbol Pair Coordinatization (phase-specific spec for the planner)

The pair (X, Y) ∈ h_3(O) ⊕ h_3(O) is coordinatized by 54 SymPy symbols, 27 per copy, on the engine-native layout.

**Symbol declaration:**
```python
import sympy as sp
xs = sp.symbols('x0:27', real=True)   # x0..x26  for X
ys = sp.symbols('y0:27', real=True)   # y0..y26  for Y
```

**Coordinate → matrix map (engine-native, unambiguous).** The 27 real coordinates per copy split as 3 diagonal reals + 3 octonions × 8 components = 3 + 24 = 27. The canonical, layout-matching assignment:

| Coord indices | Object | Matrix role (from `h3o_from_coords`, `embedding...py:213`) |
| ------------- | ------ | --------------------------------------------------------- |
| x0, x1, x2 | α, β, γ (diagonal reals) | X[0][0]=α, X[1][1]=β, X[2][2]=γ |
| x3..x10 (8 comps) | octonion **x1** | X[2][1] = x1; X[1][2] = conj(x1) |
| x11..x18 (8 comps) | octonion **x2** | X[0][2] = x2; X[2][0] = conj(x2) |
| x19..x26 (8 comps) | octonion **x3** | X[1][0] = x3; X[0][1] = conj(x3) |

Concretely, the symbolic constructor:
```python
def X_from_symbols(s):   # s = xs (27-tuple) or ys
    alpha, beta, gamma = s[0], s[1], s[2]
    x1 = [s[3+k]  for k in range(8)]   # octonion x1 as an 8-list of symbols
    x2 = [s[11+k] for k in range(8)]
    x3 = [s[19+k] for k in range(8)]
    return h3o_from_coords(alpha, beta, gamma, x1, x2, x3)
```
This map is exact and matches the engine's `_coord_from_octmat` recovery (`x3 = X[1][0], x2 = X[0][2], x1 = X[2][1]`). The planner should pin this table verbatim so X and Y use *identical* conventions (the contract's "everything downstream uses these objects identically").

**Note on basis choice:** This uses the engine-native coordinate basis, NOT the Peirce-adapted `peirce_basis_27()`. The seven invariants are functions of the coordinates and are basis-agnostic, so this is the simplest unambiguous choice for Phase 64. If Phase 65's f_4 construction prefers the Peirce-adapted basis (Spin(9) sectors), the change-of-basis is a Phase-65 concern and does not affect the invariants frozen here.

## The Seven Base Invariants (phase-specific spec)

On the 54-symbol layout, with `X = X_from_symbols(xs)`, `Y = X_from_symbols(ys)`:

| # | Invariant | SymPy expression | Degree (in X / in Y) | Bidegree |
| - | --------- | ---------------- | -------------------- | -------- |
| 1 | Tr X | `Tr(X)` = x0 + x1_coord + x2_coord (the α+β+γ = `xs[0]+xs[1]+xs[2]`) | 1 / 0 | (1,0) |
| 2 | Tr X^2 | `Tr2(X)` = `Tr(jordan(X, X))` | 2 / 0 | (2,0) |
| 3 | det X | `det_3(X)` | 3 / 0 | (3,0) |
| 4 | Tr Y | `Tr(Y)` = `ys[0]+ys[1]+ys[2]` | 0 / 1 | (0,1) |
| 5 | Tr Y^2 | `Tr2(Y)` = `Tr(jordan(Y, Y))` | 0 / 2 | (0,2) |
| 6 | det Y | `det_3(Y)` | 0 / 3 | (0,3) |
| 7 | c = Tr(X∘Y) | `Tr(jordan(X, Y))` | 1 / 1 | (1,1) |

- Invariants 1-6 are the **pointwise** generators (three per copy); their R-subalgebra is R_pt.
- Invariant 7, c, is the **coupling**; bidegree (1,1); c(X,X) = Tr X^2 (a convention lock). c is the object whose independence from R_pt is the milestone spine (Phase 66).
- Degrees match the single-state ring generator degrees (1, 2, 3) per copy, consistent with R[h_3(O)]^{F_4} = R[Tr, Tr^2, det], trdeg 3.

The planner should have the executor build these as SymPy expressions but **not** eagerly `expand()`/`simplify()` the degree-3 ones in 54 variables (swell). They are stored as expression objects; substitution/expansion is a downstream (Phase 66+) operation.

## R_pt Freezing (phase-specific spec)

**Frozen definition (document verbatim in the module and in the phase output):**

> **R_pt := the R-subalgebra of R[h_3(O) ⊕ h_3(O)]^{F_4} generated by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}**, i.e. all polynomials (sums of products) in the six single-state generators. Equivalently, **R_pt = R[Tr X, Tr X^2, det X] ⊗ R[Tr Y, Tr Y^2, det Y]**.

**Required documented consequences (to pre-empt Pitfall 7 drift):**
- `Tr(X)·Tr(Y) ∈ R_pt` — it is a product of two single-state generators (the reducible (1,1) member). RECORD this explicitly.
- Claim (b) is precisely **"c ∉ R_pt"** — c is not a polynomial in the six. RECORD this phrasing.
- "c is new" therefore means "new **modulo products** + pointwise terms" — the precise uniqueness statement is a Phase-67 concern (there are TWO bidegree-(1,1) invariants: Tr(X)Tr(Y) ∈ R_pt and c; the genuine-coupling quotient is 1-dim).

**How to document the freeze (anti-drift):** write the definition once, as a module docstring/constant and in the phase's RESEARCH/PLAN output, and have Phases 66/67/68 *cite this exact text* rather than re-phrase. The membership predicate `is_in_Rpt(p)` (used in Phase 66) must reference this six-generator definition; the test that `Tr(X)Tr(Y)` is IN and that the predicate is identical across phases is the anti-drift guard (PITFALLS Pitfall 7 detection test).

## Exact-Only Guard (Success Criterion 4, phase-specific spec)

The new module must import the SymPy octonion block and a guard must confirm no float / `numpy.linalg.matrix_rank` path is reachable from rank computations. For Phase 64 (no ranks computed yet) the guard is structural and forward-looking:

**Implementation options (planner picks; all cheap):**
1. **Import hygiene assert:** no `from octonion_algebra import ...` anywhere; `numpy` either not imported at all on the decisive path, or imported only for clearly non-decisive scaffolding with a comment. A unit-test/grep in the harness can assert `numpy.linalg` is not referenced.
2. **Module-level grep guard:** a small self-check that scans the module's own source for forbidden tokens (`numpy.linalg.matrix_rank`, `np.linalg.matrix_rank`, `from octonion_algebra`) and asserts none are present on the decisive path.
3. **Rank-routing convention (forward-looking):** document that ALL ranks (downstream) go through `sympy.Matrix(...).rank()` over Q; the guard asserts no float matrix is ever passed to a rank-bearing function.

**Recommended:** Option 1 + a one-line grep self-check (Option 2) in the harness. Keep `numpy` out of the decisive module entirely if possible (use `sympy.Rational` for any random rational points downstream). The guard's *presence* in Phase 64 is what lets Phases 65-67 inherit the float-free guarantee — that is why Success Criterion 4 is in the foundation phase even though Phase 64 computes no ranks.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that `embedding_under_E_verification.py`'s inlined T3 is *exactly* the standalone `octonion_algebra.py:2152` det_3. I verified both formulas read identically (left-assoc `(x1·x2)·x3`, same sign pattern), but the planner should have the executor cross-check the two by evaluating both on a shared rational element — cheap insurance, and it doubles as a port-correctness benchmark.
2. **Alternative dismissed:** computing the single-state ring R[Tr,Tr^2,det] from scratch (Reynolds/Jacobian on one copy). Dismissed correctly — it is established 1962-1994 mathematics; Success Criterion 3 is a citation, not a computation. Re-deriving it would waste budget and risk an error in something already certain.
3. **Limitation I may be understating:** SymPy expression swell on the 54-symbol det_3. I have said "don't expand eagerly," but if a downstream phase needs the symbolic det_3, the swell is real. For Phase 64 it is a non-issue (locks use small explicit elements), but the planner should not let Phase 64 accidentally trigger a full symbolic expansion of the 54-variable invariants as a "sanity check."
4. **Simpler method I might have overlooked:** none for the port itself — reuse-the-verified-block is the simplest correct route. The only genuine choice is import-vs-copy (a style decision; recommend copy).
5. **Would a specialist disagree?** A computational-invariant-theory specialist might want the Peirce-adapted basis from the start (to align with the Spin(9) f_4 construction in Phase 65). I recommend the engine-native coordinate basis for Phase 64 because the invariants are basis-agnostic and it is unambiguous; the Peirce question is a Phase-65 concern. This is a defensible scoping call, but the planner should flag it to Phase 65 so the basis choice is made deliberately there.

## Sources

### Primary (HIGH confidence)

- **`code/embedding_under_E_verification.py`** (in-repo, verified by inspection this session) — the exact-SymPy octonion/h_3(O) engine: Fano table (`e1e2=e4`), `oct_mul`, `h3o_from_coords`, `h3o_matmul`, `jordan` (½(AB+BA)), `_coord_from_octmat`, `_oct_normsq`, det_3 inlined in `reduced_charpoly_roots:567-580` (T1=Tr, T3=det_3, left-assoc cross term).
- **`code/octonion_algebra.py`** (in-repo, verified by inspection) — float64 reference ONLY; canonical standalone `det_3:2152` and 3-arg `polarize_d:2184` formula bodies (the port spec); the thing to GUARD against on the decisive path (399 numpy / 0 sympy).
- **`code/slice_clause_iii_verification.py`** (in-repo) — the exact-SymPy assert-based `_report`/`ALL_PASS`/`sys.exit` harness pattern (no pytest).
- **Faraut, J.; Korányi, A.**, *Analysis on Symmetric Cones*, Oxford (1994), Ch. II-IV (Thm IV.2.5 region) — single-state ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det], trdeg 3, degrees 1/2/3. Citation correction confirmed: Ch. V is conical/spherical polynomials, NOT the invariant ring (TOC verified this session: II = Euclidean Jordan algebras, III = Peirce, IV = classification, V = conical/spherical polynomials).
- **Springer, T.A.**, *Jordan Algebras and Algebraic Groups*, Ergebnisse 75, Springer (1973); Indag. Math. 24 (1962) 259-265 — cubic norm structure, F_4=Aut, det normalization, uniqueness of the cubic norm (the det_3 anchor).

### Secondary (MEDIUM confidence)

- **`.gpd/research/SUMMARY.md`** (2026-05-24, project survey) — Unified Notation (binding), Reconciliation 2 (exact engine, not float64), Phase 0 (=64) plan, the convention locks.
- **`.gpd/research/COMPUTATIONAL.md`** (2026-05-24) — the port table (reuse vs new layer), the critical correction (`octonion_algebra.py` is float64), the 54-symbol layout sketch, the polarize_d convention lock.
- **`.gpd/research/PITFALLS.md`** (2026-05-24) — Pitfall 7 (frozen R_pt), the convention traps table (Jordan ½, det normalization, sharp-vs-d), the Faraut-Korányi chapter correction.
- **Blind, B.**, *J. Lie Theory* 21 (2011) 123-144 (arXiv:0906.5525) — polarization normalization `d(X,X,X) = 6 det X` and the det polarization expansion (§3); the E_6 contrast case (NOT the target group).

### Tertiary (LOW confidence)

- Oxford University Press / Google Books TOC for Faraut-Korányi (web, this session) — confirmed the chapter structure (II-IV vs V) but not the exact theorem number IV.2.5 (paywalled; the number comes from BASE-01 + the project survey, MEDIUM confidence on the precise number, HIGH on the chapter range).

## Metadata

**Confidence breakdown:**
- Mathematical framework: HIGH — all formulas are on disk and verified by inspection; the single-state ring is established literature.
- Standard approaches (port mechanics): HIGH — the engine is verified; the four standalone functions are mechanical lifts of on-disk formulas.
- Computational tools: HIGH — SymPy 1.14.0 present; exact-over-Q is deterministic; no external tool needed for this phase.
- Validation strategies (convention locks): HIGH — the five locks are precise, exact, and runnable; the headline `d(X,X,X)=6·det` lock was previously float-verified and is expected to hold exactly.
- Citation precision (Faraut-Korányi Thm IV.2.5): MEDIUM on the exact theorem number, HIGH on the chapter range (II-IV) and the correction (not V).

**Research date:** 2026-05-25
**Valid until:** Stable — these are frozen algebraic conventions and established (1962-1994) invariant-theory facts. The only volatile element is the in-repo engine file paths/line numbers (could shift if the codebase is refactored); the formulas themselves are convention-locked.
