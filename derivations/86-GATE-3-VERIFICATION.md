# Phase 86 — GATE 3 Independent Verification (B3 the sourced field equation + the lambda_2 cross-check)

**Verifier:** independent (separate code path + from-scratch re-derivation + external literature cross-check)
**Date:** 2026-06-11
**Milestone:** v26.0 Phase 86 — "The Sourced Field Equation," J5-on-the-variety step 2

**Verdict: B3 CONFIRMED. Confidence HIGH. The external lambda_2(OP^2)=104 anchor HOLDS (ratio 13/6 matches the Cayley-plane spectrum k(k+11) exactly).**

(B4 hidden-sector also re-derived from scratch — CONFIRMED — recorded at the end.)

---

## The claim

`Sym²(26) = 1 + 26 + 324` under F₄; the only quadratic covariants of traceless M are `M#` and `TrM²·1` (since `M² = M# + (1/2)TrM²·1`). Hence
```
<M,p>² = alpha·<M#,p> + beta·TrM² + R_M(p),   R_M a level-2 (lambda_2) eigenfunction,
```
with `(alpha, beta, lambda_2)` fixed by an **overdetermined** symbolic solve (consistency IS the claim). Then
```
(Delta + lambda_1) G_M = -kappa_0·TrM² + ((lambda_2 - lambda_1)/4)·R_M,
   kappa_0 = lambda_1·(1/6 - alpha/24 + beta/4).
```
Pre-registered: `(alpha,beta,lambda_2) = (1/7, 9/182, 104)` on OP², `(2/5, 3/20, 32)` on the CP² cut; `kappa_0 = 108/13` (OP²), `9/4` (cut).

---

## What was run

1. **Executor** → Gate 3 **ALL PASS** (4 checks): OP² solve `(1/7,9/182,104)`, cut solve `(2/5,3/20,32)`, sourced-eq identity + R_M eigenfunction on both spaces, covariance closure.
2. **Independent verifier** (grad-N M#, independent solve) → OP² `(1/7,9/182,104)`; `lambda_2` eigenfunction re-derived at a **second, non-E11 point** by covariance; CROSS closed-form cross-check. PASS.
3. **From-scratch** `/tmp/v86_scratch.py` (my own octonions + adjugate M#, two products) → the level split, kappa_0, and the sourced-equation identity all reproduce on **both** octonion products. **PASS.**
4. **Raw-system probe** `/tmp/v86_probe.py` — opened the uncollapsed 26-symbol polynomial identity to confirm the over-determination is genuine (below).

---

## The over-determination is GENUINE (the central adversarial finding)

This is the most important thing I re-derived independently. The level-split identity `L - rhs = 0`, where `L = Delta[<M,.>²](E11)` over the 16-frame, is a polynomial identity in **all 26 M-params**. Expanding it produces **27 monomial coefficients**, each of which must vanish. They collapse to exactly **3 distinct equations** (OP², lambda_1=48):

| monomial block (M-params) | meaning | coefficient (must = 0) |
|---|---|---|
| `p0²` | the E11-visible/diagonal moment | `16·alpha - 2·beta·lambda_2 + lambda_2 - 96` |
| `p0p1, p1², …, p9²` | diag + (2,3)-block octonion | `alpha·lambda_2 - 32·alpha - 2·beta·lambda_2` |
| `p10²…p25²` | the V_{1/2} block (16 dirs) | `16·alpha - 2·beta·lambda_2 + 8` |

**Three different equations in three unknowns, all forced simultaneously by 27 monomials.** The decisive structural fact (re-derived by hand):
```
(p0² eqn) - (V_{1/2} eqn) = lambda_2 - 104  = 0   =>   lambda_2 = 104   FORCED, independent of (alpha,beta).
```
So `lambda_2` is pinned **before** `(alpha,beta)` are solved — by the difference between the E11-visible monomial and the V_{1/2}-block monomial. This is exactly the over-determination: the off-u directions, which are *invisible at first order* (`<M,E11>²` sees only `p0`), still constrain `lambda_2` through `L` and `TrM²`. Then `(alpha,beta) = (1/7, 9/182)` from the remaining two equations.

**Adversarial confirmation:** forcing `lambda_2 ∈ {100, 104, 108}` and solving for `(alpha,beta)`:
- `lambda_2=100` → **INCONSISTENT** (no solution)
- `lambda_2=104` → consistent
- `lambda_2=108` → **INCONSISTENT**

Only `lambda_2=104` leaves `(alpha,beta)` solvable. **Consistency is the claim; it is not a fit.** If `(alpha,beta,lambda_2)` failed to exist, B3 would fail — they exist uniquely.

**Is 104 hardwired anywhere?** No. `grep` of the solve path: `lambda2` enters the solver as a free `symbols("...")` unknown; the literal `104` appears only in `== 104` *assertions on the solver's output* (and in the verifier's `4k(k+11)` cross-check, which is a separate external comparison, not fed into the solve). My from-scratch unconstrained `sp.solve` returns `{al:1/7, be:9/182, l2:104}` with `104` never supplied.

---

## The sourced field equation + kappa_0 (re-derived from scratch, both products)

```
kappa_0(OP²) = 48·(1/6 - (1/7)/24 + (9/182)/4) = 108/13     ✓
kappa_0(cut) = 12·(1/6 - (2/5)/24 + (3/20)/4)  = 9/4         ✓
```
The exact identity `(Delta + lambda_1)G_M = -kappa_0·TrM² + ((lambda_2-lambda_1)/4)·R_M` holds at E11 for **symbolic traceless M** on both OP² and the cut, and `R_M` is verified to be a genuine `lambda_2`-eigenfunction (`Delta R_M(E11) = -lambda_2·R_M(E11)`). Covariance closes the E11 identity to all p (spot-checked with an exact (01) rotation). **INDEPENDENTLY CONFIRMED.** This is an EXPLICIT exact identity with derived constants (trap #6 exemption is legitimate — not an annihilator-existence claim).

The Gate-1 c11² control gives an independent `lambda_2=104` path **given** the master `(alpha,beta)` (I re-checked: `M0=E11-I/3` has level-2 part `R_E=36/91 ≠ 0`, and `lambda_2` solves to 104). This is a conditional independent check; the from-scratch triple solve is the unconditional one. Both agree.

---

## Cut-vs-mother spectral table (re-derived)

| space | lambda_1 | lambda_2 | lambda_2 - lambda_1 | **lambda_2/lambda_1** | (alpha, beta) |
|---|---|---|---|---|---|
| CP² cut | 12 | 32 | 20 | **8/3** | (2/5, 3/20) |
| OP² | 48 | 104 | 56 | **13/6** | (1/7, 9/182) |

---

## External cross-check: lambda_2(OP²) = 104 vs the Cayley-plane spectrum

The one genuinely underived number is `lambda_2(OP²)`. Cross-checked against the literature closed form for the scalar Laplacian on the Cayley plane OP² = F₄/Spin(9):

- **Literature (confirmed from multiple independent sources):** the scalar Laplace–Beltrami spectrum is `lambda_k = k(k+11)`, k ∈ ℤ≥0, in the standard normalization (Ricci scalar R=144). [Cayley plane = F₄/Spin(9), dim 16, rank-1 symmetric space; eigenfunctions are normalized Jacobi polynomials.] CP² Fubini–Study is `lambda_k = k(k+2)`.
- **Repo normalization:** `4k(k+11)` on OP² and `4k(k+2)` on CP². The overall **factor of 4** is the repo's geodesic chart normalization (unit-speed `t=tan(θ/2)`): it multiplies *every* eigenvalue equally (it already shows up at level 1: repo lambda_1(OP²)=48=4·12=4·1·12, lambda_1(cut)=12=4·3=4·1·3 vs literature 12 and 3).

**The normalization-independent invariant is the ratio**, and it matches exactly:
```
lambda_2/lambda_1 (OP²) = 26/12 = 13/6   [literature k(k+11): 12 → 26]   ==  repo 104/48 = 13/6   ✓
lambda_2/lambda_1 (CP²) =  8/3           [literature k(k+2):   3 →  8]   ==  repo  32/12 = 8/3    ✓
lambda_1(OP²)/lambda_1(CP²) = 12/3 = 4 = 16/4 dim ratio  ==  repo 48/12 = 4                       ✓
```
The "+11" in the Cayley-plane formula is exactly the source of the 13/6 ratio (the "+2" gives CP²'s 8/3). The derived `104` is the literature `2·13 = 26` rescaled by the same factor-of-4 that fixes lambda_1=48. **The external anchor HOLDS** (non-blocking, as pre-registered, but a strong corroboration of the one underived number).

Sources:
- [Functional determinant of Laplacian on Cayley projective plane P²(Cay) — IAS / Proc. Math. Sci. (k(k+11), R=144)](https://link.springer.com/article/10.1007/s12044-019-0503-y)
- [Cayley plane — Wikipedia (F₄/Spin(9), dim 16)](https://en.wikipedia.org/wiki/Cayley_plane)
- [Stability of Einstein metrics on symmetric spaces of compact type (OP² rank-1 data)](https://www.researchgate.net/publication/356566394_Stability_of_Einstein_metrics_on_symmetric_spaces_of_compact_type)

---

## B4 — hidden sector (re-derived from scratch)

For off-u M (octonion directions e₁..e₆ only, 18 params):
- **(invisibility)** `<M,p> = 0` for E11 and all 4 cut families over Q(t) — verified from scratch. The hidden matter has no first-order moment on the cut.
- **(still sources)** `G_M|cut = <M#,p> = -(h0²+…+h5²) ≠ 0` for M≠0 — the squares land on the diagonal/C_u. Verified.
- **(square-free)** the `-(1/4)<M,p>²` term vanishes identically on the cut → cut source is level ≤ 1, no anisotropic signature. Verified.

**B4 CONFIRMED.**

---

## Discrepancies

- **None of substance.** The "3 overdetermined eqs" wording (executor + my own count) is accurate: 27 monomials collapse to 3 distinct equations, and the over-determination is real (the lambda_2 = 104 constraint `e1-e3` is independent of and redundant-consistent with the (alpha,beta) constraints; forcing the wrong lambda_2 breaks the system). The factor-of-4 between the repo's `4k(k+11)` and the literature `k(k+11)` is a metric normalization that cancels in every ratio — not a discrepancy.

## Confidence

**HIGH.** `(alpha,beta,lambda_2) = (1/7, 9/182, 104)` reproduced on three code paths and two independent octonion algebras; the over-determination verified at the raw-monomial level with `lambda_2=104` forced by `e1-e3` independent of `(alpha,beta)`; adversarial wrong-lambda_2 confirmed inconsistent; `kappa_0=108/13` and the sourced-equation identity exact over Q for symbolic M; and the external Cayley-plane ratio 13/6 matches `k(k+11)` exactly.

**B3 CONFIRMED.**
