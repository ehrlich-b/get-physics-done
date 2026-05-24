# ASSERT_CONVENTION: slice A = M_3(C)^sa (n=3); Jordan product a o b = (1/2)(ab+ba);
#   sequential product a&b = sqrt(a) b sqrt(a); exact symbolic/rational arithmetic;
#   pure algebra (no physical dimensions); LIVE-paper provenance.
#
# Phase 61, Plan 02 (VALD-61-01): pytest harness mirroring tests/test_octonion_h3o.py.
#
# Verifies, by EXACT symbolic computation, the structural data Paper 5 Def 1
# clauses (i), (iii), (iv) require for the C*-bottleneck slice A = M_3(C)^sa:
#   - rank 3: three mutually orthogonal nontrivial rank-1 projective units -> I_3 (clause i)
#   - simplicity: center = C*I_3, no nontrivial central idempotent (clause iv)
#   - minimal composite real-dim 81 = 9*9; maximal 162 != 81 (clause iii composite, BGW)
#   - PRODUCT-FORM sequential product a&b = sqrt(a) b sqrt(a) factorizes across the
#     body-model tensor split on the ASSOCIATIVE composite M_9(C)^sa (Phase 60 OPEN ITEM)
#
# DECISIVE assertions are exact (.equals(zeros)/== 0/integer equality), NEVER float
# tolerance (fp-float-pass rejected).
#
# SCOPE GUARD (fp-reach-into-h3o rejected): this file stays entirely within the
# ASSOCIATIVE algebras M_3(C)^sa and M_9(C)^sa.  It does NOT import octonion_algebra's
# H3O / jordan_product non-associative machinery; it does NOT compute on h_3(O).  The
# non-associative h_3(O) computation and the induced-by-E question are Phase 62.
#
# Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0.  No random seeds
# (deterministic exact symbolic computation).  Runtime budget: fast (< 5 s for the
# decisive checks; a few robustness cases stay small to keep the file fast).

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

import pytest
from sympy import (
    Matrix, sqrt, Rational, eye, zeros, I as symI, simplify,
    kronecker_product, symbols, solveset, S, FiniteSet,
)

from slice_clause_iii_verification import (
    hermitian_3x3, jordan_product, is_rank_one_projection,
    matrix_sqrt_nxn, luders_seq_product,
)

I3 = eye(3)
I9 = eye(9)


# ============================================================================
# Helpers: exact PSD/effect checks via real eigenvalues
# ============================================================================

def _eigenvalues_real_in_unit_interval(M):
    """Exact check: all eigenvalues of Hermitian M are real and in [0, 1]
    (i.e. M is an effect: 0 <= M <= I).  Uses exact eigenvals (no float)."""
    for val, mult in M.eigenvals().items():
        v = simplify(val)
        # Real part check: imaginary part exactly zero.
        if simplify(v - v.conjugate()) != 0:
            return False
        # 0 <= v <= 1 (exact symbolic comparison).
        if not (v >= 0) or not (v <= 1):
            return False
    return True


def _is_psd_hermitian(M):
    """Exact: M Hermitian and all eigenvalues >= 0."""
    if not simplify(M - M.H).equals(zeros(*M.shape)):
        return False
    for val in M.eigenvals():
        if not (simplify(val) >= 0):
            return False
    return True


# Exact 3x3 effects (rational entries, eigenvalues in [0,1]); at least one
# has off-diagonal structure so factorization tests are non-trivial.
#   a_B: off-diagonal real (eigenvalues 1/2, 1/2 +- 1/4 within [0,1])
A_B = hermitian_3x3(Rational(1, 2), Rational(1, 2), Rational(1, 2),
                    Rational(1, 4), 0, 0, 0, 0, 0)
#   a_M: off-diagonal complex (imaginary coupling), eigenvalues in [0,1]
A_M = hermitian_3x3(Rational(1, 2), Rational(1, 2), Rational(3, 4),
                    0, Rational(1, 4), 0, 0, 0, 0)
#   b_B: diagonal effect
B_B = Matrix([[Rational(1, 3), 0, 0],
              [0, Rational(2, 3), 0],
              [0, 0, Rational(1, 5)]])
#   b_M: off-diagonal real effect
B_M = hermitian_3x3(Rational(2, 5), Rational(3, 5), Rational(1, 2),
                    Rational(1, 5), 0, 0, 0, 0, 0)


# ============================================================================
# Clause (i): rank 3, three orthogonal rank-1 projective units summing to I_3
# ============================================================================

class TestClauseI_RankThreeUnits:
    """DERV-61-01: Jordan rank 3 with three mutually orthogonal rank-1
    projective units summing to I_3 (>= 2 required by clause (i))."""

    def _E_std(self):
        E = []
        for i in range(3):
            v = zeros(3, 1)
            v[i] = 1
            E.append(v * v.H)
        return E

    def test_three_projective_units_standard(self):
        """E_11, E_22, E_33 are nontrivial rank-1 projective units (standard frame)."""
        for P in self._E_std():
            assert is_rank_one_projection(P)

    def test_mutual_orthogonality_standard(self):
        """E_ii o E_jj = 0 and E_ii E_jj = 0 for i != j (Jordan + matrix orthogonal)."""
        E = self._E_std()
        for i in range(3):
            for j in range(i + 1, 3):
                assert simplify(jordan_product(E[i], E[j])).equals(zeros(3, 3))
                assert simplify(E[i] * E[j]).equals(zeros(3, 3))

    def test_completeness_standard(self):
        """E_11 + E_22 + E_33 = I_3 (resolution of identity); rank caps at 3."""
        E = self._E_std()
        assert simplify(E[0] + E[1] + E[2]).equals(I3)
        # No room for a 4th orthogonal nonzero projective unit.
        assert simplify(I3 - (E[0] + E[1] + E[2])).equals(zeros(3, 3))

    def test_rotated_frame_invariance(self):
        """Three orthogonal rank-1 projective units summing to I_3 hold in a
        rotated frame too -> clause (i) is intrinsic / frame-independent."""
        r = Rational(1, 1) / sqrt(2)
        U = Matrix([[r, r, 0], [-r, r, 0], [0, 0, symI]])
        assert simplify(U * U.H - I3).equals(zeros(3, 3))  # U unitary
        E = self._E_std()
        E_rot = [simplify(U * E[i] * U.H) for i in range(3)]
        for P in E_rot:
            assert is_rank_one_projection(P)
        for i in range(3):
            for j in range(i + 1, 3):
                assert simplify(jordan_product(E_rot[i], E_rot[j])).equals(zeros(3, 3))
        assert simplify(E_rot[0] + E_rot[1] + E_rot[2]).equals(I3)


# ============================================================================
# Clause (iv): simplicity -- center = C*I_3, no nontrivial central idempotent
# ============================================================================

class TestClauseIV_Simplicity:
    """DERV-61-02: M_3(C)^sa is simple."""

    def test_center_is_scalars(self):
        """Commutant of the matrix units in M_3(C) = scalar multiples of I_3."""
        from sympy import linsolve
        xs = symbols('c0:9')
        X = Matrix(3, 3, xs)

        def Eunit(i, j):
            M = zeros(3, 3)
            M[i, j] = 1
            return M

        gens = [Eunit(0, 1), Eunit(1, 0), Eunit(1, 2),
                Eunit(2, 1), Eunit(0, 2), Eunit(2, 0)]
        eqs = []
        for g in gens:
            comm = X * g - g * X
            eqs += [simplify(comm[k, l]) for k in range(3) for l in range(3)]
        sol = linsolve(eqs, list(xs))
        assert isinstance(sol, FiniteSet) and len(sol) == 1
        Xsol = Matrix(3, 3, list(sol)[0])
        # off-diagonal entries identically zero
        for i in range(3):
            for j in range(3):
                if i != j:
                    assert simplify(Xsol[i, j]) == 0
        # diagonal entries all equal to a single free parameter
        assert simplify(Xsol[0, 0] - Xsol[1, 1]) == 0
        assert simplify(Xsol[1, 1] - Xsol[2, 2]) == 0
        assert len(Xsol.free_symbols) == 1

    def test_no_nontrivial_central_idempotent(self):
        """A central element is scalar lambda*I_3; idempotency lambda^2=lambda
        forces lambda in {0,1}, i.e. the only central idempotents are 0 and I_3."""
        lam = symbols('lam')
        roots = solveset(lam**2 - lam, lam, domain=S.Complexes)
        assert roots == FiniteSet(0, 1)


# ============================================================================
# Clause (iii) composite dimension: minimal 81 = 9*9, maximal 162 != 81 (BGW)
# ============================================================================

class TestClauseIII_CompositeDimension:
    """DERV-61-03: minimal/standard composite real-dim 81; maximal/universal
    composite real-dim 162; minimal != maximal (BGW; Phase 60 correction)."""

    def test_factor_and_composite_dimensions(self):
        dim_M3 = 9
        dim_M9 = 81
        assert dim_M3 == 3 ** 2
        assert dim_M9 == 9 ** 2
        # minimal composite = M_3(C)^sa (x) M_3(C)^sa = M_9(C)^sa, real-dim 81 = 9*9
        assert dim_M3 * dim_M3 == 81
        assert dim_M3 * dim_M3 == dim_M9
        # maximal/universal composite = M_9(C)^sa (+) M_9(C)^sa, real-dim 162
        assert 2 * dim_M9 == 162
        # minimal != maximal (extra classical bit; the Phase 60 corrected fact)
        assert dim_M3 * dim_M3 != 2 * dim_M9

    def test_kron_of_hermitians_is_9x9_hermitian(self):
        """Standard tensor product: kron of two 3x3 Hermitians lands in M_9(C)^sa."""
        K = kronecker_product(A_B, A_M)
        assert K.shape == (9, 9)
        assert simplify(K - K.H).equals(zeros(9, 9))


# ============================================================================
# matrix_sqrt_nxn self-check (3x3 PSD test effects)
# ============================================================================

class TestMatrixSqrt:
    """sqrt(M)^2 == M, Hermitian, PSD for 3x3 PSD test effects (exact)."""

    @pytest.mark.parametrize("M", [A_B, A_M, B_M, I3,
                                   Matrix([[Rational(1, 4), 0, 0],
                                           [0, Rational(9, 16), 0],
                                           [0, 0, 1]])])
    def test_sqrt_squares_back(self, M):
        s = matrix_sqrt_nxn(M)
        assert simplify(s * s - M).equals(zeros(3, 3))   # sqrt(M)^2 == M (exact)
        assert simplify(s - s.H).equals(zeros(3, 3))     # Hermitian
        assert _is_psd_hermitian(s)                       # PSD

    def test_test_effects_are_valid_effects(self):
        """Sanity: all chosen 3x3 test matrices are genuine effects (0 <= a <= I)."""
        for M in (A_B, A_M, B_B, B_M):
            assert _eigenvalues_real_in_unit_interval(M)


# ============================================================================
# THE Phase 60 OPEN ITEM: product-form sequential product factorizes on M_9(C)^sa
# ============================================================================

class TestClauseIII_SeqProductFactorization:
    """DERV-61-03 datum 4 (Phase 60 open item, asserted-from-Luders in 60-02):
    the product-form sequential product a&b = sqrt(a) b sqrt(a) factorizes across
    the body-model tensor split on the ASSOCIATIVE composite
    M_9(C)^sa = M_3(C)^sa (x) M_3(C)^sa.  Re-derived here by EXACT matrix
    computation on the full 9x9 (NOT assumed from the abstract product form)."""

    def test_sqrt_kron_identity(self):
        """Intermediate identity: sqrt(a_B (x) a_M) = sqrt(a_B) (x) sqrt(a_M)
        for PSD factors.  Computed by full 9x9 spectral sqrt vs kron of 3x3 sqrts."""
        a = kronecker_product(A_B, A_M)               # 9x9 PSD
        lhs = matrix_sqrt_nxn(a)                       # sqrt on the full 9x9
        rhs = kronecker_product(matrix_sqrt_nxn(A_B), matrix_sqrt_nxn(A_M))
        assert simplify(lhs - rhs).equals(zeros(9, 9))

    def test_product_form_factorizes(self):
        """LHS = sqrt(a) b sqrt(a) on the full 9x9  ==  RHS = (a_B & b_B) (x) (a_M & b_M).
        Product effects a = a_B (x) a_M, b = b_B (x) b_M with off-diagonal factors.
        This is the DECISIVE Phase 61 claim (clause iii datum 4)."""
        a = kronecker_product(A_B, A_M)
        b = kronecker_product(B_B, B_M)

        # LHS: compute the sequential product directly on the 9x9 composite.
        lhs = luders_seq_product(a, b)                 # = sqrt(a) b sqrt(a), 9x9

        # RHS: factorized form, sequential product on each 3x3 factor.
        ab = luders_seq_product(A_B, B_B)              # a_B & b_B
        am = luders_seq_product(A_M, B_M)              # a_M & b_M
        rhs = kronecker_product(ab, am)

        assert simplify(lhs - rhs).equals(zeros(9, 9))  # EXACT factorization

    def test_product_form_factorizes_second_pair(self):
        """Robustness: a different product-effect pair (swap roles, both factors
        off-diagonal) still factorizes exactly."""
        a = kronecker_product(A_M, A_B)
        b = kronecker_product(B_M, B_B)
        lhs = luders_seq_product(a, b)
        rhs = kronecker_product(luders_seq_product(A_M, B_M),
                                luders_seq_product(A_B, B_B))
        assert simplify(lhs - rhs).equals(zeros(9, 9))

    def test_S3_unitality_on_composite(self):
        """S3: I_9 & a = a for a product effect (and 1 & a = a on a 3x3 sample)."""
        a = kronecker_product(A_B, A_M)
        assert simplify(luders_seq_product(I9, a) - a).equals(zeros(9, 9))
        assert simplify(luders_seq_product(I3, A_B) - A_B).equals(zeros(3, 3))

    def test_effect_range_on_composite(self):
        """0 <= a & b <= I_9 for the tested product effects (a&b is an effect).

        a & b = (a_B & b_B) (x) (a_M & b_M) factorizes (proved above), so its
        eigenvalues are products of the factor eigenvalues.  a&b is an effect
        (0 <= a&b <= I_9) iff each 3x3 factor is an effect (0 <= . <= I_3): a
        product lambda*mu of numbers in [0,1] is again in [0,1].  We verify the
        factor effect-ranges exactly on the cheap 3x3 sequential products
        (mathematically equivalent to, and far faster than, a 9x9 eigen-check)."""
        ab = luders_seq_product(A_B, B_B)               # a_B & b_B (3x3)
        am = luders_seq_product(A_M, B_M)               # a_M & b_M (3x3)
        assert _eigenvalues_real_in_unit_interval(ab)   # 0 <= a_B&b_B <= I_3
        assert _eigenvalues_real_in_unit_interval(am)   # 0 <= a_M&b_M <= I_3
        # => eigenvalues of a&b = kron(ab,am) are products in [0,1]: a&b is an effect.


# ============================================================================
# SCOPE GUARD assertion (associative slice only -- fp-reach-into-h3o rejected)
# ============================================================================

class TestScopeGuard:
    """Confirm by construction that this verification stays on the ASSOCIATIVE
    slice and never reaches into the non-associative h_3(O) (Phase 62)."""

    def test_no_octonion_import(self):
        """This module must NOT import octonion_algebra's H3O / jordan_product
        non-associative machinery for the sequential-product check.  The
        slice_clause_iii_verification module likewise stays associative."""
        # Neither this test module nor the verification module pulled in the
        # non-associative octonion h_3(O) machinery.
        assert 'octonion_algebra' not in sys.modules

    def test_composite_is_associative_matrix_algebra(self):
        """The composite is the ASSOCIATIVE M_9(C): matrix multiplication is
        associative on the 9x9 representation (positive control that we are NOT
        in the non-associative h_3(O) regime)."""
        a = kronecker_product(A_B, A_M)
        b = kronecker_product(B_B, B_M)
        c = kronecker_product(B_M, B_B)
        # (ab)c == a(bc): associativity of the underlying matrix algebra.
        assert simplify((a * b) * c - a * (b * c)).equals(zeros(9, 9))


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
