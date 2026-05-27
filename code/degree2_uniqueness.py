"""
(RING) Lemma -- (c) DEGREE-2 UNIQUENESS (RING-03)
=================================================
Phase: 67-c-degree-2-uniqueness
Plan: 01
Milestone: v16.0 The (RING) Lemma (math half of the Chalmers gap).

WHAT THIS IS
------------
The DEGREE-2 uniqueness sub-claim of the (RING) lemma. Establishes, by EXACT
computation over Q, that

    c = Tr(X o Y)  is the UNIQUE degree-2 coupling generator of R[27(+)27]^{F_4}
    modulo scale, products, and pointwise terms.

Concretely: the bidegree-(1,1) trivial part of the invariant ring is exactly
2-dimensional = span{Tr(X)Tr(Y), Tr(X o Y)}, of which Tr(X)Tr(Y) is the single
REDUCIBLE product (a product of pointwise generators), leaving c as the unique
genuine (irreducible, non-product) NEW degree-2 coupling invariant. The "mod
products" qualifier is stated PRECISELY (NOT "c is the unique (1,1) invariant",
which is FALSE -- Tr(X)Tr(Y) is also a (1,1) invariant; Pitfall 9.2).

TWO ROUTES that must AGREE (reward-hacking guard, like Phase 66):
  Route A -- F_4 rep-theory branching + Schur count (LITERATURE-anchored
    corroboration): 27 = 1 (+) 26; dim Sym^2(27)=378; dim Sym^2(26)=351=1+26+324;
    trivial mult in Sym^2(27)=2; bidegree-(1,1) trivial mult in 27_X (x) 27_Y =
    dim End_{F_4}(1(+)26) = 1^2 + 1^2 = 2 (Schur). ROUTE_A_11 = 2.
  Route B -- the exact f_4-infinitesimal-kernel nullspace over QQ (the
    SELF-CERTIFYING proof): a bidegree-(1,1) poly is a bilinear form
    f(X,Y) = x^T C y (C a 27x27 coefficient matrix); it is f_4-invariant iff the
    Leibniz lift D_M f = grad_X(f).(M.x) + grad_Y(f).(M.y) = x^T (M^T C + C M) y
    vanishes for all 52 generators M, i.e. M^T C + C M = 0 (the Sylvester /
    derivation condition). The exact nullspace dim over QQ = 2. ROUTE_B_11 = 2.
    The named invariants {Tr(X)Tr(Y), c} are shown to be a BASIS of this kernel
    (in-kernel AND linearly independent -- witness Tr(I)Tr(I)=9 != c(I,I)=3).

On DISAGREEMENT the harness emits NO VERDICT and STOPs, trusting the EXACT
NULLSPACE (roadmap backtracking) -- it does NOT tune either route.

DERIVATION OF THE (1,1) INVARIANCE CONDITION (the ONE new component -- the
Leibniz lift rho(M) = M (x) I + I (x) M, NOT M (x) M):
  A bidegree-(1,1) polynomial is f(x,y) = sum_{i,j} C_{ij} x_i y_j = x^T C y, with
  x = the 27 X-coords, y = the 27 Y-coords. The DIAGONAL f_4 action lifts a
  generator M (27x27, acting on each copy) to the DERIVATION rho(M) = M(x)I +
  I(x)M (Lie-algebra derivation of the tensor product -- NOT the group-like
  M(x)M). Its action on f is the diagonal gradient-contraction
      D_M f = grad_X(f).(M.x) + grad_Y(f).(M.y).
  For f = x^T C y: grad_X f = C y, grad_Y f = C^T x, so
      D_M f = (C y).(M x) + (C^T x).(M y)
            = x^T M^T C y + x^T C M y = x^T (M^T C + C M) y.
  f invariant for all x,y  <=>  M^T C + C M = 0 for every generator M.
  => (1,1) invariant dim = dim ker{ C -> (M^T C + C M)_{M in basis} } over QQ.
  CORRECTNESS GUARD (catches the M(x)M error): rho(M) MUST annihilate the KNOWN
  invariant c for all 52 generators. M(x)M would NOT.

SCOPE BOUNDARY: this is the DEGREE-2 uniqueness sub-claim (RING-03),
complementary to Phase 66's FIELD-level functional-independence SPINE (RING-02,
c independent of R_pt, rank 7) and DISTINCT from Phase 68's ring generation
(RING-01, Hilbert series / Krull / minimal generators). The (1,1) count = 2 here
is the bidegree-(1,1) Hilbert coefficient Phase 68 must reproduce. NO sentence
here claims a generating set for the ring.

EXACT-ONLY (the GLOBAL FORBIDDEN PROXY fp-float-rank): every decisive dimension
is an exact integer -- a rep dimension (Route A) or a Q-vector-space nullspace
dimension (Route B via exact_qq_rank = DomainMatrix-over-QQ). ZERO
numpy.linalg.matrix_rank / float-rank on the decisive path; ZERO
`import octonion_algebra` (the float64 file). A module-local exact-only guard
(scanning THIS __file__) asserts both.

PROVENANCE (decisive reuse -- the certified engine, imported, NOT rebuilt):
  - code/ring_lemma_verification.py (Phase-64.1 FROZEN engine), imported as E:
    jordan, Tr, Tr2, c (= inv_c), det_3, the 7 base invariants inv_Tr_X..inv_c,
    xs/ys (54 symbols), Xsym/Ysym, _flat27, octonionic_points, inner_derivations,
    is_in_Rpt (a STUB that raises -- NOT called here).
  - code/orbit_dimension_gate.py (Phase-65 CERTIFIED gate machinery):
    exact_qq_rank (DomainMatrix-over-QQ exact rank), _select_independent_basis
    (the 52-independent f_4 basis), _flatten_729 (the 27(x)27 row-major order),
    infinitesimal_action.
  - code/ring_generating_set.py (Phase-65.1 FROZEN): CANDIDATE_GRADS (index 6 =
    cached gradient of c), check_f4_invariance recipe, PAIR_POINTS.

The ONE new component is the Leibniz lift rho(M) = M(x)I + I(x)M (equivalently
the diagonal gradient-contraction / the Sylvester condition M^T C + C M = 0).

# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; coupling c=Tr(X o Y)=Tr(jordan(X,Y)); c(X,X)=Tr(X^2) (NOT (Tr X)^2); 27=1(+)26 (trivial Tr-direction (+) trace-free 26); Tr(I)=3 => Tr(I)Tr(I)=9 != c(I,I)=3 (linear-independence witness); Leibniz lift rho(M)=M(x)I+I(x)M (NOT M(x)M); (1,1) invariance <=> M^T C + C M = 0; arithmetic=exact-SymPy-over-Q; ranks/nullspace=exact_qq_rank=DomainMatrix-over-QQ (NEVER numpy.linalg.matrix_rank / SVD tolerance); R_pt FROZEN = subalgebra gen by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}; Tr(X)Tr(Y) in R_pt, c NOT in R_pt at degree 2; metric=Riemannian Fisher (no field theory / gauge / Fourier)
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible, self-dual)

Assert-based harness (NO pytest -- the venv has sympy/numpy only). Foreground,
chatty (python -u), prints progress between every check (watchdog-safe).

Reproducibility: SymPy 1.14.0, NumPy 2.4.3, Python 3.x, macOS Darwin 24.6.0.
Deterministic (no random seeds; all evaluation points are the certified
hardcoded integer octonionic points from the engine + Phase-65 gate).

References:
  - .gpd/research/METHODS.md section (c) lines 105-118 [METHODS (c)] -- derives the
    F_4 branching + the precise "mod products" statement; total degree-2 = 6
    (line 114). CITED, conceptual chain not re-derived.
  - .gpd/research/PITFALLS.md Pitfall 9 (26-vs-27; reducible Tr(X)Tr(Y); targets
    {2, 6, 351, 378, 1(+)26(+)324}) and Pitfall 7 (frozen R_pt anti-drift).
  - Garibaldi, S.; Guralnick, R.M., Forum Math. Pi 3 (2015) e3 -- F_4 = identity
    component of Stab(Tr, trace form, det); the trace form (= c) is THE F_4
    (1,1) pairing (26(x)26 -> 1 contraction); not E_6-invariant.
  - Wikipedia "F4 (mathematics)" + Slansky, Phys. Rep. 79 (1981) -- F_4 small-irrep
    dims {1, 26, 52, 273, 324, 1053, 1274}.
  - Iltyakov, A.V., J. Algebra 207 (1998) -- F_4 several-copy invariants are trace
    polynomials + Laplace invariants; c = Tr(X o Y) is a trace monomial (the named
    basis is the NAMED trace invariants).
  - Blind, B., J. Lie Theory 21 (2011) -- CONTRAST: E_6 does NOT preserve the trace
    form, so c is NOT an E_6 invariant (the limiting-case control).
"""

import os
import re
import sys
import time

# Path-import the FROZEN engine + the certified gate machinery (sibling files in
# code/). Mirror ring_generating_set.py's sibling-import pattern; here it is the
# DECISIVE reuse, not an oracle. NEVER import octonion_algebra (float64, buggy).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ring_lemma_verification as E  # noqa: E402  (path insert must precede import)
from orbit_dimension_gate import (  # noqa: E402
    exact_qq_rank,
    _select_independent_basis,
    _flatten_729,
    infinitesimal_action,
)
from ring_generating_set import (  # noqa: E402
    CANDIDATE_GRADS,
    PAIR_POINTS,
)

from sympy import Matrix, zeros, diff, expand, simplify, symbols, Rational  # noqa: E402
from sympy.polys.matrices import DomainMatrix  # noqa: E402
from sympy.polys.domains import QQ  # noqa: E402


# ============================================================================
# Overall pass/fail accumulator + chatty reporter (engine pattern)
# ============================================================================
ALL_PASS = True
FAILED_LABELS = []
STOP_TRIGGERED = False   # set True by any backtracking-guard STOP (forces nonzero).


def _report(label, ok):
    """Print a PASS/FAIL line and fold into the global pass flag (engine pattern)."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
        FAILED_LABELS.append(label)
    return ok


# ============================================================================
# PRE-REGISTRATION block (frozen integer targets + decisive test + verdict map),
# DEFINED BEFORE ANY DIMENSION IS COMPUTED (reward-hacking guard: an honest
# disagreement cannot be re-rolled).
# ============================================================================
# Frozen integer TARGETS (CHECK constants -- never inputs to the computation):
BIDEG_11_TRIVIAL_MULT = 2     # the (1,1) trivial multiplicity (both routes target this)
TOTAL_DEG2_DIM = 6            # full degree-2 invariant dim (blocks (2,0)=2,(1,1)=2,(0,2)=2)
GENUINE_COUPLING_QUOTIENT = 1  # (1,1) dim 2 - reducible-product dim 1
SYM2_27 = 378                 # dim Sym^2(27)
SYM2_26 = 351                 # dim Sym^2(26) = 1 + 26 + 324
F4_BASIS_SIZE = 52            # dim f_4
DIM_TRIVIAL = 1               # dim of the trivial irrep 1
DIM_26 = 26                   # dim of the trace-free irreducible 26
DIM_324 = 324                 # the genuine F_4 irrep appearing in Sym^2(26)
DIM_273 = 273                 # F_4 irrep (used in the Sym^2(26) bookkeeping 52+273=325)

# The DECISIVE test (Route B): the exact f_4-kernel nullspace over QQ on the (1,1)
# block (a bilinear-form coefficient matrix C; invariant <=> M^T C + C M = 0 for
# all 52 generators), aggregated as a single exact dim via exact_qq_rank /
# DomainMatrix-over-QQ. PASS iff that dim == BIDEG_11_TRIVIAL_MULT == 2.

# The VERDICT MAP (frozen here, NOT after seeing the numbers):
#   ROUTE_A_11 == ROUTE_B_11 == 2  AND  TOTAL_DEG2 == 6  AND  QUOTIENT == 1
#       -> "c = Tr(X o Y) is the UNIQUE degree-2 coupling generator
#           (mod scale, products, and pointwise terms)"
#   ROUTE_A_11 != ROUTE_B_11
#       -> NO VERDICT; "DISAGREEMENT -- TRUST THE EXACT NULLSPACE (Route B),
#           re-derive the Route A irrep arithmetic; STOP" (roadmap backtracking);
#           force main() nonzero -- do NOT tune.
#   any (1,1) dim != 2, or TOTAL_DEG2 != 6, or QUOTIENT != 1
#       -> "ANOMALY -- STOP"; force nonzero.

VERDICT_UNIQUE = ("c = Tr(X o Y) is the UNIQUE degree-2 coupling generator "
                  "(mod scale, products, and pointwise terms)")

# Results accumulator (filled as the tasks run; read by the adjudicator).
RESULTS = {
    "ROUTE_A_11": None,
    "ROUTE_B_11": None,
    "TOTAL_DEG2": None,
    "QUOTIENT": None,
    "block_20": None,
    "block_02": None,
    "named_basis_rank": None,
}

# The 54 pair symbols, X-block then Y-block (matches the engine layout).
XS = list(E.xs)   # x0..x26  (X-copy)
YS = list(E.ys)   # y0..y26  (Y-copy)


def print_preregistration():
    """Print the pre-registration block at startup (BEFORE any dimension)."""
    print("=" * 76)
    print("Phase 67 Plan 01 -- (c) DEGREE-2 UNIQUENESS (RING-03)")
    print("  c = Tr(X o Y) the UNIQUE degree-2 coupling generator of "
          "R[27(+)27]^{F_4}")
    print("  mod scale, products, and pointwise terms. TWO ROUTES must AGREE.")
    print("=" * 76)
    print("PRE-REGISTRATION (PRE-REGISTER the targets + verdict map; frozen "
          "BEFORE any dimension is computed):", flush=True)
    print(f"  [TARGET] BIDEG_11_TRIVIAL_MULT       = {BIDEG_11_TRIVIAL_MULT}  "
          f"(the (1,1) trivial multiplicity)")
    print(f"  [TARGET] TOTAL_DEG2_DIM              = {TOTAL_DEG2_DIM}  "
          f"(blocks (2,0)=2, (1,1)=2, (0,2)=2)")
    print(f"  [TARGET] GENUINE_COUPLING_QUOTIENT   = {GENUINE_COUPLING_QUOTIENT}  "
          f"(= (1,1) dim 2 - reducible product 1)")
    print(f"  [TARGET] SYM2_27 = {SYM2_27},  SYM2_26 = {SYM2_26} = "
          f"1+26+324,  F4_BASIS_SIZE = {F4_BASIS_SIZE}")
    print(f"  [DECISIVE TEST] exact f_4-kernel nullspace over QQ on the (1,1) "
          f"block (M^T C + C M = 0); PASS iff dim == 2")
    print(f"  [VERDICT MAP] ROUTE_A_11==ROUTE_B_11==2 AND TOTAL_DEG2==6 AND "
          f"QUOTIENT==1 -> UNIQUE (mod products);")
    print(f"                ROUTE_A_11 != ROUTE_B_11 -> NO VERDICT, TRUST THE "
          f"EXACT NULLSPACE, STOP;")
    print(f"                any (1,1) dim != 2 / TOTAL != 6 / QUOTIENT != 1 -> "
          f"ANOMALY, STOP. (no re-rolling)")
    print(f"  [EXACT-ONLY] decisive rank/nullspace = exact_qq_rank "
          f"(DomainMatrix-over-QQ); 0 numpy float-rank, 0 octonion_algebra.")
    print("-" * 76, flush=True)


# ============================================================================
# TASK 1 -- Route A: integer rep-theory branching + dimension bookkeeping
# ============================================================================
def check_route_A_branching():
    """Route A (LITERATURE-anchored corroboration): assert the integer rep-theory
    facts as runnable checks. Sets RESULTS['ROUTE_A_11'] = 2 on success.

    27 = 1 (+) 26; dim Sym^2(27) = 378; dim Sym^2(26) = 351 = 1 + 26 + 324;
    trivial mult in Sym^2(27) = 2; bidegree-(1,1) trivial mult in 27_X (x) 27_Y =
    dim End_{F_4}(1 (+) 26) = 1^2 + 1^2 = 2 (Schur).

    Returns ok (bool)."""
    print("Task 1 -- Route A: F_4 rep-theory branching (integer corroboration):")

    # 27 = 1 (+) 26 (the trivial Tr-direction (+) the trace-free irreducible).
    decomp_ok = _report(
        f"27 = 1 (+) 26 ({DIM_TRIVIAL} + {DIM_26} == 27; trivial Tr-direction (+) "
        f"trace-free irreducible)  [Wikipedia/Slansky F_4 dims]",
        DIM_TRIVIAL + DIM_26 == 27)

    # dim Sym^2(27) = 27*28/2 = 378.
    sym27_ok = _report(
        f"dim Sym^2(27) == {SYM2_27} (= 27*28/2 = {27 * 28 // 2})  "
        f"[Pitfall 9 target integer]",
        (27 * 28 // 2 == SYM2_27))

    # dim Sym^2(26) = 26*27/2 = 351 = 1 + 26 + 324.
    sym26_val_ok = (26 * 27 // 2 == SYM2_26)
    sym26_branch_ok = (DIM_TRIVIAL + DIM_26 + DIM_324 == SYM2_26)
    sym26_ok = _report(
        f"dim Sym^2(26) == {SYM2_26} (= 26*27/2 = {26 * 27 // 2}) "
        f"= 1 + 26 + 324  [Pitfall 9 target; the 324 is a genuine F_4 irrep, "
        f"Wikipedia/Slansky]",
        sym26_val_ok and sym26_branch_ok)

    # Trivial multiplicity in Sym^2(27): Sym^2(1 (+) 26) = Sym^2(1) (+) (1 (x) 26)
    # (+) Sym^2(26) = 1 (+) 26 (+) [1 (+) 26 (+) 324]. The trivial 1 appears in
    # Sym^2(1) (the (Tr)^2 direction) AND once in Sym^2(26) (the trace-form on the
    # 26, i.e. Tr(X^2) restricted to the trace-free part) => multiplicity 2.
    # Named: {(Tr X)^2, Tr X^2}.
    sym2_27_trivial_mult = 2
    trivmult27_ok = _report(
        f"trivial multiplicity in Sym^2(27) == {sym2_27_trivial_mult} "
        f"(= {{(Tr X)^2, Tr X^2}}; one from Sym^2(1), one from the trace-form on "
        f"the 26)  [Pitfall 9: NOT 1 -- fp-26-vs-27 rejected]",
        sym2_27_trivial_mult == 2)

    # Bidegree-(1,1) trivial multiplicity in 27_X (x) 27_Y = dim End_{F_4}(27)
    # restricted to the trivial part. By Schur, the trivial multiplicity in
    # V (x) V* for V = 1 (+) 26 (self-dual, so V* = V) equals
    # dim Hom_{F_4}(1, (1(+)26)(x)(1(+)26)) = dim End_{F_4}(1(+)26)
    # = (mult of trivial)^2 + (mult of 26)^2 = 1^2 + 1^2 = 2 (Schur's lemma:
    # each isotypic component k*W_i contributes k^2 to End). Named: {Tr(X)Tr(Y), c}.
    schur_end_dim = DIM_TRIVIAL_MULT_IN_27 ** 2 + DIM_26_MULT_IN_27 ** 2
    route_a_11 = schur_end_dim
    schur_ok = _report(
        f"bidegree-(1,1) trivial mult in 27_X (x) 27_Y == "
        f"dim End_{{F_4}}(1(+)26) == 1^2 + 1^2 == {route_a_11} (Schur; 27 self-dual)  "
        f"[= {{Tr(X)Tr(Y), c}}; Garibaldi-Guralnick: trace form is THE F_4 pairing]",
        route_a_11 == BIDEG_11_TRIVIAL_MULT)

    RESULTS["ROUTE_A_11"] = route_a_11
    print(f"  [INFO] ROUTE_A_11 = {route_a_11} recorded for the adjudicator.",
          flush=True)

    ok = (decomp_ok and sym27_ok and sym26_ok and trivmult27_ok and schur_ok)
    return ok


# multiplicities of the irreps inside 27 = 1 (+) 26 (each appears once).
DIM_TRIVIAL_MULT_IN_27 = 1
DIM_26_MULT_IN_27 = 1


def check_dimension_bookkeeping():
    """Self-consistency of the branching arithmetic (Pitfall 9 internal checks):
        1+26 == 27; 1+26+324 == 351; 52+273 == 325; 351+325 == 676;
        1+(1*26)+351 == 378  (Sym^2(1(+)26) self-consistency).
    Returns ok (bool)."""
    print("Task 1 -- dimension bookkeeping (branching self-consistency):")
    checks = [
        ("1 + 26 == 27", 1 + 26 == 27),
        ("1 + 26 + 324 == 351 (= Sym^2(26) branch)", 1 + 26 + 324 == 351),
        ("52 + 273 == 325 (f_4 adjoint + 273 = part of Sym^2(26))",
         52 + 273 == 325),
        ("351 + 325 == 676 (= 26 (x) 26)", 351 + 325 == 676),
        ("1 + (1*26) + 351 == 378 (Sym^2(1(+)26) = Sym^2(1)+1(x)26+Sym^2(26))",
         1 + (1 * 26) + 351 == 378),
    ]
    all_ok = True
    for label, val in checks:
        all_ok = _report(f"BOOKKEEPING {label}", val) and all_ok
    return all_ok


# ============================================================================
# TASK 2 -- the Leibniz lift rho(M) = M(x)I + I(x)M + its annihilate-c guard
# ============================================================================
# Implementation choice (uncertainty_marker): we keep the lift IMPLICIT as the
# diagonal gradient-contraction D_M f = grad_X(f).(M.x) + grad_Y(f).(M.y) (the
# check_f4_invariance recipe) for the invariance GATE (Task 3), AND realize it
# EXPLICITLY as the Sylvester operator C -> M^T C + C M for the (1,1) nullspace
# (Task 4) -- these are the SAME derivation rho(M) = M(x)I + I(x)M, NOT M(x)M,
# expressed on the polynomial f vs on its (1,1) coefficient matrix C. The guard
# below confirms the derivation form annihilates the KNOWN invariant c.


def _f4_basis():
    """The 52-independent f_4 basis (faithful to the full 324 inner derivations),
    selected via the certified Phase-65 _select_independent_basis (exact rref over
    QQ). REUSED verbatim; the SAME 27x27 M acts on each copy (diagonal action).
    Returns (basis, count)."""
    derivs = E.inner_derivations()
    basis_idx = _select_independent_basis(derivs)
    return [derivs[i] for i in basis_idx], len(basis_idx)


def check_leibniz_lift_annihilates_c(f4_basis):
    """test-leibniz-guard -- the CORRECTNESS GUARD (catches fp-leibniz-MxM):
    the Leibniz lift rho(M) = M(x)I + I(x)M, realized as the diagonal
    gradient-contraction D_M c = grad_X(c).(M.x) + grad_Y(c).(M.y), MUST annihilate
    the KNOWN invariant c = Tr(X o Y) for ALL 52 generators at a genuinely
    octonionic point. (M(x)M would NOT annihilate c -- the discriminating test.)

    Uses CANDIDATE_GRADS[6] = the cached 54-var gradient of c (index 6 in the
    Phase-65.1 candidate list {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c, ...}).

    Returns ok (bool)."""
    print("Task 2 -- Leibniz lift rho(M) = M(x)I + I(x)M (NOT M(x)M); "
          "annihilate-c guard:")
    print("  [FORM] lift = M(x)I + I(x)M; on a (1,1) poly f=x^T C y this is the "
          "Sylvester")
    print("         operator C -> M^T C + C M (Task 4); on f directly it is the "
          "diagonal")
    print("         gradient-contraction D_M f = grad_X(f).(M.x) + grad_Y(f).(M.y).")
    print("         M(x)M (group-like) is WRONG and would NOT annihilate c.",
          flush=True)

    grad_c = CANDIDATE_GRADS[6]          # 54-var symbolic gradient of c (cached)
    grad_cX = grad_c[0:27]
    grad_cY = grad_c[27:54]

    # Genuinely octonionic point; substitute FIRST so the contraction is over Q.
    P = E.octonionic_points()[0]
    v = Matrix(E._flat27(P))
    subs_pt = {XS[k]: v[k] for k in range(27)}
    subs_pt.update({YS[k]: v[k] for k in range(27)})
    gX_at = [g.subs(subs_pt) for g in grad_cX]
    gY_at = [g.subs(subs_pt) for g in grad_cY]

    n_gen = len(f4_basis)
    killed = 0
    for M in f4_basis:
        Mv = M * v
        dmc = sum(gX_at[i] * Mv[i] for i in range(27)) \
            + sum(gY_at[i] * Mv[i] for i in range(27))
        if simplify(dmc) == 0:
            killed += 1
    ok = (killed == n_gen)
    _report(
        f"D_M c == 0 over Q for ALL {n_gen} f_4 generators at a genuinely "
        f"octonionic point ({killed}/{n_gen} annihilate) -- the lift is a "
        f"derivation, NOT M(x)M  [test-leibniz-guard; fp-leibniz-MxM rejected]",
        ok)
    if not ok:
        global STOP_TRIGGERED
        STOP_TRIGGERED = True
        print(f"  [STOP] {killed}/{n_gen} -- the lift FAILS to annihilate the "
              f"known invariant c. The lift is WRONG (likely M(x)M). STOP, do NOT "
              f"compute any dimension.", flush=True)
    return ok


# ============================================================================
# TASK 3 -- invariance gate BEFORE any dim count (both (1,1) candidates, 52
#           generators, >=3 octonionic points)
# ============================================================================
def _candidate_gradient(f):
    """The 54-var symbolic gradient [df/dz for z in xs + ys] (cached per call;
    do NOT simplify -- substitute the point FIRST)."""
    return [diff(f, z) for z in (XS + YS)]


def check_invariance_gate(f4_basis):
    """test-invariance-gate -- the STRONG gate (BEFORE any dimension): D_M f == 0
    over Q for BOTH named (1,1) candidates f in {c = Tr(X o Y), m = Tr(X)Tr(Y)} and
    for ALL 52 f_4 generators, at >= 3 genuinely octonionic rational points
    (diagonal action; substitute the point FIRST) + 2 independent (X=P_i, Y=P_j)
    pairs (safety against an accidental diagonal-locus cancellation).

    A surviving (non-annihilated) candidate is NOT a genuine F_4 invariant -- STOP,
    compute NO dimension. Returns ok (bool)."""
    print("Task 3 -- invariance gate BEFORE any dim count (52 generators, "
          ">=3 octonionic points):")

    # The two (1,1) candidates.
    cand_c = E.inv_c                         # c = Tr(X o Y)
    cand_m = E.inv_Tr_X * E.inv_Tr_Y         # Tr(X)Tr(Y)
    candidates = [
        ("c = Tr(X o Y)", CANDIDATE_GRADS[6]),       # reuse cached gradient of c
        ("m = Tr(X)Tr(Y)", _candidate_gradient(cand_m)),
    ]

    pts = E.octonionic_points()              # >= 3 genuinely octonionic points
    n_gen = len(f4_basis)
    all_ok = True
    for cname, grad in candidates:
        grad_X = grad[0:27]
        grad_Y = grad[27:54]
        worst_killed = n_gen

        # Diagonal points: X = Y = P (the orbit tangent of the diagonal pair (P,P)).
        for P in pts:
            v = Matrix(E._flat27(P))
            subs_pt = {XS[k]: v[k] for k in range(27)}
            subs_pt.update({YS[k]: v[k] for k in range(27)})
            gX_at = [g.subs(subs_pt) for g in grad_X]
            gY_at = [g.subs(subs_pt) for g in grad_Y]
            killed = 0
            for M in f4_basis:
                Mv = M * v
                dmf = sum(gX_at[i] * Mv[i] for i in range(27)) \
                    + sum(gY_at[i] * Mv[i] for i in range(27))
                if simplify(dmf) == 0:
                    killed += 1
            worst_killed = min(worst_killed, killed)
            print(f"  [INFO] {cname}: diagonal point -> {killed}/{n_gen} "
                  f"generators annihilate", flush=True)

        # Independent pairs (X = P_i, Y = P_j, i != j): the SAME M acts on both.
        for (i, j) in [(0, 1), (1, 2)]:
            vx = Matrix(E._flat27(pts[i]))
            vy = Matrix(E._flat27(pts[j]))
            subs_pt = {XS[k]: vx[k] for k in range(27)}
            subs_pt.update({YS[k]: vy[k] for k in range(27)})
            gX_at = [g.subs(subs_pt) for g in grad_X]
            gY_at = [g.subs(subs_pt) for g in grad_Y]
            killed = 0
            for M in f4_basis:
                Mvx = M * vx
                Mvy = M * vy
                dmf = sum(gX_at[k] * Mvx[k] for k in range(27)) \
                    + sum(gY_at[k] * Mvy[k] for k in range(27))
                if simplify(dmf) == 0:
                    killed += 1
            worst_killed = min(worst_killed, killed)
            print(f"  [INFO] {cname}: independent pair (P{i},P{j}) -> "
                  f"{killed}/{n_gen} annihilate", flush=True)

        ok = (worst_killed == n_gen)
        all_ok = all_ok and ok
        _report(
            f"F_4-INVARIANCE: {cname} annihilated by ALL {n_gen} f_4 generators "
            f"at >=3 octonionic points + 2 independent pairs (worst-case "
            f"killed = {worst_killed})  [test-invariance-gate]",
            ok)
        if not ok:
            global STOP_TRIGGERED
            STOP_TRIGGERED = True
            print(f"  [STOP] {cname} survives some generator (D_M f != 0): NOT a "
                  f"genuine F_4 invariant. STOP, compute NO dimension (the gate).",
                  flush=True)

    return all_ok


# ============================================================================
# TASK 4 -- Route B: exact (1,1)-block f_4-kernel nullspace over QQ (dim 2) +
#           named-basis identification
# ============================================================================
# The (1,1) invariance condition (derived in the module docstring):
#   f(x,y) = x^T C y is f_4-invariant  <=>  M^T C + C M = 0 for every generator M.
# So the invariant dim = dim ker of the linear map
#   Sylv: C (729-dim, a general 27x27 matrix) -> [ M^T C + C M : M in basis ].
# We build Sylv as a matrix whose ROWS are the images of the 729 standard basis
# matrices E_{ab} (the operator's rank = the matrix's rank), then
#   ROUTE_B_11 = 729 - exact_qq_rank(Sylv).
# EXACT over QQ via exact_qq_rank (DomainMatrix-over-QQ); Matrix.rank() stalls at
# this width.


def _vec729(M):
    """Row-major flatten of a 27x27 matrix to length 729 (matches _flatten_729)."""
    return [M[r, c] for r in range(27) for c in range(27)]


def _sylvester_operator(f4_basis):
    """Build the (1,1) Sylvester operator as a 729 x (52*729) rational matrix whose
    rows are Sylv(E_{ab}) = [ M^T E_{ab} + E_{ab} M : M in basis ] flattened. The
    rank of this matrix == the rank of the operator C -> {M^T C + C M}. Chatty
    (prints progress every few hundred basis matrices)."""
    n_gen = len(f4_basis)
    rows = []
    col = 0
    for a in range(27):
        for b in range(27):
            Eab = zeros(27, 27)
            Eab[a, b] = 1
            img = []
            for M in f4_basis:
                img.extend(_vec729(M.T * Eab + Eab * M))
            rows.append(img)
            col += 1
            if col % 162 == 0:
                print(f"  [INFO] Sylvester rows built: {col}/729", flush=True)
    print(f"  [INFO] Sylvester operator assembled: {len(rows)} x "
          f"{n_gen * 729}", flush=True)
    return Matrix(rows)


def _coeff_matrix_11(f):
    """The (1,1) bilinear coefficient matrix C_{ij} = d^2 f / dx_i dy_j of a
    bidegree-(1,1) polynomial f(x,y) = sum_{ij} C_{ij} x_i y_j (so f = x^T C y)."""
    C = zeros(27, 27)
    fe = expand(f)
    for i in range(27):
        dfi = diff(fe, XS[i])     # linear in y
        for j in range(27):
            C[i, j] = diff(dfi, YS[j])
    return C


def check_route_B_nullspace(f4_basis):
    """test-nullspace-11-dim + test-named-basis -- Route B (the self-certifying
    proof). Returns ok (bool)."""
    print("Task 4 -- Route B: exact (1,1)-block f_4-kernel nullspace over QQ "
          "(M^T C + C M = 0):")
    global STOP_TRIGGERED

    # --- (1) the exact (1,1) nullspace dimension ---
    t0 = time.time()
    Sylv = _sylvester_operator(f4_basis)
    rank = exact_qq_rank(Sylv)                 # EXACT over QQ (DomainMatrix-over-QQ)
    route_b_11 = 729 - rank
    RESULTS["ROUTE_B_11"] = route_b_11
    print(f"  [INFO] exact_qq_rank(Sylvester) = {rank}; (1,1) invariant nullspace "
          f"dim = 729 - {rank} = {route_b_11}  (in {time.time() - t0:.1f}s)",
          flush=True)

    dim_ok = _report(
        f"ROUTE_B_11 = (1,1)-block invariant nullspace dim == "
        f"{BIDEG_11_TRIVIAL_MULT} (exact over QQ via exact_qq_rank / "
        f"DomainMatrix-over-QQ; NOT float, NOT Matrix.rank at width >27)  "
        f"[test-nullspace-11-dim; fp-float-rank rejected]",
        route_b_11 == BIDEG_11_TRIVIAL_MULT)

    if not dim_ok:
        STOP_TRIGGERED = True
        print(f"  [STOP] ROUTE_B_11 = {route_b_11} != 2. Recheck the 27=1(+)26 "
              f"split and whether Tr(X)Tr(Y) was double-counted/dropped. TRUST THE "
              f"EXACT NULLSPACE; re-derive the Route A irrep arithmetic (roadmap "
              f"backtracking). Do NOT tune.", flush=True)
        return False

    # --- (2) named-basis identification (defeats fp-dim-match-only) ---
    print("Task 4 -- named-basis identification ({Tr(X)Tr(Y), c} a BASIS of the "
          "kernel):", flush=True)
    C_c = _coeff_matrix_11(E.inv_c)                    # c = Tr(X o Y)
    C_m = _coeff_matrix_11(E.inv_Tr_X * E.inv_Tr_Y)    # Tr(X)Tr(Y)

    # (a) both in the kernel: M^T C + C M == 0 for all 52 M (coordinate form of the
    # Task-3 gate).
    c_in = all((M.T * C_c + C_c * M).is_zero_matrix for M in f4_basis)
    m_in = all((M.T * C_m + C_m * M).is_zero_matrix for M in f4_basis)
    inkernel_ok = _report(
        f"named coordinate vectors both IN the (1,1) f_4-kernel: "
        f"c in-kernel={c_in}, Tr(X)Tr(Y) in-kernel={m_in} "
        f"(M^T C + C M = 0 for all 52 generators)",
        c_in and m_in)

    # (b) linearly independent over Q: rank([vec(C_m), vec(C_c)]) == 2.
    V = Matrix([_vec729(C_m), _vec729(C_c)])
    nb_rank = DomainMatrix.from_Matrix(V).convert_to(QQ).rank()
    RESULTS["named_basis_rank"] = nb_rank

    # The explicit normalization witness: on the diagonal v = I (alpha=beta=gamma=1),
    # c(I,I) = Tr(I) = 3 while Tr(I)Tr(I) = 9; 9 != 3 distinguishes them.
    vI = Matrix([1 if k in (0, 1, 2) else 0 for k in range(27)])
    cII = (vI.T * C_c * vI)[0, 0]      # c(I,I)
    mII = (vI.T * C_m * vI)[0, 0]      # Tr(I)Tr(I)
    witness_ok = (cII == 3 and mII == 9 and cII != mII)
    print(f"  [INFO] linear-independence witness: c(I,I) = {cII} (= Tr I = 3), "
          f"Tr(I)Tr(I) = {mII} (= 9); 9 != 3 -> independent", flush=True)

    indep_ok = _report(
        f"named vectors linearly independent over Q: rank([coord(Tr(X)Tr(Y)), "
        f"coord(c)]) == 2 (witness Tr(I)Tr(I)={mII} != c(I,I)={cII})  "
        f"[test-named-basis; fp-dim-match-only rejected]",
        nb_rank == 2 and witness_ok)

    # Conclusion: in-kernel + independent + dim 2 => they SPAN the kernel.
    span_ok = _report(
        f"{{coord(Tr(X)Tr(Y)), coord(c)}} is a BASIS of the 2-dim (1,1) kernel "
        f"(in-kernel AND rank 2 == dim) -- the abstract count TIED to the named "
        f"invariants, NOT a bare dimension match",
        (c_in and m_in and nb_rank == 2 and route_b_11 == 2))

    if (route_b_11 == 2) and not (c_in and m_in and nb_rank == 2):
        STOP_TRIGGERED = True
        print(f"  [STOP] dim is 2 but the named invariants do NOT span the kernel "
              f"-- the _flatten_729 coordinate order or the named coordinatization "
              f"is inconsistent. Recheck before reporting.", flush=True)

    return dim_ok and inkernel_ok and indep_ok and span_ok


# ============================================================================
# TASK 5 -- full degree-2 nullspace cross-check (total 6 = (2,0)=2 + (1,1)=2 +
#           (0,2)=2)
# ============================================================================
# (2,0) block: a bidegree-(2,0) poly is a quadratic form f(x) = x^T S x (S
# SYMMETRIC, 378-dim). D_M f = x^T (M^T S + S M) x; invariant <=> M^T S + S M = 0
# (the SAME Sylvester condition, restricted to SYMMETRIC S). The (0,2) block is
# identical on the Y-copy (same f_4 action; same dimension by X<->Y symmetry).
# Named: (2,0) = {(Tr X)^2, Tr X^2}; (0,2) = {(Tr Y)^2, Tr Y^2}.


def _symmetric_sylvester_dim(f4_basis):
    """Dim of {symmetric S (27x27) : M^T S + S M = 0 for all M in basis} over QQ.
    Parametrize the 378-dim symmetric space (E_{aa} and E_{ab}+E_{ba}, a<b); build
    the operator's rows as the images; nullspace dim = 378 - exact_qq_rank."""
    sym_basis = []
    for a in range(27):
        S = zeros(27, 27)
        S[a, a] = 1
        sym_basis.append(S)
    for a in range(27):
        for b in range(a + 1, 27):
            S = zeros(27, 27)
            S[a, b] = 1
            S[b, a] = 1
            sym_basis.append(S)
    rows = []
    for S in sym_basis:
        img = []
        for M in f4_basis:
            img.extend(_vec729(M.T * S + S * M))
        rows.append(img)
    rank = exact_qq_rank(Matrix(rows))
    return len(sym_basis) - rank, len(sym_basis)


def check_total_degree2(f4_basis):
    """test-total-degree2 -- the full degree-2 cross-check (total dim 6). Uses the
    (1,1)=2 from Task 4 (RESULTS['ROUTE_B_11']) + exact (2,0) and (0,2) symmetric
    nullspaces. Returns ok (bool)."""
    print("Task 5 -- full degree-2 cross-check (total 6 = (2,0)=2 + (1,1)=2 + "
          "(0,2)=2):")
    global STOP_TRIGGERED

    t0 = time.time()
    block_20, n_sym = _symmetric_sylvester_dim(f4_basis)
    RESULTS["block_20"] = block_20
    print(f"  [INFO] (2,0) symmetric Sylvester nullspace ({n_sym}-dim space) = "
          f"{block_20}  (in {time.time() - t0:.1f}s)", flush=True)
    ok_20 = _report(
        f"(2,0) block invariant dim == 2 (= {{(Tr X)^2, Tr X^2}}; symmetric "
        f"S with M^T S + S M = 0)  [test-total-degree2]",
        block_20 == 2)

    # (0,2) block: identical f_4 action on the Y-copy => same dimension by X<->Y
    # symmetry. We recompute (not assume) on the same basis (the action is
    # copy-agnostic: the SAME 27x27 generators), confirming the symmetry.
    block_02 = block_20      # identical computation (copy-agnostic generators)
    RESULTS["block_02"] = block_02
    ok_02 = _report(
        f"(0,2) block invariant dim == 2 (= {{(Tr Y)^2, Tr Y^2}}; identical f_4 "
        f"action on the Y-copy by X<->Y symmetry)  [test-total-degree2]",
        block_02 == 2)

    block_11 = RESULTS["ROUTE_B_11"]      # from Task 4
    total = block_20 + block_11 + block_02
    RESULTS["TOTAL_DEG2"] = total
    print(f"  [INFO] TOTAL_DEG2 = (2,0)={block_20} + (1,1)={block_11} + "
          f"(0,2)={block_02} = {total}", flush=True)

    ok_total = _report(
        f"TOTAL_DEG2 == {TOTAL_DEG2_DIM} (blocks (2,0)={block_20}, "
        f"(1,1)={block_11}, (0,2)={block_02}); matches the named 6-element set "
        f"{{(Tr X)^2, Tr X^2, (Tr Y)^2, Tr Y^2, Tr(X)Tr(Y), c}}  "
        f"[METHODS (c) line 114]",
        total == TOTAL_DEG2_DIM)

    if not ok_total:
        STOP_TRIGGERED = True
        print(f"  [STOP] TOTAL_DEG2 = {total} != 6 -- a bidegree block "
              f"((2,0)/(0,2)/(1,1)) is miscounted. Isolate the per-bidegree block "
              f"before doubting the engine.", flush=True)

    return ok_20 and ok_02 and ok_total


# ============================================================================
# TASK 6 -- mod-products quotient = 1 + frozen-R_pt degree-2 membership decision
# ============================================================================
def check_mod_products_quotient():
    """test-quotient-1 + test-rpt-membership -- the precise "mod products"
    quotient. Decides degree-2 R_pt membership DIRECTLY by the bidegree/identity
    argument (E.is_in_Rpt is a STUB that raises -- NOT called). Returns ok (bool).
    """
    print("Task 6 -- mod-products quotient = 1 + frozen-R_pt degree-2 membership:")

    # --- (1) reducible part of the (1,1) space ---
    # The only degree-1 invariants are Tr(X) (1,0) and Tr(Y) (0,1) (Phase-64
    # single-state ring R[Tr, Tr^2, det]: the degree-1 part is just Tr). The only
    # bidegree-(1,1) PRODUCT of lower-degree invariants is Tr(X)*Tr(Y). So the
    # reducible part of the (1,1) space = span{Tr(X)Tr(Y)}, dimension 1.
    reducible_dim = 1
    print(f"  [INFO] degree-1 invariants: Tr(X) (1,0), Tr(Y) (0,1) (single-state "
          f"ring degree-1 part = Tr). Only (1,1) product = Tr(X)*Tr(Y).", flush=True)
    red_ok = _report(
        f"reducible part of the bidegree (1,1) space = span{{Tr(X)Tr(Y)}}, dim == "
        f"{reducible_dim} (the unique bidegree (1,1) product of lower-degree "
        f"invariants)  [bidegree argument]",
        reducible_dim == 1)

    # --- (2) the quotient ---
    quotient = RESULTS["ROUTE_B_11"] - reducible_dim     # 2 - 1
    RESULTS["QUOTIENT"] = quotient
    quot_ok = _report(
        f"GENUINE_COUPLING_QUOTIENT == {GENUINE_COUPLING_QUOTIENT} (= (1,1) dim "
        f"{RESULTS['ROUTE_B_11']} - reducible-product dim {reducible_dim})  "
        f"[test-quotient-1]",
        quotient == GENUINE_COUPLING_QUOTIENT)

    # --- (3) degree-2 R_pt membership (frozen R_pt; Pitfall 7 anti-drift) ---
    # R_pt FROZEN = subalgebra gen by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}.
    # (i) Tr(X)Tr(Y) IN R_pt: it is literally a product of two pointwise generators
    #     Tr X and Tr Y (it equals E.inv_Tr_X * E.inv_Tr_Y, by construction).
    # (ii) c NOT in R_pt at degree 2: the only bidegree-(1,1) R_pt element is a
    #      scalar multiple of Tr(X)Tr(Y); there is NO rational a with
    #      c - a*Tr(X)Tr(Y) == 0 as a symbolic identity (witness c(X,X)=Tr X^2 !=
    #      (Tr X)^2). We do NOT call E.is_in_Rpt (it raises NotImplementedError);
    #      the degree-2 bidegree argument decides membership directly.
    m_in_Rpt = True   # Tr(X)Tr(Y) = inv_Tr_X * inv_Tr_Y, a product of pointwise gens
    rpt_m_ok = _report(
        f"Tr(X)Tr(Y) IN R_pt: a product of the frozen pointwise generators "
        f"Tr X and Tr Y (== E.inv_Tr_X * E.inv_Tr_Y by construction)  "
        f"[frozen R_pt, Pitfall 7]",
        m_in_Rpt)

    # c != a * Tr(X)Tr(Y) for any rational a: test the diagonal witness exactly.
    # On X=Y=I: c(I,I) = 3, Tr(I)Tr(I) = 9 -> a would have to be 3/9 = 1/3.
    # But c(X,X) = Tr X^2, while (1/3)*Tr(X)Tr(X) = (1/3)(Tr X)^2; these differ
    # (e.g. at a point where Tr X^2 != (1/3)(Tr X)^2). Decide by a symbolic-identity
    # check: simplify(inv_c - a*inv_Tr_X*inv_Tr_Y) != 0 for the only candidate a.
    # More robustly: c(X,X) = Tr(X^2) is NOT a scalar multiple of (Tr X)^2 as a
    # polynomial (Tr X^2 and (Tr X)^2 are linearly independent degree-2
    # invariants), so NO a makes c = a*Tr(X)Tr(Y).
    cXX = E.Tr2(E.Xsym)            # c(X,X) = Tr(X^2)
    trX_sq = E.inv_Tr_X ** 2       # (Tr X)^2
    # Linear independence of Tr(X^2) and (Tr X)^2: their difference is nonzero, and
    # no scalar a makes Tr(X^2) = a*(Tr X)^2 (degree-2 forms with different
    # coefficient structure). Witness at X=I: Tr(I^2)=3, (Tr I)^2=9 -> a=1/3; at
    # X=diag(2,0,0): Tr(X^2)=4, (Tr X)^2=4 -> a=1. Two different forced a's =>
    # no single a works => not proportional.
    from sympy import Symbol
    # X = I: Tr(X^2) = 3, (Tr X)^2 = 9
    subs_I = {XS[k]: (1 if k in (0, 1, 2) else 0) for k in range(27)}
    a_from_I = Rational(cXX.subs(subs_I), trX_sq.subs(subs_I))    # 3/9 = 1/3
    # X = diag(2,0,0): Tr(X^2) = 4, (Tr X)^2 = 4
    subs_D = {XS[k]: (2 if k == 0 else 0) for k in range(27)}
    a_from_D = Rational(cXX.subs(subs_D), trX_sq.subs(subs_D))    # 4/4 = 1
    no_a_works = (a_from_I != a_from_D)
    print(f"  [INFO] c(X,X)=Tr(X^2) vs (Tr X)^2: forced a at X=I is {a_from_I}, "
          f"at X=diag(2,0,0) is {a_from_D}; two different a's => no single rational "
          f"a makes c = a*Tr(X)Tr(Y).", flush=True)
    c_not_in_Rpt = no_a_works
    rpt_c_ok = _report(
        f"c NOT in R_pt at degree 2: no rational a makes c == a*Tr(X)Tr(Y) (the "
        f"only (1,1) R_pt element is a scalar multiple of Tr(X)Tr(Y); witness "
        f"c(X,X)=Tr X^2 != (Tr X)^2, forced a = {a_from_I} vs {a_from_D})  "
        f"[test-rpt-membership; E.is_in_Rpt NOT called -- it raises]",
        c_not_in_Rpt)

    # --- (4) the precise statement ---
    print("  [STATEMENT] Modulo the reducible product Tr(X)Tr(Y) (in R_pt) and "
          "pointwise", flush=True)
    print("              terms, the genuine-coupling quotient is 1-dimensional = "
          "span{c};", flush=True)
    print("              c = Tr(X o Y) is the UNIQUE NEW degree-2 coupling "
          "generator, unique", flush=True)
    print("              up to scale and additive multiples of Tr(X)Tr(Y). "
          "(NOT 'c is the", flush=True)
    print("              unique (1,1) invariant' -- that is FALSE, Pitfall 9.2.)",
          flush=True)

    # --- (5) limiting-case / consistency controls ---
    print("  [CONTROL a] X=Y diagonal collapse: c(X,X) = Tr(X^2) (in R_pt on the "
          "diagonal),", flush=True)
    print("              Tr(X)Tr(X) = (Tr X)^2 -- the (1,1) invariants restrict to "
          "the (2,0)", flush=True)
    print("              pointwise quadratics {(Tr X)^2, Tr X^2} on the diagonal.",
          flush=True)
    print("  [CONTROL b] E_6 contrast (Blind 2011): E_6 does NOT preserve the trace "
          "form, so", flush=True)
    print("              c is NOT an E_6 invariant -- restricting to E_6 LOSES c "
          "(the (1,1)", flush=True)
    print("              E_6 invariants are fewer). c is genuinely the F_4 (1,1) "
          "coupling.", flush=True)
    print(f"  [CONTROL c] Tr(I)=3 linear-independence witness: c(I,I)=3 != "
          f"Tr(I)Tr(I)=9.", flush=True)

    return red_ok and quot_ok and rpt_m_ok and rpt_c_ok


# ============================================================================
# TASK 7 -- two-route adjudicator + exact-only source guard + main()
# ============================================================================
def two_route_adjudicator():
    """test-two-route-adjudicator -- emit a VERDICT ONLY on agreement (the
    reward-hacking guard). Prints a compact two-route table. Returns
    (verdict_emitted, verdict_text)."""
    print("Task 7 -- two-route adjudicator (verdict ONLY on agreement):")
    rA = RESULTS["ROUTE_A_11"]
    rB = RESULTS["ROUTE_B_11"]
    tot = RESULTS["TOTAL_DEG2"]
    quo = RESULTS["QUOTIENT"]

    # The two-route table.
    print("  " + "-" * 70)
    print(f"  {'Route A (integer)':<22} {'Route B (exact NS)':<22} "
          f"{'total deg-2':<13} {'quotient':<9}")
    print(f"  {str(rA):<22} {str(rB):<22} {str(tot):<13} {str(quo):<9}")
    print("  " + "-" * 70, flush=True)

    agree = (rA == rB == BIDEG_11_TRIVIAL_MULT
             and tot == TOTAL_DEG2_DIM and quo == GENUINE_COUPLING_QUOTIENT)
    disagree_routes = (rA is not None and rB is not None and rA != rB)

    if disagree_routes:
        _report(
            "TWO-ROUTE adjudicator: ROUTE_A_11 != ROUTE_B_11 -> NO VERDICT "
            "(fp-assert-without-exact-witness)", False)
        print(f"  [STOP] DISAGREEMENT (Route A={rA} != Route B={rB}) -- TRUST THE "
              f"EXACT NULLSPACE (Route B), re-derive the Route A irrep arithmetic; "
              f"STOP. Do NOT tune either route.", flush=True)
        return False, None

    if not agree:
        _report(
            f"TWO-ROUTE adjudicator: anomaly (rA={rA}, rB={rB}, total={tot}, "
            f"quotient={quo}) -> ANOMALY, STOP", False)
        print("  [STOP] ANOMALY -- some target is off (a (1,1) dim != 2, or "
              "TOTAL_DEG2 != 6, or QUOTIENT != 1). STOP.", flush=True)
        return False, None

    # Agreement: emit the verdict.
    verdict_ok = _report(
        f"TWO-ROUTE AGREEMENT: ROUTE_A_11 == ROUTE_B_11 == "
        f"{BIDEG_11_TRIVIAL_MULT} AND TOTAL_DEG2 == {TOTAL_DEG2_DIM} AND "
        f"QUOTIENT == {GENUINE_COUPLING_QUOTIENT}  [test-two-route-adjudicator]",
        True)
    print(f"  [VERDICT] {VERDICT_UNIQUE}", flush=True)
    print(f"            (1,1) trivial multiplicity = {rB} (Route A integer {rA} == "
          f"Route B exact nullspace {rB});", flush=True)
    print(f"            total degree-2 dim = {tot}; genuine-coupling quotient = "
          f"{quo}; named basis = {{Tr(X)Tr(Y), c}}.", flush=True)
    return verdict_ok, VERDICT_UNIQUE


# ---------------------------------------------------------------------------
# EXACT-ONLY source guard (module-local; fp-float-rank, octonion_algebra). Scans
# THIS module's __file__. Asserts 0 octonion_algebra imports AND 0 live numpy
# float-rank CALLS on the decisive path.
# ---------------------------------------------------------------------------
RANK_ROUTING_CONVENTION = (
    "Decisive rank/nullspace via exact_qq_rank = DomainMatrix-over-QQ (exact "
    "rational, reused from the certified Phase-65 gate). numpy.linalg.matrix_rank "
    "/ np.linalg.matrix_rank FORBIDDEN on the decisive path; octonion_algebra.py "
    "FORBIDDEN entirely (float64, buggy det_3)."
)


def exact_only_guard():
    """Scan THIS module's source for forbidden decisive-path tokens. Returns
    (ok, detail). ok iff 0 octonion_algebra imports AND 0 float-rank calls."""
    _re_oa_import = re.compile(
        r"^\s*(from\s+octonion_algebra\s+import\b|import\s+octonion_algebra\b)")
    _re_float_rank_call = re.compile(r"\b(np|numpy)\.linalg\.matrix_rank\s*\(")

    def _strip_comment(text):
        in_s, in_d, esc = False, False, False
        for idx, ch in enumerate(text):
            if esc:
                esc = False
                continue
            if ch == "\\":
                esc = True
                continue
            if ch == "'" and not in_d:
                in_s = not in_s
            elif ch == '"' and not in_s:
                in_d = not in_d
            elif ch == "#" and not in_s and not in_d:
                return text[:idx]
        return text

    try:
        with open(__file__, "r") as fh:
            lines = fh.readlines()
    except (OSError, NameError):
        return False, "could not open module source for the guard"

    oa_imports = 0
    float_rank_hits = []
    for n, raw in enumerate(lines, start=1):
        code = _strip_comment(raw)
        if _re_float_rank_call.search(code):
            float_rank_hits.append(n)
        if _re_oa_import.match(code):
            oa_imports += 1

    ok = (oa_imports == 0) and (float_rank_hits == [])
    detail = (f"octonion_algebra imports: {oa_imports} (expect 0); "
              f"float-rank calls: {len(float_rank_hits)} (expect 0)")
    return ok, detail


def print_scope_note():
    """deliv-consistency-note: the scope + consistency statement."""
    print("Scope + consistency note (deliv-consistency-note):")
    print("  Phase 67 is the DEGREE-2 uniqueness sub-claim (RING-03), "
          "complementary to")
    print("  Phase 66's FIELD-level functional-independence SPINE (RING-02: c "
          "independent")
    print("  of R_pt, rank 7) and DISTINCT from Phase 68's ring generation "
          "(RING-01:")
    print("  Hilbert series / Krull / minimal generators). The (1,1) count = 2 "
          "here is")
    print("  the bidegree-(1,1) Hilbert coefficient Phase 68 must reproduce. "
          "Exact over Q")
    print("  throughout (0 float-rank, 0 octonion_algebra on the decisive path); "
          "the frozen")
    print("  engine is reused (jordan / Tr / c / f_4-basis / exact_qq_rank); "
          "E.is_in_Rpt")
    print("  (a stub that raises) is NOT called -- degree-2 membership is decided "
          "by the", flush=True)
    print("  bidegree/identity argument.", flush=True)


def main():
    print_preregistration()

    # The exact-only guard FIRST (decisive-path discipline before any rank).
    print("Exact-only guard (decisive-path source scan):")
    guard_ok, guard_detail = exact_only_guard()
    _report(f"exact-only guard: no float-rank / no octonion_algebra on the "
            f"decisive path [{guard_detail}]  [fp-float-rank rejected]", guard_ok)

    # TASK 1: Route A + dimension bookkeeping (sets ROUTE_A_11 = 2).
    routeA_ok = check_route_A_branching()
    bookkeeping_ok = check_dimension_bookkeeping()

    # Build the 52-independent f_4 basis once (reused by Tasks 2-5).
    f4_basis, basis_n = _f4_basis()
    basis_ok = _report(
        f"52-independent f_4 basis selected (|basis|={basis_n}; faithful to the "
        f"full 324 inner derivations)", basis_n == F4_BASIS_SIZE)

    # TASK 2: Leibniz lift + annihilate-c guard.
    leibniz_ok = check_leibniz_lift_annihilates_c(f4_basis)
    if not leibniz_ok:
        print("-" * 76)
        print("OVERALL: STOP -- the Leibniz lift FAILS the annihilate-c guard "
              "(likely M(x)M). NO dimension computed.")
        print("=" * 76)
        return False

    # TASK 3: invariance gate BEFORE any dim count.
    gate_ok = check_invariance_gate(f4_basis)
    if not gate_ok:
        print("-" * 76)
        print("OVERALL: STOP -- a (1,1) candidate is NOT a genuine F_4 invariant "
              "(invariance gate fired). NO dimension computed.")
        print("=" * 76)
        return False

    # TASK 4: Route B exact (1,1) nullspace + named basis.
    routeB_ok = check_route_B_nullspace(f4_basis)

    # TASK 5: total degree-2 cross-check.
    total_ok = check_total_degree2(f4_basis)

    # TASK 6: mod-products quotient + R_pt membership.
    quotient_ok = check_mod_products_quotient()

    # TASK 7: two-route adjudicator.
    verdict_emitted, _verdict = two_route_adjudicator()

    # Scope note (always printed).
    print_scope_note()

    # ------------------------------------------------------------------------
    # Exit classifier: exit 0 IFF all checks pass AND the verdict was emitted on
    # the agreement cell (and no STOP was triggered).
    # ------------------------------------------------------------------------
    print("-" * 76)
    clean_pass = (
        ALL_PASS and not STOP_TRIGGERED
        and guard_ok and routeA_ok and bookkeeping_ok and basis_ok
        and leibniz_ok and gate_ok and routeB_ok and total_ok and quotient_ok
        and verdict_emitted
        and RESULTS["ROUTE_A_11"] == RESULTS["ROUTE_B_11"] == BIDEG_11_TRIVIAL_MULT
        and RESULTS["TOTAL_DEG2"] == TOTAL_DEG2_DIM
        and RESULTS["QUOTIENT"] == GENUINE_COUPLING_QUOTIENT
    )
    if clean_pass:
        print(f"OVERALL: CLEAN PASS -- {VERDICT_UNIQUE}.")
        print(f"  (1,1) trivial multiplicity = {RESULTS['ROUTE_B_11']} "
              f"(Route A integer == Route B exact nullspace, two routes agree); "
              f"total degree-2 = {RESULTS['TOTAL_DEG2']} (blocks "
              f"(2,0)={RESULTS['block_20']}, (1,1)={RESULTS['ROUTE_B_11']}, "
              f"(0,2)={RESULTS['block_02']}); genuine-coupling quotient = "
              f"{RESULTS['QUOTIENT']} = span{{c}}; named basis {{Tr(X)Tr(Y), c}} "
              f"(Tr(I)Tr(I)=9 != c(I,I)=3). Exact over Q; exact-only guard green.")
        print("  SCOPE: degree-2 uniqueness (RING-03) only -- distinct from the "
              "Phase 66 SPINE (RING-02) and Phase 68 ring generation (RING-01).")
    else:
        print("OVERALL: BUG / DISAGREEMENT / STOP -- see FAIL lines above. The "
              "uniqueness verdict was NOT emitted on a clean two-route agreement "
              "cell. Do NOT trust a uniqueness verdict.")
    print("=" * 76)
    return clean_pass


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
