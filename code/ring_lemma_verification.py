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

from sympy import Rational, simplify, symbols, Poly  # noqa: F401  (Poly reserved for downstream)

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
# 4. 54-symbol pair coordinatization + seven base invariants  (Task 4)
# ============================================================================
# TODO(Task 4): xs/ys symbols, X_from_symbols, the seven base invariants.


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


def main():
    print("=" * 76)
    print("VALD-64-01 : (RING) exact-SymPy foundation — convention locks & freeze")
    print("=" * 76)

    # ---- Task 3: five convention locks (headline first) + one-time oracle ----
    # TODO(Task 3): five locks (d=6det first), then the fenced float-det oracle.

    # ---- Task 4: 54-symbol layout round-trip + bidegree checks ----
    # TODO(Task 4).

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
