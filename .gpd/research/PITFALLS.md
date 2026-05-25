# Known Pitfalls Research — (RING) Lemma: Joint F_4-Invariants of 27 ⊕ 27

**Domain:** Computational invariant theory of the exceptional group F_4 = Aut(h_3(O)) acting diagonally on the Albert algebra 27 = h_3(O); polarization of the cubic norm; Jacobian/orbit-dimension functional-independence proofs.
**Researched:** 2026-05-24
**Confidence:** HIGH on the invariant-theory failure modes and citations; HIGH on the five reward-hacking traps (each named verbatim in the milestone prompt and each given a runnable detection test below).

### Scope Boundary

This file is the FAILURE-MODE catalog for proving (RING). It complements METHODS.md (the recommended proof methods) and PRIOR-WORK.md (established results + the literature verdict). It does NOT re-derive R[h_3(O)]^{F_4} = R[Tr, Tr², det], does NOT touch the v15.0 basin-restriction result (the prompt forbids entangling them), and treats (REDUCIBILITY) only insofar as the milestone STATES it (the autonomous-vs-driven trap is a (RING)-adjacent reward-hacking guard, listed below).

### The single sentence to remember

The genuine content of (RING) is NOT "does polarization work?" — it is **"is the 27 of F_4 in the 'good' class where polarizing the single-copy generators actually generates the pair ring (it generically is NOT, even over C — Schwarz), and is the proof of c's independence a DEMONSTRATED exact-arithmetic orbit/Jacobian fact rather than an assertion?"** Get those two right and the milestone is sound; a decisive NEGATIVE (c expressible in the pointwise ring) is an equally acceptable, must-report outcome.

---

## Critical Pitfalls

### Pitfall 1 — [(a), THE central trap] Conflating Weyl's polarization theorem (needs dim V = 27 copies) with the "k-polarization property" (polarize the SINGLE copy), and assuming the latter holds in char 0

**What goes wrong:**
Two genuinely different theorems travel under the word "polarization," and the milestone needs to keep them apart.

- **Weyl's polarization theorem (strong form, Domokos–Kemper Thm 1.3, char 0):** if S generates `K[V^n]^G` for `n = dim V`, then `⟨S⟩_{GL_m}` generates `K[V^m]^G` for all `m ≥ n`. For the 27 this requires **starting from n = 27 copies** — not 1, not 2.
- **The k-polarization property (Schwarz, arXiv:math/0609078):** `pol_k(V)^G = C[kV]^G`, i.e. polarizing the **single-copy** generators of `C[V]^G` generates the k-copy ring. Schwarz's main theorem is precisely the **classification of which simple G and modules V have this property**, and "most representations do **not** have the 2-polarization property" — *even over C, char 0*. His Example 1.1 (SL_2 on C²) already shows polarizing the single det generator yields only 3 of the 6 generators of `C[4V]^G`.

The trap (and METHODS.md's executive line "polarizing a single-copy generating set DOES yield a generating set for any number of copies" leans toward it) is to assume that because char = 0, polarizing `{Tr, Tr², det}` automatically generates `R[27⊕27]^{F_4}`. That is the **2-polarization property for the 27 of F_4**, which is NOT licensed by char 0 alone — it must be checked, and it may simply be false (in which case there are "genuinely new" generators at bidegrees the single-copy polarizations never reach).

**Why it happens:**
The phrase "Weyl polarization holds in char 0 for all reductive groups" is true (Domokos–Kemper Thm 1.2/1.3) but is about going from **dim-V copies** to more copies. People drop the "from dim V copies" and silently restate it as "from 1 copy," which is a different (often false) claim.

**How to avoid:**
- State which theorem you invoke. If you want generation of the pair ring from single-copy generators, that is the **2-polarization property**, and it requires a CERTIFICATE, not a char-0 hand-wave.
- The certificate is the **bigraded Hilbert/Molien series match** (METHODS.md): compute `H(s,t) = Σ dim(R[27⊕27]^{F_4})_{(i,j)} sⁱtʲ` by Weyl integration over F_4, and confirm the candidate generator list (six pointwise + c + the mixed det-polarizations f(X,X,Y), f(X,Y,Y) + any trace monomials Tr(X²∘Y), Tr(X∘Y²)) reproduces it coefficient-by-coefficient through total degree ≤ 6.
- Note PRIOR-WORK's contrast case: Blind (2011) proves the **E_6** pair ring IS free on 4 det-polarizations — but E_6 is the det-stabilizer, a different group; F_4 (which also fixes the trace form) has a strictly LARGER pair ring including the trace-form coupling c. Do not import the E_6 cleanliness to F_4.

**Detection test (runnable):**
```python
# Hilbert-series completeness check, bidegree by bidegree, to total degree 6.
# Ground truth H(s,t): Reynolds/infinitesimal-kernel dimension of invariants in each (i,j).
# Candidate: dimension reachable by products of the proposed generators in (i,j).
for i in range(0, 7):
    for j in range(0, 7 - i):
        d_true = invariant_dim_bidegree(i, j)          # f_4-kernel on monomials (exact)
        d_cand = candidate_generated_dim(i, j, gens)   # products of proposed gens
        assert d_cand == d_true, (i, j, d_cand, d_true)
# A MISMATCH at any (i,j) with d_true > d_cand  =>  a genuinely-new generator is MISSING
# at that bidegree  =>  the 2-polarization property FAILS and the candidate list is incomplete.
```
Warning sign: any bidegree where the invariant dimension exceeds what the candidate generators produce. That is a missing generator, full stop — not a rounding issue (the kernel computation is exact).

**Phase to address:** The (a) generating-set phase. This is its primary risk and its primary deliverable (the Hilbert-series certificate).

---

### Pitfall 2 — [(b), reward-hacking guard #1] Asserting c's independence from the orbit/transcendence picture alone, without the exact-arithmetic demonstration on the actual algebra

**What goes wrong:**
The orbit argument ("fix generic Y, c varies on the F_4-orbit of X while pointwise invariants are constant ⇒ c ∉ R_pt") is *correct as a conceptual proof* but the milestone's reward-hacking guard (PROJECT.md, verbatim) forbids asserting independence "without the explicit orbit/Jacobian demonstration on the actual algebra." A prose orbit argument with no computation is exactly the banned move.

**Why it happens:**
The orbit argument feels airtight, so it is tempting to skip the machine check. But the argument has load-bearing facts that are NOT self-evident and must be verified on h_3(O): (i) the orbit O_X is actually positive-dimensional at the chosen X; (ii) the trace pairing T(X,Y) = Tr(X∘Y) is genuinely F_4-equivariant and non-degenerate; (iii) c genuinely varies along the orbit (it could, in principle, be orbit-constant for a non-generic Y).

**How to avoid:**
Do BOTH, exactly as METHODS.md prescribes:
1. **Algebraic (decisive):** the 7×54 Jacobian of `(Tr X, Tr X², det X, Tr Y, Tr Y², det Y, c)` has rank 7 at a generic rational point.
2. **Geometric (explanatory):** the infinitesimal orbit-derivative — `d/dt c(exp(tξ)X, Y)|_0 ≠ 0` for some `ξ ∈ f_4`, while every pointwise generator has zero derivative along the same ξ.

**Detection test (runnable):**
```python
import sympy as sp
# 54 EXACT symbolic variables; build c and the 6 pointwise invariants on the EXACT layer.
J = sp.Matrix([[sp.diff(f, v) for v in vars] for f in [g1,g2,g3,g4,g5,g6,c]])  # 7 x 54
pt = {v: sp.Rational(*rand_small_coprime()) for v in vars}     # generic rational point
assert J.subs(pt).rank() == 7        # c is independent
J6 = J[:6, :]
assert J6.subs(pt).rank() == 6       # the 6 pointwise alone are independent (baseline)
# Orbit derivative cross-check (exact or high-precision):
xi = f4_basis[k]                     # one of the 52 f_4 generators
assert sp.diff(c_along_orbit(xi, t), t).subs(t, 0).subs(pt) != 0   # c varies
for g in [g1,g2,g3,g4,g5,g6]:
    assert sp.diff(g_along_orbit(g, xi, t), t).subs(t, 0).subs(pt) == 0  # pointwise constant
```
The pair (nonzero orbit-derivative of c, zero orbit-derivative of every pointwise generator) IS the demonstrated independence.

**Phase to address:** The (b) independence phase. This is the milestone's load-bearing, most-guarded result.

---

### Pitfall 3 — [(b), reward-hacking guard #2] Floating-point Jacobian rank — a near-degenerate float matrix gives a FALSE rank drop (false NEGATIVE) or a FALSE full rank (false POSITIVE)

**What goes wrong:**
Matrix rank is **discontinuous**. With float arithmetic and a tolerance threshold, a singular value that is "small" gets called zero (spurious rank drop ⇒ falsely concluding c IS dependent, a fabricated NEGATIVE) or a singular value that is "barely nonzero" due to roundoff gets called nonzero (spurious full rank ⇒ falsely concluding c is independent, a fabricated POSITIVE). Either way the conclusion is an artifact of the SVD tolerance, not of the algebra. This is the **single most dangerous numerical trap** because the wrong answer looks like a clean integer rank.

**Why it happens:**
- The warm harness `code/octonion_algebra.py` is **float64** (30 `np.float64` sites, no SymPy). Reusing it for the Jacobian — as a loose reading of METHODS.md ("reuse the warm `octonion_algebra.py`") invites — runs the decisive rank check in floats.
- `np.linalg.matrix_rank` with a default `tol` will silently make the call for you.
- Octonionic determinants in 54 variables produce large integer coefficients; intermediate float products lose precision fast.

**How to avoid:**
- Run the rank on the **EXACT SymPy layer**, not the float harness. The exact h_3(O) Jordan arithmetic for this project lives in `code/embedding_under_E_verification.py` / `tests/test_embedding_under_E.py` (the v15.0 warm exact harness the prompt points to), NOT in `code/octonion_algebra.py`. Port `jordan_product`/`det_3` to `sympy.Rational` or reuse the embedding-under-E exact layer.
- Use `Matrix.rank()` over an exact field (Q), never `np.linalg.matrix_rank`.
- Pick a rational point with small coprime integer entries (e.g. components from {±1, ±2, ±3, ±5}); exact rank at such a point is a theorem, not an estimate.

**Detection test (runnable):**
```python
# Confirm you are exact: rank must be identical at the symbolic level and at the point.
assert J.subs(pt).rank() == J.rank()           # exact: point-rank == generic rank
# Float canary: if someone reran in floats, the tolerance sensitivity exposes it.
svals = np.linalg.svd(np.array(J.subs(pt)).astype(float), compute_uv=False)
gap = svals[6] / svals[7] if len(svals) > 7 else float('inf')  # ratio at the rank boundary
assert gap > 1e6, "rank boundary is float-fragile; you MUST use exact arithmetic here"
```
Warning sign: the rank changes when you tighten or loosen the SVD tolerance. If it does, the result is meaningless — switch to exact.

**Phase to address:** The (b) independence phase. Build/confirm the exact arithmetic layer BEFORE attempting the rank.

---

### Pitfall 4 — [(b), reward-hacking guard #3] Evaluating the Jacobian (or orbit map) at a NON-GENERIC point and drawing a generic conclusion

**What goes wrong:**
The Jacobian criterion gives trdeg = rank **at a generic point** = rank on a dense open set. If you evaluate at a special point — X with extra symmetry, X commuting with Y, X or Y with degenerate (repeated) spectrum, a point on the discriminant locus, or X = Y (the diagonal, where c(X,X) = Tr(X²) collapses to a pointwise invariant) — the rank can DROP below the generic value. You would then falsely conclude c is dependent (a fabricated NEGATIVE). Symmetrically, but more rarely, a contrived point could mask a real degeneracy.

**Why it happens:**
"Random" rational points generated carelessly land on special loci more often than intuition suggests: zero components, equal diagonal entries, octonionic off-diagonals that happen to associate, or X proportional to Y. The diagonal X=Y is especially seductive because it is the natural "sanity" point and is *exactly* where c stops being independent (c(X,X) = Tr X²).

**How to avoid:**
- Evaluate at **≥ 2 (preferably 3) independent random rational points** with generic, all-nonzero, mutually incommensurate-looking entries; require X ≠ λY and distinct diagonal entries.
- If the rank is the same (7) at all of them, you are generically on the dense open set. If it differs between points, you hit a non-generic point — investigate which.
- Optional belt-and-suspenders: compute the **symbolic rank over the function field Q(x_a, y_b)** (costlier) to remove the genericity assumption entirely.
- Explicitly AVOID the diagonal X=Y as a test point for independence (use it only as a separate consistency check that c(X,X) = Tr X² — see Pitfall 11).

**Detection test (runnable):**
```python
ranks = []
for seed in range(3):
    pt = generic_rational_point(seed)   # all-nonzero, distinct diagonals, X != lambda*Y
    ranks.append(J.subs(pt).rank())
assert ranks == [7, 7, 7], f"rank varies across points {ranks} -> a non-generic point was hit"
# Diagonal trap canary: this MUST drop to 6, confirming X=Y is non-generic (do NOT use it):
pt_diag = {**{xv: 2 for xv in x_vars}, **{yv: 2 for yv in y_vars}}  # X = Y
assert J.subs(pt_diag).rank() <= 6
```
Warning sign: rank that depends on the point. Generic conclusions require generic points; two agreeing points are cheap insurance.

**Phase to address:** The (b) independence phase.

---

### Pitfall 5 — [(b)/(c), reward-hacking guard #4] Getting the orbit dimension / generic stabilizer wrong — the Spin(8)-triality principal-isotropy count corrupts every transcendence-degree statement

**What goes wrong:**
The orbit argument and any Krull-dimension/Hilbert-series target depend on `dim O_X = 52 − dim Stab_{F_4}(X)` and, for the pair, on the **principal isotropy subgroup of F_4 on 27⊕27**. PRIOR-WORK flags this as "the single most important numerical fact to verify." The naive back-of-envelope ("once X is generic, F_4_X = Spin(8); Spin(8) acts on the second 27, generic vector has finite stabilizer ⇒ pair-stabilizer trivial ⇒ orbit dim 52 ⇒ trdeg = 54−52 = 2") **contradicts** the six pointwise invariants already giving trdeg 6. So the naive count is WRONG, and any argument built on it is corrupted.

The resolution (PRIOR-WORK Open Q #4): the six pointwise + c give 7 functionally independent invariants ⇒ generic orbit dim ≤ 54 − 7 = 47 ⇒ the generic pair-stabilizer has dim ≥ 5. The Spin(8)-on-(8_v ⊕ 8_s ⊕ 8_c ⊕ scalars) generic stabilizer is a delicate triality/G_2-flavored question (a generic Spin(8) orbit configuration relates to a ~14-dim subgroup, NOT the trivial group). Getting this number wrong in either direction sets the wrong Hilbert-series Krull dimension and either hides a missing generator or invents a phantom relation.

**Why it happens:**
F_4 ≅ Spin(8) + 8_v + 8_s + 8_c (triality) makes the "Spin(8) acts transitively enough" intuition feel safe, but triality means the three 8s are permuted and a generic element of one is NOT generically stabilized trivially by the diagonal Spin(8) action that survives after fixing X.

**How to avoid:**
- Do NOT trust any back-of-envelope stabilizer dimension. **Compute it in the harness**: build the 27×52 infinitesimal-action matrix `[components of ξ_k · X]` for the 52 f_4 generators at a generic rational X; its rank = dim O_X, and `dim Stab(X) = 52 − rank`. Repeat for the pair: the 54×52 matrix `[ξ_k·(X,Y)]`; its rank = generic pair-orbit dimension.
- Cross-check the two routes: `(generic pair-orbit dim from infinitesimal rank)` must satisfy `54 − (orbit dim) = Krull dim of the invariant ring = trdeg of a maximal algebraically independent subset of generators`. With 7 functionally independent invariants you expect orbit dim ≤ 47.
- Cite Garibaldi–Guralnick (arXiv:2105.09486, Lemma 8.1: s.g.p. of F_4 on 26 = Spin(8); Thm 1.3: dim k[V]^G = dim V − dim G when dim V > dim G) for the single-copy count, and treat the PAIR principal isotropy as a harness computation, not a literature lookup.

**Detection test (runnable):**
```python
# Single-copy sanity: orbit dim should be 24, stabilizer 28 (= dim Spin(8)).
A1 = infinitesimal_action_matrix(f4_basis, X_generic)        # 27 x 52, exact or hi-precision
assert A1.rank() == 24 and 52 - A1.rank() == 28               # Spin(8) = 28-dim  (GG 2021)
# Single-copy trdeg cross-check: 27 - 24 = 3 = #{Tr, Tr^2, det}.
assert 27 - A1.rank() == 3
# PAIR: compute, do NOT assume.
A2 = infinitesimal_action_matrix(f4_basis, (X_generic, Y_generic))  # 54 x 52
orbit_dim = A2.rank()
stab_dim  = 52 - orbit_dim
assert orbit_dim <= 47, "pair-orbit too big -> contradicts 7 independent invariants"
assert stab_dim  >= 5,  "pair-stabilizer too small -> naive triality count crept in"
# Krull-dim consistency with the Hilbert-series target:
assert 54 - orbit_dim == krull_dim_from_hilbert_series
```
Warning sign: a pair-orbit dimension of 52 (trivial stabilizer) or any value that makes `54 − orbit_dim < 7`. Both contradict the known independent invariants.

**Phase to address:** A shared dimension-count phase feeding both (b) and the (a) Hilbert-series Krull-dimension target. This is the highest-leverage single computation in the milestone.

---

### Pitfall 6 — [(b), reward-hacking guard #5] Forcing a positive when the honest outcome is the decisive NEGATIVE (c IS expressible in the pointwise generators)

**What goes wrong:**
The milestone's mechanism (the Chalmers-gap reading: the cross-term escapes the single-frame Observable ring) WANTS c to be independent. That creates pressure to massage the computation toward rank 7 — loosening tolerances, cherry-picking the one rational point that gives 7, re-defining "pointwise ring" to exclude products until c looks new, or quietly dropping a generator that would have spanned c. If the honest exact computation returns rank 6 (c IS in R_pt), that is a **decisive NEGATIVE that kills the mechanism** and MUST be reported, not buried. PROJECT.md: "A negative result, cleanly characterized, is a fully acceptable outcome."

**Why it happens:**
Confirmation pressure plus a discontinuous, tolerance-sensitive quantity (rank) is the perfect storm for unconscious p-hacking.

**How to avoid:**
- Pre-register the test: exact arithmetic, ≥3 generic rational points, fixed definition of R_pt (the subring generated by `{Tr X, Tr X², det X, Tr Y, Tr Y², det Y}` and their products — see Pitfall 7), report the rank you get.
- If rank 6: state the NEGATIVE plainly, then DEMONSTRATE the expression (find the explicit polynomial P with c = P(g_1,…,g_6) by solving the linear system in the degree-2 invariant basis) — a constructive negative is far stronger than "rank came out 6."
- Treat a too-clean positive with suspicion: re-run from scratch on a fresh point and confirm the orbit-derivative of c is genuinely nonzero (Pitfall 2).

**Detection test (runnable):**
```python
rank = J.subs(generic_pt).rank()
if rank == 6:
    # HONEST NEGATIVE: construct the explicit expression and verify it exactly.
    basis2 = degree2_invariant_basis()          # {Tr X^2, Tr Y^2, (Tr X)^2, (Tr Y)^2, Tr X Tr Y}
    coeffs = solve_linear(c, basis2)             # exact solve
    assert sp.simplify(c - sum(k*b for k, b in zip(coeffs, basis2))) == 0
    report("DECISIVE NEGATIVE: c = " + str(coeffs) + " in the pointwise ring; mechanism killed")
elif rank == 7:
    report("c independent; re-verified on fresh point + nonzero orbit-derivative")
```
Warning sign: a result that only appears at one special point, or that requires redefining the pointwise ring to obtain. Either is a red flag for a forced positive.

**Phase to address:** The (b) independence phase, with an explicit "report the verdict either way" gate.

---

### Pitfall 7 — [reward-hacking guard, definitional] Redefining "reducible"/"pointwise" so the cross-term c trivially lands in (or out of) the invariant ring

**What goes wrong:**
The entire claim is sensitive to the precise definition of the pointwise (single-frame) subring R_pt. If "pointwise" is silently taken to mean only the linear generators `{Tr X, Tr Y}`, then c is trivially "not pointwise." If it is stretched to include arbitrary smooth functions or an ad-hoc closure, c can be argued either in or out. Both are the banned definitional reward-hack (PROJECT.md: "redefine 'reducible' so it trivially equals the invariant ring").

**Why it happens:**
"Pointwise," "reducible," and "single-frame Observable" are used loosely in the narrative; without a frozen algebraic definition the proof can drift to whatever conclusion is wanted.

**How to avoid:**
Freeze ONE definition before any computation and use it everywhere:
> **R_pt := the R-subalgebra of R[27⊕27]^{F_4} generated by `{Tr X, Tr X², det X, Tr Y, Tr Y², det Y}`** — i.e. all *polynomials* (sums of products) in the six single-state generators. Equivalently R_pt = R[Tr X, Tr X², det X] ⊗ R[Tr Y, Tr Y², det Y].
The claim "(b) c ∉ R_pt" then means: c is not a polynomial in those six. Products like `Tr(X)Tr(Y)` ARE in R_pt (they are products of single-state generators) — so "c is new" must mean "new modulo products," handled precisely in (c).

**Detection test (runnable):**
```python
# Pin R_pt as the SIX generators' polynomial closure. Verify the boundary cases land correctly:
assert is_in_Rpt(Tr_X * Tr_Y)        # reducible product -> IN R_pt  (must be True)
assert is_in_Rpt(Tr_X**2)            # IN R_pt
assert not is_in_Rpt(c)              # the claim under test (b): c NOT in R_pt
# Consistency: the test must give the SAME answer regardless of how R_pt is phrased.
assert is_in_Rpt is frozen_definition  # one definition, used in (a),(b),(c) identically
```
Warning sign: the membership predicate for R_pt differs between the (b) section and the (c) section, or the word "pointwise" is used without pointing back to the six-generator definition.

**Phase to address:** A definitions/setup phase preceding (a), (b), (c); the definition must be cited identically in all three.

---

### Pitfall 8 — [(a)] Conflating a SPANNING set of invariants with a minimal GENERATING set, and ignoring the Second Fundamental Theorem (relations) when claiming "minimal" or "new"

**What goes wrong:**
Three distinct notions get blurred:
- a **spanning set** of a graded piece (e.g. all degree-2 invariants),
- a **generating set** of the ring (the FFT object — generators whose products span everything),
- a **minimal generating set** (no generator is a polynomial in the others).
The Reynolds-operator route (averaging monomials) yields a **redundant** spanning/generating set by design (Derksen–Kemper). Claiming a coupling generator is "new" (not expressible in lower-degree generators + products) requires knowing the **relations** — the Second Fundamental Theorem (SFT) ideal of syzygies. Without it, you can both over-count (list a "generator" that is actually a product of two lower ones) and under-count (miss a generator hidden behind a relation).

**Why it happens:**
"I found an invariant of degree d that I can't immediately write in terms of the others" is mistaken for "this is a new generator," skipping the check that it is not a polynomial in lower-degree generators.

**How to avoid:**
- Distinguish FFT (generation, in scope) from SFT (full syzygy ideal, OUT of scope — METHODS.md). (RING) needs generation + a degree-2 *minimality* statement only.
- For minimality at low degree, check whether each candidate generator lies in the subalgebra generated by lower-degree ones (a linear-algebra membership test in that bidegree), NOT a vague "looks irreducible" claim.
- Use the Hilbert series to detect both over- and under-counting (Pitfall 1).

**Detection test (runnable):**
```python
# Is candidate generator G_d at degree d genuinely new, or a product of lower-degree gens?
lower_products = span_of_products(gens_below_degree_d, target_bidegree(G_d))  # exact basis
assert not in_span(G_d, lower_products), "G_d is reducible (a product) -> NOT a new generator"
# Minimal-generator count must match (Hilbert series of free algebra on gens) vs (true H(s,t)).
assert hilbert_series(free_on(gens))[:deg 6] == true_hilbert_series[:deg 6]
```
Warning sign: a candidate generator whose bidegree already has its dimension fully accounted for by products of lower generators — it is not new.

**Phase to address:** The (a) generating-set phase (minimality sub-step).

---

### Pitfall 9 — [(a)/(c)] Confusing the 26 (trace-free irreducible) with the full 27 (= 1 ⊕ 26), and mishandling the reducible Tr(X)Tr(Y) when counting (1,1) couplings

**What goes wrong:**
The F_4 representation on h_3(O) is **27 = 1 ⊕ 26** (trivial ⊕ trace-free irreducible). Two errors follow from blurring these:
1. **Branching/multiplicity errors in (c):** if you compute Sym²(26) instead of Sym²(27), or forget the trivial summand, the trivial-multiplicity count is wrong. The correct counts (METHODS.md): Sym²(27) has trivial multiplicity 2; the bidegree-(1,1) part 27⊗27 has trivial multiplicity `dim End_{F_4}(1⊕26) = 1 + 1 = 2`, spanned by `Tr(X)Tr(Y)` (reducible product, the 1⊗1 piece) and `Tr(X∘Y)` (the genuine 26⊗26 → 1 coupling). Total degree-2 diagonal invariants = 6.
2. **Forgetting Tr(X)Tr(Y) is also a bidegree-(1,1) invariant in (c):** there are TWO invariant (1,1) couplings, not one. The uniqueness claim is "c is unique **modulo the reducible product Tr(X)Tr(Y) and the single-state terms**," not "c is the only (1,1) invariant." Stating it without the "mod products" qualifier is false.

**Why it happens:**
"The 27" and "the 26" are used interchangeably in physics-side prose; the trivial direction (the identity / Tr) is easy to drop.

**How to avoid:**
- Always carry 27 = 1 ⊕ 26 explicitly. The "1" is the Tr direction (identity element), the "26" the trace-free part.
- State (c) precisely: the genuine-coupling space at bidegree (1,1), *after quotienting the reducible product Tr(X)Tr(Y)*, is 1-dimensional = span{c}. Equivalently `dim Hom_{F_4}(26 ⊗ 26, triv)|_{symmetric} = 1` for the trace-free coupling.
- Cross-check dimensions: Sym²(26) = 1 ⊕ 26 ⊕ 324, dim 351 = 1+26+324 ✓; Sym²(27) = 378.

**Detection test (runnable):**
```python
# Branching/multiplicity must reproduce these exact integers (SageMath WeylCharacterRing('F4')):
assert mult_trivial(Sym2(rep27)) == 2          # Tr(X)^2 and Tr(X^2)
assert mult_trivial(tensor(rep27, rep27)) == 2  # Tr(X)Tr(Y) and Tr(X o Y)
assert dim(Sym2(rep27)) == 378
assert dim(Sym2(rep26)) == 351
# The (1,1) genuine-coupling space modulo the product is exactly 1-dim:
assert dim(span([Tr_XoY])) == 1
assert is_in_Rpt(Tr_X * Tr_Y)   # the OTHER (1,1) invariant is reducible, in R_pt
```
Warning sign: a Sym² dimension that doesn't match {351, 378}, or a (c) statement omitting "modulo Tr(X)Tr(Y)."

**Phase to address:** The (c) degree-2 uniqueness phase.

---

### Pitfall 10 — [(REDUCIBILITY), stated-only] Asserting irreducibility from "it's nonlinear, so it's chaotic," and conflating the AUTONOMOUS F_3-contraction (reducible) with the DRIVEN stream (the open-system source of irreducibility)

**What goes wrong:**
The milestone only STATES (REDUCIBILITY); it must not prove the open-system irreducibility, and must not use a chaos argument. Two banned moves (both named in PROJECT.md's reward-hacking guard):
1. "The self-modeling map is nonlinear ⇒ chaotic ⇒ irreducible." No chaos argument is valid here. The framework is invariant theory + (eventually) a STRUCTURAL finite-capacity / Breuer argument, never NKS/chaos.
2. Conflating the **autonomous** map `X_{k+1} = P_psd((1−ε)X_k² + εS_k)` with `S_k` fixed (a contraction to a fixed point — REDUCIBLE, reconstructible by re-running from (S, law)) with the **driven** stream where `S_k` is an exogenous input (the genuine open-system source of irreducibility). Using the autonomous map's reconstructibility to claim irreducibility "falsely kills the engine."

The cross-term decomposes (mod P_psd, via X_k∘X_k² = X_k³):
`Tr(X_k ∘ X_{k+1}) = (1−ε)Tr(X_k³)` [pointwise, reducible] `+ ε Tr(X_k ∘ S_k)` [self-world overlap, the irreducible piece]. Irreducibility is INHERITED from the input's unpredictability, NOT chaos of the autonomous map.

**Why it happens:**
"Nonlinear ⇒ chaotic ⇒ unpredictable ⇒ irreducible" is a seductive but invalid shortcut; and the autonomous fixed-point map is the natural thing to simulate, so it is easy to mistake its dynamics for the lived (driven) Stream's.

**How to avoid:**
- For THIS milestone, only STATE (REDUCIBILITY): write the cross-term decomposition and the capacity reduction as the precise target, flag the autonomous-vs-driven trap explicitly, and stop. Do not assert the open-system irreducibility.
- If a corollary is written, it must route to the structural (Breuer / no-proper-subsystem-models-the-whole / finite-capacity) argument — never to chaos or NKS.

**Detection test (conceptual, with a numerical canary):**
```python
# Canary: the AUTONOMOUS map (S fixed) must be shown REDUCIBLE (contraction to a fixed point),
# i.e. re-runnable from (S, law) -> NOT a source of irreducibility.
X = X0
for _ in range(N):
    X = P_psd((1-eps)*jordan_sq(X) + eps*S_fixed)   # S_fixed constant
assert converges_to_fixed_point(X)        # autonomous => reducible; do NOT cite as irreducible
# Statement gate (not a proof): the irreducible piece is eps*Tr(X_k o S_k) with S_k EXOGENOUS;
# this milestone STATES that and does not assert its incompressibility.
assert milestone_only_states_reducibility is True
```
Warning sign: any sentence of the form "nonlinear/complex ⇒ chaotic ⇒ irreducible," or a simulation of the fixed-`S` map used to argue the lived Stream is irreducible.

**Phase to address:** The "state the dynamical bridge" phase (final, do-not-attempt-the-verdict).

---

## Approximation Shortcuts

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
| --- | --- | --- | --- |
| Float `octonion_algebra.py` for the (b) Jacobian rank | Reuse the warm harness; fast | Tolerance-dependent rank ⇒ fabricated positive/negative (Pitfall 3) | NEVER for the decisive rank; OK only for a rough pre-check before the exact run |
| Single random point for the Jacobian | One substitution | Could be non-generic ⇒ false rank drop (Pitfall 4) | Only as a first look; the certificate needs ≥3 points or symbolic rank |
| Back-of-envelope Spin(8)-triality stabilizer count | No computation | Wrong Krull dimension ⇒ missing/phantom generators (Pitfall 5) | NEVER as the basis of a claim; compute the infinitesimal-action rank |
| Reynolds-operator generating set without minimality check | Quick dimension counts | Redundant generators mistaken for minimal (Pitfall 8) | OK as a spanning/dimension cross-check, not as the minimal list |
| Numerical Haar-average (random exp(f_4)) for invariant dimensions | Fast sanity check | Sampling/conditioning error; not a proof | OK to corroborate the exact f_4-kernel count, never to replace it |
| Hilbert series only to degree ≤ 4 | Cheaper | A surprise generator could hide at degree 5–6 | Only if a separate argument bounds generator degrees ≤ 4; otherwise go to ≤ 6 |
| Importing the E_6 4-generator pair result for F_4 | Clean, citable (Blind 2011) | E_6 ≠ F_4; F_4 ring is larger (has c) — wrong ring (Pitfall 1) | NEVER as the F_4 answer; only as a contrast case |

## Convention Traps

| Convention Issue | Common Mistake | Correct Approach |
| --- | --- | --- |
| Jordan product normalization | Using `XY` (matrix product) where `X∘Y = ½(XY+YX)` is meant; off-by-½ in c = Tr(X∘Y) | Fix `X∘Y = ½(XY+YX)` (harness `jordan_product`); note `Tr(X∘Y) = Re Tr(XY)` for Hermitian X,Y |
| Trace-form sign / normalization | Sign of the trace bilinear form `τ(X,Y) = Tr(X∘Y)`; some sources use `−` or a factor | Pin `c(X,Y) = Tr(X∘Y)`, positive-definite on the formally-real h_3(O); verify `c(X,X) = Tr(X²) > 0` for X ≠ 0 (harness `det_2`/Gram already fix signs) |
| det / cubic norm convention | Conflating Jordan `det X = N(X)` with naive octonionic "determinant"; wrong factor in `det X = (1/3)Tr(X#∘X)` | Use the Freudenthal/Springer cubic norm; verify `f(X,X,X) = 6 det X` numerically before polarizing (PRIOR-WORK caution) |
| Sharp/cross product `×` ambiguity | Freudenthal product vs sharp-polarization `X×Y = (X+Y)#−X#−Y#` differ by trace-term shifts and a factor; both circulate as "×" | Fix the sharp-polarization (gives `f(X,Y,Z) = ⟨X×Y,Z⟩` directly, Springer 1973 ch.4 (5) p.56); verify in harness |
| 26 vs 27 | Treating "the 27" as irreducible; using Sym²(26) where Sym²(27) is needed | Carry `27 = 1 ⊕ 26`; the 1 is the Tr/identity direction (Pitfall 9) |
| Group: F_4 vs E_6 | Using E_6 (det-stabilizer) results where F_4 = Aut (also fixes the trace form) is meant | F_4 ⊋-invariants include the trace-form coupling c, which is NOT E_6-invariant (PRIOR-WORK) |
| Faraut–Korányi citation chapter | Citing "FK Ch. V" for the single-state ring | FK Ch. V is the *classification*; the norm/trace/invariant-ring facts are in Ch. II–IV (+ VIII), per PRIOR-WORK correction |
| "Polarization" overload | "Weyl polarization holds in char 0" used to mean "from 1 copy" | Weyl's theorem goes from `dim V = 27` copies; "from 1 copy" is the *k-polarization property* (Schwarz), generically false even in char 0 (Pitfall 1) |

## Numerical Traps

| Trap | Symptoms | Prevention | When It Breaks |
| --- | --- | --- | --- |
| Float Jacobian rank | Rank changes with `tol`; integer-looking rank that is an SVD artifact | Exact `sympy.Matrix.rank()` over Q; never `np.linalg.matrix_rank` for the decisive check | Always at the rank boundary for 54-variable octonionic determinants |
| Non-generic evaluation point | Rank differs between random points; rank 6 at X=Y | ≥3 generic rational points, all-nonzero, distinct diagonals, X ≠ λY | Whenever the point lands on the discriminant / diagonal / commuting locus |
| Large integer coefficient blow-up | SymPy slows or memory-spikes building det in 54 vars | Substitute the rational point EARLY (before full symbolic expansion) when only the point-rank is needed; or use modular rank over a large prime then lift | Full symbolic cubic-norm expansion on 54 variables |
| `np.linalg.matrix_rank` default tol on the orbit-action matrix | Wrong orbit dimension ⇒ wrong stabilizer (Pitfall 5) | Exact rank, or high-precision SVD with an explicit, justified gap check | Near-degenerate infinitesimal-action matrices at semi-generic X |
| Reynolds Haar-average non-convergence | Invariant-dimension estimate fluctuates with sample size | Use the exact f_4-infinitesimal-kernel (`D_ξ f = 0` for all 52 ξ) instead of group sampling | Always — sampling is a cross-check, not a certificate |
| Modular-arithmetic rank with an unlucky prime | Rank drops at a prime dividing a minor | Use a large random prime AND confirm exact rank agrees; or compute over Q | Rare, but silent — always cross-check the prime |

## Interpretation Mistakes

| Mistake | Risk | Prevention |
| --- | --- | --- |
| "rank 7 ⇒ all 7 generators algebraically independent" | False over-claim; the *ring's* Krull dim is `54 − orbit dim`, not 7 | Claim only the true, weaker statement: c ∉ R_pt (trdeg jump 6→7), NOT joint algebraic independence of all 7 (METHODS.md "What NOT to use") |
| "c is the unique (1,1) invariant" | False — Tr(X)Tr(Y) is also (1,1) | State "unique modulo the reducible product Tr(X)Tr(Y) and single-state terms" (Pitfall 9) |
| "polarization works in char 0 ⇒ (a) is trivial" | Hides the 2-polarization-property gap (Pitfall 1) | The Hilbert-series certificate IS the content of (a) |
| "Spin(8) generic stabilizer ⇒ pair-orbit is 52-dim" | Contradicts 7 known invariants; corrupts Krull dim | Compute the pair principal isotropy in the harness (Pitfall 5) |
| Reading the autonomous fixed-point convergence as "irreducible" | Falsely kills/credits the engine (Pitfall 10) | Autonomous map is REDUCIBLE; irreducibility (if any) is open-system, only STATED |
| Treating a NEGATIVE (c ∈ R_pt) as a failure to hide | Suppresses a valid, decisive result | A clean negative is a full pass; construct the explicit expression and report it (Pitfall 6) |
| Equating "functionally independent" with "algebraically independent" | Wrong notion; the claim is "c is not a polynomial in the six" | Use the precise statement c ∉ R_pt; the Jacobian rank-jump is its checkable form (METHODS.md (b)) |

## "Looks Correct But Is Not" Checklist

- [ ] **(a) generating set:** Often missing the *completeness certificate* — verify the bigraded Hilbert series matches term-by-term to total degree ≤ 6, not just "we polarized and got some generators."
- [ ] **(a) minimality:** Often missing the *reducibility check* — verify each "new" generator is not a product of lower-degree ones (in-span test in its bidegree).
- [ ] **(b) independence:** Often missing the *exact-arithmetic* run — verify the rank is computed over Q (point-rank == symbolic rank), not via float SVD with a tolerance.
- [ ] **(b) genericity:** Often missing *multiple points* — verify rank 7 at ≥3 independent generic rational points, and that X=Y correctly gives ≤6.
- [ ] **(b) orbit dimension:** Often missing the *computed* stabilizer — verify the pair-orbit dimension from the infinitesimal-action rank, not a triality back-of-envelope; cross-check `54 − orbit dim = Krull dim`.
- [ ] **(c) uniqueness:** Often missing the *"modulo products"* qualifier and the *Tr(X)Tr(Y)* term — verify the (1,1) invariant space is 2-dim {Tr(X)Tr(Y), c} and the genuine-coupling quotient is 1-dim.
- [ ] **Definitions:** Often missing a *frozen* R_pt — verify the same membership predicate for the pointwise ring is used identically in (a), (b), (c).
- [ ] **Conventions:** Often missing the *f(X,X,X)=6 det X* and *c(X,X)=Tr(X²)* sanity checks — verify both numerically before building anything on the cubic norm.
- [ ] **(REDUCIBILITY):** Often missing the *autonomous-vs-driven* flag — verify the write-up only STATES it and routes any irreducibility to a structural (Breuer/finite-capacity) argument, never chaos.

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
| --- | --- | --- |
| Float Jacobian gave wrong rank (P3) | LOW | Port `jordan_product`/`det_3` to `sympy.Rational` (or reuse `embedding_under_E_verification.py`); rerun `Matrix.rank()` over Q |
| Non-generic point gave rank 6 (P4) | LOW | Regenerate point with all-nonzero, distinct-diagonal, X≠λY entries; rerun at ≥3 points |
| Wrong stabilizer/Krull dim (P5) | MEDIUM | Recompute the 54×52 infinitesimal-action rank exactly; re-target the Hilbert series to `54 − orbit dim`; re-audit (a) completeness |
| 2-polarization assumed, generator missing (P1, P8) | MEDIUM–HIGH | Run the bidegree Hilbert-series match; at the first mismatch, find the missing generator by Reynolds-projecting that bidegree; add and recheck |
| Sym² multiplicity miscount (P9) | LOW | Recompute via `WeylCharacterRing('F4')`; reconcile against {351, 378} and the 6-dim degree-2 invariant total |
| Forced positive later found spurious (P6) | MEDIUM | Re-run exact on a fresh point + orbit-derivative; if rank is really 6, construct and report the explicit pointwise expression for c |
| Convention drift (∘ vs matrix product, × ambiguity, det factor) | LOW–MEDIUM | Re-pin conventions; re-verify `f(X,X,X)=6 det X`, `c(X,X)=Tr(X²)`; propagate the fix through all generators |
| Chaos/NKS argument crept into (REDUCIBILITY) (P10) | LOW | Delete the chaos claim; restate as STATED-only with the structural (Breuer) route flagged |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
| --- | --- | --- |
| P7 frozen R_pt definition | Setup/Definitions (before a,b,c) | Same membership predicate cited in all three sub-claims; boundary cases (Tr X·Tr Y in, c under test) pass |
| P1 Weyl-vs-k-polarization; 2-polarization gap | (a) Generating set | Bigraded Hilbert series matches term-by-term to total degree ≤ 6 |
| P8 spanning vs minimal generating; SFT | (a) Generating set (minimality) | Each generator fails the in-span-of-lower-products test; free-algebra Hilbert series matches |
| P2 orbit/Jacobian asserted not demonstrated | (b) Independence | Both rank-7 Jacobian AND nonzero orbit-derivative of c present, on the exact algebra |
| P3 float rank | (b) Independence | `J.subs(pt).rank() == J.rank()` over Q; float gap-ratio canary > 1e6 |
| P4 non-generic point | (b) Independence | rank == [7,7,7] at 3 points; X=Y gives ≤6 |
| P5 stabilizer/Krull-dim miscount | Shared dimension-count (feeds a & b) | single-copy: orbit 24 / stab 28 / trdeg 3; pair: orbit ≤ 47, stab ≥ 5, `54−orbit = Krull dim` |
| P6 forced positive over honest negative | (b) Independence (verdict gate) | Pre-registered exact test; if rank 6, explicit pointwise expression constructed and reported |
| P9 26-vs-27; reducible (1,1) product | (c) Degree-2 uniqueness | mult_trivial(Sym²27)=2, mult_trivial(27⊗27)=2; Sym² dims {351,378}; (1,1) genuine-coupling quotient = 1-dim |
| P10 chaos/autonomous-vs-driven | (REDUCIBILITY) statement (final) | Write-up STATES only; autonomous map shown reducible; irreducibility routed to structural argument |

## Sources

- **G. W. Schwarz**, "When Polarizations Generate," arXiv:math/0609078 (2006); *Transform. Groups* 12 (2007) 761–767. — Classifies which simple G and modules V have the **k-polarization property** `pol_k(V)^G = C[kV]^G`; "most representations do **not** have the 2-polarization property" *even over C*. **THE citation that polarizing single-copy generators need not generate the pair ring in char 0** (Pitfall 1, 8). [verified, text extracted]
- **M. Domokos, G. Kemper**, "Weyl's Polarization Theorem in Positive Characteristic," arXiv:1803.03602; *Transform. Groups* (2020). — Weyl strong form (Thm 1.3): in char 0, polarizing a generating set of `K[V^n]^G` (n = dim V) generates `K[V^m]^G` for m ≥ n, for all reductive G; weak form (Thm 1.2): `β(K[V^m]^G) ≤ β(K[V^n]^G)`. Confirms the "from dim-V copies" framing and the char-0 validity for reductive (incl. exceptional) groups; positive-characteristic failures and the *separating-invariant* analogue. [verified, text extracted]
- **J. Draisma, G. Kemper, D. Wehlau**, "Polarization of Separating Invariants," *Canad. J. Math.* — polarizing a SEPARATING set yields a generating set of vector invariants **only in char 0**; a characteristic-free analogue holds for *separating* (not generating) invariants. Sharpens the separating-vs-generating distinction (Pitfall 8). [verified via search summary]
- **H. Derksen, G. Kemper**, *Computational Invariant Theory*, Springer (2002; 2nd ed. 2015). — Jacobian criterion (char 0: trdeg = generic Jacobian rank; the "dependent ⇒ rank-deficient" direction holds in ALL char, so a rank-7 result is decisive), Reynolds operator yields redundant generators, Derksen algorithm, Hilbert/Molien series. (Pitfalls 2, 3, 8) [canonical reference]
- **Garibaldi, Guralnick**, "Generic Stabilizers for Simple Algebraic Groups," arXiv:2105.09486 (2021). — s.g.p. of F_4 on the 26 = **Spin(8)** (Lemma 8.1, dim 28); `dim k[V]^G = dim V − dim G` when `dim V > dim G` (Thm 1.3). Anchors the single-copy orbit count (24) and trdeg (3); the PAIR principal isotropy must be computed, not read off (Pitfall 5). [verified in PRIOR-WORK]
- **B. Blind**, "Algèbres de Jordan et théorie des invariants," *J. Lie Theory* 21 (2011) 123–144 (arXiv:0906.5525). — `C[27⊕27]^{E_6}` is FREE on 4 det-polarizations (Thm 3.1, Vust method). The **E_6 contrast case**; F_4 (= Aut, also fixing the trace form) has a larger pair ring including c — do NOT import the E_6 cleanliness (Pitfall 1, convention trap). [verified in PRIOR-WORK]
- **A. V. Iltyakov**, "Laplace Operator and Polynomial Invariants," *J. Algebra* 207 (1998) 256–271. — F_4 several-copy invariants via trace polynomials + Laplace operators; m ≤ 2 Artin–Procesi–Iltyakov equality (rational F_4-invariants = Frac(trace algebra)). Supports c being a needed trace-monomial generator (Pitfall 1, 8). [verified in PRIOR-WORK]
- **T. A. Springer**, *Jordan Algebras and Algebraic Groups*, Ergebnisse der Math. 75, Springer (1973); **Springer–Veldkamp**, *Octonions, Jordan Algebras and Exceptional Groups*, Springer (2000). — cubic norm structure, sharp/cross product, `f(X,Y,Z)=⟨X×Y,Z⟩` (1973, ch.4 (5) p.56); F_4=Aut, E_6=Stab(det). Authority for the convention traps (sharp/× ambiguity, det factor). [verified in PRIOR-WORK]
- **J. Faraut, A. Korányi**, *Analysis on Symmetric Cones*, Oxford (1994). — Euclidean Jordan algebras; trace, trace form `τ(x,y)=tr(x∘y)`, cubic norm; single-state invariant ring. **Chapter correction:** the norm/trace/invariant-ring facts are in Ch. II–IV (+ VIII), NOT Ch. V (= classification) — per PRIOR-WORK (convention trap). [verified in PRIOR-WORK]
- **Milestone prompt** (`phi-reducibility-lemma-prompt.md`) and **PROJECT/research context** — the five reward-hacking traps verbatim (redefine reducible/pointwise; nonlinear⇒chaotic; autonomous-vs-driven; assert independence without orbit/Jacobian; force a positive over an honest negative). [authoritative for Pitfalls 2, 6, 7, 10]
- **Sibling research files** `.gpd/research/METHODS.md` (the proof recipes these pitfalls guard) and `.gpd/research/PRIOR-WORK.md` (literature verdict; Open Q #4 = the pair principal-isotropy count flagged as the single most important numerical check). [internal, HIGH]
- **Harness reality check** — `code/octonion_algebra.py` is **float64** (no SymPy); the EXACT SymPy h_3(O) layer is `code/embedding_under_E_verification.py` / `tests/test_embedding_under_E.py` (v15.0 warm harness). The (b) rank MUST run on the exact layer (Pitfall 3). [verified by inspection]

---

_Known pitfalls research for: v16.0 (RING) lemma — joint F_4-invariants of 27 ⊕ 27._
_Researched: 2026-05-24. Confidence HIGH on invariant-theory failure modes and the five reward-hacking traps; the load-bearing refinement is Pitfall 1 (Weyl's theorem needs dim-V copies; the single-copy "2-polarization property" generically FAILS even in char 0 — Schwarz), which sharpens METHODS.md's char-0 claim into a Hilbert-series certificate obligation._
