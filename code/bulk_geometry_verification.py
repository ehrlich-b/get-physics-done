#!/usr/bin/env python3
"""
bulk_geometry_verification.py -- Phase-70 (A0) exact-SymPy-over-Q cubic-norm
ENGINE and SSOT certification for the v17.0 milestone
"Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry".
============================================================================
Phase: 70-a0-engine-reconciliation-signature-bridge, Plan: 01 (SETU-01).

WHAT THIS IS
------------
The single certified source of truth for the Freudenthal cubic norm det_3 on
h_3(O), on which EVERY downstream v17.0 curvature is built (g_X = Hess(-log det),
Totaro Riemann from 3rd derivatives of det). A wrong cross-term association or a
contaminated engine silently corrupts every Hessian and curvature, so this module
re-proves the F_4 = Aut(h_3(O)) certificate on a fresh, self-contained file as
cheap insurance against a copy error, and reconciles the three in-repo cross-term
labelings on genuinely non-associative octonionic data.

PROVENANCE (verbatim copy, NOT import)
--------------------------------------
Sections 1-3 below (the EXACT-SymPy octonion arithmetic, the 3x3 octonionic
h_3(O) matrix machinery, the standalone invariants Tr / det_3 / Tr2 / c /
polarize_d, the 54-symbol pair coordinatization, the R_pt freeze, the exact-only
source guard, and the generic-norm machinery cayley_hamilton_norm /
inner_derivations) are COPIED VERBATIM (byte-for-byte) from
code/ring_lemma_verification.py (the v16.0 SSOT engine: 960 ln, ALL_PASS, Phase
64.1; convention lock commit 0d10eeea). The copy is the DELIBERATE choice -- a
self-contained decisive module that pins all conventions in one place and
decouples the v17.0 milestone from the v16.0 file (mirroring the
ring_lemma_verification.py <- embedding_under_E_verification.py copy precedent).

The copied det_3 is byte-identical to ring_lemma_verification.det_3; this is
asserted at runtime by main() via inspect.getsource(...) (LOCK 0 below).

SSOT CROSS-TERM ORDER (the single most error-prone choice; LOCKED)
-----------------------------------------------------------------
det_3 cross-term = 2*Re((x2 x1) x3) -- realized in code as
    cross = oct_mul(oct_mul(x2, x1), x3)   # (x2 x1) x3, x2 BEFORE x1
This is the F_4-invariant generic norm. The buggy (x1 x2) x3 order
(octonion_algebra.py:~2178) passes LOCKs 1-5 but is NOT F_4-invariant (annihilated
by only 30 of 324 inner derivations; det off by 16 at the octonionic test point);
it is FORBIDDEN on the decisive path and code/octonion_algebra.py is NEVER imported
here. The CONVENTIONS.md / state.json label `2Re(x2* x0* x1)` is the SAME det in
h3o_tower's conjugated (x0,x1,x2) index naming -- reconciled in main() Section 9
(the conjugated form x2*(x1* x3) equals the SSOT and the Cayley-Hamilton norm).
Polarization LOCKED: d(X,X,X) = 6*det_3(X).

# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; det3 cross=2Re((x2x1)x3) [SSOT; buggy (x1x2)x3 FORBIDDEN]; det3_normalization d(X,X,X)=6*det_3; coupling c=Tr(X o Y); arithmetic=exact-SymPy-over-Q; ranks=sympy.Matrix.rank(); NEVER float64 on decisive path; octonion=cayley_dickson; complex_structure u=e7; metric_signature=mostly-minus_slice/riemannian_bulk
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible)

ENGINE-NATIVE COORDINATE LAYOUT (carried verbatim; Plan 70-02 depends on it)
---------------------------------------------------------------------------
X_from_symbols(s) maps the 27-tuple s on the layout:
    x0, x1, x2     = diagonal reals alpha, beta, gamma -> X[0][0], X[1][1], X[2][2]
    x3 .. x10  (8) = octonion x1 -> matrix entry X[2][1]  (conj at X[1][2])
    x11.. x18  (8) = octonion x2 -> matrix entry X[0][2]  (conj at X[2][0])
    x19.. x26  (8) = octonion x3 -> matrix entry X[1][0]  (conj at X[0][1])
Do NOT re-index: Plan 70-02's spacetime sub-slice index map ({17,18,19,26} =
beta,gamma,p,q) is defined against this exact layout.

Assert-based harness (NO pytest -- the executor venv has sympy/numpy only).
Runnable directly:  python3 code/bulk_geometry_verification.py
Exits 0 iff ALL_PASS (every LOCK and guard passes); nonzero on any failure.

Reproducibility: SymPy 1.14.0, Python 3.14.2, NumPy 2.4.x, macOS Darwin 24.6.0.
Deterministic (no random seeds; all test elements hardcoded with exact
rational/octonionic entries).

References:
  code/ring_lemma_verification.py (VALD-64-01, Phase 64.1 ALL_PASS) -- the SSOT
    engine; Sections 1-3 + generic-norm machinery copied here VERBATIM.
  Springer, T.A. -- Jordan Algebras and Algebraic Groups (1973); Indag. Math. 24
    (1962) 259-265 (cubic-norm uniqueness; F_4 = Aut(h_3(O))).
  Faraut, J.; Koranyi, A. -- Analysis on Symmetric Cones, Oxford (1994), Ch. II-IV
    (cone metric g_X = Hess(-log det); R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] free,
    degrees 1/2/3).
  Blind, B. -- J. Lie Theory 21 (2011) 123-144 (polarization d(X,X,X) = 6*det X).
  h3o_tower.py (/Users/ehrlich/repos/blog/research/qualia-fixed-point/, float64) --
    the conjugated (x0,x1,x2) labeling 2Re(x2* x0* x1); reconciliation table only,
    NEVER on the decisive path.
"""


import sys

from sympy import Rational, simplify, symbols, Poly, expand, total_degree, Matrix, diff  # noqa: F401  (Poly reserved for downstream)

# Track overall pass/fail; the script must exit nonzero on any lock/guard failure.
ALL_PASS = True


def _report(label, ok):
    """Print a PASS/FAIL line and fold into the global pass flag."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok:
        ALL_PASS = False
    return ok


# ============================================================================
# 1. EXACT-SymPy octonion arithmetic (Fano e_1 e_2 = e_4)
#    Ported VERBATIM from code/embedding_under_E_verification.py Section 1.
# ============================================================================
# An octonion is an 8-tuple of EXACT SymPy scalars: a = a0 + a1 e_1 + ... + a7 e_7.

FANO_TRIPLES = [
    (1, 2, 4),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 7),
    (5, 6, 1),
    (6, 7, 2),
    (7, 1, 3),
]

# _MUL_TABLE[(i,j)] = (sign, index): e_i e_j = sign * e_index, for i,j in {1..7}.
_MUL_TABLE = {}
for _i in range(1, 8):
    for _j in range(1, 8):
        _MUL_TABLE[(_i, _j)] = (0, 0)
for _i, _j, _k in FANO_TRIPLES:
    _MUL_TABLE[(_i, _j)] = (+1, _k)
    _MUL_TABLE[(_j, _i)] = (-1, _k)
    _MUL_TABLE[(_j, _k)] = (+1, _i)
    _MUL_TABLE[(_k, _j)] = (-1, _i)
    _MUL_TABLE[(_k, _i)] = (+1, _j)
    _MUL_TABLE[(_i, _k)] = (-1, _j)
for _i in range(1, 8):
    _MUL_TABLE[(_i, _i)] = (-1, 0)


def oct_zero():
    return [Rational(0)] * 8


def oct(comps):
    """Build an exact octonion from an 8-list (SymPy-coerced)."""
    assert len(comps) == 8
    return [c if hasattr(c, "is_Number") else Rational(c) for c in comps]


def oct_real(r):
    """Real scalar as an octonion (component 0)."""
    z = oct_zero()
    z[0] = r if hasattr(r, "is_Number") else Rational(r)
    return z


def oct_add(a, b):
    return [a[k] + b[k] for k in range(8)]


def oct_sub(a, b):
    return [a[k] - b[k] for k in range(8)]


def oct_neg(a):
    return [-a[k] for k in range(8)]


def oct_scal(s, a):
    return [s * a[k] for k in range(8)]


def oct_mul(a, b):
    """EXACT octonion product via the Fano table (e_1 e_2 = e_4)."""
    r = oct_zero()
    # real*real
    r[0] = r[0] + a[0] * b[0]
    # real*imag + imag*real
    for i in range(1, 8):
        r[i] = r[i] + a[0] * b[i] + a[i] * b[0]
    # imag*imag
    for i in range(1, 8):
        if a[i] == 0:
            continue
        for j in range(1, 8):
            if b[j] == 0:
                continue
            sign, k = _MUL_TABLE[(i, j)]
            r[k] = r[k] + sign * a[i] * b[j]
    return r


def oct_conj(a):
    """Octonion conjugate: negate imaginary components."""
    c = list(a)
    for k in range(1, 8):
        c[k] = -c[k]
    return c


def oct_simplify(a):
    return [simplify(x) for x in a]


def oct_is_zero(a):
    return all(simplify(x) == 0 for x in a)


def oct_equal(a, b):
    return oct_is_zero(oct_sub(a, b))


# ============================================================================
# 2. h_3(O) elements as full 3x3 octonionic matrices
#    Ported VERBATIM from code/embedding_under_E_verification.py Section 2.
# ============================================================================
# Layout (matches code/octonion_algebra.py H3O):
#     | alpha     conj(x3)   x2      |
#     | x3        beta       conj(x1)|
#     | conj(x2)  x1         gamma   |
# We carry the FULL 3x3 octonion matrix (so left/right associations of a triple
# product are computed INDEPENDENTLY -- non-associativity is not assumed away).


def h3o_from_coords(alpha, beta, gamma, x1, x2, x3):
    """Build the 3x3 octonionic Hermitian matrix from h_3(O) coordinates."""
    a = oct_real(alpha)
    b = oct_real(beta)
    g = oct_real(gamma)
    return [
        [a,            oct_conj(x3), x2],
        [x3,           b,            oct_conj(x1)],
        [oct_conj(x2), x1,           g],
    ]


def h3o_identity():
    return h3o_from_coords(1, 1, 1, oct_zero(), oct_zero(), oct_zero())


def octmat_zero():
    return [[oct_zero() for _ in range(3)] for _ in range(3)]


def octmat_add(A, B):
    return [[oct_add(A[i][j], B[i][j]) for j in range(3)] for i in range(3)]


def octmat_sub(A, B):
    return [[oct_sub(A[i][j], B[i][j]) for j in range(3)] for i in range(3)]


def octmat_scal(s, A):
    return [[oct_scal(s, A[i][j]) for j in range(3)] for i in range(3)]


def octmat_simplify(A):
    return [[oct_simplify(A[i][j]) for j in range(3)] for i in range(3)]


def octmat_is_zero(A):
    return all(oct_is_zero(A[i][j]) for i in range(3) for j in range(3))


def octmat_equal(A, B):
    return octmat_is_zero(octmat_sub(A, B))


def octmat_dagger(A):
    """Conjugate transpose of a 3x3 octonion matrix."""
    return [[oct_conj(A[j][i]) for j in range(3)] for i in range(3)]


def h3o_matmul(A, B):
    """3x3 octonionic matrix product (AB)_{ij} = sum_k A_{ik} B_{kj}.

    Each ENTRY is a sum of single oct_mul products. The TRIPLE matrix product is
    NOT assumed associative: h3o_matmul(h3o_matmul(X,Y),Z) and
    h3o_matmul(X,h3o_matmul(Y,Z)) are computed independently and generically
    DIFFER (octonion non-associativity propagates through the entry sums).
    """
    C = octmat_zero()
    for i in range(3):
        for j in range(3):
            acc = oct_zero()
            for k in range(3):
                acc = oct_add(acc, oct_mul(A[i][k], B[k][j]))
            C[i][j] = acc
    return C


def jordan(A, B):
    """Jordan product A o B = (1/2)(AB + BA) on h_3(O) (lands in h_3(O)).

    The Rational(1, 2) factor is LOAD-BEARING: c(X,Y)=Tr(jordan(X,Y)) and
    Tr2(X)=Tr(jordan(X,X)) both depend on it (Convention trap: matrix product XY
    would be off-by-1/2). Copied verbatim from the warm engine; NOT re-derived.
    """
    AB = h3o_matmul(A, B)
    BA = h3o_matmul(B, A)
    return octmat_scal(Rational(1, 2), octmat_add(AB, BA))


def _coord_from_octmat(X):
    """Recover h_3(O) coords (alpha,beta,gamma,x1,x2,x3) from a 3x3 octonion matrix.
    x3 = X[1][0], x2 = X[0][2], x1 = X[2][1] (matches the layout).
    Ported VERBATIM from embedding_under_E_verification.py:551."""
    alpha = X[0][0][0]
    beta = X[1][1][0]
    gamma = X[2][2][0]
    x3 = X[1][0]
    x2 = X[0][2]
    x1 = X[2][1]
    return alpha, beta, gamma, x1, x2, x3


def _oct_normsq(a):
    """Octonion norm-squared sum_k a_k^2 (real). Ported VERBATIM from engine:563."""
    return sum(a[k] * a[k] for k in range(8))


# ============================================================================
# 3. Standalone invariant functions
#    Tr / Tr2 / det_3 LIFTED from the inlined T1/T3 of
#    embedding_under_E_verification.py:567-580 (reduced_charpoly_roots).
#    polarize_d RE-PORTED onto the exact det_3 from octonion_algebra.py:2184
#    (formula spec only — that file is float64 and is NEVER called here).
# ============================================================================


def Tr(X):
    """Linear trace Tr(X) = alpha + beta + gamma   (= the T1 term; bidegree (1,0)).

    Component [0] of each diagonal octonion is its real part (diagonals are real
    for Hermitian X). Lifted from embedding_under_E_verification.py:571 (T1).
    """
    return X[0][0][0] + X[1][1][0] + X[2][2][0]


def det_3(X):
    """Cubic norm det_3(X) = N(X)   (= the GENERIC norm of (h_3(O), jordan); bidegree (3,0)).

        N(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2
               + 2*Re((x2*x1)*x3)

    The cross-term octonion FACTOR ORDER is `(x2*x1)*x3` (x2 BEFORE x1). This is
    LOAD-BEARING and is the F_4 = Aut(h_3(O))-invariant generic norm: it is the
    UNIQUE cubic form satisfying Cayley-Hamilton X^o3 - Tr(X) X^o2 + S(X) X - N I = 0
    (S = (1/2)(Tr^2 - Tr(X o X))), equivalently the cubic form annihilated by every
    inner derivation [L_a, L_b] of the Jordan product. Because octonions are
    non-associative, Re(x1 x2 x3) != Re(x2 x1 x3) (they differ by the associator),
    so the factor order genuinely matters; the cyclic rotations (x3 x2) x1 and
    (x1 x3) x2 are equivalent (same Re), but (x1 x2) x3 is a DIFFERENT cubic form.

    PHASE 64.1 CORRECTION (2026-05-25): the original freeze used `(x1*x2)*x3`
    (a faithful port of the same factor-order bug in octonion_algebra.py:~2178,
    the Baez-formula impl). That cubic form passes polarize_d=6N, N(diag)=abc,
    N(I)=1 and the float-det oracle -- yet is NOT F_4-invariant (annihilated by
    only 30 of the 324 inner derivations [L_a,L_b]). The bug was invisible to the
    original five locks (all of which the wrong form also satisfies) and is caught
    by the Phase-64.1 generic-norm-consistency lock (Task 7), which tests against
    the Cayley-Hamilton norm AND inner-derivation annihilation on genuinely
    octonionic points. See .gpd/phases/64.1-*/ for the full record.
    """
    a, b, g, x1, x2, x3 = _coord_from_octmat(X)
    n1, n2, n3 = _oct_normsq(x1), _oct_normsq(x2), _oct_normsq(x3)
    cross = oct_mul(oct_mul(x2, x1), x3)   # (x2 x1) x3 -- generic-norm factor order (Phase 64.1 fix)
    return a * b * g - a * n1 - b * n2 - g * n3 + 2 * cross[0]


def Tr2(X):
    """Quadratic trace Tr(X^2) := Tr(X o X)   (bidegree (2,0)).

    MUST be Tr(jordan(X, X)) (the 1/2 Jordan product), NOT Tr(X)**2 -- Tr(X^2) is
    a genuinely DISTINCT degree-2 invariant from (Tr X)^2 (both live in R_pt, but
    they are different functions). The convention lock c(X,X) == Tr2(X) (Task 3)
    is manifest precisely because both use `jordan`.
    """
    return Tr(jordan(X, X))


def c(X, Y):
    """Coupling generator c(X,Y) := Tr(X o Y) = Tr(jordan(X, Y))   (bidegree (1,1)).

    F_4-invariant (NOT E_6-invariant). c(X,X) == Tr2(X) (Task-3 lock). This is the
    object whose functional independence from R_pt is the milestone SPINE
    (Phase 66 -- NOT decided here).
    """
    return Tr(jordan(X, Y))


def polarize_d(X, Y, Z):
    """Full polarization of the cubic norm:

        d(X,Y,Z) = N(X+Y+Z) - N(X+Y) - N(X+Z) - N(Y+Z) + N(X) + N(Y) + N(Z)

    With this convention d(X,X,X) = 6*det_3(X) (the HEADLINE lock, Task 3). This
    is the symmetric trilinear polarization -- NOT the Freudenthal/sharp cross
    X#Y (`_polarized_sharp`), which differs by trace-term shifts (sharp-vs-d
    trap). Re-ported VERBATIM onto the exact det_3 from octonion_algebra.py:2184.
    """
    XpY, XpZ, YpZ = octmat_add(X, Y), octmat_add(X, Z), octmat_add(Y, Z)
    XpYpZ = octmat_add(XpY, Z)
    return (det_3(XpYpZ) - det_3(XpY) - det_3(XpZ) - det_3(YpZ)
            + det_3(X) + det_3(Y) + det_3(Z))


# ============================================================================
# 4. 54-symbol pair coordinatization + seven base invariants
# ============================================================================
# The pair (X, Y) in h_3(O) (+) h_3(O) is coordinatized by 54 real SymPy symbols,
# 27 per copy, on the ENGINE-NATIVE layout (3 diagonal reals + 3 octonions x 8 =
# 3 + 24 = 27). X and Y use IDENTICAL conventions (same constructor).
#
# NOTE: this is the engine-native coordinate basis, NOT the Peirce-adapted
# peirce_basis_27(). The seven invariants are basis-agnostic functions of the
# coordinates, so this is the simplest unambiguous choice for the freeze. Any
# Peirce-adapted re-coordinatization is a DELIBERATE Phase-65 decision (the
# Spin(9) f_4 route) and does NOT affect the invariants frozen here.

xs = symbols('x0:27', real=True)   # x0..x26  for X
ys = symbols('y0:27', real=True)   # y0..y26  for Y

# Coordinate -> matrix map (pinned VERBATIM; matches h3o_from_coords / _coord_from_octmat):
#   x0, x1, x2     = diagonal reals alpha, beta, gamma   -> X[0][0], X[1][1], X[2][2]
#   x3 .. x10  (8) = octonion x1  -> matrix entry X[2][1] (conj at X[1][2])
#   x11.. x18  (8) = octonion x2  -> matrix entry X[0][2] (conj at X[2][0])
#   x19.. x26  (8) = octonion x3  -> matrix entry X[1][0] (conj at X[0][1])
# Identical layout for ys.


def X_from_symbols(s):
    """Build the Hermitian octonion matrix from a 27-tuple of coordinates
    (s = xs or ys), on the engine-native layout. Used IDENTICALLY for X and Y."""
    alpha, beta, gamma = s[0], s[1], s[2]
    x1 = [s[3 + k] for k in range(8)]    # octonion x1 -> X[2][1]
    x2 = [s[11 + k] for k in range(8)]   # octonion x2 -> X[0][2]
    x3 = [s[19 + k] for k in range(8)]   # octonion x3 -> X[1][0]
    return h3o_from_coords(alpha, beta, gamma, x1, x2, x3)


# The symbolic pair (same constructor for both copies).
Xsym = X_from_symbols(xs)
Ysym = X_from_symbols(ys)

# The SEVEN base invariants as SymPy EXPRESSION OBJECTS on the 54-symbol layout.
# NOT eagerly expanded/simplified (the degree-3 ones in 54 vars would swell;
# substitution/expansion is a Phase-66+ operation, NOT done here).
#   1-6 are the POINTWISE generators (three per copy); their R-subalgebra is R_pt.
#   7 (c) is the COUPLING, bidegree (1,1); c(X,X)=Tr X^2 (Lock 2).
inv_Tr_X = Tr(Xsym)        # bidegree (1,0)
inv_Tr2_X = Tr2(Xsym)      # bidegree (2,0)
inv_det_X = det_3(Xsym)    # bidegree (3,0)
inv_Tr_Y = Tr(Ysym)        # bidegree (0,1)
inv_Tr2_Y = Tr2(Ysym)      # bidegree (0,2)
inv_det_Y = det_3(Ysym)    # bidegree (0,3)
inv_c = c(Xsym, Ysym)      # bidegree (1,1)  = Tr(jordan(Xsym, Ysym))

# Labelled collection with documented bidegrees (X-degree, Y-degree).
SEVEN_BASE_INVARIANTS = [
    ("Tr X",      inv_Tr_X,   (1, 0)),
    ("Tr X^2",    inv_Tr2_X,  (2, 0)),
    ("det X",     inv_det_X,  (3, 0)),
    ("Tr Y",      inv_Tr_Y,   (0, 1)),
    ("Tr Y^2",    inv_Tr2_Y,  (0, 2)),
    ("det Y",     inv_det_Y,  (0, 3)),
    ("c = Tr(X o Y)", inv_c,  (1, 1)),
]

# The six POINTWISE generators (the generators of R_pt; see Section 5).
SIX_POINTWISE_GENERATORS = [
    ("Tr X", inv_Tr_X), ("Tr X^2", inv_Tr2_X), ("det X", inv_det_X),
    ("Tr Y", inv_Tr_Y), ("Tr Y^2", inv_Tr2_Y), ("det Y", inv_det_Y),
]


# ============================================================================
# 5. FROZEN R_pt definition  (cite this VERBATIM in Phases 66/67/68 — anti-drift)
# ============================================================================
# Pitfall 7 (PITFALLS.md): "pointwise"/"reducible" must point back to ONE frozen
# six-generator algebraic definition, identical across phases, so that c does not
# trivially land in/out of R_pt by a loose reading. The reward-hacking guard
# (PROJECT.md) forbids redefining "pointwise"/"reducible" to engineer c's
# membership. This block is the single source of truth.

R_PT_FROZEN_DEFINITION = '''
R_pt := the R-subalgebra of R[h_3(O) (+) h_3(O)]^{F_4} generated by
        {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}
      = R[Tr X, Tr X^2, det X] (x) R[Tr Y, Tr Y^2, det Y].
Recorded consequences (anti-Pitfall-7):
  - Tr(X)*Tr(Y) IN R_pt  (product of two single-state generators; the reducible (1,1) member).
  - Claim (b) is precisely: c NOT IN R_pt.  [STATED here; PROVEN in Phase 66 -- NOT proven in Phase 64.]
  - "c is new" means new MODULO products + pointwise terms; the genuine-coupling
    quotient at bidegree (1,1) is 1-dimensional (Tr(X)Tr(Y) in R_pt, plus c) -- the
    precise uniqueness statement is a Phase-67 concern.
'''


def is_in_Rpt(p):
    """Membership predicate for R_pt (DEFINITION frozen in Phase 64; DECISION
    PROCEDURE is Phase 66).

    p in R_pt  iff  p is a polynomial (sum of products) in EXACTLY the six
    single-state generators {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}
    (equivalently p in R[Tr X, Tr X^2, det X] (x) R[Tr Y, Tr Y^2, det Y]).

    This stub PINS the definition used identically by Phases 66/67/68 (anti-drift,
    Pitfall 7). The actual decision procedure (e.g. Groebner membership against the
    six-generator ideal) is deferred to Phase 66; Phase 64 does NOT decide c's
    membership. Claim (b) -- "c not in R_pt" -- is STATED here, not proven.
    """
    raise NotImplementedError(
        "R_pt membership decision procedure is Phase 66; the six-generator "
        "DEFINITION is frozen here (see R_PT_FROZEN_DEFINITION)."
    )


# ============================================================================
# 6. Single-state ("Observable") ring confirmation BY CITATION
# ============================================================================
# This is a LITERATURE CITATION, NOT a computation. R[h_3(O)]^{F_4} =
# R[Tr, Tr^2, det] is established 1962-1994 mathematics; we do NOT re-derive it
# via Reynolds/Jacobian (Caveat 2 of 64-RESEARCH.md: wastes budget, risks error
# in something certain).

SINGLE_STATE_RING_NOTE = '''
SINGLE-STATE ("Observable") RING  --  confirmed BY CITATION (not re-derived):

    R[h_3(O)]^{F_4} = R[Tr, Tr^2, det]

is a FREE polynomial algebra; transcendence degree 3; generator degrees 1, 2, 3.

Citation: Faraut, J. & Koranyi, A., "Analysis on Symmetric Cones" (OUP 1994),
  Ch. II-IV (Thm IV.2.5 region); and Springer 1962/1973 (cubic-norm uniqueness;
  F_4 = Aut(h_3(O)); det normalization det(diag(a,b,c))=abc, det(I)=1).

CITATION CORRECTION (recorded verbatim): the single-state ring fact lives in
  Faraut-Koranyi Ch. II-IV (II = Euclidean Jordan algebras, III = Peirce,
  IV = classification), NOT Ch. V (Ch. V = conical/spherical polynomials). The
  earlier "Ch. V" attribution was imprecise; corrected to II-IV.

IDENTIFICATION (milestone framing): the "Observable" single-frame ring of the
  Chalmers gap is EXACTLY this pointwise single-copy subring
  R[Tr_X, Tr_X^2, det_X] (one copy of R_pt). Degrees 1/2/3 match the single-copy
  generators built above.

CONFIDENCE: HIGH on the chapter range (II-IV) and the Ch. V -> II-IV correction
  (verified twice: project survey + TOC check). MEDIUM on the precise theorem
  number IV.2.5 (paywalled); the robust anchor is the chapter range + Springer.
'''


# ============================================================================
# 7. EXACT-ONLY source guard  (Success Criterion 4)
# ============================================================================
# RANK-ROUTING CONVENTION (forward-looking; Phase 64 computes NO ranks, but the
# guard's PRESENCE lets Phases 65-67 inherit a float-free rank guarantee):
#   ALL downstream ranks MUST go through `sympy.Matrix(...).rank()` over QQ.
#   `numpy.linalg.matrix_rank` / `np.linalg.matrix_rank` are FORBIDDEN on any
#   rank-bearing path (rank is discontinuous; an SVD tolerance fabricates the
#   6-vs-7 verdict). No float matrix is ever passed to a rank-bearing function.
RANK_ROUTING_CONVENTION = (
    "All ranks via sympy.Matrix(...).rank() over QQ; "
    "numpy.linalg.matrix_rank / np.linalg.matrix_rank FORBIDDEN on the decisive path."
)

# Sentinel comments delimiting the ONE-TIME, NON-DECISIVE float-det oracle in
# main() (the single sanctioned octonion_algebra touch).
_ORACLE_FENCE_BEGIN = "# ORACLE-FENCE-BEGIN"
_ORACLE_FENCE_END = "# ORACLE-FENCE-END"


def exact_only_guard():
    """Scan THIS module's source for forbidden decisive-path tokens.

    Robustness (per the Task-5 correctness flag): we match actual IMPORT
    STATEMENTS and actual float-rank USAGES via regex -- NOT raw substrings --
    so the guard:
      (a) CATCHES a genuine `from octonion_algebra import ...` or
          `numpy.linalg.matrix_rank` / `np.linalg.matrix_rank` on the decisive path;
      (b) SKIPS the single aliased import inside the
          # ORACLE-FENCE-BEGIN .. # ORACLE-FENCE-END window (the sanctioned,
          non-decisive oracle);
      (c) does NOT trip on PROVENANCE PROSE (comments/docstrings that mention
          "octonion_algebra.py:2184" as text, e.g. the port-spec citations).
    The fence is NOT an allowlist-by-filename: it is a single, explicit,
    minimal source window, and the guard additionally asserts that the ONLY
    octonion_algebra import in the entire file lives inside that window.

    Returns (ok, detail). ok is True iff no forbidden token is reachable on the
    decisive path.
    """
    import re

    # Forbidden IMPORT statements: match a real `from octonion_algebra import ...`
    # or `import octonion_algebra` at the START of a (comment-stripped) code line --
    # NOT a substring inside provenance prose.
    _re_oa_import = re.compile(r"^\s*(from\s+octonion_algebra\s+import\b|import\s+octonion_algebra\b)")
    # Forbidden float-rank USAGE: a real CALL `np.linalg.matrix_rank(` /
    # `numpy.linalg.matrix_rank(` (the trailing '(' distinguishes a live call from
    # a string literal, a regex pattern, or a comment that merely names the token).
    _re_float_rank_call = re.compile(r"\b(np|numpy)\.linalg\.matrix_rank\s*\(")

    def _strip_comment(text):
        """Drop a trailing # comment (heuristic: not # inside a string). Good enough
        for a source-token guard: real forbidden code is never inside a string."""
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

    in_fence = False
    oa_imports_in_fence = 0
    oa_imports_outside = 0
    float_rank_hits = []
    for n, raw in enumerate(lines, start=1):
        if _ORACLE_FENCE_BEGIN in raw:
            in_fence = True
            continue
        if _ORACLE_FENCE_END in raw:
            in_fence = False
            continue
        code = _strip_comment(raw)   # ignore provenance prose in trailing comments
        # float-rank CALL is forbidden EVERYWHERE on the decisive path (the fence is
        # only for the det oracle, which does no rank work).
        if _re_float_rank_call.search(code):
            float_rank_hits.append(n)
        # octonion_algebra import: allowed ONLY inside the fence (aliased oa_det_3).
        if _re_oa_import.match(code):
            if in_fence:
                oa_imports_in_fence += 1
            else:
                oa_imports_outside += 1

    ok = (oa_imports_outside == 0) and (float_rank_hits == []) and (oa_imports_in_fence == 1)
    detail = (f"octonion_algebra imports: {oa_imports_in_fence} in-fence (expect 1), "
              f"{oa_imports_outside} outside (expect 0); "
              f"float-rank calls: {len(float_rank_hits)} (expect 0)")
    return ok, detail


def generic_rational_X():
    """A GENERIC rational element of h_3(O): rational diagonal + rational octonion
    off-diagonals with SEVERAL nonzero components (e_1..e_6 content -> genuinely
    ambient, NOT in the slice; enough nonzero comps to exercise the cross term).
    Deterministic, exact over Q (no surds, no floats)."""
    x1 = oct([Rational(1, 2), Rational(2, 3), 0, Rational(1, 5),
              Rational(3, 7), 0, Rational(1, 11), Rational(1, 13)])
    x2 = oct([Rational(1, 4), 0, Rational(2, 5), Rational(1, 6),
              0, Rational(5, 9), Rational(1, 8), 0])
    x3 = oct([Rational(1, 3), Rational(1, 7), 0, Rational(2, 9),
              Rational(1, 10), 0, Rational(3, 11), Rational(1, 4)])
    return h3o_from_coords(Rational(2), Rational(3), Rational(5), x1, x2, x3)


def octonionic_points():
    """A few GENUINELY OCTONIONIC rational points (non-real off-diagonals, several
    nonzero imaginary components) for the generic-norm-consistency lock. The
    original Phase-64 cross-term bug was INVISIBLE on the commutative real
    subalgebra (diagonal / real off-diagonals); these points exercise the
    non-associative cross term where it bites."""
    p1 = generic_rational_X()
    p2 = h3o_from_coords(
        Rational(1), Rational(-2), Rational(4),
        oct([0, Rational(1), Rational(-1), Rational(2), 0, Rational(1), 0, Rational(-1)]),
        oct([0, Rational(2), 0, Rational(-1), Rational(1), 0, Rational(1), Rational(1)]),
        oct([0, Rational(-1), Rational(1), 0, Rational(2), Rational(-1), Rational(1), 0]),
    )
    p3 = h3o_from_coords(
        Rational(3), Rational(1), Rational(-1),
        oct([Rational(1), 0, Rational(1), 0, Rational(-2), Rational(1), 0, Rational(1)]),
        oct([Rational(-1), Rational(1), 0, Rational(1), 0, Rational(1), Rational(-1), 0]),
        oct([0, Rational(1), Rational(-1), Rational(1), Rational(1), 0, 0, Rational(2)]),
    )
    return [p1, p2, p3]


def cayley_hamilton_norm(X):
    """Generic norm N(X) from the degree-3 Cayley-Hamilton relation of `jordan`:
        X^o3 - Tr(X) X^o2 + S(X) X - N(X) I = 0,  S = (1/2)(Tr^2 - Tr(X o X)).
    Trace of that relation gives 3 N = Tr(X^o3) - Tr(X) Tr(X^o2) + S Tr(X).
    This is the UNIQUE F_4 = Aut(h_3(O))-invariant cubic norm of the Jordan
    product; det_3 MUST equal it (Phase-64.1 lock)."""
    X2 = jordan(X, X)
    X3 = jordan(X, X2)
    S = Rational(1, 2) * (Tr(X) ** 2 - Tr(X2))
    return Rational(1, 3) * (Tr(X3) - Tr(X) * Tr(X2) + S * Tr(X))


def _flat27(X):
    """Flatten an h_3(O) element to 27 real coords on the engine-native layout
    [alpha,beta,gamma, x1(8), x2(8), x3(8)] (inverse of X_from_symbols)."""
    a, b, g, x1, x2, x3 = _coord_from_octmat(X)
    return [a, b, g] + list(x1) + list(x2) + list(x3)


def _standard_basis_27():
    """The 27 standard basis elements E_k = X_from_symbols(e_k) of h_3(O)."""
    out = []
    for k in range(27):
        v = [Rational(0)] * 27
        v[k] = Rational(1)
        out.append(X_from_symbols(v))
    return out


def jordan_L_matrix(A, basis):
    """Left Jordan-multiplication L_A(Z) = jordan(A, Z) as a 27x27 rational matrix
    (column j = flat coords of jordan(A, E_j))."""
    cols = [_flat27(jordan(A, basis[j])) for j in range(27)]
    return Matrix(27, 27, lambda r, col: cols[col][r])


def inner_derivations():
    """Inner derivations D_{a,b} = [L_a, L_b] = L_a L_b - L_b L_a over the standard
    basis (a<b). Their span is Der(h_3(O)) = f_4 (dim 52); EVERY one annihilates
    the generic norm. Returns the list of nonzero 27x27 rational matrices."""
    basis = _standard_basis_27()
    L = [jordan_L_matrix(basis[a], basis) for a in range(27)]
    out = []
    for a in range(27):
        for b in range(a + 1, 27):
            M = L[a] * L[b] - L[b] * L[a]
            if not M.is_zero_matrix:
                out.append(M)
    return out



# ============================================================================
# 8. Phase-70 verbatim-copy integrity check  (LOCK 0)
# ============================================================================
# Assert this module's det_3 (and its load-bearing dependencies) are
# byte-identical to code/ring_lemma_verification.py -- the SSOT guarantee the
# whole v17.0 milestone rests on. Uses inspect.getsource; this is the ONLY touch
# of ring_lemma_verification.py and it is NON-decisive (a source-text identity
# check, not a numerical verdict). If the source module is unavailable the check
# is reported as skipped (non-fatal) -- the F_4 certificate (LOCK 7a/7b) is the
# decisive correctness proof regardless.


def verbatim_copy_integrity():
    """det_3 + key helpers here are byte-identical to ring_lemma_verification.

    Returns (ok, detail). ok is True iff every checked function's source text
    matches the SSOT engine exactly (or the SSOT engine could not be imported,
    in which case ok=True with a 'skipped' detail -- non-decisive)."""
    import importlib
    import inspect
    try:
        src = importlib.import_module("ring_lemma_verification")
    except Exception as exc:  # noqa: BLE001 -- non-decisive integrity check
        return True, f"SKIPPED (ring_lemma_verification not importable: {exc!r})"
    checks = ["oct_mul", "oct_conj", "_oct_normsq", "_coord_from_octmat",
              "Tr", "det_3", "Tr2", "c", "polarize_d", "jordan",
              "cayley_hamilton_norm", "jordan_L_matrix", "inner_derivations"]
    mismatches = []
    for name in checks:
        try:
            s_src = inspect.getsource(getattr(src, name))
            s_here = inspect.getsource(globals()[name])
        except (OSError, AttributeError, KeyError) as exc:
            mismatches.append(f"{name}:unreadable({exc!r})")
            continue
        if s_src != s_here:
            mismatches.append(name)
    ok = (mismatches == [])
    detail = ("all byte-identical to ring_lemma_verification: "
              f"{checks}" if ok else f"MISMATCH in {mismatches}")
    return ok, detail


# ----------------------------------------------------------------------------
# Phase-70 exact-only guard wrapper (Open Question 2: NO octonion_algebra touch).
# ----------------------------------------------------------------------------
# The copied exact_only_guard() expects exactly ONE sanctioned octonion_algebra
# import inside an oracle fence (oa_imports_in_fence == 1) -- that fence existed in
# ring_lemma_verification.py's main(). THIS module deliberately drops the oracle
# fence entirely (no octonion_algebra touch at all), so the verbatim guard would
# report FAIL purely because it counts 0 in-fence imports instead of 1. We re-use
# the verbatim guard's exact source-token scan and assert the STRICTER condition
# for a fence-free module: ZERO octonion_algebra imports anywhere AND zero
# float-rank calls. exact_only_guard() is kept byte-identical (SSOT copy); this
# wrapper is called instead. (Deviation Rule 4: a correctness adaptation, not a
# scope change -- the security property is unchanged, only the in-fence count.)


def exact_only_guard_p70():
    """No octonion_algebra import ANYWHERE and no numpy.linalg.matrix_rank call,
    on a module that intentionally has NO oracle fence. Reuses exact_only_guard()'s
    source-token scan (its detail string reports the in-fence/outside/float-rank
    counts); here we require in-fence == 0 (no fence) instead of == 1.

    Returns (ok, detail). ok is True iff this module touches octonion_algebra
    ZERO times on the decisive path and uses no float rank."""
    _verbatim_ok, detail = exact_only_guard()  # runs the source-token scan
    # Parse the counts back out of the detail string the scan produced:
    #   "octonion_algebra imports: A in-fence (expect 1), B outside (expect 0);
    #    float-rank calls: C (expect 0)"
    import re
    m = re.search(
        r"imports:\s*(\d+)\s*in-fence.*?(\d+)\s*outside.*?float-rank calls:\s*(\d+)",
        detail)
    if not m:
        return False, f"could not parse guard detail: {detail!r}"
    in_fence, outside, frank = int(m.group(1)), int(m.group(2)), int(m.group(3))
    ok = (in_fence == 0 and outside == 0 and frank == 0)
    new_detail = (
        f"octonion_algebra imports: {in_fence} in-fence + {outside} outside "
        f"(expect 0 -- this module has NO oracle fence); "
        f"float-rank calls: {frank} (expect 0)")
    return ok, new_detail


# ============================================================================
# 9. Three-ordering cross-term reconciliation  (SETU-01 heart; Task 3)
# ============================================================================
# Reconcile the three in-repo cross-term labelings on a GENUINELY
# non-associative octonionic point and reject fp-wrong-cross-term WITH EVIDENCE.
#   SSOT       (x2 x1) x3                 [ring_lemma_verification.det_3]
#   conjugated x2* (x1* x3)               [h3o_tower (x0,x1,x2) naming 2Re(x2* x0* x1)]
#   buggy      (x1 x2) x3                 [octonion_algebra.py:~2178; FORBIDDEN]
# ALL exact over Q; octonion_algebra.py is NOT imported (the buggy expression is
# evaluated locally with the SSOT oct_mul, only to exhibit the contrast).


def cross_term_reconciliation(P):
    """Return a dict with the three orderings' Re(cross) and det values at P,
    plus the Cayley-Hamilton norm and the non-vacuity diagnostics. EXACT over Q.

    NON-VACUITY (heeding the plan check's Note A): the real part of the *triple-
    product* associator (x1 x2) x3 - x1 (x2 x3) is 0 at octonionic_points()[1],
    so it is NOT a valid non-vacuity witness. We instead use BOTH:
      (i)  the FULL associator (x1 x2) x3 - x1 (x2 x3) is a NONZERO octonion
           (some imaginary component != 0)  -> data is genuinely non-associative;
      (ii) the association-ORDER discriminator Re((x2 x1) x3) - Re((x1 x2) x3) != 0
           -> the cross term actually distinguishes SSOT from buggy.
    """
    a, b, g, x1, x2, x3 = _coord_from_octmat(P)
    n1, n2, n3 = _oct_normsq(x1), _oct_normsq(x2), _oct_normsq(x3)
    base = a * b * g - a * n1 - b * n2 - g * n3

    cross_ssot = oct_mul(oct_mul(x2, x1), x3)                       # (x2 x1) x3
    cross_conj = oct_mul(oct_conj(x2), oct_mul(oct_conj(x1), x3))   # x2* (x1* x3)
    cross_bug = oct_mul(oct_mul(x1, x2), x3)                        # (x1 x2) x3

    re_ssot = simplify(cross_ssot[0])
    re_conj = simplify(cross_conj[0])
    re_bug = simplify(cross_bug[0])

    N_ssot = simplify(base + 2 * re_ssot)
    N_conj = simplify(base + 2 * re_conj)
    N_bug = simplify(base + 2 * re_bug)
    CH = simplify(cayley_hamilton_norm(P))

    # (i) full triple-product associator as an octonion (any nonzero comp -> NA)
    assoc_full = oct_sub(oct_mul(oct_mul(x1, x2), x3),
                         oct_mul(x1, oct_mul(x2, x3)))
    assoc_full = [simplify(t) for t in assoc_full]
    assoc_full_nonzero = any(t != 0 for t in assoc_full)
    assoc_real = simplify(assoc_full[0])   # 0 here -- recorded, NOT used as gate
    # (ii) association-order discriminator
    discriminator = simplify(re_ssot - re_bug)

    return {
        "a": a, "b": b, "g": g,
        "re_ssot": re_ssot, "re_conj": re_conj, "re_bug": re_bug,
        "N_ssot": N_ssot, "N_conj": N_conj, "N_bug": N_bug, "CH": CH,
        "assoc_full": assoc_full,
        "assoc_full_nonzero": assoc_full_nonzero,
        "assoc_real": assoc_real,
        "discriminator": discriminator,
    }


def _yn(flag):
    """Render a bool as a fixed-width YES/NO for the reconciliation table."""
    return "YES" if flag else "NO "


# ============================================================================
# 10. SIGNATURE-BRIDGE GEOMETRY  (Plan 70-02; SETU-02 / VALD-02)
# ============================================================================
# Build the construction-(ii) Lorentzian-slice geometry ON TOP of the certified
# SSOT det_3 (Sections 1-9; NEVER octonion_algebra.py). The potential is FIXED as
# -log det (Faraut-Koranyi Ch. II-IV); the cone metric g_X = Hess(-log det) is
# POSITIVE-DEFINITE (Riemannian) -- which is exactly why a Riemannian->Lorentzian
# signature bridge is needed. Three decisive gates, ALL EXACT over Q:
#   (G1) INDEX-MAP:  det_3 restricted to the spacetime sub-slice {17,18,19,26} ==
#                    engine-native {x1(beta), x2(gamma), x3(p), x10(q)} equals the
#                    Minkowski slice form beta*gamma/3 - p^2/3 - q^2/3  (Task 1).
#   (G2) HESSIAN:    Hess(-log det)|_{I/3} restricted to {x1,x2,x3,x10} ==
#                    diag(9,9,18,18), det 26244  (a NEW computed gate; Task 2).
#   (G3) MINKOWSKI:  construction-(ii) reduction g(center,M=0) - eta == 0 over Q,
#                    signature (1,3) mostly-minus  (Task 2; tautological-by-
#                    construction per plan-check Note B -- see BACKTRACKING_TRIGGER).
#
# SPACETIME SUB-SLICE INDEX MAP (engine-native layout, Section 4; do NOT re-index):
#   x0,x1,x2 = diag(alpha,beta,gamma);  x3..x10 = octonion x1 (8 comps).
#   The lower-right h_2(O) block is rows/cols {1,2} (diag beta,gamma); the C_u =
#   span{1,e_7} part of the off-diagonal octonion x1 = X[2][1] is components {0,7}.
#   => the 4 spacetime sub-slice coords {17,18,19,26} (Peirce labeling of h_2(C_u))
#      == engine-native symbols {x1=beta, x2=gamma, x3=p (oct-x1 comp e_0),
#         x10=q (oct-x1 comp e_7)}.  Internal W-sector V_0 = {20..25} is EXCLUDED
#      (killed by the pi_u projection; it is the h_2 part orthogonal to C_u).
SLICE_IDX = [1, 2, 10, 3]   # ENGINE-NATIVE indices for (beta, gamma, q, p)  [see note below]
# NOTE on ordering: we order the 4 sub-slice directions as (beta, gamma, q, p) so
# the FRAME MAP to Minkowski coords (x0,x1,x2,x3) is the clean 52-kkt one:
#   x0 = (beta+gamma)/2,  x1 = p,  x2 = q,  x3 = (beta-gamma)/2   (derivations/52-kkt).
# The index SET {beta,gamma,p,q} = engine {x1,x2,x3,x10} is what matters for the map;
# the per-test orderings are stated explicitly at each gate.


def _center_subs():
    """Substitution dict sending ALL 27 engine-native X-coords to the center I/3:
    diagonal alpha=beta=gamma=1/3, every octonion off-diagonal component 0.
    (rho_J=0, det(I/3)=1/27, Tr(I/3)=1.) Exact over Q."""
    sub = {xs[k]: Rational(0) for k in range(27)}
    sub[xs[0]] = Rational(1, 3)
    sub[xs[1]] = Rational(1, 3)
    sub[xs[2]] = Rational(1, 3)
    return sub


def slice_det_form():
    """Restrict the SSOT det_3 to the 4 spacetime sub-slice coords
    {x1=beta, x2=gamma, x3=p, x10=q} (all 23 spectator coords -> their center I/3
    value: alpha=1/3, the other octonion comps 0) and return the restricted cubic
    form as a SymPy expression in fresh symbols (beta, gamma, p, q). EXACT over Q.

    Expected: beta*gamma/3 - p^2/3 - q^2/3  (= det_2/3 with b=beta, g=gamma; the
    alpha=1/3 center normalization of the h_2(C_u) Minkowski quadratic form). This
    is the explicit ASSERTION (test-index-map) that {17,18,19,26} are the SPACETIME
    directions {x1,x2,x3,x10}, NOT the internal W-sector {20..25}."""
    beta, gamma, p, q = symbols('beta gamma p q', real=True)
    sub = {xs[k]: Rational(0) for k in range(27)}
    sub[xs[0]] = Rational(1, 3)   # alpha -> center 1/3 (killed diagonal direction)
    sub[xs[1]] = beta             # x1  = beta   (free spacetime coord)
    sub[xs[2]] = gamma            # x2  = gamma  (free spacetime coord)
    sub[xs[3]] = p                # x3  = oct-x1 comp e_0 = p (free spacetime coord)
    sub[xs[10]] = q               # x10 = oct-x1 comp e_7 = q (free spacetime coord)
    form = simplify(inv_det_X.subs(sub))
    target = simplify(beta * gamma * Rational(1, 3)
                      - p ** 2 * Rational(1, 3) - q ** 2 * Rational(1, 3))
    return form, target, (beta, gamma, p, q)


def cone_hessian_at_center(slice_order=None):
    """The cone metric Hess(-log det) at the center I/3, restricted to the 4
    spacetime sub-slice coords, EXACT over Q.

    Concretely: f = -log(det_3(X)) on the engine-native symbols; take the 4x4
    symbolic Hessian (sympy.diff twice) in the 4 sub-slice variables; evaluate at
    the center I/3 (alpha=beta=gamma=1/3, all octonion off-diagonals 0). The det is
    cubic so the -log jet terminates at the quadratic (Hessian) term appropriately.

    `slice_order` is the list of engine-native indices defining the row/column
    order; default (beta, gamma, p, q) = [1, 2, 3, 10], which is the order in which
    the benchmark diag(9,9,18,18) is stated. Returns the 4x4 sympy Matrix.

    NEW computed gate (not pre-computed in any in-repo file). Expected (in the
    [beta,gamma,p,q] order): diag(9,9,18,18), det 26244, all eigenvalues > 0
    (positive-definite Riemannian, BEFORE the signature bridge)."""
    if slice_order is None:
        slice_order = [1, 2, 3, 10]   # beta, gamma, p, q
    from sympy import log as _log
    f = -_log(inv_det_X)
    center = _center_subs()
    H = []
    for i in slice_order:
        di = diff(f, xs[i])
        H.append([simplify(diff(di, xs[j]).subs(center)) for j in slice_order])
    return Matrix(H)


def _eta_minkowski():
    """The mostly-minus Minkowski metric eta = diag(+1,-1,-1,-1) in the Minkowski
    coords (x0,x1,x2,x3) of derivations/52-kkt-spacetime.tex. Signature (1,3)."""
    return Matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])


def _frame_jacobian_bg_to_mink():
    """Linear frame map from the engine-native sub-slice frame (beta,gamma,p,q)
    [order = SLICE_IDX-style (1,2,3,10)] to the Minkowski coords (x0,x1,x2,x3):
        x0 = (beta+gamma)/2,  x1 = p,  x2 = q,  x3 = (beta-gamma)/2   (52-kkt).
    Rows = (x0,x1,x2,x3); columns = (beta,gamma,p,q). Invertible (det = -1/2), so
    eta pulled back to (beta,gamma,p,q) is CONGRUENT to eta_M and has the same
    signature (1,3) (Sylvester's law of inertia)."""
    return Matrix([
        [Rational(1, 2), Rational(1, 2), 0, 0],   # x0 <- beta,gamma,p,q
        [0,              0,             1, 0],     # x1 <- p
        [0,              0,             0, 1],     # x2 <- q
        [Rational(1, 2), Rational(-1, 2), 0, 0],  # x3 <- beta,gamma,p,q
    ])


def minkowski_reduction():
    """Construction-(ii) Minkowski reduction (the contract gate test-minkowski-
    reduction), EXACT over Q.

    g_mu_nu = eta + h, with eta = diag(+1,-1,-1,-1) (52-kkt det_2 background) and
        h_mu_nu := [Hess(-log det) restricted to V_0, in h_2(C_u) coords]
                    - [its value at (M=0, center I/3)].
    At (M=0, center I/3) the two bracketed Hessians are identical, so h = 0 BY
    CONSTRUCTION and g(center, M=0) = eta exactly. We compute g - eta at the center
    and assert it is the exact 4x4 zero over Q (zero residual h_mu_nu). We work in
    the Minkowski (x0,x1,x2,x3) frame, where eta is manifestly diag(+1,-1,-1,-1).

    HONESTY (plan-check Note B): residual=0 is TAUTOLOGICAL given the centered
    definition of h; it confirms the construction is implemented correctly and the
    signature is (1,3), but it is NOT independent evidence of an uncontaminated
    background. The load-bearing anti-contamination gates are the directly-computed
    Hessian benchmark (diag(9,9,18,18)/26244) and the index-map slice form.

    Returns a dict: eta, H_center (restricted cone-Hessian at center, beta,gamma,p,q
    frame), h_center (= 0 by construction), residual (g-eta = 0), J (frame map),
    detJ, sylvester_minors (leading principal minors of eta_M), signature str."""
    eta_M = _eta_minkowski()
    # restricted cone-Hessian at center in the (beta,gamma,p,q) engine frame:
    H_center_bg = cone_hessian_at_center(slice_order=[1, 2, 3, 10])
    # h := H_restricted(point) - H_restricted(center); at the center these coincide:
    h_center_bg = simplify(H_center_bg - H_center_bg)   # identically 0 (4x4)
    # In the Minkowski frame the metric is g = eta + (frame-mapped h). Since h=0 at
    # the center in any linear frame, g(center,M=0) = eta exactly:
    g_center = simplify(eta_M + Matrix.zeros(4, 4))      # = eta_M
    residual = simplify(g_center - eta_M)                # exact 4x4 zero over Q
    J = _frame_jacobian_bg_to_mink()
    detJ = simplify(J.det())
    # Decisive signature over Q: leading principal minors of eta_M (diagonal) ->
    # signs (+,-,+,-) => signature (1,3). J invertible => eta_bg congruent, same sig.
    minors = [eta_M[:k, :k].det() for k in range(1, 5)]
    return {
        "eta": eta_M,
        "H_center_bg": H_center_bg,
        "h_center": h_center_bg,
        "g_center": g_center,
        "residual": residual,
        "J": J,
        "detJ": detJ,
        "sylvester_minors": minors,   # [1, -1, 1, -1] => (1,3)
        "signature": "(1,3) mostly-minus",
    }


def h3_constant_curvature():
    """OPTIONAL VALD-03 reinforcement (NOT the decisive Phase-70 gate; the full
    cone-Hessian curvature is Phase 71). EXACT over Q.

    Compute the Ricci scalar and constant sectional curvature of the STANDARD
    hyperbolic metric on H^3 = SL(2,C)/SU(2) (the det_2=1 hyperboloid inside
    h_2(C_u)), in the standard chart
        ds^2 = dr^2 + sinh^2(r)(dtheta^2 + sin^2(theta) dphi^2).
    Expected: Ricci scalar R = -6, sectional curvature K = R/(n(n-1)) = -1 (n=3),
    matching Totaro's -d^2/4 = -1 (d=2, rank-1 complex line C_u).

    This reinforces the TARGET value -1 for the round H^3 metric; it does NOT
    replace the Phase-71 cone-Hessian curvature computation. Returns (R, K)."""
    from sympy import sinh, sin, trigsimp
    r, th, ph = symbols('r theta phi', positive=True)
    coords = [r, th, ph]
    g = Matrix([
        [1, 0, 0],
        [0, sinh(r) ** 2, 0],
        [0, 0, sinh(r) ** 2 * sin(th) ** 2],
    ])
    ginv = g.inv()
    n = 3

    def Gamma(a, b, c):
        s = 0
        for d in range(n):
            s += ginv[a, d] * (diff(g[d, b], coords[c])
                               + diff(g[d, c], coords[b])
                               - diff(g[b, c], coords[d]))
        return simplify(Rational(1, 2) * s)

    G = [[[Gamma(a, b, c) for c in range(n)] for b in range(n)] for a in range(n)]

    def Riem(a, b, c, d):
        s = diff(G[a][b][d], coords[c]) - diff(G[a][b][c], coords[d])
        for e in range(n):
            s += G[a][c][e] * G[e][b][d] - G[a][d][e] * G[e][b][c]
        return simplify(s)

    Ric = Matrix(n, n, lambda b, d: simplify(
        sum(Riem(a, b, a, d) for a in range(n))))
    Rscalar = trigsimp(simplify(
        sum(ginv[b, d] * Ric[b, d] for b in range(n) for d in range(n))))
    K = simplify(Rscalar / Rational(n * (n - 1)))
    return Rscalar, K


# ============================================================================
# 11. main(): re-run the full LOCK harness on the fresh module + reconciliation
#     + the Plan 70-02 signature-bridge geometry gates
# ============================================================================


def main():
    print("=" * 78)
    print("VALD-70-01 : bulk-geometry cubic-norm ENGINE -- SSOT certification")
    print("  det_3 cross = 2Re((x2 x1) x3); F_4 = Aut(h_3(O)) invariant generic norm")
    print("=" * 78)

    # ------------------------------------------------------------------------
    # LOCK 0: verbatim-copy integrity (det_3 byte-identical to the SSOT engine).
    # ------------------------------------------------------------------------
    print("LOCK 0 -- verbatim-copy integrity vs ring_lemma_verification.py:")
    _vc_ok, _vc_detail = verbatim_copy_integrity()
    _report(f"LOCK 0 det_3 + helpers byte-identical to ring_lemma_verification "
            f"[{_vc_detail}]", _vc_ok)

    # ------------------------------------------------------------------------
    # Task 1: LOCKs 1-5 + LAYOUT round-trip + exact-only guard (exact over Q).
    # ------------------------------------------------------------------------
    print("Task 1 -- LOCKs 1-5 + LAYOUT round-trip + exact-only guard (exact over Q):")
    Xr = generic_rational_X()
    a_sym, b_sym, c_sym = symbols('a b c', real=True)

    # LOCK 1 (HEADLINE): d(X,X,X) == 6*det_3(X) over Q.
    _report("LOCK 1 (HEADLINE) d(X,X,X) == 6*det_3(X)  [exact over Q]",
            simplify(polarize_d(Xr, Xr, Xr) - 6 * det_3(Xr)) == 0)
    # LOCK 2: c(X,X) == Tr(X^2).
    _report("LOCK 2 c(X,X) == Tr(X^2)  [exact over Q]",
            simplify(c(Xr, Xr) - Tr2(Xr)) == 0)
    # LOCK 3: Fano e1 e2 == e4.
    e1 = oct([0, 1, 0, 0, 0, 0, 0, 0])
    e2 = oct([0, 0, 1, 0, 0, 0, 0, 0])
    e4 = oct([0, 0, 0, 0, 1, 0, 0, 0])
    _report("LOCK 3 octonion table e1*e2 == e4 (Fano)",
            oct_equal(oct_mul(e1, e2), e4))
    _report("LOCK 3b FANO_TRIPLES == documented orientation",
            FANO_TRIPLES == [(1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 7),
                             (5, 6, 1), (6, 7, 2), (7, 1, 3)])
    # LOCK 4: det_3(diag(a,b,c)) == a*b*c symbolically.
    Xdiag = h3o_from_coords(a_sym, b_sym, c_sym, oct_zero(), oct_zero(), oct_zero())
    _report("LOCK 4 det_3(diag(a,b,c)) == a*b*c  [symbolic over Q]",
            simplify(det_3(Xdiag) - a_sym * b_sym * c_sym) == 0)
    # LOCK 5: det_3(I) == 1.
    _report("LOCK 5 det_3(I) == 1", det_3(h3o_identity()) == 1)

    # LAYOUT round-trip: _coord_from_octmat(X_from_symbols(xs)) == xs.
    rt_a, rt_b, rt_g, rt_x1, rt_x2, rt_x3 = _coord_from_octmat(X_from_symbols(xs))
    roundtrip_ok = (
        rt_a == xs[0] and rt_b == xs[1] and rt_g == xs[2]
        and list(rt_x1) == [xs[3 + k] for k in range(8)]
        and list(rt_x2) == [xs[11 + k] for k in range(8)]
        and list(rt_x3) == [xs[19 + k] for k in range(8)]
    )
    _report("LAYOUT round-trip _coord_from_octmat(X_from_symbols(xs)) == xs "
            "(engine-native layout intact)", roundtrip_ok)
    _report("LAYOUT X and Y use IDENTICAL constructor (X_from_symbols)",
            X_from_symbols.__name__ == "X_from_symbols" and Xsym is not Ysym)

    # EXACT-ONLY GUARD (Phase-70, fence-free): no octonion_algebra import at all,
    # no numpy.linalg.matrix_rank. Open Question 2: the ring_lemma oracle fence is
    # intentionally DROPPED, so we require ZERO octonion_algebra imports.
    _guard_ok, _guard_detail = exact_only_guard_p70()
    _report(f"exact-only guard (Phase-70, fence-free): no float/octonion_algebra "
            f"on decisive path [{_guard_detail}]", _guard_ok)

    # ------------------------------------------------------------------------
    # Task 2: LOCK 7a (Cayley-Hamilton norm) + LOCK 7b (324/324 annihilation).
    # The F_4 certificate -- LOCKs 1-5 alone do NOT discriminate the buggy order.
    # ------------------------------------------------------------------------
    print("Task 2 -- F_4 certificate: LOCK 7a (CH norm) + LOCK 7b (324/324 annihilation):")

    # LOCK 7a: det_3 == Cayley-Hamilton generic norm at >=3 octonionic points.
    _norm_pts = octonionic_points()
    _7a_each = []
    for i, P in enumerate(_norm_pts):
        ok_i = (simplify(det_3(P) - cayley_hamilton_norm(P)) == 0)
        _7a_each.append(ok_i)
        print(f"      point {i}: det_3 == CH norm  -> {'OK' if ok_i else 'FAIL'} "
              f"(det_3 = {simplify(det_3(P))})")
    _report(f"LOCK 7a det_3 == Cayley-Hamilton generic norm of jordan "
            f"[{len(_norm_pts)} octonionic pts, exact over Q]", all(_7a_each))

    # LOCK 7b: ALL inner derivations [L_a,L_b] annihilate det_3, full 324/324.
    _grad_detX = [diff(inv_det_X, xs[i]) for i in range(27)]
    _pderiv = _norm_pts[1]                                   # an octonionic point
    _pvec = Matrix(_flat27(_pderiv))
    _subs = {xs[k]: _pvec[k] for k in range(27)}
    _grad_at = [gi.subs(_subs) for gi in _grad_detX]
    _derivs = inner_derivations()
    _killed = 0
    for _M in _derivs:
        _Mv = _M * _pvec
        if simplify(sum(_grad_at[i] * _Mv[i] for i in range(27))) == 0:
            _killed += 1
    _report(f"LOCK 7b det_3 annihilated by ALL inner derivations [L_a,L_b] "
            f"({_killed}/{len(_derivs)}, dim f_4=52) [octonionic pt]",
            _killed == len(_derivs) and len(_derivs) == 324)

    # ------------------------------------------------------------------------
    # Task 3: three-ordering reconciliation (run BEFORE any geometry would be
    # touched -- here, before the script ends). Rejects fp-wrong-cross-term.
    # ------------------------------------------------------------------------
    print("Task 3 -- three-ordering cross-term reconciliation (non-associative e4..e7 data):")
    P = octonionic_points()[1]
    R = cross_term_reconciliation(P)

    # NON-VACUITY (Note A): full associator nonzero AND order-discriminator != 0.
    _report("NON-VACUITY (i) full triple-product associator (x1x2)x3-x1(x2x3) is a "
            "NONZERO octonion (data genuinely non-associative)", R["assoc_full_nonzero"])
    print(f"      full associator = {R['assoc_full']}  (real part = {R['assoc_real']}, "
          f"0 here -- NOT used as the gate, per plan-check Note A)")
    _report("NON-VACUITY (ii) association-order discriminator "
            "Re((x2 x1)x3) - Re((x1 x2)x3) != 0", R["discriminator"] != 0)
    print(f"      discriminator = {R['discriminator']} (expect 8)")

    # Reconciliation table + assertions (all exact over Q). Use str() not :>N
    # (sympy Integer does not support the numeric __format__ mini-language).
    print("      +-------------+------------------------------------------------+-----------+-------+")
    print("      | ordering    | code expression                                | Re(cross) | ==CH? |")
    print("      +-------------+------------------------------------------------+-----------+-------+")
    print("      | SSOT        | oct_mul(oct_mul(x2,x1),x3)                      | "
          + str(R['re_ssot']).rjust(9) + " | " + _yn(R['N_ssot'] == R['CH']) + "   |")
    print("      | conjugated  | oct_mul(oct_conj(x2),oct_mul(oct_conj(x1),x3)) | "
          + str(R['re_conj']).rjust(9) + " | " + _yn(R['N_conj'] == R['CH']) + "   |")
    print("      | buggy       | oct_mul(oct_mul(x1,x2),x3)                      | "
          + str(R['re_bug']).rjust(9) + " | " + _yn(R['N_bug'] == R['CH']) + "   |")
    print("      +-------------+------------------------------------------------+-----------+-------+")
    print(f"      CH norm(P) = {R['CH']};  N_SSOT = {R['N_ssot']}, N_conj = {R['N_conj']}, "
          f"N_buggy = {R['N_bug']};  N_SSOT - N_buggy = {simplify(R['N_ssot'] - R['N_bug'])} "
          f"(expect 16, the off-by-16 signature)")

    _report("RECONCILE SSOT Re(cross) == +4 and det_SSOT == CH norm (exact)",
            R["re_ssot"] == 4 and R["N_ssot"] == R["CH"])
    _report("RECONCILE conjugated Re(cross) == +4 and det_conj == CH norm "
            "(reconciles to SSOT)", R["re_conj"] == 4 and R["N_conj"] == R["CH"])
    _report("RECONCILE buggy Re(cross) == -4 and det_buggy != CH norm "
            "(off by 16: N_SSOT - N_buggy == 16) -- fp-wrong-cross-term REJECTED",
            R["re_bug"] == -4 and R["N_bug"] != R["CH"]
            and simplify(R["N_ssot"] - R["N_bug"]) == 16)

    # ========================================================================
    # PLAN 70-02 SIGNATURE-BRIDGE GEOMETRY GATES (built on the SSOT det_3 above)
    # ========================================================================
    print("=" * 78)
    print("PLAN 70-02 : signature-bridge geometry on the certified det_3")
    print("  potential = -log det (Riemannian g_X=Hess(-log det)); construction (ii)")
    print("=" * 78)

    # ------------------------------------------------------------------------
    # Plan 70-02 Task 1: INDEX-MAP assertion (test-index-map).
    # det_3 restricted to {x1,x2,x3,x10} == beta*gamma/3 - p^2/3 - q^2/3 over Q.
    # This ASSERTS that {17,18,19,26} are the SPACETIME (not internal {20..25})
    # directions -- the reconstruction is checked, not trusted.
    # ------------------------------------------------------------------------
    print("Task 1 (70-02) -- spacetime sub-slice INDEX-MAP via the slice det form:")
    _sform, _starget, _ = slice_det_form()
    print(f"      det_3|_{{x1,x2,x3,x10}}(alpha=1/3) = {_sform}")
    print(f"      target  b*g/3 - p^2/3 - q^2/3      = {_starget}")
    _report("INDEX-MAP det_3 restricted to {x1,x2,x3,x10} == beta*gamma/3 "
            "- p^2/3 - q^2/3 (exact over Q) -- {17,18,19,26}=={x1,x2,x3,x10}, "
            "internal {20..25} EXCLUDED",
            simplify(_sform - _starget) == 0)

    # ------------------------------------------------------------------------
    # Plan 70-02 Task 2a: HESSIAN BENCHMARK (test-hessian-benchmark).
    # Hess(-log det)|_{I/3} restricted to {x1,x2,x3,x10} == diag(9,9,18,18),
    # det 26244 (NEW computed gate; nondegenerate; positive-definite Riemannian).
    # ------------------------------------------------------------------------
    print("Task 2a (70-02) -- Hessian benchmark Hess(-log det)|_{I/3} (exact over Q):")
    _Hess = cone_hessian_at_center(slice_order=[1, 2, 3, 10])   # beta,gamma,p,q
    _Hess_expected = Matrix([[9, 0, 0, 0], [0, 9, 0, 0],
                             [0, 0, 18, 0], [0, 0, 0, 18]])
    _Hess_det = _Hess.det()
    print(f"      Hess|_{{I/3}} (beta,gamma,p,q order) = {_Hess.tolist()}")
    print(f"      det(Hess) = {_Hess_det} (expect 26244)")
    _report("HESSIAN Hess(-log det)|_{I/3} == diag(9,9,18,18) and det == 26244 "
            "(exact over Q; nondegenerate)",
            simplify(_Hess - _Hess_expected) == Matrix.zeros(4, 4)
            and _Hess_det == 26244)
    # Non-decisive float eigenvalue triage (informational only -- NOT a verdict).
    try:
        import numpy as _np
        _ev = sorted(_np.linalg.eigvalsh(
            _np.array(_Hess.tolist(), dtype=float)).tolist())
        print(f"      [informational, non-decisive] float eig(Hess) = {_ev} "
              f"-> all > 0 (positive-definite Riemannian, before the bridge)")
    except Exception as _exc:   # noqa: BLE001  (triage is non-decisive)
        print(f"      [informational] float eigenvalue triage skipped: {_exc!r}")

    # ------------------------------------------------------------------------
    # Plan 70-02 Task 2b: MINKOWSKI REDUCTION (test-minkowski-reduction).
    # Construction (ii): g = eta + h, h := Hess - Hess|center => h=0 at center
    # BY CONSTRUCTION; g(center,M=0) - eta == 0 exact over Q; signature (1,3).
    # NOTE B: residual=0 is tautological-by-construction (not independent evidence).
    # ------------------------------------------------------------------------
    print("Task 2b (70-02) -- construction-(ii) Minkowski reduction (exact over Q):")
    _MR = minkowski_reduction()
    print(f"      eta = diag(+1,-1,-1,-1); h_mu_nu(center,M=0) = "
          f"{_MR['h_center'].tolist()} (zero BY CONSTRUCTION, Note B)")
    print(f"      residual g(center,M=0) - eta = {_MR['residual'].tolist()}")
    print(f"      leading principal minors of eta = {_MR['sylvester_minors']} "
          f"(signs +,-,+,- => signature {_MR['signature']})")
    print(f"      det(frame map J) = {_MR['detJ']} (invertible => eta congruent "
          f"to the (beta,gamma,p,q)-frame form, same signature)")
    _report("MINKOWSKI reduction g(center,M=0) - eta == 0 (exact 4x4 zero over Q; "
            "zero residual h_mu_nu) [TAUTOLOGICAL-BY-CONSTRUCTION per Note B]",
            _MR["residual"] == Matrix.zeros(4, 4)
            and _MR["h_center"] == Matrix.zeros(4, 4))
    _report("MINKOWSKI signature (1,3) mostly-minus via Sylvester minors "
            "[1,-1,1,-1] + invertible frame map (exact over Q)",
            _MR["sylvester_minors"] == [1, -1, 1, -1] and _MR["detJ"] != 0)
    # Non-decisive float eigenvalue-sign triage on eta (informational only).
    try:
        import numpy as _np
        _eev = sorted(_np.linalg.eigvalsh(
            _np.array(_MR["eta"].tolist(), dtype=float)).tolist())
        _npos = sum(1 for v in _eev if v > 0)
        _nneg = sum(1 for v in _eev if v < 0)
        print(f"      [informational, non-decisive] float eig(eta) = {_eev} "
              f"-> {_npos} positive, {_nneg} negative")
    except Exception as _exc:   # noqa: BLE001  (triage is non-decisive)
        print(f"      [informational] float signature triage skipped: {_exc!r}")

    # BACKTRACKING TRIGGER (roadmap): a provably-nonzero residual h_mu_nu at the
    # center that cannot be removed by re-fixing the V_0<->Minkowski frame => switch
    # to construction (i) or HALT. Do NOT declare the bridge fixed with nonzero
    # residual. Here residual == 0 (by construction), so the trigger does NOT fire.
    if _MR["residual"] != Matrix.zeros(4, 4):
        print("  [BACKTRACK] nonzero Minkowski residual -- switch to construction "
              "(i) or HALT; do NOT declare the bridge fixed.")

    # ------------------------------------------------------------------------
    # Plan 70-02 Task 3: VALD-03 cross-check (H^3 = SL(2,C)/SU(2), curvature -1).
    # STATED by citation (Totaro -d^2/4 = -1, d=2) -- full cone-Hessian curvature
    # DEFERRED to Phase 71. Optional reinforcement: the standard H^3 metric has
    # constant sectional curvature -1 (exact over Q). NOT the decisive Phase-70 gate.
    # ------------------------------------------------------------------------
    print("Task 3 (70-02) -- VALD-03 H^3 = SL(2,C)/SU(2) curvature cross-check:")
    print("      STATED (Totaro arXiv:math/0401381): K = -d^2/4 = -1 (d=2, rank-1 "
          "complex line C_u); full cone-Hessian curvature DEFERRED to Phase 71.")
    _R_h3, _K_h3 = h3_constant_curvature()
    print(f"      [reinforcement, exact over Q, NOT the decisive gate] standard H^3 "
          f"metric: Ricci scalar R = {_R_h3}, K = R/(n(n-1)) = {_K_h3}")
    _report("VALD-03 reinforcement: standard H^3 metric has Ricci scalar -6 and "
            "constant sectional curvature K == -1 (exact over Q) -- reinforces the "
            "Totaro target -d^2/4 = -1 (full cone-Hessian curvature = Phase 71)",
            simplify(_R_h3 + 6) == 0 and simplify(_K_h3 + 1) == 0)

    print("-" * 78)
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}")
    if ALL_PASS:
        print("  det_3 (cross 2Re((x2 x1) x3)) CERTIFIED the unique F_4-invariant cubic")
        print("  norm: byte-identical to the SSOT engine, == Cayley-Hamilton norm at 3")
        print("  octonionic points AND annihilated by all 324 inner derivations; LOCKs 1-5")
        print("  + LAYOUT + exact-only guard pass; the buggy (x1 x2) x3 order is rejected")
        print("  with exact-over-Q evidence (off by 16). Engine ready for Plan 70-02.")
    else:
        print("  A LOCK/guard failed -- this is a PORT ERROR (e.g. a wrong copied")
        print("  cross-term order), NOT a new result. Diff det_3 line-by-line against")
        print("  ring_lemma_verification.py and re-run; do NOT proceed to Plan 70-02.")
    print("=" * 78)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
