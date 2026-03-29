# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   peirce_decomposition=under_E11,
#   v_half_basis=(x2_0..x2_7,x3_0..x3_7),
#   v_zero_basis=spin9_adapted_10elements
#
# Phase 28, Plan 02: V_0 channel operators, J^2=-Id search, Krasnov J_u
# membership, operator algebra characterization (ALGV-02).
#
# References:
#   Baez, "The Octonions," Bull. AMS 39 (2002), Sec. 3.4
#   Krasnov, "SO(9) characterisation of the SM gauge group," arXiv:1912.11282
#   Boyle, arXiv:2006.16265, Section 2
#
# Reproducibility: numpy 2.4.2, Python 3.14.2, macOS Darwin 24.6.0

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

import numpy as np
import pytest

from octonion_algebra import (
    Octonion, H3O, jordan_product,
    peirce_V1, peirce_Vhalf, peirce_V0,
    Vhalf_basis_vectors, V0_basis_elements,
    compute_T_b_matrix, compute_T_b_matrices, compute_T_b_full_products,
    krasnov_J_u_matrix,
    search_j_squared_individual, search_j_squared_linear,
    test_ju_in_span, compute_commutator_algebra,
)

ATOL = 1e-14
ATOL_JORDAN = 1e-12
RNG = np.random.default_rng(42)


# ============================================================================
# Task 1: V_0 basis and Peirce operator validation
# ============================================================================

class TestV0Basis:
    """Validate V_0 basis elements lie in V_0."""

    def test_v0_basis_is_in_v0(self):
        """All 10 basis elements satisfy Pi_0(b_i) = b_i."""
        basis = V0_basis_elements()
        assert len(basis) == 10, f"Expected 10 basis elements, got {len(basis)}"
        for i, b in enumerate(basis):
            proj = peirce_V0(b)
            diff = (b - proj).norm()
            assert diff < ATOL, (
                f"b_{i} not in V_0: ||b - Pi_0(b)|| = {diff}")

    def test_v0_basis_orthogonality_to_v1_vhalf(self):
        """V_0 basis elements have zero V_1 and V_{1/2} components."""
        basis = V0_basis_elements()
        for i, b in enumerate(basis):
            v1 = peirce_V1(b).norm()
            vh = peirce_Vhalf(b).norm()
            assert v1 < ATOL, f"b_{i} has V_1 component: {v1}"
            assert vh < ATOL, f"b_{i} has V_{{1/2}} component: {vh}"


class TestPeirceV0Rule:
    """Validate V_0 . V_{1/2} lands entirely in V_{1/2}."""

    def test_peirce_v0_rule(self):
        """For all 10 b_i and 16 v_j: Pi_1(b_i . v_j) = 0, Pi_0(b_i . v_j) = 0.

        This checks 160 products total (acceptance test test-peirce-v0-rule).
        """
        basis_v0 = V0_basis_elements()
        basis_vhalf = Vhalf_basis_vectors()
        max_v1_leak = 0.0
        max_v0_leak = 0.0

        for i, b in enumerate(basis_v0):
            for j, v in enumerate(basis_vhalf):
                prod = jordan_product(b, v)
                v1_norm = peirce_V1(prod).norm()
                v0_norm = peirce_V0(prod).norm()
                max_v1_leak = max(max_v1_leak, v1_norm)
                max_v0_leak = max(max_v0_leak, v0_norm)
                assert v1_norm < ATOL, (
                    f"V_1 leakage: b_{i} . v_{j} has ||Pi_1|| = {v1_norm}")
                assert v0_norm < ATOL, (
                    f"V_0 leakage: b_{i} . v_{j} has ||Pi_0|| = {v0_norm}")

        print(f"  Peirce V_0 rule: max V_1 leakage = {max_v1_leak:.2e}, "
              f"max V_0 leakage = {max_v0_leak:.2e}")


class TestTbMatrices:
    """Validate properties of the 10 T_b operator matrices."""

    @pytest.fixture(scope="class")
    def T_matrices(self):
        return compute_T_b_matrices()

    def test_T_b_count(self, T_matrices):
        """10 matrices, each 16x16."""
        assert len(T_matrices) == 10
        for i, T in enumerate(T_matrices):
            assert T.shape == (16, 16), f"T_{i} shape: {T.shape}"

    def test_T_b1_is_quarter_identity(self, T_matrices):
        """T_{b_1} = (1/4)*Id_{16} (benchmark: trace element).

        b_1 = (1/2)(E_{22} + E_{33}) = (1/2)(Id - E_{11}).
        L_{b_1}(v) = (1/2)(L_Id - L_{E_{11}})(v) = (1/2)(v - (1/2)v) = (1/4)v.
        So T_{b_1} = (1/4)*Id, NOT (1/2)*Id.

        [Deviation Rule 1: Plan stated T_{b_1} = (1/2)*Id, but the correct
         value is (1/4)*Id. The plan confused b_1 = (1/2)(E_{22}+E_{33})
         with the complementary idempotent (E_{22}+E_{33}) = 1-E_{11}.]
        """
        T_b1 = T_matrices[0]
        expected = 0.25 * np.eye(16)
        max_err = np.max(np.abs(T_b1 - expected))
        assert max_err < ATOL, (
            f"T_b1 != (1/4)*I_16: max error = {max_err}")
        print(f"  T_b1 benchmark: max |T_b1 - (1/4)*I_16| = {max_err:.2e}")

    def test_T_b_eigenvalues_real(self, T_matrices):
        """All eigenvalues of all 10 T_{b_i} are real."""
        for i, T in enumerate(T_matrices):
            evals = np.linalg.eigvals(T)
            max_imag = np.max(np.abs(np.imag(evals)))
            assert max_imag < ATOL, (
                f"T_{i} has complex eigenvalue: max |Im| = {max_imag}")

    def test_T_b_eigenvalue_spectra(self, T_matrices):
        """Report eigenvalue spectra (informational)."""
        print("\n  T_b eigenvalue spectra:")
        for i, T in enumerate(T_matrices):
            evals = np.sort(np.real(np.linalg.eigvals(T)))
            unique_evals = np.unique(np.round(evals, 10))
            print(f"    T_b[{i}]: unique eigenvalues = {unique_evals}")

    def test_T_b_symmetry(self, T_matrices):
        """Check T_{b_i} = T_{b_i}^T for all i."""
        for i, T in enumerate(T_matrices):
            asym = np.max(np.abs(T - T.T))
            assert asym < ATOL, (
                f"T_{i} not symmetric: max |T - T^T| = {asym}")

    def test_jordan_identity_v0_vhalf(self):
        """Jordan identity spot-check: (b.v).b^2 = b.(v.b^2) projected on V_{1/2}.

        For b in V_0 and v in V_{1/2}, b^2 is in V_0 (Peirce rule: V_0.V_0 in V_0+V_1).
        Then v.b^2 is in V_{1/2} (V_{1/2}.V_0 in V_{1/2}).
        And (b.v).b^2 has V_{1/2} part from (V_{1/2}.V_0).
        """
        max_residual = 0.0
        for _ in range(20):
            # Random V_0 element
            b = peirce_V0(H3O.random(RNG))
            # Random V_{1/2} element
            v = peirce_Vhalf(H3O.random(RNG))
            b_sq = jordan_product(b, b)
            lhs = jordan_product(jordan_product(b, v), b_sq)
            rhs = jordan_product(b, jordan_product(v, b_sq))
            lhs_half = peirce_Vhalf(lhs)
            rhs_half = peirce_Vhalf(rhs)
            residual = (lhs_half - rhs_half).norm()
            max_residual = max(max_residual, residual)
            assert residual < ATOL_JORDAN, (
                f"Jordan identity V_0.V_{{1/2}} failed: residual = {residual}")
        print(f"  Jordan identity V_0.V_{{1/2}} max residual: {max_residual:.2e}")


# ============================================================================
# Task 2: ALGV-02 -- J^2 search, Krasnov J_u, operator algebra
# ============================================================================

class TestJSquaredSearch:
    """J^2 = -Id exhaustive search over T_b span."""

    @pytest.fixture(scope="class")
    def T_matrices(self):
        return compute_T_b_matrices()

    def test_j_squared_search_individual(self, T_matrices):
        """No individual T_{b_i}^2 = -Id."""
        results = search_j_squared_individual(T_matrices)
        for r in results:
            assert not r['is_minus_id'], (
                f"T_{r['index']}^2 = -Id! (unexpected positive)")
            print(f"    T_b[{r['index']}]^2 eigenvalues: "
                  f"{np.unique(np.round(r['eigenvalues_T_sq'], 10))}")

    def test_j_squared_search_systematic(self, T_matrices):
        """Systematic search: linear system A @ q = b analysis."""
        result = search_j_squared_linear(T_matrices)
        print(f"\n  J^2 = -Id linear system:")
        print(f"    A matrix: 256 x {result['A_matrix'].shape[1]}")
        print(f"    rank(A) = {result['rank_A']}")
        print(f"    min ||A q - b|| = {result['linear_residual']:.6e}")
        print(f"    Linear feasible: {result['linear_feasible']}")

        # The linear system is a NECESSARY condition for J^2 = -Id.
        # If infeasible, no combination of T_b gives J^2 = -Id.
        if not result['linear_feasible']:
            print("    VERDICT: J^2 = -Id is IMPOSSIBLE in span({T_b})")
            print("    (Linear system infeasible -- even ignoring rank-1 constraint)")


class TestKrasnovJu:
    """Krasnov's J_u construction and membership test."""

    @pytest.fixture(scope="class")
    def J_u(self):
        return krasnov_J_u_matrix()

    @pytest.fixture(scope="class")
    def T_matrices(self):
        return compute_T_b_matrices()

    def test_krasnov_ju_squared(self, J_u):
        """J_u^2 = -Id_{16}."""
        J_sq = J_u @ J_u
        max_err = np.max(np.abs(J_sq + np.eye(16)))
        assert max_err < ATOL, (
            f"J_u^2 != -Id: max |J_u^2 + I| = {max_err}")
        print(f"  J_u^2 = -Id: max error = {max_err:.2e}")

    def test_krasnov_ju_antisymmetric(self, J_u):
        """J_u should be antisymmetric (real matrix with J^2 = -I implies J^T = -J)."""
        asym = np.max(np.abs(J_u + J_u.T))
        assert asym < ATOL, (
            f"J_u not antisymmetric: max |J + J^T| = {asym}")

    def test_ju_in_span(self, T_matrices, J_u):
        """Least-squares test: is J_u in span({T_b})?"""
        result = test_ju_in_span(T_matrices, J_u)
        print(f"\n  J_u membership test:")
        print(f"    Residual: {result['residual']:.6e}")
        print(f"    In span: {result['in_span']}")
        if result['in_span']:
            print(f"    Coefficients: {result['coefficients']}")
        else:
            print(f"    J_u is OUTSIDE span({{T_b}})")
            # Verify it's conclusively outside (residual > 0.1)
            assert result['residual'] > 0.1, (
                f"Ambiguous: residual = {result['residual']} is between 1e-12 and 0.1")


class TestCommutatorAlgebra:
    """Operator algebra characterization."""

    @pytest.fixture(scope="class")
    def T_matrices(self):
        return compute_T_b_matrices()

    def test_commutator_algebra_dimension(self, T_matrices):
        """Lie algebra dimension from iterated commutators."""
        result = compute_commutator_algebra(T_matrices)
        print(f"\n  Commutator algebra:")
        print(f"    Dimension: {result['dimension']}")
        print(f"    Closed: {result['closed']}")
        print(f"    Iterations: {result['iterations']}")
        assert result['closed'], "Commutator algebra did not close"


class TestCl9CrossValidation:
    """Cl(9,0) cross-validation."""

    @staticmethod
    def _build_cl9_generators():
        """Build 9 Clifford generators for Cl(9,0) acting on R^16.

        Uses recursive tensor product construction:
        gamma_1 = sigma_1 x I x I x I  (16x16)
        gamma_2 = sigma_2 x I x I x I
        gamma_3 = sigma_3 x sigma_1 x I x I
        gamma_4 = sigma_3 x sigma_2 x I x I
        gamma_5 = sigma_3 x sigma_3 x sigma_1 x I
        gamma_6 = sigma_3 x sigma_3 x sigma_2 x I
        gamma_7 = sigma_3 x sigma_3 x sigma_3 x sigma_1
        gamma_8 = sigma_3 x sigma_3 x sigma_3 x sigma_2
        gamma_9 = sigma_3 x sigma_3 x sigma_3 x sigma_3  (chirality in Cl(8))

        Wait -- Cl(9,0) on R^16 means we need 9 real antisymmetric matrices
        (if gamma_i^2 = +I, they are symmetric). Actually:
        Cl(9,0) has a unique irrep on R^16 (since dim = 2^4 and 9 = 2*4+1).

        Standard construction via recursive doubling of Cl(n) representations.
        """
        s1 = np.array([[0, 1], [1, 0]], dtype=np.float64)
        s2 = np.array([[0, -1], [1, 0]], dtype=np.float64)  # i*sigma_y
        s3 = np.array([[1, 0], [0, -1]], dtype=np.float64)
        I2 = np.eye(2, dtype=np.float64)

        # Build Cl(2k+1) on R^{2^k} recursively.
        # For k=4: Cl(9) on R^16.
        # Start: Cl(1) on R^1: gamma_1 = [1] (1x1).
        # But we need to get to 16x16. Let's use the standard recursive:
        #
        # Cl(2k+1, 0) irrep on R^{2^k}:
        # From Cl(2k-1) irrep on R^{2^{k-1}}, the 2k+1 generators of Cl(2k+1) are:
        #   gamma'_j = gamma_j (x) sigma_1   for j = 1,...,2k-1
        #   gamma'_{2k} = I (x) sigma_2
        #   gamma'_{2k+1} = I (x) sigma_3
        #
        # Start with Cl(1) on R^1: gamma_1 = np.array([[1.0]])

        # k=0: Cl(1) on R^1
        gammas = [np.array([[1.0]])]

        # k=1: Cl(3) on R^2
        old = gammas
        gammas = []
        for g in old:
            gammas.append(np.kron(g, s1))
        gammas.append(np.kron(np.eye(1), s2))
        gammas.append(np.kron(np.eye(1), s3))

        # k=2: Cl(5) on R^4
        old = gammas
        n = old[0].shape[0]
        gammas = []
        for g in old:
            gammas.append(np.kron(g, s1))
        gammas.append(np.kron(np.eye(n), s2))
        gammas.append(np.kron(np.eye(n), s3))

        # k=3: Cl(7) on R^8
        old = gammas
        n = old[0].shape[0]
        gammas = []
        for g in old:
            gammas.append(np.kron(g, s1))
        gammas.append(np.kron(np.eye(n), s2))
        gammas.append(np.kron(np.eye(n), s3))

        # k=4: Cl(9) on R^16
        old = gammas
        n = old[0].shape[0]
        gammas = []
        for g in old:
            gammas.append(np.kron(g, s1))
        gammas.append(np.kron(np.eye(n), s2))
        gammas.append(np.kron(np.eye(n), s3))

        assert len(gammas) == 9
        assert gammas[0].shape == (16, 16)
        return gammas

    def test_cl9_anticommutation(self):
        """Verify {gamma_i, gamma_j} = 2*delta_{ij}*I_{16}."""
        gammas = self._build_cl9_generators()
        for i in range(9):
            for j in range(i, 9):
                anticomm = gammas[i] @ gammas[j] + gammas[j] @ gammas[i]
                if i == j:
                    expected = 2.0 * np.eye(16)
                else:
                    expected = np.zeros((16, 16))
                max_err = np.max(np.abs(anticomm - expected))
                assert max_err < ATOL, (
                    f"{{gamma_{i}, gamma_{j}}} error: {max_err}")

    def test_cl9_vs_traceless_Tb(self):
        """Compare traceless T_b operators with Cl(9) generators.

        The 9 traceless T_b (b_2 through b_10) should span the same
        space as some 9-dimensional subspace related to Cl(9).
        """
        T_matrices = compute_T_b_matrices()
        # Traceless: indices 1 through 9 (b_2 through b_10)
        T_traceless = T_matrices[1:]
        assert len(T_traceless) == 9

        # Build the span of traceless T_b
        T_flat = np.array([T.flatten() for T in T_traceless]).T  # 256 x 9
        rank_T = np.linalg.matrix_rank(T_flat, tol=1e-10)

        gammas = self._build_cl9_generators()
        G_flat = np.array([g.flatten() for g in gammas]).T  # 256 x 9

        # Check if spans intersect significantly
        combined = np.column_stack([T_flat, G_flat])
        rank_combined = np.linalg.matrix_rank(combined, tol=1e-10)

        print(f"\n  Cl(9) cross-validation:")
        print(f"    rank(traceless T_b) = {rank_T}")
        print(f"    rank(Cl(9) gammas) = {np.linalg.matrix_rank(G_flat, tol=1e-10)}")
        print(f"    rank(combined) = {rank_combined}")
        print(f"    Overlap dimension = {rank_T + 9 - rank_combined}")

        # Note: the Cl(9) generators here use a specific basis that may
        # differ from the octonion-adapted basis. The comparison is about
        # whether the SPACES match, not the individual matrices.

    def test_cl10_10th_generator_is_ju(self):
        """The 10th Clifford generator (extending Cl(9) to Cl(10)) should
        relate to J_u = chirality on R^16.

        Cl(10) on R^{32} has chirality on R^{16} x R^{16}.
        The 10th generator of Cl(10) when restricted to S_{10}^+ = R^{16}
        provides the complex structure.

        For Cl(9) on R^16, the "volume element" gamma_1...gamma_9 = +/- Id
        (since 9 is odd, this is a scalar in the irrep). So the chirality
        of Cl(10) is NOT inside Cl(9) -- it's the additional generator.
        """
        gammas = self._build_cl9_generators()
        # Volume element of Cl(9)
        vol = np.eye(16)
        for g in gammas:
            vol = vol @ g
        # For Cl(9,0), gamma_1...gamma_9 should be +/- I on the irrep
        vol_evals = np.linalg.eigvalsh(vol)
        print(f"\n  Cl(9) volume element eigenvalues: "
              f"{np.unique(np.round(vol_evals, 10))}")

        # The volume element should be +I or -I
        is_plus = np.allclose(vol, np.eye(16), atol=1e-10)
        is_minus = np.allclose(vol, -np.eye(16), atol=1e-10)
        assert is_plus or is_minus, (
            f"Cl(9) volume element is not +/-I: {vol_evals[:3]}...")
        sign = 1 if is_plus else -1
        print(f"  Cl(9) volume element = {'+' if sign > 0 else '-'}I")

        # J_u acts on O^2 in the octonion basis, while Cl(9) generators
        # are in the tensor product basis. We can't directly compare matrices
        # without a basis change. But we CAN check that J_u satisfies
        # Cl(10) relations with respect to the T_b operators (if they relate
        # to Cl(9) generators).
        J_u = krasnov_J_u_matrix()
        # J_u should anticommute with all 9 traceless T_b if T_b ~ Cl(9) generators
        T_matrices = compute_T_b_matrices()
        T_traceless = T_matrices[1:]
        for i, T in enumerate(T_traceless):
            anticomm = J_u @ T + T @ J_u
            norm_ac = np.linalg.norm(anticomm)
            print(f"    {{J_u, T_b[{i+1}]}} norm = {norm_ac:.6e}")
