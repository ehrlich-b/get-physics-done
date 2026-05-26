"""
(RING) Lemma -- THE SPINE: functional independence of c = Tr(X o Y)
====================================================================
Phase: 66-b-functional-independence-of-c-the-spine, Plan: 01  (RING-02, THE SPINE)
Milestone: v16.0 The (RING) Lemma (math half of the Chalmers gap).

WHAT THIS IS
------------
The single load-bearing, chain-critical result of milestone v16.0. It DEMONSTRATES,
by EXACT computation over Q on the actual non-associative Albert algebra h_3(O),
whether the coupling

    c = Tr(X o Y)              (bidegree (1,1), F_4-invariant)

is functionally (= algebraically, in char 0) INDEPENDENT of the six pointwise
generators

    {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}.

The verdict is EXACTLY one of:
  - rank 7  =>  c INDEPENDENT  (positive pass: the complete single-frame
                third-person record does NOT determine the coupling Phi), OR
  - rank 6  =>  c DEPENDENT    (decisive NEGATIVE, EQUALLY a full pass: c is
                expressible in the pointwise ring R_pt; kills the Phi mechanism).

NEGATIVE-RESULT-IS-SUCCESS: a rank-6 NEGATIVE is a full pass and SHIPS the explicit
pointwise expression P with c = P (verified as a symbolic identity over Q). The
expected verdict (per the committed Phase-65.1 r7==7 preview, RE-DEMONSTRATED here
as this phase's own pre-registered decisive result) is rank 7 / c INDEPENDENT, but
whichever fires is reported HONESTLY.

TWO INDEPENDENT MANDATORY ROUTES that must AGREE (the reward-hacking guard):
  ROUTE 1 (Jacobian): the exact 7x54 sub-Jacobian rank over Q at >=3 generic
    rational point-pairs + a fresh pair (Derksen-Kemper char-0 criterion:
    trdeg = generic Jacobian rank). MAX over the fixed pairs = SPINE_RANK.
  ROUTE 2 (orbit-derivative): exhibit an f_4 direction xi along the F_4-orbit of X
    on which every pointwise generator has ZERO derivative while c has NONZERO
    derivative D_xi c = Tr((xi.X) o Y). Computationally independent of the 7x54 rank.
  ADJUDICATOR: report a verdict ONLY on a DIAGONAL agreement cell --
    (7, exists) => INDEPENDENT; (6, none) => DEPENDENT. Either off-diagonal cell
    ((7,none) or (6,exists)) => NO VERDICT, "CONTRADICTION -- STOP", nonzero exit.

SCOPE BOUNDARY: this establishes FIELD-LEVEL functional independence of c ONLY
(c not in the algebraic closure of R_pt). It does NOT establish ring generation
(Hilbert series / Krull / minimal generators = Phase 68) and is NOT the degree-2
uniqueness Sym^2 branching (Phase 67).

CORRECTED CONSISTENCY (ITEM 4a): rank 7 <= ORBIT_DERIVED_TRDEG (== 10, from the
Phase-65 GATE pair orbit dim 44 => trdeg 54-44=10). rank 7 saturates the
{6 pointwise + c} SUBSET (a 7x54 matrix has rank <= 7) but does NOT saturate the
full transcendence degree -- c is the FIRST of FOUR mixed joint invariants
{c, Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)}. The stale roadmap success-criterion-5
wording "rank 7 saturates trdeg = 54 - orbit_dim = 7" is the FORBIDDEN
Spin(8)-triality back-of-envelope and is explicitly flagged superseded and NOT used.

EXACT-ONLY (the GLOBAL FORBIDDEN PROXY fp-float-rank): every decisive rank is
exact_qq_rank (DomainMatrix-over-QQ), reused VERBATIM from the certified Phase-65
gate. ZERO numpy.linalg.matrix_rank / float-rank / SVD-tolerance on the decisive
path; ZERO `import octonion_algebra` (the float64 file with the det_3 cross-term
bug). A module-local exact-only source guard (scanning THIS __file__) asserts both.

PROVENANCE (decisive REUSE of the FROZEN, certified primitives -- not an oracle;
re-implementing det_3 / jordan / the f_4 builder / exact_qq_rank from scratch risks
a (x1 x2)x3 cross-term port slip that is NOT F_4-invariant and silently corrupts
the rank -- Phase-64.1 fixed exactly this in E.det_3):
  - code/ring_lemma_verification.py (Phase-64.1 FROZEN engine), imported as E:
    jordan, Tr, Tr2, c, det_3, polarize_d, Xsym, Ysym, xs, ys, X_from_symbols,
    _flat27, octonionic_points, inner_derivations, and the 7 base invariants
    inv_Tr_X..inv_c. The trace form Tr(A o B) = E.Tr(E.jordan(A, B)) IS c when
    A=X, B=Y. NEVER touches octonion_algebra.py; NEVER re-freezes det_3.
  - code/orbit_dimension_gate.py (Phase-65 CERTIFIED gate machinery):
    exact_qq_rank (the anti-float guard), infinitesimal_action,
    _select_independent_basis, PAIR_POINTS (4 generic integer octonionic pairs),
    SINGLE_COPY_POINTS (for the X=Y control), _pair_not_proportional,
    _is_genuinely_octonionic_integer, exact_rank_route_crosscheck.
  - code/ring_generating_set.py (Phase-65.1 FROZEN candidate machinery):
    CANDIDATE_GRADS (CANDIDATE_GRADS[0:7] = the 6 pointwise + c rows, FIXED order),
    prefix_rank, candidate_jacobian_matrix_at, _f4_basis, ORBIT_DERIVED_TRDEG (==10),
    check_tier_increments, NAMES, BIDEGREES. REUSE verbatim; slice first-7 for Route 1.

CONVENTION (carry verbatim from the frozen engine):
# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; det3 cross=2Re((x2x1)x3) [generic norm; Phase64.1 factor-order fix]; det3_normalization d(X,X,X)=6*det_3; coupling c=Tr(X o Y) bidegree (1,1) c(X,X)=Tr X^2; f4=span{[L_a,L_b]} dim 52; arithmetic=exact-SymPy-over-Q; ranks=exact_qq_rank=DomainMatrix-over-QQ; NEVER float64 / numpy.linalg.matrix_rank on the decisive path
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible)
# METRIC: Riemannian Fisher (pure algebra; field-theory / gauge / Fourier convention fields are N/A)

RUN DISCIPLINE (watchdog): run FOREGROUND with `python -u code/spine_independence.py`
(unbuffered) -- every check prints a one-line progress marker (per-pair, per-route)
so the run never goes silent (the executor stream-watchdog kills long no-output
symbolic runs ~600s; ~150s precedent in Phase 65.1). Substitute the generic integer
point FIRST (the cached CANDIDATE_GRADS are deliberately un-simplified) so each rank
is ~0.01s; the full run is well under a minute.

Assert-based harness (NO pytest -- the executor venv has sympy/numpy only).
main() exits 0 IFF all checks pass AND a verdict is emitted on a diagonal cell.

Reproducibility: SymPy 1.14.0, NumPy 2.4.3, Python 3.14.2, macOS Darwin 24.6.0.
Deterministic (no random seeds; all evaluation points are the certified hardcoded
integer octonionic pairs from the Phase-65 gate + ONE fresh inline pair defined
here + the engine's octonionic_points()).

References:
  Derksen, H.; Kemper, G. -- Computational Invariant Theory, 2nd ed. (Springer
    2015), Jacobian-criterion section: char-0 trdeg = generic Jacobian rank. THE
    theorem licensing "rank 7 <=> the 7 algebraically (hence functionally)
    independent <=> c not in R_pt". Route 1's license.
  Springer, T.A.; Veldkamp, F.D. -- Octonions, Jordan Algebras and Exceptional
    Groups (Springer 2000); Springer (1973): F_4 = automorphisms preserving Tr and
    the cubic norm => the trace form Tr(X o Y) is F_4-equivariant and non-degenerate
    on the 26 -- exactly what makes xi -> Tr((xi.X) o Y) a nonzero linear functional
    for generic X, Y (the separating direction exists). Route 2's ground.
  Schafer, R.D. -- An Introduction to Nonassociative Algebras (1966):
    Der(h_3(O)) = f_4; inner-derivation formula D_{a,b} = [L_a, L_b]. Grounds the
    f_4 builder reused for Route 2.
  Garibaldi, S.; Guralnick, R.M. -- arXiv:2105.09486 (Lemma 8.1), 2308.08214:
    single-copy F_4-on-26 orbit 24 / Spin(8) / trdeg 3 (reproduced by the certified
    gate) grounds the 6x54 baseline == 6 cross-check (3 X-block + 3 Y-block).
  code/ring_lemma_verification.py + code/orbit_dimension_gate.py +
    code/ring_generating_set.py -- the FROZEN engine + certified gate + candidate
    machinery, reused verbatim.
"""

import os
import re
import sys

# Path-import the FROZEN engine + the certified gate + the candidate machinery
# (sibling files in code/), EXACTLY as ring_generating_set.py does: sys.path insert
# then import. This is the DECISIVE reuse of the certified primitives, NOT an oracle.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ring_lemma_verification as E  # noqa: E402  (path insert must precede import)
from orbit_dimension_gate import (  # noqa: E402
    exact_qq_rank,
    infinitesimal_action,
    _select_independent_basis,
    PAIR_POINTS,
    SINGLE_COPY_POINTS,
    _pair_not_proportional,
    _is_genuinely_octonionic_integer,
    exact_rank_route_crosscheck,
)
from ring_generating_set import (  # noqa: E402
    CANDIDATE_GRADS,
    prefix_rank,
    candidate_jacobian_matrix_at,
    _f4_basis,
    ORBIT_DERIVED_TRDEG,
    check_tier_increments,
    NAMES,
    BIDEGREES,
)

import sympy  # noqa: E402
from sympy import Matrix, diff, simplify, expand, symbols, Rational  # noqa: E402
from sympy.polys.matrices import DomainMatrix  # noqa: E402
from sympy.polys.domains import QQ, ZZ  # noqa: E402


# ============================================================================
# Global pass/fail accumulator + the results dict the adjudicator (Task 4) reads
# ============================================================================
ALL_PASS = True
FAILED_LABELS = []      # labels of every FAIL (for the exit classifier).
RESULTS = {}            # cross-task accumulator: SPINE_RANK, per-pair ranks,
                        # ROUTE2_VERDICT, witness, baseline, controls, etc.


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
# PRE-REGISTRATION (TASK 1) -- frozen as CODE *before* any rank is computed.
#   This defeats fp-force-positive: the points, the exact rank test, and the
#   verdict map are fixed here; an honest NEGATIVE cannot be re-rolled into a
#   positive, and a positive cannot be tuned into existence.
# ============================================================================

# --- The pre-registered CHECK constant (NOT an input to any rank) -----------
# Read from the Phase-65 orbit-dimension GATE: pair orbit dim 44 => trdeg
# 54 - 44 = 10. Imported as ring_generating_set.ORBIT_DERIVED_TRDEG; re-stated
# here as the consistency CHECK that the SPINE rank must satisfy (rank 7 <= 10).
TRDEG_CONSISTENCY_CAP = ORBIT_DERIVED_TRDEG    # == 10

# --- The exact rank test (frozen): exact_qq_rank = DomainMatrix-over-QQ ------
# NEVER numpy.linalg.matrix_rank / SVD-tolerance / sympy float .rank().
# (The symbol is imported above; this line documents the frozen choice.)
RANK_TEST_NAME = "exact_qq_rank = DomainMatrix.from_Matrix(A).convert_to(QQ).rank()"

# --- The aggregator (frozen): MAX over the fixed TEST_PAIRS ------------------
# Rank is lower-semicontinuous: a special (non-generic) point can only UNDER-report
# the rank, so the generic value is the MAX over the fixed generic pairs.
AGGREGATOR_NAME = "MAX over the fixed TEST_PAIRS (rank lower-semicontinuous)"

# --- The FRESH generic integer pair (defined inline; NOT a member of -------
#     PAIR_POINTS). Orchestrator/verifier-independent re-confirmation, mirroring
#     the Phase-65/65.1 hardening. All-nonzero-ish octonion content (>=2 nonzero
#     imaginary comps per off-diagonal), distinct diagonals, X != Y, X not prop Y.
FRESH_X = [4, -1, 2,
           1, -1, 2, 0, 1, -1, 0, 1,      # x1 octonion (imag 1,2,4,5,7)
           0, 1, -2, 1, 0, 1, -1, 0,      # x2 octonion (imag 1,2,3,5,6)
           2, 0, 1, -1, 0, 1, 1, -1]      # x3 octonion (imag 2,3,5,6,7)
FRESH_Y = [-3, 2, 5,
           0, 1, 1, -1, 2, 0, 1, -1,      # x1 octonion (imag 1,2,3,4,6,7)
           1, -1, 0, 2, -1, 1, 0, 1,      # x2 octonion (imag 1,3,4,5,7)
           -1, 2, 1, 0, 1, -1, 1, 0]      # x3 octonion (imag 1,2,4,5,6)
FRESH_LABEL = "PFxPF (fresh inline)"

# --- The fixed TEST_PAIRS: the >=3 certified generic pairs from the gate's ----
#     PAIR_POINTS, PLUS the fresh inline pair. ORDERED dict; iteration order is
#     stable. Every pair is gated below (Task 1) BEFORE any rank is taken.
TEST_PAIRS = dict(PAIR_POINTS)             # P1xP2, P2xP3, P1xP3, P4xP5 (>=3)
TEST_PAIRS[FRESH_LABEL] = (FRESH_X, FRESH_Y)

# --- The VERDICT MAP (frozen here, NOT after seeing the rank) ----------------
# SPINE_RANK -> label. 7 -> INDEPENDENT; 6 -> DEPENDENT (NEGATIVE); else -> STOP.
VERDICT_MAP = {
    7: "c INDEPENDENT (positive pass)",
    6: "c DEPENDENT (decisive NEGATIVE, full pass)",
}


def _verdict_label(rank):
    """The pre-registered verdict label for a SPINE rank (frozen mapping)."""
    return VERDICT_MAP.get(rank, "ANOMALY / STOP (rank not in {6,7})")


def print_preregistration():
    """Print the pre-registration block at startup, BEFORE any rank is computed.
    Gate EVERY TEST pair (>=3 PAIR_POINTS + the fresh inline pair) for genericity
    (_pair_not_proportional + distinct diagonals + genuinely octonionic), and
    confirm the fresh pair is NOT a member of PAIR_POINTS. Returns ok (bool)."""
    print("=" * 76)
    print("PRE-REGISTRATION (frozen as CODE before ANY rank -- defeats fp-force-positive)")
    print("=" * 76)
    print(f"  SymPy {sympy.__version__}; engine E + gate + candidate machinery imported.")
    print(f"  RANK TEST  (frozen): {RANK_TEST_NAME}")
    print(f"             NEVER numpy.linalg.matrix_rank / SVD-tolerance / float .rank().")
    print(f"  AGGREGATOR (frozen): {AGGREGATOR_NAME}")
    print(f"  CONSISTENCY CAP      : SPINE_RANK <= ORBIT_DERIVED_TRDEG == "
          f"{TRDEG_CONSISTENCY_CAP} (Phase-65 GATE: 54 - 44).")
    print(f"  VERDICT MAP (frozen): 7 -> '{VERDICT_MAP[7]}'; "
          f"6 -> '{VERDICT_MAP[6]}'; else -> 'ANOMALY / STOP'.")
    print("  TWO-ROUTE ADJUDICATION (frozen): verdict ONLY on a diagonal cell")
    print("    (7, exists) => INDEPENDENT ; (6, none) => DEPENDENT ;")
    print("    (7, none) or (6, exists) => NO VERDICT, CONTRADICTION -- STOP, nonzero exit.")
    print("")
    print(f"  FIXED TEST_PAIRS ({len(TEST_PAIRS)} total = >=3 PAIR_POINTS + 1 fresh inline):")

    all_ok = True
    fresh_distinct = True
    pair_member_lists = [(list(X), list(Y)) for (X, Y) in PAIR_POINTS.values()]
    for label, (X, Y) in TEST_PAIRS.items():
        okx, dx = _is_genuinely_octonionic_integer(X)
        oky, dy = _is_genuinely_octonionic_integer(Y)
        not_prop = _pair_not_proportional(X, Y)
        not_equal = (list(X) != list(Y))
        gen_ok = okx and oky and not_prop and not_equal
        all_ok = all_ok and _report(
            f"TEST pair {label}: X-octonionic={okx}, Y-octonionic={oky}, "
            f"X!=Y={not_equal}, X-not-prop-Y={not_prop} (genericity gate)",
            gen_ok)

    # The fresh pair must NOT be one of the PAIR_POINTS members (independence).
    fresh_distinct = ((list(FRESH_X), list(FRESH_Y)) not in pair_member_lists) and \
                     (list(FRESH_X) not in [m for pair in pair_member_lists for m in pair]) and \
                     (list(FRESH_Y) not in [m for pair in pair_member_lists for m in pair])
    all_ok = all_ok and _report(
        f"FRESH pair {FRESH_LABEL} is NOT a member of PAIR_POINTS "
        f"(orchestrator/verifier-independent re-confirmation)",
        fresh_distinct)

    # Confirm the verdict map is frozen as code (7/6/else) BEFORE evaluation.
    map_ok = (VERDICT_MAP.get(7, "").startswith("c INDEPENDENT")
              and VERDICT_MAP.get(6, "").startswith("c DEPENDENT")
              and _verdict_label(5) == "ANOMALY / STOP (rank not in {6,7})")
    all_ok = all_ok and _report(
        "VERDICT MAP frozen as code (7->INDEPENDENT, 6->DEPENDENT, else->STOP) "
        "BEFORE any rank computed",
        map_ok)

    RESULTS["preregistration_ok"] = all_ok
    return all_ok


# ============================================================================
# ROUTE 1 (TASK 2) -- exact 7x54 sub-Jacobian rank over Q (+ baseline + X=Y
#   control + three-exact-domain cross-check). REUSE the frozen candidate
#   machinery: prefix_rank(k, pp) slices CANDIDATE_GRADS[0:k], substitutes the
#   integer point FIRST (the cached gradients are deliberately un-simplified --
#   det_3 deg 3 / 54-var swell control, fp-rank-before-substitution rejected),
#   then exact_qq_rank. CANDIDATE_GRADS[0:7] = {Tr X, Tr X^2, det X, Tr Y, Tr Y^2,
#   det Y, c} in FIXED order; CANDIDATE_GRADS[0:6] = the pointwise sextet.
#
# Derksen-Kemper char-0 criterion: trdeg Q(f_1..f_7) = generic rank of the 7x54
# Jacobian [d f_i / d z_j]. A 7x54 matrix has rank <= 7, so SPINE_RANK in {7, 6}:
#   rank 7 <=> the 7 are algebraically (hence functionally) independent <=> c not
#             in the algebraic closure of R_pt (c INDEPENDENT, the positive);
#   rank 6 <=> c is dependent on the pointwise sextet (c DEPENDENT, the NEGATIVE).
# ============================================================================

def route1_spine_rank():
    """test-route1-rank + test-rank-stability: for each generic pair in TEST_PAIRS
    (>=3 PAIR_POINTS + the fresh inline pair), compute the 7x54 sub-Jacobian rank
    prefix_rank(7, pp) (rows = CANDIDATE_GRADS[0:7]; substitute-first then
    exact_qq_rank). SPINE_RANK = MAX over TEST_PAIRS (rank lower-semicontinuous).
    Assert the rank is STABLE (the SAME) at every generic pair.

    Returns (ok, spine_rank, per_pair)."""
    print("Task 2 (Route 1) -- 7x54 sub-Jacobian rank over Q (MAX over TEST_PAIRS):")
    per_pair = {}
    for label, pp in TEST_PAIRS.items():
        r = prefix_rank(7, pp)                 # exact_qq_rank of the 7x54 (substitute-first)
        per_pair[label] = r
        print(f"  [INFO] prefix_rank(7, {label}) = {r}  (exact over Q)")
    spine_rank = max(per_pair.values())

    pairs_str = ", ".join(f"{lbl}={r}" for lbl, r in per_pair.items())
    print(f"  [INFO] per-pair 7x54 rank: {pairs_str}; SPINE_RANK = MAX = {spine_rank}")

    # SPINE_RANK is a definite integer in {7, 6} (a 7x54 matrix has rank <= 7).
    definite_ok = _report(
        f"SPINE_RANK == {spine_rank} is a definite integer in {{6,7}} "
        f"(MAX over {len(per_pair)} generic pairs via exact_qq_rank; "
        f"7x54 maxes at 7)  [test-route1-rank]",
        spine_rank in (6, 7))

    # Rank stability: the SAME rank at every generic pair (a differing pair would
    # be secretly non-generic -- check _pair_not_proportional + distinct diagonals
    # before doubting the engine; STOP rather than tune).
    stable = (len(set(per_pair.values())) == 1)
    stable_ok = _report(
        f"7x54 rank STABLE across all {len(per_pair)} generic pairs "
        f"(all == {spine_rank}; rank lower-semicontinuous, MAX = generic value)  "
        f"[test-rank-stability]",
        stable)
    if not stable:
        worst = min(per_pair, key=lambda k: per_pair[k])
        print(f"  [STOP-HINT] rank differs at {worst} (={per_pair[worst]}): that pair "
              f"is likely secretly NON-generic. Recheck _pair_not_proportional + "
              f"distinct diagonals BEFORE doubting the engine; do NOT tune.")

    RESULTS["SPINE_RANK"] = spine_rank
    RESULTS["route1_per_pair"] = per_pair
    return (definite_ok and stable_ok), spine_rank, per_pair


def route1_baseline_six():
    """test-baseline-6: the 6x54 pointwise-sextet control. prefix_rank(6, pp)
    (CANDIDATE_GRADS[0:6]) MUST be exactly 6 at every generic pair (3 X-block +
    3 Y-block; single-copy trdeg 3 + 3, Garibaldi-Guralnick). If != 6 the
    engine/builder is broken -- STOP, do NOT tune.

    Returns (ok, per_pair)."""
    print("Task 2 (Route 1) -- 6x54 pointwise-sextet baseline control:")
    per_pair = {}
    for label, pp in TEST_PAIRS.items():
        r = prefix_rank(6, pp)
        per_pair[label] = r
        print(f"  [INFO] prefix_rank(6, {label}) = {r}")
    all_six = all(r == 6 for r in per_pair.values())
    pairs_str = ", ".join(f"{lbl}={r}" for lbl, r in per_pair.items())
    ok = _report(
        f"6x54 pointwise baseline == 6 at EVERY generic pair ({pairs_str}); "
        f"3 X-block + 3 Y-block (Garibaldi-Guralnick single-copy trdeg 3+3)  "
        f"[test-baseline-6]",
        all_six)
    if not all_six:
        print("  [HARD-STOP] baseline != 6 at some generic pair: the pointwise-sextet "
              "independence is certified upstream (single-copy trdeg 3). This is an "
              "engine/layout/base-invariant BUG -- STOP, do NOT trust any verdict.")
    RESULTS["baseline_per_pair"] = per_pair
    return ok, per_pair


def route1_xeqy_control():
    """test-xeqy-control: degeneracy control. Evaluate prefix_rank(7, (P, P)) at a
    DIAGONAL pair X = Y (P a certified generic single point). MUST be <= 6: X=Y
    collapses c to Tr X^2 in R_pt, so the {6 pointwise + c} set drops rank. This is
    a control EXPECTED to fail to reach 7 -- NOT a counterexample, NOT a valid
    independence-test point (fp-non-generic-point: X=Y is run ONLY as a control).

    Returns (ok, rank_xeqy)."""
    print("Task 2 (Route 1) -- X=Y degeneracy control (EXPECTED <= 6, NOT a test point):")
    # P = a certified generic single point from the gate (genuinely octonionic).
    P = SINGLE_COPY_POINTS["P1 (planner spike)"]
    r = prefix_rank(7, (P, P))
    print(f"  [INFO] prefix_rank(7, (P,P)) = {r}  (X=Y diagonal control)")
    ok = _report(
        f"X=Y control: prefix_rank(7, (P,P)) == {r} <= 6 (X=Y collapses c to "
        f"Tr X^2 in R_pt; degenerate, EXCLUDED as a test point -- NOT a "
        f"counterexample)  [test-xeqy-control]",
        r <= 6)
    RESULTS["xeqy_control_rank"] = r
    return ok, r


def _seven_row_jacobian_at(pp):
    """Build the 7x54 sub-Jacobian at a pair by slicing CANDIDATE_GRADS[0:7] and
    substituting the integer point FIRST (NOT simplify-ing the symbolic gradient).
    Equivalent to candidate_jacobian_matrix_at(pp)[0:7, :] but built directly from
    the cached 7 rows. Returns (A_Q, A_Z) the rational and integer-cleared Matrices."""
    from sympy import lcm, denom, Integer
    X27, Y27 = pp
    subs_pt = {E.xs[k]: Rational(X27[k]) for k in range(27)}
    subs_pt.update({E.ys[k]: Rational(Y27[k]) for k in range(27)})
    rowsQ, rowsZ = [], []
    for grad in CANDIDATE_GRADS[0:7]:
        row = [g.subs(subs_pt) for g in grad]      # length-54 rational row
        rowsQ.append(list(row))
        d = 1
        for e in row:
            d = lcm(d, denom(e))
        rowsZ.append([Integer(e * d) for e in row])
    return Matrix(rowsQ), Matrix(rowsZ)


def route1_exactness_crosscheck():
    """test-exactness-crosscheck: run the three-exact-domain cross-check on the
    DECISIVE 7x54 sub-Jacobian at ONE generic pair: QQ-on-fractional ==
    QQ-on-integer-cleared == ZZ-on-integer-cleared. All three must agree, certifying
    exact_qq_rank is genuinely EXACT over Q at width 54 -- NOT a float proxy
    (fp-float-rank rejected). Also confirm the gate's exact_rank_route_crosscheck
    agrees on ITS object (the 52x54 f_4-tangent rank) as an independent exactness
    witness reused verbatim.

    Returns ok (bool)."""
    print("Task 2 (Route 1) -- three-exact-domain cross-check on the 7x54 (width 54):")
    first_label = next(iter(TEST_PAIRS))
    pp = TEST_PAIRS[first_label]
    A_Q, A_Z = _seven_row_jacobian_at(pp)
    r_qq_frac = DomainMatrix.from_Matrix(A_Q).convert_to(QQ).rank()
    r_qq_int = DomainMatrix.from_Matrix(A_Z).convert_to(QQ).rank()
    r_zz_int = DomainMatrix.from_Matrix(A_Z).convert_to(ZZ).rank()
    seven_agree = (r_qq_frac == r_qq_int == r_zz_int)

    # Independent exactness witness: the gate helper on the f_4-tangent (52x54).
    X27, Y27 = pp
    f4_basis, _n = _f4_basis()
    gate_agree, gate_triple = exact_rank_route_crosscheck(f4_basis, X27, Y27)

    ok = _report(
        f"THREE-EXACT-DOMAIN at {first_label}: 7x54 candidate Jacobian "
        f"QQ-frac/QQ-int/ZZ-int = ({r_qq_frac},{r_qq_int},{r_zz_int}) all agree; "
        f"gate f_4-tangent cross-check {gate_triple} agree={gate_agree} "
        f"(exact_qq_rank EXACT over Q at width 54, not a float proxy)  "
        f"[test-exactness-crosscheck; fp-float-rank rejected]",
        seven_agree and gate_agree)
    RESULTS["exactness_triple_7x54"] = (r_qq_frac, r_qq_int, r_zz_int)
    return ok


def run_route1():
    """Run all Route-1 checks in order. Returns (ok, spine_rank)."""
    spine_ok, spine_rank, _pp = route1_spine_rank()
    baseline_ok, _bp = route1_baseline_six()
    xeqy_ok, _rxy = route1_xeqy_control()
    exact_ok = route1_exactness_crosscheck()
    # The 7x54 shape is structurally guaranteed (7 cached rows, 54 columns); record.
    shape_ok = _report(
        "Route-1 Jacobian shape == 7x54 (rows = 6 pointwise + c; cols = 27 X + 27 Y)",
        len(CANDIDATE_GRADS[0:7]) == 7 and len(CANDIDATE_GRADS[0]) == 54)
    return (spine_ok and baseline_ok and xeqy_ok and exact_ok and shape_ok), spine_rank


# ============================================================================
# main() -- assembled in Task 6. Interim version (Tasks 1-2): pre-registration
#   then Route 1. Tasks 3-6 add Route 2, the adjudicator, the NEGATIVE
#   constructor, and the full ordered main().
# ============================================================================
def main():
    """Interim main (Tasks 1-2): pre-registration -> Route 1. Route 2 + adjudicator
    + NEGATIVE constructor + the full ordered main() are wired in Tasks 3-6."""
    prereg_ok = print_preregistration()
    print("-" * 76)
    route1_ok, spine_rank = run_route1()
    print("-" * 76)
    print(f"TASKS 1-2: pre-registration + Route 1 done. SPINE_RANK = {spine_rank} "
          f"({_verdict_label(spine_rank)}). Route 2 + adjudicator wired in Tasks 3-6.")
    print("=" * 76)
    return prereg_ok and route1_ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
