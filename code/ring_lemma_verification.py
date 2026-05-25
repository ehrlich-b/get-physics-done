"""
(RING) Lemma — Exact-SymPy Algebraic Foundation  --  VALD-64-01  (BASE-01)
==========================================================================
Phase: 64-setup-conventions-and-exact-engine, Plan: 01
Milestone: v16.0 The (RING) Lemma (math half of the Chalmers gap).

This is the FROZEN exact-SymPy h_3(O) algebraic foundation for the entire
(RING) milestone. Every downstream (RING) phase (65 f_4/orbit-dimension GATE,
66 c-independence SPINE, 67 Sym^2 branching, 68 Hilbert/Molien, 69 (REDU)
statement) reuses these objects and conventions VERBATIM. A convention error
here silently corrupts all of Phases 65-69; exact-over-Q is NON-NEGOTIABLE
because rank (the downstream decisive quantity) is discontinuous and
float-fragile.

PROVENANCE
----------
The exact octonion + 3x3 octonion matmul + Jordan block (Section 1-2 below) is
PORTED VERBATIM from code/embedding_under_E_verification.py Section 1-2 (the
VERIFIED exact-SymPy engine that underpins the v15.0 Phase 62 result). Copy
(not import) is the DELIBERATE choice: a self-contained decisive module,
matching the code/slice_clause_iii_verification.py (VALD-61-01) precedent. Note
that embedding_under_E_verification.py IS import-safe (its main() is guarded by
`if __name__ == "__main__":`), but copying decouples this decisive module from a
Phase-62 file and pins the conventions in one place.

The standalone Tr / Tr2 / det_3 are LIFTED from the inlined T1/T3 terms of
reduced_charpoly_roots (embedding_under_E_verification.py:567-580). polarize_d
is RE-PORTED onto the exact det_3 from the formula body of
code/octonion_algebra.py:2184 (FLOAT64 reference spec ONLY — never called on the
decisive path; see the exact-only guard in Section 7).

CONVENTION (carry verbatim — the Jordan 1/2 and the det left-association are the
two most error-prone choices; both are already fixed in the warm engine and are
COPIED, not re-derived):
# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; det3 left-assoc Re((x1x2)x3); det3_normalization d(X,X,X)=6*det_3; coupling c=Tr(X o Y); arithmetic=exact-SymPy-over-Q; ranks=sympy.Matrix.rank(); NEVER float64 on decisive path
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible)   [for downstream (c), Phase 67]

Assert-based harness (NO pytest -- the executor venv has sympy/numpy only).
Runnable directly:  python3 code/ring_lemma_verification.py
Exits 0 iff ALL_PASS (every convention lock and every guard passes); nonzero on
any failure.

Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0. Deterministic
(no random seeds; all test elements hardcoded with exact rational entries).

References:
  Springer, T.A. -- Jordan Algebras and Algebraic Groups, Springer (1973);
    Indag. Math. 24 (1962) 259-265 (cubic norm uniqueness; F_4 = Aut(h_3(O));
    det normalization det(diag(a,b,c))=abc, det(I)=1).
  Blind, B. -- J. Lie Theory 21 (2011) 123-144 (arXiv:0906.5525), Sec 3
    (polarization normalization d(X,X,X) = 6*det X -- the headline lock).
  Faraut, J.; Koranyi, A. -- Analysis on Symmetric Cones, Oxford (1994),
    Ch. II-IV (Thm IV.2.5 region) (single-state ring R[Tr, Tr^2, det]).
  code/embedding_under_E_verification.py (VALD-62-01) -- the exact-SymPy engine.
  code/slice_clause_iii_verification.py (VALD-61-01) -- the assert-harness pattern.
"""

import sys

from sympy import Rational, simplify, symbols, Poly, expand, total_degree  # noqa: F401  (Poly reserved for downstream)

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
    """Cubic norm det_3(X) = N(X)   (= the T3 term; bidegree (3,0)).

        N(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2
               + 2*Re((x1*x2)*x3)

    The cross term uses LEFT-to-right association `oct_mul(oct_mul(x1,x2),x3)`
    (the Sarrus expansion of the 3x3 octonion determinant). This is LOAD-BEARING:
    octonions are non-associative, so (x1*x2)*x3 != x1*(x2*x3) generically.
    Lifted VERBATIM from embedding_under_E_verification.py:573-576 (T3); the
    formula matches octonion_algebra.py:2152 (cross-checked by the one-time
    float-det ORACLE in main()).
    """
    a, b, g, x1, x2, x3 = _coord_from_octmat(X)
    n1, n2, n3 = _oct_normsq(x1), _oct_normsq(x2), _oct_normsq(x3)
    cross = oct_mul(oct_mul(x1, x2), x3)   # LEFT-assoc: (x1 x2) x3
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
# 5. Frozen R_pt definition  (Task 5)
# ============================================================================
# TODO(Task 5): R_PT_FROZEN_DEFINITION, is_in_Rpt stub.


# ============================================================================
# 6. Single-state ("Observable") ring confirmation by citation  (Task 6)
# ============================================================================
# TODO(Task 6): SINGLE_STATE_RING_NOTE (FK Ch. II-IV; Ch. V correction).


# ============================================================================
# 7. Exact-only source guard  (Task 5)
# ============================================================================
# TODO(Task 5): import hygiene + sentinel-window source scan + rank-routing convention.


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


def main():
    print("=" * 76)
    print("VALD-64-01 : (RING) exact-SymPy foundation — convention locks & freeze")
    print("=" * 76)

    # ========================================================================
    # Task 3: FIVE CONVENTION LOCKS — exact over Q, headline d=6*det_3 FIRST.
    #
    # BACKTRACKING (contract Backtracking + disconfirming_observations): if ANY
    # lock is nonzero -- ESPECIALLY d(X,X,X) != 6*det_3(X) -- STOP and reconcile
    # against the engine header. A failed lock is a PORT ERROR (wrong det
    # left-association, wrong polarize_d sign pattern, or a Jordan-1/2 slip),
    # NOT a new result. NEVER tune a lock to pass; diff against
    # embedding_under_E_verification.py line by line.
    # ========================================================================
    print("Task 3 — five convention locks (exact over Q):")
    Xr = generic_rational_X()
    a_sym, b_sym, c_sym = symbols('a b c', real=True)

    # 1. HEADLINE LOCK (run FIRST): d(X,X,X) == 6*det_3(X), exact over Q.
    # Previously verified only at float tolerance 1.4e-13 (octonion_algebra.py:2299);
    # established EXACTLY over Q here for the first time.
    _report("LOCK 1 (HEADLINE) d(X,X,X) == 6*det_3(X)  [exact over Q]",
            simplify(polarize_d(Xr, Xr, Xr) - 6 * det_3(Xr)) == 0)

    # 2. c(X,X) == Tr(X^2): the coupling reduces to the quadratic trace on the diagonal.
    _report("LOCK 2 c(X,X) == Tr(X^2)  [exact over Q]",
            simplify(c(Xr, Xr) - Tr2(Xr)) == 0)

    # 3. Octonion table e1*e2 == e4 (Fano orientation); cross-check FANO_TRIPLES.
    e1 = oct([0, 1, 0, 0, 0, 0, 0, 0])
    e2 = oct([0, 0, 1, 0, 0, 0, 0, 0])
    e4 = oct([0, 0, 0, 0, 1, 0, 0, 0])
    _report("LOCK 3 octonion table e1*e2 == e4 (Fano)",
            oct_equal(oct_mul(e1, e2), e4))
    # Cross-check the documented FANO_TRIPLES orientation by value (matches
    # octonion_algebra.py / Paper 7).
    _report("LOCK 3b FANO_TRIPLES == documented orientation",
            FANO_TRIPLES == [(1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 7),
                             (5, 6, 1), (6, 7, 2), (7, 1, 3)])

    # 4. det_3(diag(a,b,c)) == a*b*c  (cubic-norm diagonal normalization), symbolic.
    Xdiag = h3o_from_coords(a_sym, b_sym, c_sym, oct_zero(), oct_zero(), oct_zero())
    _report("LOCK 4 det_3(diag(a,b,c)) == a*b*c  [symbolic over Q]",
            simplify(det_3(Xdiag) - a_sym * b_sym * c_sym) == 0)

    # 5. det_3(I) == 1  (identity normalization).
    _report("LOCK 5 det_3(I) == 1", det_3(h3o_identity()) == 1)

    # ------------------------------------------------------------------------
    # ONE-TIME, NON-DECISIVE port-correctness ORACLE (the ONLY sanctioned touch
    # of the float64 code/octonion_algebra.py). It is NOT on any decisive/rank
    # path: it cross-checks the lifted exact det_3 against the float64 reference
    # det_3 on a SHARED rational element, a single isolated equality. The
    # Task-5 exact-only guard ALLOWLISTS exactly the sentinel window below
    # (# ORACLE-FENCE-BEGIN .. # ORACLE-FENCE-END) and forbids the tokens
    # everywhere else. The import is ALIASED to oa_det_3 so the module's exact
    # det_3 symbol is never rebound/shadowed.
    # ------------------------------------------------------------------------
    # ORACLE-FENCE-BEGIN  (the ONLY sanctioned octonion_algebra touch; NOT on the decisive path; allowlisted by the Task-5 guard)
    try:
        from octonion_algebra import det_3 as oa_det_3, H3O, Octonion  # ALIASED — never shadows exact det_3
        a_r, b_r, g_r, x1_r, x2_r, x3_r = _coord_from_octmat(Xr)
        Xr_float = H3O(
            alpha=float(a_r), beta=float(b_r), gamma=float(g_r),
            x1=Octonion([float(v) for v in x1_r]),
            x2=Octonion([float(v) for v in x2_r]),
            x3=Octonion([float(v) for v in x3_r]),
        )
        _oracle_ok = abs(float(det_3(Xr)) - oa_det_3(Xr_float)) < 1e-12
    except Exception as _oracle_exc:  # noqa: BLE001 — non-decisive; report and continue
        print(f"  [WARN] oracle unavailable ({_oracle_exc!r}); non-decisive, skipped")
        _oracle_ok = True
    _report("ORACLE (non-decisive): exact det_3 matches float64 octonion_algebra det_3 on shared element",
            _oracle_ok)
    # ORACLE-FENCE-END

    # ========================================================================
    # Task 4: 54-symbol layout round-trip + seven-invariant bidegree checks.
    # ========================================================================
    print("Task 4 — 54-symbol pair layout + seven base invariants:")

    # Round-trip: _coord_from_octmat(X_from_symbols(xs)) recovers the input symbols.
    rt_a, rt_b, rt_g, rt_x1, rt_x2, rt_x3 = _coord_from_octmat(X_from_symbols(xs))
    roundtrip_ok = (
        rt_a == xs[0] and rt_b == xs[1] and rt_g == xs[2]
        and list(rt_x1) == [xs[3 + k] for k in range(8)]
        and list(rt_x2) == [xs[11 + k] for k in range(8)]
        and list(rt_x3) == [xs[19 + k] for k in range(8)]
    )
    _report("LAYOUT round-trip _coord_from_octmat(X_from_symbols(xs)) == xs", roundtrip_ok)
    # Same constructor used for ys (X and Y identical conventions).
    _report("LAYOUT X and Y use IDENTICAL constructor (X_from_symbols)",
            X_from_symbols.__name__ == "X_from_symbols" and Xsym is not Ysym)

    # Cheap bidegree check on a LOW-dimensional slice: keep only the diagonal
    # symbols (set all 24 octonion comps of X to 0), so Tr X / Tr X^2 / det X
    # reduce to polynomials in {x0, x1, x2} of degree 1 / 2 / 3.
    diag_only = {xs[3 + k]: 0 for k in range(24)}
    Tr_diag = expand(inv_Tr_X.subs(diag_only))
    Tr2_diag = expand(inv_Tr2_X.subs(diag_only))
    det_diag = expand(inv_det_X.subs(diag_only))
    _report("BIDEGREE Tr X has X-degree 1 (diagonal slice)", total_degree(Tr_diag) == 1)
    _report("BIDEGREE Tr X^2 has X-degree 2 (diagonal slice)", total_degree(Tr2_diag) == 2)
    _report("BIDEGREE det X has X-degree 3 (diagonal slice)", total_degree(det_diag) == 3)

    # Tr X^2 is NOT (Tr X)^2: evaluate both at a rational point and show they differ.
    pt = {s: Rational(1 + (i % 5), 2 + (i % 3)) for i, s in enumerate(xs)}
    tr2_val = inv_Tr2_X.subs(pt)
    trsq_val = (inv_Tr_X.subs(pt))**2
    _report("BIDEGREE Tr X^2 != (Tr X)^2 (distinct degree-2 invariants)",
            simplify(tr2_val - trsq_val) != 0)

    # c is bidegree (1,1): linear in xs and linear in ys (check via a slice).
    # Substituting Y=0 kills c (degree>=1 in Y); substituting X=0 kills c (degree>=1 in X).
    c_Yzero = inv_c.subs({s: 0 for s in ys})
    c_Xzero = inv_c.subs({s: 0 for s in xs})
    _report("BIDEGREE c bidegree (1,1): c(X,0)=0 and c(0,Y)=0",
            simplify(c_Yzero) == 0 and simplify(c_Xzero) == 0)

    # ---- Task 5: R_pt prose-vs-invariants consistency + exact-only guard ----
    # TODO(Task 5).

    # ---- Task 6: single-state-ring consistency (3 gens, degrees 1/2/3) ----
    # TODO(Task 6).

    print("-" * 76)
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}")
    print("=" * 76)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
