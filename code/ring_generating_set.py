"""
(RING) Lemma -- Generating-set COUNT correction: the 3 missing joint invariants
================================================================================
Phase: 65.1-generating-set-count-correction-pin-down-the-3-missing-joint-invariants-trdeg-10
Plan: 01
Milestone: v16.0 The (RING) Lemma (math half of the Chalmers gap).

WHAT THIS IS
------------
The FIELD-LEVEL DUAL of the Phase-65 orbit-dimension GATE. Phase 65 COMPUTED
(triple-confirmed) that the generic pair orbit dimension of F_4 acting DIAGONALLY
on h_3(O) (+) h_3(O) is 44, so trdeg R[27(+)27]^{F_4} = 54 - 44 = 10, NOT the
naive-anchor 7. The "six pointwise + c" generating set is therefore functionally
INCOMPLETE by exactly 3 joint invariants (trdeg 10 = 3(X) + 3(Y) + 4 mixed; c is
one of the 4 mixed, so 3 more are missing).

This module CONFIRMS, by EXACT computation over Q, that the 10-candidate set

    {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c, Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)}

realizes Jacobian rank 10 over Q (Derksen-Kemper char-0 criterion: the generic
rank of the k x 54 Jacobian [d f_i / d z_j] equals the transcendence degree of
the subfield the f_i generate). Rank 10 == the Phase-65 orbit-derived trdeg 10 is
the decisive TWO-ROUTE cross-check (orbit-tangent rank in Phase 65 vs
invariant-Jacobian rank here).

SCOPE BOUNDARY: rank 10 establishes FIELD-LEVEL functional completeness
(trdeg-saturating; the invariant field is algebraic over Q(f_1..f_10)). It does
NOT establish ring generation (Hilbert series / Krull dimension / minimal
generators) -- that is Phase 68. No sentence here claims the 10 invariants
"generate the ring".

EXACT-ONLY (the GLOBAL FORBIDDEN PROXY): the decisive rank is exact_qq_rank
(DomainMatrix-over-QQ), reused VERBATIM from the certified Phase-65 gate. ZERO
numpy.linalg.matrix_rank / float-rank on the decisive path; ZERO
`import octonion_algebra` (the float64 file with the cross-term bug). A
module-local exact-only guard (scanning THIS __file__) asserts both.

PROVENANCE (decisive reuse -- not an oracle)
--------------------------------------------
  - code/ring_lemma_verification.py (Phase-64.1 FROZEN engine), imported as E:
    jordan, Tr, Tr2, c, det_3, polarize_d, Xsym, Ysym, xs, ys, X_from_symbols,
    _flat27, octonionic_points, inner_derivations, and the 7 base invariants
    inv_Tr_X..inv_c. Built on top of E.jordan + E.Tr; NEVER touches
    octonion_algebra.py and NEVER re-freezes det_3.
  - code/orbit_dimension_gate.py (Phase-65 CERTIFIED gate machinery):
    exact_qq_rank (DomainMatrix-over-QQ exact rank, width-54), PAIR_POINTS
    (4 generic integer octonionic pairs), _pair_not_proportional,
    exact_rank_route_crosscheck (three-exact-domain cross-check),
    _select_independent_basis (the 52-independent f_4 basis, faithful to the full
    324), _is_genuinely_octonionic_integer.

CONVENTION (carry verbatim from the frozen engine):
# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; det3 cross=2Re((x2x1)x3) [generic norm; Phase64.1 factor-order fix]; det3_normalization d(X,X,X)=6*det_3; coupling c=Tr(X o Y); f4=span{[L_a,L_b]} dim 52; arithmetic=exact-SymPy-over-Q; ranks=exact_qq_rank=DomainMatrix-over-QQ; NEVER float64 / numpy.linalg.matrix_rank on the decisive path
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible)

Assert-based harness (NO pytest -- the executor venv has sympy/numpy only).

Reproducibility: SymPy 1.14.0, NumPy 2.4.3, Python 3.14.2, macOS Darwin 24.6.0.
Deterministic (no random seeds; all evaluation points are the certified
hardcoded integer octonionic points from the Phase-65 gate + the engine's
octonionic_points()).

References:
  Derksen, H.; Kemper, G. -- Computational Invariant Theory, Sec 4 (char-0
    Jacobian criterion: generic Jacobian rank of f_1..f_k = trdeg of the field
    they generate). THE decisive criterion -- the exact DUAL of the Phase-65
    orbit-dimension computation.
  Iltyakov, A.V. (1995) + Polikarpov, S.V. (1991) -- Artin-Procesi-Iltyakov
    equality: for the split Albert algebra in char 0, the invariant ring of
    m in {1,2} elements EQUALS the trace algebra. Warrants the trace-monomial
    candidate FAMILY (the answer is COMPUTED, not assumed from this).
  code/ring_lemma_verification.py (VALD-64-01) + code/orbit_dimension_gate.py
    (Phase-65) -- the FROZEN engine + certified gate machinery, reused verbatim.
  Schwarz, G.W. -- math/0609078 (2-polarization can fail generically in char 0):
    motivates the COMPUTE-not-assume deterministic fallback ladder (Task 4).
"""

import os
import re
import sys

# Path-import the FROZEN engine + the certified gate machinery (sibling files in
# code/). Mirror the gate's own sibling-touch pattern; here it is the DECISIVE
# reuse, not an oracle.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ring_lemma_verification as E  # noqa: E402  (path insert must precede import)
from orbit_dimension_gate import (  # noqa: E402
    exact_qq_rank,
    PAIR_POINTS,
    _pair_not_proportional,
    exact_rank_route_crosscheck,
    _select_independent_basis,
    _is_genuinely_octonionic_integer,
)

from sympy import Matrix, diff, simplify, expand, total_degree, symbols, Rational  # noqa: E402

# Track overall pass/fail; the harness must exit nonzero on any check failure.
ALL_PASS = True
FAILED_LABELS = []   # labels of every FAIL (for exit classification).


def _report(label, ok):
    """Print a PASS/FAIL line and fold into the global pass flag (engine pattern)."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok:
        ALL_PASS = False
        FAILED_LABELS.append(label)
    return ok


# ============================================================================
# Pre-registered CHECK constants (NOT inputs -- reward-hacking guard fp-force-count)
# ============================================================================
# The target trdeg is a pre-registered CHECK, never an input to the computation.
# Read from the Phase-65 orbit-dimension GATE SUMMARY (65-03-SUMMARY.md):
# pair orbit dim 44 => trdeg = 54 - 44 = 10 (triple-confirmed).
AMBIENT_PAIR = 54                     # h_3(O) (+) h_3(O).
ORBIT_DERIVED_TRDEG = AMBIENT_PAIR - 44   # == 10, from Phase 65 (pair orbit dim 44).
TRDEG_TARGET = 10                     # the pre-registered CHECK constant (== ORBIT_DERIVED_TRDEG).
TOTAL_DEGREE_CAP = 5                  # fallback ladder degree cap (Task 4; stated bound).


# ============================================================================
# TASK 1 -- build the 3 mixed invariants; gate them BEFORE any rank
#   (grouping-unambiguity, F_4-invariance, bidegree)
# ============================================================================
# A non-invariant or mis-grouped candidate is not an invariant at all, so all
# three correctness gates run BEFORE any Jacobian rank.
#
# CANONICAL groupings (X^2 := jordan(X,X) is unambiguous; the OUTER grouping is
# irrelevant under Tr by trace associativity Tr((A o B) o C) = Tr(A o (B o C)) --
# verified in check_grouping_unambiguity -- but we PIN the canonical form):
#   f_21 = Tr(jordan(jordan(X,X), Y))        # Tr(X^2 o Y),  bidegree (2,1)
#   f_12 = Tr(jordan(X, jordan(Y,Y)))        # Tr(X o Y^2),  bidegree (1,2)
#   f_22 = Tr(jordan(jordan(X,X), jordan(Y,Y)))  # Tr(X^2 o Y^2), bidegree (2,2)

f_21 = E.Tr(E.jordan(E.jordan(E.Xsym, E.Xsym), E.Ysym))        # (2,1)
f_12 = E.Tr(E.jordan(E.Xsym, E.jordan(E.Ysym, E.Ysym)))        # (1,2)
f_22 = E.Tr(E.jordan(E.jordan(E.Xsym, E.Xsym), E.jordan(E.Ysym, E.Ysym)))  # (2,2)

# The ORDERED 10-candidate list (FIXED order -- LOAD-BEARING for the tier
# increments in Task 3). The 7 base invariants are reused VERBATIM from the
# frozen engine; the 3 mixed are built above on jordan+Tr.
CANDIDATES = [
    E.inv_Tr_X, E.inv_Tr2_X, E.inv_det_X,
    E.inv_Tr_Y, E.inv_Tr2_Y, E.inv_det_Y,
    E.inv_c,
    f_21, f_12, f_22,
]
NAMES = [
    "Tr X", "Tr X^2", "det X",
    "Tr Y", "Tr Y^2", "det Y",
    "c = Tr(X o Y)",
    "Tr(X^2 o Y)", "Tr(X o Y^2)", "Tr(X^2 o Y^2)",
]
BIDEGREES = [
    (1, 0), (2, 0), (3, 0),
    (0, 1), (0, 2), (0, 3),
    (1, 1),
    (2, 1), (1, 2), (2, 2),
]
# Builder expressions (text) for the downstream handoff bidegree table.
BUILDERS = [
    "Tr(Xsym)", "Tr2(Xsym)", "det_3(Xsym)",
    "Tr(Ysym)", "Tr2(Ysym)", "det_3(Ysym)",
    "Tr(jordan(Xsym,Ysym))",
    "Tr(jordan(jordan(Xsym,Xsym),Ysym))",
    "Tr(jordan(Xsym,jordan(Ysym,Ysym)))",
    "Tr(jordan(jordan(Xsym,Xsym),jordan(Ysym,Ysym)))",
]

# The 54 pair symbols, X-block then Y-block (matches the engine layout).
ALL_SYMS = list(E.xs) + list(E.ys)   # length 54


def _cached_candidate_gradients():
    """The 54-symbol symbolic gradient of EACH of the 10 candidates,
    [d f / d z for z in xs + ys]. Cached once at module scope (reused in Tasks
    2-3). Do NOT simplify() the symbolic 54-var gradient -- substitute the
    integer point FIRST per the Phase-65 _gradients_in_X pattern (det X is deg 3,
    f_22 is deg 4; simplify on the full 54-var gradient would swell)."""
    grads = []
    for f in CANDIDATES:
        grads.append([diff(f, z) for z in ALL_SYMS])
    return grads


# Built once; reused by Tasks 2-3 (substitute the point into these FIRST).
CANDIDATE_GRADS = _cached_candidate_gradients()


def check_grouping_unambiguity():
    """test-grouping-unambiguous: at a generic octonionic point, verify
        Tr((X o X) o Y) - Tr(X o (X o Y)) == 0   exactly over Q
    (the trace bilinear form is associative even though jordan is NOT, so the
    mixed monomial builders have NO grouping/ordering ambiguity). If != 0, the
    engine jordan/Tr reuse is wrong -- STOP before anything else.

    Returns ok (bool)."""
    # Use the engine's first genuinely octonionic point; substitute into the 54
    # X+Y symbols (X = point, Y = a second independent octonionic point so the
    # mixed grouping is non-trivial).
    pts = E.octonionic_points()
    Xpt = pts[0]
    Ypt = pts[1]
    subs_pt = {}
    for k, val in enumerate(E._flat27(Xpt)):
        subs_pt[E.xs[k]] = val
    for k, val in enumerate(E._flat27(Ypt)):
        subs_pt[E.ys[k]] = val

    left_group = E.Tr(E.jordan(E.jordan(E.Xsym, E.Xsym), E.Ysym))   # Tr((X o X) o Y)
    right_group = E.Tr(E.jordan(E.Xsym, E.jordan(E.Xsym, E.Ysym)))  # Tr(X o (X o Y))
    diff_val = simplify((left_group - right_group).subs(subs_pt))
    ok = (diff_val == 0)
    return _report(
        "GROUPING-UNAMBIGUOUS: Tr((XoX)oY) - Tr(Xo(XoY)) == 0 exactly over Q "
        "at a generic octonionic point (trace associativity; no ordering bug)  "
        "[test-grouping-unambiguous]",
        ok)


def _f4_basis():
    """The 52-independent f_4 basis (faithful to the full 324 inner derivations),
    selected via the certified Phase-65 _select_independent_basis (exact rref over
    QQ). The same M acts on each copy under the DIAGONAL action."""
    derivs = E.inner_derivations()
    basis_idx = _select_independent_basis(derivs)
    return [derivs[i] for i in basis_idx], len(basis_idx)


def check_f4_invariance(f4_basis):
    """test-f4-invariance -- the STRONG correctness gate (BEFORE any rank): for
    each mixed invariant f in {f_21, f_12, f_22}, verify D_M f == 0 over Q for
    EVERY f_4 generator M (the 52-independent basis), at >=3 genuinely octonionic
    rational points.

    DIAGONAL action: the SAME 27x27 generator M acts on both copies. The pair
    orbit tangent at a pair point is concat(M.v_x, M.v_y), so
        D_M f = grad_X(f).(M.v_x) + grad_Y(f).(M.v_y).
    (NOTE: the gate's infinitesimal_action() is single-copy / 27-wide; here we
    build the 54-wide diagonal contraction directly, splitting the cached 54-var
    gradient into its X-block [0:27] and Y-block [27:54].) Substitute the point
    into the gradient FIRST so the contraction is over rationals.

    A non-invariant candidate is not an invariant at all. If ANY generator
    survives (D_M f != 0): the builder is wrong -- STOP, do NOT compute any rank.

    Returns (ok, detail)."""
    pts = E.octonionic_points()   # >=3 genuinely octonionic rational points
    n_gen = len(f4_basis)
    mixed = [("f_21 Tr(X^2 o Y)", 7), ("f_12 Tr(X o Y^2)", 8), ("f_22 Tr(X^2 o Y^2)", 9)]
    all_ok = True
    detail_lines = []
    for fname, idx in mixed:
        grad = CANDIDATE_GRADS[idx]          # 54-var symbolic gradient (cached)
        grad_X = grad[0:27]
        grad_Y = grad[27:54]
        worst_killed = n_gen
        for P in pts:
            # DIAGONAL action: same point on both copies (X = Y = P is fine HERE
            # because this is the INVARIANCE test, not the rank -- we just need a
            # genuinely octonionic point at which to check D_M f = 0; the diagonal
            # tangent concat(M.v, M.v) is the orbit tangent of the diagonal pair
            # (P, P)). Using independent X, Y would also work; the SAME-point
            # choice keeps the substitution simple and is still genuinely
            # octonionic. We verify annihilation at the diagonal point AND, to be
            # safe against an accidental diagonal-locus cancellation, at an
            # independent (X=P_i, Y=P_j) pair below.
            v = Matrix(E._flat27(P))
            subs_pt = {E.xs[k]: v[k] for k in range(27)}
            subs_pt.update({E.ys[k]: v[k] for k in range(27)})
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

        # Independent-pair safety check (X != Y, distinct octonionic points): the
        # diagonal action sends (X,Y) -> concat(M.v_x, M.v_y) with the SAME M.
        for (i, j) in [(0, 1), (1, 2)]:
            vx = Matrix(E._flat27(pts[i]))
            vy = Matrix(E._flat27(pts[j]))
            subs_pt = {E.xs[k]: vx[k] for k in range(27)}
            subs_pt.update({E.ys[k]: vy[k] for k in range(27)})
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

        ok = (worst_killed == n_gen)
        all_ok = all_ok and ok
        detail_lines.append(f"{fname}: {worst_killed}/{n_gen} generators annihilate")
        _report(
            f"F_4-INVARIANCE D_M {fname} == 0 over Q for ALL {n_gen} f_4 generators "
            f"at >=3 genuinely octonionic points + 2 independent pairs "
            f"(worst-case killed = {worst_killed})  [test-f4-invariance]",
            ok)
    return all_ok, "; ".join(detail_lines)


def check_bidegree():
    """test-bidegree: verify each candidate's claimed bidegree (deg_X, deg_Y) by
    SCALING. Substitute X-coords -> s*x_i (all 27 X-symbols) and Y-coords ->
    t*y_j (all 27 Y-symbols), expand, and assert the invariant scales as
    s^{deg_X} * t^{deg_Y} times the original.

    Pass: f_21 ~ s^2 t^1, f_12 ~ s^1 t^2, f_22 ~ s^2 t^2; the 7 base reproduce
    their tabulated bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1).

    Returns (ok, detail)."""
    s, t = symbols('s t', positive=True)
    subs_scale = {E.xs[k]: s * E.xs[k] for k in range(27)}
    subs_scale.update({E.ys[k]: t * E.ys[k] for k in range(27)})
    all_ok = True
    detail_lines = []
    for name, f, (dX, dY) in zip(NAMES, CANDIDATES, BIDEGREES):
        scaled = expand(f.subs(subs_scale))
        expected = expand(s**dX * t**dY * f)
        ok = (expand(scaled - expected) == 0)
        all_ok = all_ok and ok
        detail_lines.append(f"{name}~s^{dX}t^{dY}:{ok}")
        _report(
            f"BIDEGREE {name} homogeneous of bidegree ({dX},{dY}) "
            f"(scales as s^{dX} t^{dY})  [test-bidegree]",
            ok)
    return all_ok, "; ".join(detail_lines)


def check_mixed_builders(f4_basis):
    """Run the THREE correctness gates on the 3 mixed invariants, ALL before any
    Jacobian rank: (a) grouping-unambiguity, (b) F_4-invariance (the strong gate),
    (c) bidegree. Also confirm the 3 mixed evaluate to sane nonzero rationals at a
    generic pair (a non-trivial-monomial sanity, RESEARCH intermediate result).

    Returns (ok, detail) with per-check booleans recorded via _report."""
    print("Task 1 -- build + gate the 3 mixed invariants (BEFORE any rank):")

    grouping_ok = check_grouping_unambiguity()
    inv_ok, inv_detail = check_f4_invariance(f4_basis)
    bideg_ok, bideg_detail = check_bidegree()

    # Sane nonzero rationals at a generic integer pair (the monomials are
    # non-trivial). Reuse the first generic pair from PAIR_POINTS.
    first_label = next(iter(PAIR_POINTS))
    X27, Y27 = PAIR_POINTS[first_label]
    subs_pt = {E.xs[k]: Rational(X27[k]) for k in range(27)}
    subs_pt.update({E.ys[k]: Rational(Y27[k]) for k in range(27)})
    mixed_vals = {
        "f_21": simplify(f_21.subs(subs_pt)),
        "f_12": simplify(f_12.subs(subs_pt)),
        "f_22": simplify(f_22.subs(subs_pt)),
    }
    sane_ok = all(v.is_rational and v != 0 for v in mixed_vals.values())
    _report(
        f"SANITY: the 3 mixed invariants are nonzero rationals at {first_label} "
        f"(f_21={mixed_vals['f_21']}, f_12={mixed_vals['f_12']}, "
        f"f_22={mixed_vals['f_22']})  [research intermediate]",
        sane_ok)

    ok = grouping_ok and inv_ok and bideg_ok and sane_ok
    detail = (f"grouping={grouping_ok}; invariance=[{inv_detail}]; "
              f"bidegree-all={bideg_ok}; sane={sane_ok}")
    return ok, detail


# ============================================================================
# TASK 2 -- full 10x54 candidate Jacobian rank (MAX over >=3 generic pairs)
# ============================================================================
# The DUAL of the Phase-65 orbit-tangent rank: same substitute-first /
# DomainMatrix-over-QQ recipe, on a 10x54 matrix instead of 52x54 (strictly
# cheaper). exact_qq_rank reused verbatim from the certified gate.

def candidate_jacobian_matrix_at(point_pair):
    """The 10x54 candidate Jacobian at a generic integer pair (X27, Y27): for each
    of the 10 candidates, substitute the point into its CACHED 54-symbol gradient
    FIRST (-> a length-54 rational row), stack into a 10x54 sympy.Matrix.

    Substitute-first controls det-X (deg 3) and f_22 (deg 4) expression swell -- do
    NOT simplify the symbolic gradient."""
    X27, Y27 = point_pair
    subs_pt = {E.xs[k]: Rational(X27[k]) for k in range(27)}
    subs_pt.update({E.ys[k]: Rational(Y27[k]) for k in range(27)})
    rows = []
    for grad in CANDIDATE_GRADS:
        rows.append([g.subs(subs_pt) for g in grad])   # length-54 rational row
    return Matrix(rows)   # 10 x 54


def full_candidate_rank(point_pair):
    """Exact rank over QQ of the 10x54 candidate Jacobian at one generic pair, via
    exact_qq_rank (DomainMatrix-over-QQ). NEVER numpy/float; sympy.Matrix.rank()
    stalls at width 54."""
    return exact_qq_rank(candidate_jacobian_matrix_at(point_pair))


def check_full_jacobian_rank():
    """test-full-rank-10: compute full_candidate_rank at EACH generic integer pair
    in PAIR_POINTS (>=3), take MAX_RANK = max(...). Use ONLY generic pairs (assert
    _pair_not_proportional for each). Pre-register against TRDEG_TARGET = 10.

    Returns (ok, max_rank, per_pair, needs_fallback).

    PASS condition (test-full-rank-10): MAX_RANK == 10 (the success path).
    If MAX_RANK == 9: set needs_fallback=True (NOT a hard fail -- Task 4 walks the
    ladder; the Task-3 tier increments name the dependent slot).
    If MAX_RANK > 10: HARD STOP (impossible -- would exceed the orbit-derived
    trdeg; signals a Jacobian/point/builder bug)."""
    print("Task 2 -- full 10x54 candidate Jacobian rank (MAX over >=3 generic pairs):")

    # Genericity: every pair must be non-proportional (rejects fp-nongeneric-point).
    pts_ok = True
    for label, (X, Y) in PAIR_POINTS.items():
        not_prop = _pair_not_proportional(X, Y)
        not_equal = (list(X) != list(Y))
        pts_ok = pts_ok and _report(
            f"pair {label} generic: X!=Y={not_equal}, X not-prop-Y={not_prop}",
            not_prop and not_equal)

    per_pair = {}
    for label, point_pair in PAIR_POINTS.items():
        per_pair[label] = full_candidate_rank(point_pair)
    max_rank = max(per_pair.values())

    pairs_str = ", ".join(f"{lbl}={r}" for lbl, r in per_pair.items())
    print(f"  [INFO] per-pair full candidate Jacobian rank: {pairs_str}; MAX={max_rank}")

    # Sanity bound: MAX_RANK <= 10 always (> 10 is impossible).
    le_target_ok = _report(
        f"MAX candidate Jacobian rank == {max_rank} <= {TRDEG_TARGET} "
        f"(sanity bound; > {TRDEG_TARGET} impossible -- would exceed orbit-derived "
        f"trdeg)",
        max_rank <= TRDEG_TARGET)

    if max_rank > TRDEG_TARGET:
        # HARD STOP: contradicts the Phase-65 orbit-derived trdeg.
        print(f"  [HARD-STOP] MAX_RANK = {max_rank} > {TRDEG_TARGET}: IMPOSSIBLE. "
              f"This CONTRADICTS the Phase-65 orbit-derived trdeg ({ORBIT_DERIVED_TRDEG}) "
              f"and signals a Jacobian-construction / point / builder bug. STOP -- "
              f"do NOT report a rank verdict; investigate the builder.")
        return False, max_rank, per_pair, False

    needs_fallback = (max_rank == TRDEG_TARGET - 1)   # rank 9
    # The PRIMARY pass condition: MAX_RANK == 10. Rank 9 is NOT a hard fail (it
    # routes to the fallback ladder in Task 4); we report it distinctly.
    rank10_ok = _report(
        f"FULL candidate Jacobian rank (MAX over {len(per_pair)} generic integer "
        f"pairs) == {TRDEG_TARGET} (the success path)  [test-full-rank-10]  "
        f"[COMPUTED MAX_RANK = {max_rank}]",
        max_rank == TRDEG_TARGET)

    if needs_fallback:
        print(f"  [NEEDS_FALLBACK] MAX_RANK = {max_rank} == {TRDEG_TARGET - 1}: the "
              f"natural three are functionally DEFICIENT by 1. NOT a failure -- the "
              f"deterministic fallback ladder (Task 4) fills the dependent slot "
              f"(named by the Task-3 tier increments). The honest computed minimal "
              f"completing set is the deliverable.")

    # ok at the Task-2 level means "no hard stop" (rank <= 10 and a definite
    # integer). The rank10 PASS vs needs_fallback distinction is carried forward.
    ok = le_target_ok and (rank10_ok or needs_fallback)
    return ok, max_rank, per_pair, needs_fallback


# ============================================================================
# TASK 3 -- fine-grained tier increments 6->7->8->9->10 (the dependent-slot pinpoint)
# ============================================================================
# Prefix Jacobian ranks in the FIXED candidate order, so the executor pinpoints
# EXACTLY which candidate adds independence vs is redundant (essential input for
# the Task-4 fallback). Two FREE cross-checks fall out: r6 == 6 (single-copy 3+3,
# Garibaldi-Guralnick / Faraut-Koranyi) and r7 == 7 (c independent of the
# pointwise sextet -- previews the Phase-66 SPINE).

def prefix_rank(k, point_pair):
    """Exact rank over QQ (exact_qq_rank) of the first k rows (k candidates) of the
    10x54 Jacobian at that pair (substitute-first)."""
    X27, Y27 = point_pair
    subs_pt = {E.xs[m]: Rational(X27[m]) for m in range(27)}
    subs_pt.update({E.ys[m]: Rational(Y27[m]) for m in range(27)})
    rows = []
    for grad in CANDIDATE_GRADS[:k]:
        rows.append([g.subs(subs_pt) for g in grad])
    return exact_qq_rank(Matrix(rows))


def check_tier_increments(max_rank):
    """test-tier-increments: for k in [6,7,8,9,10], compute MAX over PAIR_POINTS of
    prefix_rank(k, .). Print the ladder (r6,r7,r8,r9,r10) and the per-step
    increments, labeling each addition {independent if +1, redundant if +0}.

    Asserts:
      - r6 == 6 (6-pointwise sub-rank = 3 X-block + 3 Y-block; if != 6 -> STOP,
        engine/layout/base-invariant bug).
      - r7 == 7 (+c functionally independent of the pointwise sextet; previews the
        Phase-66 SPINE; if != 7 -> SURPRISING Phase-66-relevant finding, reported
        loudly).
      - each increment r_{k+1} - r_k in {0, 1}.
      - r10 == max_rank from Task 2 (consistency of prefix-10 vs full rank).

    Returns (ok, ladder, increments, bumped) where bumped maps the mixed-candidate
    name -> True if it bumped the prefix rank (independent) / False (redundant)."""
    print("Task 3 -- fine-grained tier increments 6->7->8->9->10 "
          "(MAX over generic pairs):")

    ladder = {}
    for k in [6, 7, 8, 9, 10]:
        ladder[k] = max(prefix_rank(k, pp) for pp in PAIR_POINTS.values())

    r6, r7, r8, r9, r10 = ladder[6], ladder[7], ladder[8], ladder[9], ladder[10]
    increments = {7: r7 - r6, 8: r8 - r7, 9: r9 - r8, 10: r10 - r9}
    # Which mixed candidate (index 7,8,9 = f_21,f_12,f_22) bumped the rank.
    bumped = {
        "Tr(X^2 o Y) [k=7->8]": (increments[8] == 1),
        "Tr(X o Y^2) [k=8->9]": (increments[9] == 1),
        "Tr(X^2 o Y^2) [k=9->10]": (increments[10] == 1),
    }

    ladder_str = f"r6={r6}, r7={r7}, r8={r8}, r9={r9}, r10={r10}"
    incr_str = (f"+c:{increments[7]:+d}, +Tr(X^2oY):{increments[8]:+d}, "
                f"+Tr(XoY^2):{increments[9]:+d}, +Tr(X^2oY^2):{increments[10]:+d}")
    print(f"  [INFO] tier ladder: {ladder_str}")
    print(f"  [INFO] increments:  {incr_str}  "
          f"(each labeled independent if +1, redundant if +0)")

    # r6 == 6: the single-copy 3+3 cross-check (Garibaldi-Guralnick / Faraut-Koranyi).
    r6_ok = _report(
        f"6-POINTWISE prefix rank == 6 (= 3 X-block + 3 Y-block; single-copy "
        f"trdeg-3 decomposition)  [test-tier-increments; r6={r6}]",
        r6 == 6)
    if not r6_ok:
        print(f"  [HARD-STOP] r6 = {r6} != 6: the pointwise sextet independence "
              f"is certified upstream (single-copy trdeg 3). This is an "
              f"engine/layout/base-invariant bug -- STOP, do NOT trust any "
              f"completeness verdict.")

    # r7 == 7: +c previews the Phase-66 SPINE.
    r7_ok = _report(
        f"+c prefix rank == 7 (c functionally independent of the pointwise "
        f"sextet; previews the Phase-66 SPINE)  [test-tier-increments; r7={r7}]",
        r7 == 7)
    if not r7_ok:
        print(f"  [SURPRISE] r7 = {r7} != 7: +c did NOT bump 6->7. This is a "
              f"SURPRISING Phase-66-relevant finding (NOT the expected branch) -- "
              f"reported loudly; do NOT silently continue.")

    # Each increment in {0, 1}.
    incr_ok = _report(
        f"each tier increment in {{0,1}} (a single new generator adds at most 1 "
        f"to the trdeg)  [increments: {incr_str}]",
        all(d in (0, 1) for d in increments.values()))

    # r10 == max_rank (prefix-10 == full rank from Task 2).
    consistency_ok = _report(
        f"r10 == full rank from Task 2 (prefix-10 {r10} == MAX_RANK {max_rank}; "
        f"consistency of the prefix and full Jacobian)",
        r10 == max_rank)

    # Report the success-path ladder explicitly.
    success_ladder = (r6 == 6 and r7 == 7 and r8 == 8 and r9 == 9 and r10 == 10)
    _report(
        f"tier ladder on the success path is (6,7,8,9,10) with every increment "
        f"== 1 (all three natural mixed monomials independent)  "
        f"[actual: ({r6},{r7},{r8},{r9},{r10})]",
        success_ladder)

    ok = r6_ok and r7_ok and incr_ok and consistency_ok
    return ok, ladder, increments, bumped


# ============================================================================
# Decisive two-route pre-check (consistency, reported at the first-result gate)
# ============================================================================
def two_route_precheck(max_rank):
    """The decisive TWO-ROUTE pre-check (full test-trdeg-match is wired in Task 5):
    does the candidate-Jacobian-derived trdeg (MAX_RANK) look consistent with the
    Phase-65 orbit-derived trdeg (54 - 44 = 10)? Reported at the first-result gate.

    Returns (consistent, max_rank, orbit_derived)."""
    consistent = (max_rank == ORBIT_DERIVED_TRDEG)
    print("Two-route trdeg pre-check (decisive cross-check; full wiring in Task 5):")
    print(f"  [INFO] candidate-Jacobian trdeg (MAX_RANK) = {max_rank}")
    print(f"  [INFO] Phase-65 orbit-derived trdeg = 54 - 44 = {ORBIT_DERIVED_TRDEG}")
    _report(
        f"TWO-ROUTE pre-check: candidate-Jacobian trdeg ({max_rank}) == "
        f"orbit-derived trdeg ({ORBIT_DERIVED_TRDEG})  [two independent routes agree]",
        consistent)
    return consistent, max_rank, ORBIT_DERIVED_TRDEG


# ============================================================================
# EXACT-ONLY source guard (module-local; forbidden proxies fp-float-rank, fp-norm-bug)
# ============================================================================
# Mirrors orbit_dimension_gate.py's exact_only_guard, but scans THIS module's
# __file__ (importing the gate's guard would scan the WRONG file). Asserts:
#   (a) 0 `import octonion_algebra` / `from octonion_algebra import ...` anywhere
#       (this module reuses the FROZEN engine's corrected det_3 via E.);
#   (b) 0 live np.linalg / numpy.linalg float-rank CALL (trailing '(' marks a live
#       call, not this prose mention). A non-decisive numpy float pre-screen, if
#       present, must be prose-distinguishable and never call matrix_rank.
RANK_ROUTING_CONVENTION = (
    "Decisive rank via exact_qq_rank = DomainMatrix-over-QQ (exact rational, reused "
    "from the certified Phase-65 gate); numpy.linalg.matrix_rank / np.linalg.matrix_rank "
    "FORBIDDEN on the decisive path; octonion_algebra.py FORBIDDEN entirely (buggy det_3)."
)


def exact_only_guard():
    """Scan THIS module's source for forbidden decisive-path tokens. Returns
    (ok, detail). ok is True iff 0 octonion_algebra imports AND 0 float-rank calls."""
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


# ============================================================================
# BOUNDED first-segment harness (Tasks 1-3 only; Tasks 4-6 deferred)
# ============================================================================
# This is a BOUNDED first execution segment per the orchestrator: run the Task-1
# correctness gates, the Task-2 full Jacobian rank, and the Task-3 tier ladder,
# then STOP at the first-result review gate. Tasks 4 (fallback ladder), 5
# (decisive cross-checks + main()), and 6 (handoff print) are NOT run yet.

def segment_main():
    print("=" * 76)
    print("Phase 65.1 Plan 01 -- candidate generating-set Jacobian rank "
          "(FIELD-level trdeg 10)")
    print("  BOUNDED FIRST SEGMENT: Tasks 1-3 only (gates + full rank + tier ladder).")
    print("  Tasks 4-6 (fallback ladder, decisive cross-checks/main, handoff) DEFERRED.")
    print("=" * 76)

    # The exact-only guard FIRST (the decisive-path discipline must hold before we
    # trust any rank reported below).
    print("Exact-only guard (decisive-path source scan):")
    guard_ok, guard_detail = exact_only_guard()
    _report(f"exact-only guard: no float-rank / no octonion_algebra on decisive "
            f"path [{guard_detail}]", guard_ok)

    # Build the 52-independent f_4 basis once (reused by the invariance gate).
    f4_basis, basis_n = _f4_basis()
    _report(f"52-independent f_4 basis selected (|basis|={basis_n}; faithful to the "
            f"full 324 inner derivations)", basis_n == 52)

    # TASK 1: correctness gates BEFORE any rank.
    builders_ok, builders_detail = check_mixed_builders(f4_basis)

    # If the Task-1 correctness gates FAIL, STOP before any rank (a broken builder
    # must not produce a rank verdict).
    if not builders_ok:
        print("-" * 76)
        print("OVERALL: TASK-1 GATE FAILURE -- a correctness gate (grouping / "
              "F_4-invariance / bidegree) FAILED. STOPPING before any Jacobian "
              "rank: a non-invariant or mis-grouped candidate is not an invariant "
              "at all. Do NOT report a rank verdict on a broken builder.")
        print("=" * 76)
        return 1, {"stage": "task1-gate-fail", "detail": builders_detail}

    # TASK 2: full 10x54 Jacobian rank, MAX over generic pairs, pre-registered.
    rank_ok, max_rank, per_pair, needs_fallback = check_full_jacobian_rank()

    # If a HARD STOP fired (rank > 10), STOP -- do not continue to the tier ladder.
    if max_rank > TRDEG_TARGET:
        print("-" * 76)
        print(f"OVERALL: HARD STOP -- MAX_RANK = {max_rank} > {TRDEG_TARGET}. "
              f"Contradicts the Phase-65 orbit-derived trdeg; Jacobian/point/"
              f"builder bug. Do NOT report a completeness verdict.")
        print("=" * 76)
        return 1, {"stage": "task2-hard-stop", "max_rank": max_rank,
                   "per_pair": per_pair}

    # TASK 3: fine-grained tier increments (names the dependent slot if any).
    tier_ok, ladder, increments, bumped = check_tier_increments(max_rank)

    # Decisive two-route pre-check (full wiring deferred to Task 5).
    two_route_ok, _, orbit_derived = two_route_precheck(max_rank)

    print("-" * 76)
    # Segment classification.
    if max_rank == TRDEG_TARGET and tier_ok and builders_ok and not needs_fallback:
        print(f"OVERALL: FIRST SEGMENT CLEAN -- full candidate Jacobian rank "
              f"== {max_rank} == orbit-derived trdeg {orbit_derived} (two routes "
              f"agree); tier ladder "
              f"({ladder[6]},{ladder[7]},{ladder[8]},{ladder[9]},{ladder[10]}); "
              f"all Task-1 correctness gates GREEN. PAUSED at the first-result "
              f"gate (Tasks 4-6 deferred for human review).")
    elif needs_fallback:
        print(f"OVERALL: FIRST SEGMENT -- NEEDS_FALLBACK (MAX_RANK = {max_rank} == "
              f"{TRDEG_TARGET - 1}). The natural three are deficient by 1; the "
              f"Task-4 fallback ladder must fill the dependent slot. Tier ladder "
              f"({ladder[6]},{ladder[7]},{ladder[8]},{ladder[9]},{ladder[10]}); "
              f"dependent slot named by the increments above. PAUSED for review.")
    else:
        print("OVERALL: FIRST SEGMENT -- FAILURES PRESENT (see FAIL lines above). "
              "PAUSED for review.")
    print("=" * 76)

    result = {
        "stage": "tasks-1-3-complete",
        "guard_ok": guard_ok,
        "builders_ok": builders_ok,
        "max_rank": max_rank,
        "per_pair": per_pair,
        "needs_fallback": needs_fallback,
        "ladder": ladder,
        "increments": increments,
        "bumped": bumped,
        "two_route_ok": two_route_ok,
        "orbit_derived": orbit_derived,
    }
    return (0 if ALL_PASS else 1), result


if __name__ == "__main__":
    _code, _res = segment_main()
    sys.exit(_code)
