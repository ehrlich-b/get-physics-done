# Computational Approaches: Exact-Arithmetic Verification of the (RING) Lemma — Joint F_4-Invariants of 27 ⊕ 27

**Surveyed:** 2026-05-24
**Domain:** Computational invariant theory / exceptional Jordan algebra h_3(O), F_4 = Aut(h_3(O))
**Confidence:** HIGH (reuse + algorithm design), MEDIUM (Molien-series completeness step, which depends on a SageMath install that is NOT currently present)

> **Scope boundary.** This file covers the computational TOOLS, exact-arithmetic procedures, software, and resource estimates for verifying (RING). The mathematical content of the lemma (what the generators *are*, the proof strategy) lives in METHODS.md / PRIOR-WORK.md.

---

## Recommended Stack (1-paragraph summary)

**Primary engine: exact SymPy over Q (and Q-adjoin-surds), built on TOP of the warm octonion/h_3(O) harness already in this repo.** The decisive parts — (b) Jacobian-rank and the orbit-dimension gate, and (c) degree-2 coupling uniqueness — are *linear-algebra-over-Q at random rational points*: they need `Matrix.rank()` over an exact field, NOT floats. The only step that genuinely benefits from a CAS the repo does not have is (a) the **Molien/Hilbert-series completeness check**, which wants SageMath's `WeylCharacterRing("F4")` (plethysm / `symmetric_power` / `invariant_degree`). SymPy is the workhorse for everything that touches the actual algebra; SageMath is an *optional, isolated* second tool used only to produce the target generating-function degrees. **Do NOT use Singular/Macaulay2/Magma Gröbner-basis invariant-ring machinery on the 54 variables** — it is the anti-approach (see below).

---

## CRITICAL CORRECTION to the spawn context (read first)

The milestone context states a "warm exact-SymPy octonionic harness already exists … `code/octonion_algebra.py`." **This is half-right and the half that is wrong will bite the executor.**

- `code/octonion_algebra.py` (5502 lines) is the **float64 NumPy** harness. Its `jordan_product`, `det_3`, `polarize_d`, `_compute_sharp`, `peirce_basis_27`, `to_vector`/`from_vector`, `_g2_derivation_matrix`, `compute_T_b_matrices`, `rescale_to_clifford_generators` are all `np.float64`. It is the **structural reference** (formulas, Fano table, conventions, VERIFIED-result comments), NOT a drop-in exact engine.
- The **actual warm exact-SymPy harness** is two *other* files that already PORTED the octonion/h_3(O) structure into exact SymPy:
  - `code/embedding_under_E_verification.py` — has exact-SymPy `FANO_TRIPLES`/`_MUL_TABLE` (e1e2=e4), octonion arithmetic on 8-tuples of SymPy `Rational`, the H3O coordinate layout, the `_mat_mul_h3o` M11..M33 entry formulas, `proj_u`, Peirce projectors — all over `Rational`. It explicitly says: *"PORTS the octonion path to EXACT SymPy (the existing infra is float64 NumPy)."*
  - `code/slice_clause_iii_verification.py` — exact-SymPy spectral-sqrt + assert-based `_report`/`ALL_PASS`/`sys.exit` harness pattern (VALD-61-01), no pytest.
  - `code/sp_verification.py`, `code/verify_sequential_product.py` — additional exact-SymPy precedents (`from sympy import Matrix, sqrt, Rational, eye, zeros, simplify`).

**Consequence for the executor (who has SymPy + NumPy only, NO web, NO Sage):** the reuse target is the **exact-SymPy octonion block of `embedding_under_E_verification.py`** plus the **float64 formula bodies of `octonion_algebra.py`** as the spec to re-port. Do NOT reuse the float64 functions on the decisive path — float rank is unreliable (see Anti-Approaches and PITFALLS).

---

## What to reuse vs. what is a thin new layer

| Needed for (RING) | Source (exact provenance) | Status | Action |
|---|---|---|---|
| Octonion mult (e1e2=e4) | `embedding_under_E_verification.py` `FANO_TRIPLES`/`_MUL_TABLE`/`oct_mul` (exact SymPy) | **REUSE as-is** | import/copy the exact block |
| h_3(O) coord layout (α,β,γ,x1,x2,x3) | `octonion_algebra.py` `H3O`; exact mirror in embedding file | **REUSE structure** | port to exact if not already |
| 3×3 octonion matmul `_mat_mul_h3o` M11..M33 | `octonion_algebra.py:290`; exact mirror in embedding file | **REUSE formulas** | exact version exists in embedding file |
| `jordan_product` = (1/2)(AB+BA) | `octonion_algebra.py:374` (float); exact pattern in embedding file | **REUSE formula** | use exact matmul + 0.5 (exact Rational) |
| `det_3` cubic norm (left-assoc (x1*x2)*x3) | `octonion_algebra.py:2152` | **REUSE formula** | re-port to exact SymPy (1 fn) |
| `polarize_d` (d(X,X,X)=6N) | `octonion_algebra.py:2184` | **REUSE formula** | already validated d(X,X,X)=6·det_3 |
| `_compute_sharp` X#, `_polarized_sharp` | `octonion_algebra.py:3858/3876` | **REUSE formula** | for X# / mixed-quadratic checks |
| `_g2_derivation_matrix` (Schafer D=[L,L]+[L,R]+[R,R]) | `octonion_algebra.py:2349` | **REUSE formula** | the 14 g_2 generators, exact |
| `compute_T_b_matrices` → `rescale_to_clifford_generators` (Spin(9) γ_a) | `octonion_algebra.py:661/938` | **REUSE formula** | the 36 grade-2 Spin(9) generators |
| `to_vector`/`from_vector` (R^27) | `octonion_algebra.py:268/276` | **REUSE** | basis of the 27-coordinatization |

**Thin NEW layer the executor must write (small, ~150-300 lines exact SymPy):**

1. **54-real-dim pair coordinatization.** `X = Σ_{i=0}^{26} x_i E_i`, `Y = Σ_{j=0}^{26} y_j E_j` with symbolic `x_i, y_j = symbols('x0:27 y0:27')` and `E_i = peirce_basis_27()` (or the simpler standard basis). A point in 27⊕27 is the 54-tuple `(x_0..x_26, y_0..y_26)`. Provide `pair_from_coords(vec54) -> (H3O_X, H3O_Y)` and a symbolic constructor that returns H3O elements whose entries are SymPy linear forms in the 54 symbols.
2. **The seven base invariants as SymPy expressions** in those 54 symbols: `Tr X, Tr(X∘X), det_3 X, Tr Y, Tr(Y∘Y), det_3 Y, c = Tr(X∘Y)`. (Tr = α+β+γ; Tr(X∘X)=Tr of `jordan_product(X,X)`; det via the exact `det_3`.)
3. **The f_4 = Der(h_3(O)) action operator** `D_ξ` on a pair (see next section) — the genuinely new derivation-builder.
4. **Polarized mixed cubics** f(X,X,Y), f(X,Y,Y) via `polarize_d` (see §6).

---

## The f_4 (52-generator) action — the "do this FIRST" gate

The prior-work scout flagged the **generic orbit dimension** as the gate that fixes the target Krull dimension / transcendence degree, and therefore the *expected* Jacobian rank. Build f_4 = Der(h_3(O)) explicitly, then compute the rank of the infinitesimal-action matrix at a random rational point.

### Building the 52 derivations Der(h_3(O)) = f_4

The cleanest reuse-driven construction (Tits / Schafer; matches what the harness already has):

> **f_4 = g_2 ⊕ (so(3)-traceless part) — concretely, the standard decomposition** Der(h_3(O)) ≅ Der(O) ⊕ {traceless A acting by `[L_A, ·]`}, with the well-known dimension count **14 (g_2) + 26 + 12 = 52**, OR the Spin(9)-adapted **f_4 = so(9) ⊕ Δ_16** (36 + 16 = 52). The repo already has BOTH halves of the Spin(9) route:

- **so(9) part (36 generators):** the grade-2 Clifford bivectors `gammas[a] @ gammas[b]` (a<b) from `rescale_to_clifford_generators(compute_T_b_matrices())` — already used inside `verify_f4_invariance_det3` (octonion_algebra.py:2560-2564). These act on V_{1/2}=R^16 (spinor) and V_0=R^10 (vector) of the Peirce decomposition under E_{11}.
- **the 16 "boost"/Δ_16 generators** complete so(9) to f_4 (f_4/so(9) is the 16-dim spinor; F_4/Spin(9)=OP^2 is the 16-dim Cayley plane — confirmed: the harness comment at octonion_algebra.py:5147 already records "Orbit = OP^2 = F_4/Spin(9), dim = 52 − 36 = 16").

**Recommended construction for the executor (most robust, least bookkeeping):** build the derivation algebra *generatively* and verify it is 52-dimensional, rather than hand-listing a basis.

1. Seed with the **14 g_2 derivations** `_g2_derivation_matrix(i,j)` lifted to act on h_3(O) (acts identically on x1,x2,x3; trivially on the diagonal — exactly the lift used in `verify_f4_invariance_det3`).
2. Add the **"diagonal-traceless" derivations** `D = [L_A, ·]` for A a traceless h_3(O) element (the inner derivations from Jordan multiplication commutators `D_{A,B} = [L_A, L_B]`). The repo already builds `[L_A, L_B]`-type Jordan-multiplication commutators (octonion_algebra.py:4440 `D_{ij}=[L_{e_i},L_{e_j}]`, and `compute_commutator_algebra` closes a set under brackets).
3. **Close under commutator** (`compute_commutator_algebra` pattern) and assert the closed Lie algebra has dimension **exactly 52** over Q. Each generator is a 27×27 rational matrix acting on `to_vector(X)`.

> **Self-check (must pass before trusting anything):** the 52 generators must satisfy `D_ξ (det_3 X) = 0` and `D_ξ (Tr X) = 0` and `D_ξ (Tr X∘X) = 0` for ALL ξ, at a random rational X. This is the *exact* infinitesimal-invariance test (`D_ξ f := ∇f · (D_ξ · vec(X))`, evaluated as a SymPy expression that must `simplify()` to `0`). It REPLACES finite-group sampling and is decisive — no epsilon tolerance.

### Generic orbit dimension on 27 ⊕ 27 (the gate)

The F_4 action on the **pair** is the diagonal action: `D_ξ` acts on X and on Y by the *same* 27×27 matrix `M_ξ`. Build the **52 × 54 infinitesimal-action matrix** `J_orbit` whose ξ-th row is `(M_ξ · x , M_ξ · y)` (a 54-vector) evaluated at a **random rational pair** `(x*, y*) ∈ Q^54`. Then:

```
generic_orbit_dim = J_orbit.rank()      # rank over Q, EXACT
generic_stabilizer_dim = 52 - generic_orbit_dim
```

**Anchor / expected value (LITERATURE-CONFIRMED, HIGH confidence):** F_4 on the 26-dim trace-zero rep V(ω₄) has **generic stabilizer Spin(8)** (dim 28), so generic orbit on the 26 is 52−28 = **24** (Garibaldi–Guralnick / Lawther; confirmed via the type-F_4 stabilizer literature, arXiv:2308.08214 and arXiv:1508.02918). On the full 27 = 1 ⊕ 26 the trace direction is fixed pointwise, so a single generic X still has a 24-dim orbit. For a **generic pair** (X,Y) the two points break more stabilizer; the generic orbit dimension is **expected to be larger than 24 and at most min(52, 54)=52**, and the executor must COMPUTE it (do not assume). The transcendence degree of the invariant field is then `54 − generic_orbit_dim`; this is the number of functionally independent invariants — i.e. **the target rank for the (b) Jacobian check.**

> **This is why orbit-dim is the gate:** if `54 − generic_orbit_dim = 7`, then the 7 base invariants {Tr X, Tr X², det X, Tr Y, Tr Y², det Y, c} can be a transcendence basis and rank-7 in (b) is the *consistent* expected result. If `54 − generic_orbit_dim ≠ 7`, the whole generating-set claim must be reconsidered before any further work.

---

## Numerical Algorithms (all EXACT over Q)

| Algorithm | Problem | Exactness criterion | Cost / Size | Key Reference |
|---|---|---|---|---|
| **Lie-algebra closure** (`compute_commutator_algebra` over Q) | Build & verify f_4 (52 gens, 27×27) | `Matrix.rank()` over Q = 52 exactly | 52 matrices 27×27; rank of ≤27²×N | Schafer 1966; harness:857 |
| **Orbit-dim rank** | rank of 52×54 `J_orbit` at random rational pt | exact `Matrix.rank()` over Q | one 52×54 rank | Derksen–Kemper 2002 §4 |
| **(b) Jacobian rank** | rank of 7×54 Jacobian of base invariants | exact `Matrix.rank()` over Q (= transcendence degree at generic pt) | one 7×54 rank, repeat ≥3 pts | Jacobian criterion (char 0) |
| **(c) degree-2 coupling uniqueness** | dim of F_4-invariant degree-2 mixed polynomials | exact nullspace over Q of `D_ξ`-action on Sym²-mixed monomials | linear solve, ~few hundred monomials | linear algebra over Q |
| **(a) Molien/Hilbert series** | bigraded dim of R[27⊕27]^{F_4} per (d_X,d_Y) | exact rational generating function / integer coeffs | Weyl-integral residue OR Sage plethysm | Molien–Weyl; Hanany et al. 1902.10550 |

### Exactness criteria spelled out (per step)

- **Orbit dim & (b) Jacobian:** "rank" means SymPy `Matrix(...).rank()` (or `.rref()` row count) over the field **Q**. Build the Jacobian symbolically (`sympy.Matrix([[sympy.diff(f_k, v) for v in vars54] for f_k in invariants])`), then **substitute a random rational point** `subs({v: Rational(p,q)})` and take `.rank()`. **Never** `numpy.linalg.matrix_rank` — float SVD will return a wrong integer near rank-deficiency (this is the central PITFALL).
- **Random point hygiene:** draw 54 independent rationals with numerator/denominator in, say, [−97, 97] (use a fixed seed + `Rational`). **Re-check at ≥3 independent random rational points.** Rationale: the Jacobian rank is generic almost everywhere; a single point could accidentally land on the (measure-zero) lower-rank locus. If all 3 agree, the generic rank is established with overwhelming confidence; if they disagree, the *maximum* over points is the generic rank (rank is lower-semicontinuous: it can only DROP on special loci). 3 points is the standard, cheap insurance; 5 if any entry of the invariants is suspiciously sparse.
- **(c) uniqueness:** enumerate all bidegree-(1,1)-and-(2,0)-and-(0,2) monomials in the 54 vars that could be degree-2 invariants (i.e. quadratics). The F_4-invariant quadratics form the nullspace of the linear map `q ↦ (D_ξ q)_{ξ=1..52}`. Solve over Q. **Decisive claim "c is the unique degree-2 coupling generator"** = the *mixed* (one-X, one-Y) invariant quadratics form a **1-dimensional** space spanned by `Tr(X∘Y)`. (Tr X·Tr Y is also degree-2 mixed but reducible — it is a product of degree-1 invariants Tr X and Tr Y; the executor must quotient by products of lower-degree invariants, i.e. take the **plethystic-logarithm / primitive** part, not the raw invariant count.)

### Convergence / termination

These are finite exact computations — there is no convergence rate, only termination. The only "rate" concern is **SymPy expression swell**: `det_3` of a symbolic 54-variable H3O is a degree-3 polynomial in 54 vars with octonion cross-terms; its symbolic `diff` then `subs(rational)` is fine, but `simplify()` on the full symbolic Jacobian before substitution can blow up. **Substitute the random rational point FIRST, then rank** (rank of a concrete rational matrix is cheap and exact).

---

## (a) Hilbert / Molien-series completeness check — the SageMath step

**Goal:** confirm the candidate generating set {6 pointwise + coupling generators} is COMPLETE up to total degree ≤ 6 by matching the **bigraded** (degree-in-X, degree-in-Y) Hilbert series of R[27⊕27]^{F_4} term-by-term.

Two routes; **recommend Route B (character/plethysm in Sage)** because the repo has no numerical contour-integration setup and the plethysm route is exact-integer.

- **Route A — Molien–Weyl integral (no Sage needed, SymPy-only fallback).** For compact F_4, the Hilbert series is the Weyl-integral (Molien–Weyl theorem):
  `H(t_X, t_Y) = ∫_{F_4} det(1 − t_X ρ(g))^{−1} det(1 − t_Y ρ(g))^{−1} dg`, reduced by the Weyl integration formula to a 4-dimensional (rank-4) torus residue with the F_4 Weyl-denominator/Jacobian. The torus eigenvalues of the 27 are the weights of V(ω₄)⊕(trivial). This is doable in SymPy as **iterated residues / constant-term extraction** in 4 torus variables, but it is fiddly (one must encode the 24 short + long roots of F_4 and the 27 weights). MEDIUM confidence it is worth the bespoke effort.
- **Route B — character / plethysm degree-by-degree (SageMath, RECOMMENDED).** The dimension of degree-(d_X, d_Y) invariants = multiplicity of the trivial rep in `Sym^{d_X}(27) ⊗ Sym^{d_Y}(27)`. In Sage:
  ```python
  F4 = WeylCharacterRing("F4")
  fw = F4.fundamental_weights()
  R27 = F4(fw[4]) + F4.one()          # 26 (=V(ω4)) ⊕ 1 (trivial trace dir) = 27
  # bigraded coefficient (dX, dY):
  inv = (R27.symmetric_power(dX) * R27.symmetric_power(dY)).invariant_degree()
  ```
  `invariant_degree()` returns exactly the multiplicity of the trivial rep (confirmed in the Sage Weyl-character-ring reference). Loop `dX + dY ≤ 6`. The **plethystic logarithm** of the resulting bigraded series gives the *primitive generators* per bidegree; matching that to the candidate set (Tr X at (1,0), Tr Y at (0,1), c at (1,1), Tr X²/det X at (2,0)/(3,0), the mixed cubics at (2,1)/(1,2), …) is the completeness proof up to degree 6. This is exactly the workflow of "Standard Model Plethystics" (Hanany–Khoze–Riley–Torri, arXiv:1902.10550): Molien–Weyl/Hilbert-series + plethystic-log to read off generators and relations (syzygies).

> **Tooling reality (MEDIUM-confidence flag):** SageMath is **NOT installed** in this environment (no `sage` on PATH; only `python3`+`sympy 1.14.0`+`numpy 2.4.2`). The Molien step therefore either (i) requires the orchestrator/user to run a one-off Sage script and PASTE the bigraded integer table into the plan as a fixture (recommended — keeps the executor self-contained), or (ii) the executor implements Route A in pure SymPy. **Do not assume the executor can call Sage.** Recommend (i): a ~30-line Sage snippet, run once, producing the (d_X,d_Y)→multiplicity table for d_X+d_Y≤6, staged as data.

---

## Software Ecosystem

### Primary tools

| Tool | Version | Purpose | License | Maturity | Present here? |
|---|---|---|---|---|---|
| **SymPy** | **1.14.0** | EXACT arithmetic: octonion/h_3(O) algebra, det_3, f_4 derivations, all rank/nullspace over Q | BSD | stable | **YES** |
| **NumPy** | **2.4.2** | float64 cross-checks ONLY (random-point generation, sanity scaffolding, the existing octonion_algebra.py) | BSD | stable | **YES** |
| **SageMath** | 10.x (current ≈10.5, 2025) | F_4 `WeylCharacterRing`, `symmetric_power`, `invariant_degree`, plethysm/branching → the (a) Molien series target | GPL | stable | **NO — must install or run externally** |

### Supporting / optional tools

| Tool | Version | Purpose | When needed |
|---|---|---|---|
| **LiE** | 2.2.2 | classic Lie-rep tensor/sym-power/plethysm (`sym_tensor`, `plethysm`) — lightweight alt to Sage for (a) | if Sage unavailable and a quick rep-theory check is wanted |
| **Singular** | 4.4.x | invariant rings of finite groups (`primary_invariants`, `invariant_ring`) | NOT for this problem — see Anti-Approaches |
| **Macaulay2** | 1.24.x | Gröbner, `InvariantRing` package | NOT for this problem — see Anti-Approaches |
| **Magma** | 2.28-x | strong invariant-theory + reductive-group machinery | only if a fully independent re-derivation is demanded (commercial; not present) |

### Install / setup

```bash
# Already satisfied for the decisive path:
python3 -c "import sympy, numpy; print(sympy.__version__, numpy.__version__)"   # 1.14.0 2.4.2

# Optional, for the (a) Molien step only — run ONCE externally, paste the table:
# conda create -n sage -c conda-forge sage   # heavy (~2-4 GB); or use a Sage Docker image
# sage molien_f4.sage  > f4_bigraded_multiplicities.txt
```

---

## (6) Polarization of det_3 → mixed cubic coupling generators

The mixed cubic invariants f(X,X,Y) and f(X,Y,Y) come from polarizing the cubic norm. The harness **already provides** `polarize_d(X,Y,Z)` (octonion_algebra.py:2184) with the convention `d(X,X,X) = 6·det_3(X)` (VERIFIED, octonion_algebra.py:2299: "d(X,X,X) = 6*N(X): max rel err 1.4e-13").

- **Convention lock (do this BEFORE building):** verify `polarize_d(X,X,X) == 6 * det_3(X)` exactly (SymPy `simplify(... ) == 0`) at a random rational X. This pins the symmetric trilinear form `d` so that the two mixed cubics are unambiguously:
  - `f_XXY := d(X,X,Y)` (bidegree (2,1)), and
  - `f_XYY := d(X,Y,Y)` (bidegree (1,2)).
- **Sharp-vs-d hazard.** Two distinct but related bilinear/trilinear objects live in the harness: the **sharp / Freudenthal cross product** `_compute_sharp` (X#, `X∘X# = det_3(X)·I`) with its polarization `_polarized_sharp(X,Y) = cross(X,Y)` (octonion_algebra.py:3876), AND the **trace-trilinear** `d` from `polarize_d`. They are related by `d(X,Y,Z) = Tr( cross(X,Y) ∘ Z )` (the harness uses exactly this at octonion_algebra.py:3901, `M_{ab}=Tr(cross(e_a,e_b)∘E)`). **Pick ONE convention** — recommend the **`polarize_d` trilinear** because (i) it is already validated to `6·det`, (ii) it makes F_4-invariance manifest (det_3 is F_4-invariant ⇒ every polarization is), and (iii) the executor never has to chase the X×Y "sharp" sign/normalization convention. Document the choice in an `ASSERT_CONVENTION` header line: `det3_polarization=d(X,X,X)=6*det_3, mixed_cubics=d(X,X,Y)_and_d(X,Y,Y)`.
- **F_4-invariance is automatic** for `d(·,·,·)` once `D_ξ det_3 = 0` is verified (it is, both numerically in the harness and exactly via the §"do this FIRST" self-check), because `d` is a polarization of `det_3`. Still, run the exact `D_ξ f_XXY = 0` and `D_ξ f_XYY = 0` self-check for all 52 ξ.

---

## Data Flow

```
random rational seed
 -> (54 symbols x0..x26, y0..y26)  +  E_i = peirce_basis_27()          [thin new layer]
 -> exact-SymPy H3O(X), H3O(Y) as linear forms                          [reuse embedding-file octonion block]
 -> base invariants {TrX,TrX²,detX, TrY,TrY²,detY, c=Tr(X∘Y)}           [reuse det_3, jordan_product]
 -> 52 f_4 generators M_ξ (27×27 over Q), closure-verified dim=52       [reuse _g2_derivation_matrix + [L_A,L_B] + compute_commutator_algebra]
 -> GATE: orbit-dim = rank(52×54 J_orbit) at random rational pt         [EXACT rank over Q]  ──► fixes target trdeg = 54 − orbit_dim
 -> (b) rank(7×54 Jacobian) at ≥3 random rational pts                   [EXACT rank over Q]  ──► 7 ⇒ independent; 6 ⇒ NEGATIVE
 -> (c) nullspace of D_ξ on degree-2 mixed monomials, minus reducibles  [EXACT over Q]       ──► dim 1 ⇒ c unique
 -> (6) mixed cubics f(X,X,Y),f(X,Y,Y) via polarize_d; D_ξ f=0 check    [reuse polarize_d]
 -> (a) Sage/LiE bigraded multiplicities (d_X+d_Y≤6) + plethystic log   [EXTERNAL Sage, paste as fixture]  ──► completeness up to deg 6
 -> assert-based _report / ALL_PASS / sys.exit harness                  [reuse slice_clause_iii pattern]
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Parallelize? |
|---|---|---|---|
| Port exact octonion/H3O/det_3 layer | embedding-file + octonion_algebra.py formulas | exact base ops | n/a (foundation) |
| Build & close f_4 (dim=52 check) | exact base ops | 52 M_ξ over Q | no |
| **Orbit-dim GATE** | f_4 generators | trdeg target | no (gates everything) |
| (b) Jacobian rank | base invariants + orbit-dim target | rank ∈ {6,7} verdict | yes (per random point) |
| (c) degree-2 uniqueness | f_4 generators | dim of mixed quadratic invariants | yes |
| (6) mixed cubics + invariance | polarize_d + f_4 | f(X,X,Y), f(X,Y,Y) | yes |
| (a) Molien completeness | external Sage table | bigraded mult ≤ deg 6 | externally, once |

## Resource Estimates

| Computation | Time (exact SymPy) | Memory | Hardware |
|---|---|---|---|
| Exact octonion/det_3 port + smoke tests | minutes (dev) / < 1 s run | trivial | laptop |
| f_4 build + commutator closure to dim 52 | seconds–1 min (27×27 rational rank, ~hundreds of brackets) | < 200 MB | laptop |
| Orbit-dim rank (52×54 over Q, random pt) | seconds (one exact rank) | < 100 MB | laptop |
| (b) Jacobian rank (7×54 over Q) × 3 pts | seconds total | < 100 MB | laptop |
| (c) degree-2 nullspace over Q | seconds (a few hundred monomials) | < 200 MB | laptop |
| (6) polarized cubics + 52 invariance checks | seconds–minutes (det_3 symbolic diff swell if not subbing first) | < 500 MB if point-substituted | laptop |
| (a) Sage bigraded multiplicities ≤ deg 6 | seconds–minutes in Sage | < 1 GB | needs Sage install |

**Bottom line:** the entire decisive verification is a **laptop-minutes, single-core** exact computation. There is no HPC, no GPU, no sign problem. The only "cost" is SymPy expression swell, fully avoided by **substituting the random rational point before taking ranks.**

## Integration with Existing Code

- **Input format:** H3O elements as `(α,β,γ,x1,x2,x3)` with octonions as 8-tuples — IDENTICAL to `octonion_algebra.py` and the exact embedding-file port. `to_vector`/`from_vector` give the R^27 ↔ H3O bridge for stacking the 54-vector.
- **Output format:** assert-based PASS/FAIL lines + `sys.exit(0/1)` (the VALD-61 `slice_clause_iii_verification.py` pattern). No pytest on the decisive path (executor venv = sympy/numpy only).
- **Interface point:** new file `code/ring_lemma_verification.py`, importing the exact octonion block (either `from code.embedding_under_E_verification import oct_mul, ...` or a copied exact block), the `det_3`/`polarize_d`/derivation **formulas** re-ported to exact SymPy. **Do NOT entangle with the v15.0 basin-restriction result** — this is a fresh invariant-theory computation; reuse algebra only.

## Validation Strategy

| Result | Validation method | Benchmark (exact) | Source |
|---|---|---|---|
| octonion port correct | e1·e2 == e4; (e1·e2)·e3 ≠ e1·(e2·e3) on a triple | Fano + nonassoc | octonion_algebra.py header |
| det_3 port correct | det_3(diag(a,b,c)) == a·b·c; det_3(I_3)==1; det_3(E_ii)==0 | exact equalities | octonion_algebra.py:2296 |
| polarization convention | polarize_d(X,X,X) − 6·det_3(X) `simplify`==0 | exact 0 | octonion_algebra.py:2299 |
| f_4 correct | dim(closure)==52; D_ξ(det_3)=D_ξ(TrX)=D_ξ(TrX²)=0 ∀ξ | exact 0, dim 52 | Schafer 1966 |
| orbit-dim sane | 54 − orbit_dim == 7 (consistency with 7 base invariants) | integer match | Garibaldi–Guralnick |
| (b) verdict | rank stable across ≥3 random rational points | 7 (or decisive 6) | Jacobian criterion |
| (c) verdict | mixed degree-2 invariant space (mod reducibles) dim==1 | exact 1 | linear algebra/Q |
| (a) completeness | candidate plethystic-log == Sage bigraded series, d_X+d_Y≤6 | integer-by-integer | 1902.10550 method |

---

## Open Questions

| Question | Why open | Impact | Approaches |
|---|---|---|---|
| Exact generic orbit dimension of F_4 on 27⊕27 | not a standard textbook number (single-27 is Spin(8), 24-dim; the *pair* is what we need) | fixes the (b) target rank and the whole trdeg | **compute it first** via 52×54 rank over Q |
| Is SageMath available to the executor? | environment has SymPy/NumPy only; no `sage` on PATH | (a) Molien step blocks if not | run Sage once externally, paste integer table as fixture; OR pure-SymPy Molien–Weyl residue (Route A) |
| Reducible vs. primitive degree-2 invariants | Tr X·Tr Y is degree-2 mixed but reducible | (c) must count *primitive* generators, not raw invariants | quotient by products of lower-degree invariants (plethystic log) |
| det_3 symbolic swell in 54 vars | degree-3 in 54 vars with octonion cross-terms | (6)/(b) could be slow if simplified symbolically | substitute random rational point BEFORE rank/diff-evaluation |

## Anti-Approaches

| Anti-Approach | Why avoid | Do instead |
|---|---|---|
| **Gröbner-basis invariant-ring computation on 54 variables** (Singular `invariant_ring`, Macaulay2 `InvariantRing`, Derksen-ideal elimination) | Buchberger/F4 Gröbner is **doubly-exponential in the number of variables**; 54 vars + a continuous reductive group is far outside feasibility (the cyclic-9 ideal in 9 vars was a milestone). The "essential variables" reduction does not apply here. | Use the **Jacobian/orbit-dimension** criterion (b) + **Molien series** (a) — neither needs a Gröbner basis. Generators are *hypothesized* (the 6 + c + cubics) and *verified*, not *computed from scratch*. |
| **Float64 rank** (`numpy.linalg.matrix_rank`, SVD tolerance) for orbit-dim or (b) Jacobian | Float SVD returns an integer via a heuristic tolerance; near rank-deficiency it can report rank 7 when the true rank is 6 (or vice versa) — **fatally** ambiguous for a decisive NEGATIVE. The existing harness even shows float det_3 noise at 1e-13. | **Exact `Matrix.rank()` over Q** at random *rational* points. Float is acceptable ONLY as a fast pre-screen/scaffold, never as the verdict. |
| **Finite-group sampling** to check F_4-invariance (apply random group elements, compare) | F_4 is a continuous 52-dim group; finite sampling gives only approximate, tolerance-dependent invariance and can never *prove* invariance. | **Infinitesimal test** `D_ξ f = 0` for all 52 Lie-algebra generators, exact SymPy `simplify == 0`. (The harness's `verify_f4_invariance_det3` uses exp(εD) finite tests — fine as corroboration, but the EXACT decisive test is the Lie-algebra annihilation.) |
| **Rebuilding octonion/h_3(O) arithmetic from scratch** | wastes effort and risks convention drift (Fano sign, det_3 left-association, Jordan 1/2) | **Reuse** the exact-SymPy octonion block (`embedding_under_E_verification.py`) + the validated `det_3`/`polarize_d`/derivation formulas. |

## Logical Dependencies

```
exact octonion port (e1e2=e4, nonassoc) -> det_3 (left-assoc (x1*x2)*x3) -> polarize_d (d(X,X,X)=6 det)
f_4 = Der(h_3(O)) closure (dim 52)  -> orbit-dim rank (52×54/Q)  -> target trdeg = 54 − orbit_dim
target trdeg == 7  REQUIRED for  (b) Jacobian rank == 7 to be the consistent PASS
D_ξ det_3 = 0 (exact, all 52)  =>  every polarization d(X,..) is F_4-invariant  (mixed cubics automatic)
(c) "c unique deg-2 coupling"  ==  dim( mixed deg-2 invariants / reducibles ) == 1   (nullspace of D_ξ over Q)
(a) plethystic-log of Sage bigraded series  ==  candidate generator bidegrees  (completeness ≤ deg 6)
```

## Recommended Investigation Scope

Prioritize (in order — the first is the gate):
1. **Port the exact-SymPy base layer + reproduce the harness's exact validation benchmarks** (det_3 of diag, e1e2=e4, d(X,X,X)=6·det). Cheap, de-risks everything.
2. **Build f_4 (verify dim 52) and compute the generic orbit dimension** of F_4 on 27⊕27 via exact 52×54 rank — this fixes the target transcendence degree and is the prior-work-flagged "do this FIRST."
3. **(b) Jacobian rank** (the decisive functional-independence test) and **(c) degree-2 uniqueness** — both pure exact linear algebra over Q, fast.
4. **(6) mixed cubic generators** via `polarize_d` with the convention lock + exact invariance self-check.

Defer: **(a) Molien/Hilbert-series completeness** to last and treat its SageMath dependency as an **external one-off** (paste the bigraded multiplicity table as a data fixture) — it is the only step needing a tool the executor lacks, and it confirms completeness rather than gating the decisive (b)/(c) verdicts.

## Key References

- Derksen, H. & Kemper, G., *Computational Invariant Theory*, 2nd ed., Springer (2015) — Jacobian criterion for functional independence (char 0), orbit-dimension via infinitesimal action, Derksen ideal. (Kemper ISSAC-2010 tutorial: issac-conference.org/2010/assets/TutorialKemper.pdf; Springer link.springer.com/chapter/10.1007/978-3-031-62127-7_12)
- Hanany, Khoze, Riley, Torri, *Standard Model Plethystics*, arXiv:1902.10550 — directly analogous: Hilbert/Molien series + plethystic logarithm to read off invariant generators and syzygies for physics gauge-rep invariant rings.
- Molien–Weyl theorem / Weyl integration formula for compact-Lie-group invariants — Sturmfels invariant-theory notes; "Invariants and relative invariants under compact Lie groups," arXiv:1207.1513.
- SageMath WeylCharacterRing reference (F4, `symmetric_power`, `invariant_degree`, plethysm/branching): doc.sagemath.org/html/en/reference/combinat/sage/combinat/root_system/weyl_characters.html ; thematic tutorial doc.sagemath.org/html/en/thematic_tutorials/lie/weyl_character_ring.html
- Springer, T.A., Indag. Math. 24 (1962) 259-265 — uniqueness of the cubic norm on h_3(O) (cited by the harness for det_3).
- Schafer, R.D., *An Introduction to Nonassociative Algebras* (1966) — derivation formula D_{a,b}=[L_a,L_b]+[L_a,R_b]+[R_a,R_b]; Der(h_3(O))=f_4. (Used by `_g2_derivation_matrix`.)
- Garibaldi–Guralnick / Lawther, generic stabilizers for F_4 on the 26: arXiv:2308.08214 ("Generic stabilizers for simple algebraic groups"), arXiv:1508.02918 — generic stabilizer Spin(8), generic orbit dim 24 on V(ω₄).
- Baez, J., "The Octonions," Bull. AMS 39 (2002), math/0105155, Sec. 3.4 — cubic norm / det formula (harness's det_3 reference).
- In-repo provenance: `code/octonion_algebra.py` (float64 formulas + VERIFIED comments), `code/embedding_under_E_verification.py` (exact-SymPy octonion port), `code/slice_clause_iii_verification.py` (exact-SymPy assert-harness pattern), `code/sp_verification.py` (exact SymPy Matrix/Rational usage).
