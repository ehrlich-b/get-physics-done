# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   peirce_decomposition=under_E11,
#   v_half_basis=(x2_0..x2_7,x3_0..x3_7)
#
# Phase 28, Plan 01: Comprehensive validation of octonion arithmetic,
# h_3(O) Jordan product, Peirce decomposition, and ALGV-01 (L_{E_{11}}).
#
# References:
#   Baez, "The Octonions," Bull. AMS 39 (2002), Sec. 3.4
#   Alfsen-Shultz, State Spaces of Operator Algebras (2001), Ch. 8-9
#
# Reproducibility: numpy 2.4.2, Python 3.14.2, macOS Darwin 24.6.0
# Random seed: 42 for all random tests.

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

import numpy as np
import pytest

from octonion_algebra import (
    Octonion, FANO_TRIPLES,
    H3O, jordan_product,
    peirce_V1, peirce_Vhalf, peirce_V0,
    L_E11, L_E11_matrix_on_Vhalf, Vhalf_basis_vectors,
)

ATOL = 1e-14
ATOL_JORDAN = 1e-12  # Jordan identity accumulates more floating-point error

RNG = np.random.default_rng(42)


# ============================================================================
# Octonion unit tests
# ============================================================================

class TestOctonionBasics:
    """Tests 13-17: Octonion arithmetic validation."""

    def test_octonion_unit_squares(self):
        """Test 13: e_i^2 = -1 for i=1,...,7."""
        for i in range(1, 8):
            ei = Octonion.basis(i)
            ei_sq = ei * ei
            expected = np.zeros(8)
            expected[0] = -1.0
            np.testing.assert_allclose(ei_sq.c, expected, atol=ATOL,
                                       err_msg=f"e_{i}^2 != -1")

    def test_octonion_fano_triples(self):
        """Test 14: All 7 Fano triples with correct signs."""
        for i, j, k in FANO_TRIPLES:
            ei = Octonion.basis(i)
            ej = Octonion.basis(j)
            ek = Octonion.basis(k)

            # e_i * e_j = +e_k
            result = ei * ej
            np.testing.assert_allclose(result.c, ek.c, atol=ATOL,
                                       err_msg=f"e_{i}*e_{j} != +e_{k}")

            # e_j * e_i = -e_k (anticommutativity)
            result = ej * ei
            np.testing.assert_allclose(result.c, (-ek).c, atol=ATOL,
                                       err_msg=f"e_{j}*e_{i} != -e_{k}")

            # Cyclic: e_j * e_k = +e_i
            result = ej * ek
            np.testing.assert_allclose(result.c, ei.c, atol=ATOL,
                                       err_msg=f"e_{j}*e_{k} != +e_{i}")

            # Cyclic: e_k * e_i = +e_j
            result = ek * ei
            np.testing.assert_allclose(result.c, ej.c, atol=ATOL,
                                       err_msg=f"e_{k}*e_{i} != +e_{j}")

    def test_octonion_norm_multiplicativity(self):
        """Test 15: |a*b| = |a|*|b| for 100 random pairs."""
        max_err = 0.0
        for _ in range(100):
            a = Octonion.random(RNG)
            b = Octonion.random(RNG)
            prod_norm = (a * b).norm()
            norms_prod = a.norm() * b.norm()
            if norms_prod > 0:
                err = abs(prod_norm - norms_prod) / norms_prod
                max_err = max(max_err, err)
                assert err < ATOL, (
                    f"Norm multiplicativity failed: rel err = {err}")
        print(f"  Norm multiplicativity max relative error: {max_err:.2e}")

    def test_octonion_non_associativity(self):
        """Test 16: (e_1*e_2)*e_3 != e_1*(e_2*e_3) as witness."""
        e1 = Octonion.basis(1)
        e2 = Octonion.basis(2)
        e3 = Octonion.basis(3)

        lhs = (e1 * e2) * e3  # e_4 * e_3 = -e_6 (reverse of triple (3,4,6))
        rhs = e1 * (e2 * e3)  # e_1 * e_5 = -e_6... wait, let me check
        # Actually: e_2*e_3 = e_5 (triple (2,3,5))
        # e_1*e_5 = ? From (5,6,1): e_5*e_6=e_1, so e_1*e_5=e_6... but reversed:
        # From (5,6,1): e_6*e_1=e_5, e_1*e_5= -e_6? No:
        # (5,6,1) means e_5*e_6=e_1, e_6*e_1=e_5, e_1*e_5=e_6.
        # Wait: For triple (i,j,k)=(5,6,1): e_i*e_j=e_k means e_5*e_6=e_1
        # Then e_j*e_k=e_i means e_6*e_1=e_5
        # Then e_k*e_i=e_j means e_1*e_5=e_6
        # So RHS = e_1*(e_2*e_3) = e_1*e_5 = e_6
        # LHS = (e_1*e_2)*e_3 = e_4*e_3
        # For (3,4,6): e_3*e_4=e_6, so e_4*e_3=-e_6
        # So LHS = -e_6, RHS = +e_6.  Indeed different!
        diff = (lhs - rhs).norm()
        assert diff > 1.0, (
            f"Non-associativity witness failed: ||(e1*e2)*e3 - e1*(e2*e3)|| = {diff}")

    def test_octonion_conjugation(self):
        """Test 17: a*conj(a) is real and equals |a|^2."""
        for _ in range(50):
            a = Octonion.random(RNG)
            prod = a * a.conjugate()
            # Should be real
            assert np.allclose(prod.c[1:], 0.0, atol=ATOL), (
                f"a*conj(a) has imaginary part: {prod.c[1:]}")
            # Real part should be |a|^2
            assert abs(prod.c[0] - a.norm_sq()) < ATOL, (
                f"a*conj(a) real part {prod.c[0]} != |a|^2 = {a.norm_sq()}")


# ============================================================================
# h_3(O) Jordan product tests
# ============================================================================

class TestJordanProduct:
    """Tests 18-19: Jordan product validation."""

    def test_jordan_product_commutativity(self):
        """Test 18: A.B = B.A for 50 random pairs."""
        max_err = 0.0
        for _ in range(50):
            A = H3O.random(RNG)
            B = H3O.random(RNG)
            AB = jordan_product(A, B)
            BA = jordan_product(B, A)
            diff = (AB - BA).norm()
            max_err = max(max_err, diff)
            assert diff < ATOL, (
                f"Jordan commutativity failed: ||A.B - B.A|| = {diff}")
        print(f"  Jordan commutativity max error: {max_err:.2e}")

    def test_jordan_identity(self):
        """Test 19: ||(A.B).A^2 - A.(B.A^2)|| < 1e-12 for 100 random pairs.

        The Jordan identity: (x . y) . x^2 = x . (y . x^2)
        """
        max_residual = 0.0
        for _ in range(100):
            A = H3O.random(RNG)
            B = H3O.random(RNG)
            A_sq = jordan_product(A, A)
            lhs = jordan_product(jordan_product(A, B), A_sq)
            rhs = jordan_product(A, jordan_product(B, A_sq))
            residual = (lhs - rhs).norm()
            max_residual = max(max_residual, residual)
            assert residual < ATOL_JORDAN, (
                f"Jordan identity failed: residual = {residual}")
        print(f"  Jordan identity max residual: {max_residual:.2e}")


# ============================================================================
# Peirce decomposition tests
# ============================================================================

class TestPeirceDecomposition:
    """Tests 20-22: Peirce projection validation."""

    def test_peirce_projections_sum_to_identity(self):
        """Test 20: Pi_1(X) + Pi_{1/2}(X) + Pi_0(X) = X for 50 random X."""
        for _ in range(50):
            X = H3O.random(RNG)
            recon = peirce_V1(X) + peirce_Vhalf(X) + peirce_V0(X)
            diff = (X - recon).norm()
            assert diff < ATOL, (
                f"Peirce projections don't sum to identity: ||X - sum|| = {diff}")

    def test_peirce_dimensions(self):
        """Test 21: dim(V_1) = 1, dim(V_{1/2}) = 16, dim(V_0) = 10.

        We construct the 27x27 projection matrices and check their ranks.
        """
        # Generate 27 random h_3(O) elements and project each
        # Use the projection to build the 27x27 matrix representation
        basis_27 = []
        # Canonical basis: alpha, beta, gamma (3 reals), then x1[0:8], x2[0:8], x3[0:8]
        for i in range(27):
            v = np.zeros(27)
            v[i] = 1.0
            basis_27.append(H3O.from_vector(v))

        # Build projection matrices
        P1 = np.zeros((27, 27))
        Phalf = np.zeros((27, 27))
        P0 = np.zeros((27, 27))
        for j, bj in enumerate(basis_27):
            P1[:, j] = peirce_V1(bj).to_vector()
            Phalf[:, j] = peirce_Vhalf(bj).to_vector()
            P0[:, j] = peirce_V0(bj).to_vector()

        rank_V1 = np.linalg.matrix_rank(P1, tol=1e-10)
        rank_Vhalf = np.linalg.matrix_rank(Phalf, tol=1e-10)
        rank_V0 = np.linalg.matrix_rank(P0, tol=1e-10)

        assert rank_V1 == 1, f"dim(V_1) = {rank_V1}, expected 1"
        assert rank_Vhalf == 16, f"dim(V_{{1/2}}) = {rank_Vhalf}, expected 16"
        assert rank_V0 == 10, f"dim(V_0) = {rank_V0}, expected 10"
        assert rank_V1 + rank_Vhalf + rank_V0 == 27, "Dimensions don't sum to 27"

    def test_peirce_multiplication_rules(self):
        """Test 22: Peirce multiplication rules.

        V_0 . V_{1/2} subset V_{1/2}
        V_1 . V_0 = 0
        V_{1/2} . V_{1/2} subset V_1 + V_0
        """
        for _ in range(50):
            # V_0 . V_{1/2} subset V_{1/2}
            b = peirce_V0(H3O.random(RNG))   # element of V_0
            v = peirce_Vhalf(H3O.random(RNG))  # element of V_{1/2}
            prod = jordan_product(b, v)
            v1_comp = peirce_V1(prod).norm()
            v0_comp = peirce_V0(prod).norm()
            assert v1_comp < ATOL, (
                f"V_0 . V_{{1/2}} has V_1 component: {v1_comp}")
            assert v0_comp < ATOL, (
                f"V_0 . V_{{1/2}} has V_0 component: {v0_comp}")

            # V_1 . V_0 = 0
            a = peirce_V1(H3O.random(RNG))   # element of V_1
            b = peirce_V0(H3O.random(RNG))   # element of V_0
            prod = jordan_product(a, b)
            assert prod.norm() < ATOL, (
                f"V_1 . V_0 != 0: norm = {prod.norm()}")

            # V_{1/2} . V_{1/2} subset V_1 + V_0
            u = peirce_Vhalf(H3O.random(RNG))
            w = peirce_Vhalf(H3O.random(RNG))
            prod = jordan_product(u, w)
            vhalf_comp = peirce_Vhalf(prod).norm()
            assert vhalf_comp < ATOL, (
                f"V_{{1/2}} . V_{{1/2}} has V_{{1/2}} component: {vhalf_comp}")


class TestFanoConventionCrossCheck:
    """Test 23: Fano convention matches test_cl6_sm.py."""

    def test_fano_convention_matches_cl6(self):
        """Verify e_1*e_2 = e_4 matches test_cl6_sm.py ASSERT_CONVENTION."""
        # test_cl6_sm.py declares: octonion_basis=fano_e1e2=e4
        e1 = Octonion.basis(1)
        e2 = Octonion.basis(2)
        result = e1 * e2
        e4 = Octonion.basis(4)
        np.testing.assert_allclose(result.c, e4.c, atol=ATOL,
                                   err_msg="e_1*e_2 != e_4 -- convention mismatch!")


# ============================================================================
# ALGV-01: L_{E_{11}} on V_{1/2}
# ============================================================================

class TestALGV01:
    """Tests 10-13 from Task 2: L_{E_{11}} verification."""

    def test_L_E11_is_half_identity(self):
        """Test 10: L_{E_{11}} = (1/2)*I_{16} on V_{1/2}."""
        M = L_E11_matrix_on_Vhalf()
        expected = 0.5 * np.eye(16)
        max_err = np.max(np.abs(M - expected))
        assert max_err < ATOL, (
            f"L_E11 != (1/2)*I_16: max error = {max_err}")

    def test_L_E11_no_V1_leakage(self):
        """Test 11: Pi_1 component of L_{E_{11}}(v_j) is zero for all j."""
        basis = Vhalf_basis_vectors()
        for j, v_j in enumerate(basis):
            Lv = L_E11(v_j)
            v1_comp = peirce_V1(Lv).norm()
            assert v1_comp < ATOL, (
                f"V_1 leakage for basis vector {j}: {v1_comp}")

    def test_L_E11_no_V0_leakage(self):
        """Test 12: Pi_0 component of L_{E_{11}}(v_j) is zero for all j."""
        basis = Vhalf_basis_vectors()
        for j, v_j in enumerate(basis):
            Lv = L_E11(v_j)
            v0_comp = peirce_V0(Lv).norm()
            assert v0_comp < ATOL, (
                f"V_0 leakage for basis vector {j}: {v0_comp}")

    def test_V1_is_one_dimensional(self):
        """Test 13: V_1 acts as scalar multiplication on V_{1/2}.

        For arbitrary alpha*E_{11}, the action on V_{1/2} is
        (alpha/2)*Id. Only 1 free parameter => dim(V_1) = 1.
        """
        basis = Vhalf_basis_vectors()
        for alpha in [1.0, 2.5, -3.7, 0.001]:
            a_E11 = H3O(alpha=alpha)
            for j, v_j in enumerate(basis):
                result = jordan_product(a_E11, v_j)
                result_half = peirce_Vhalf(result)
                expected = (alpha / 2.0) * v_j
                diff = (result_half - expected).norm()
                assert diff < ATOL, (
                    f"V_1 not scalar on V_{{1/2}}: alpha={alpha}, j={j}, "
                    f"diff={diff}")
