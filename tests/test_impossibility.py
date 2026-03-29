# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   peirce_decomposition=under_E11,
#   v_half_basis=(x2_0..x2_7,x3_0..x3_7),
#   clifford_signature=Cl(9,0)_gamma_i_sq=+I,
#   clifford_normalization=gamma_1=4*T_b[1]_gamma_k=2*T_b[k]_for_k=2..9
#
# Phase 30, Plan 01: Computational verification of three impossibility theorems.
#
# Theorem 1: No Spin(9)-equivariant complex structure on V_{1/2}.
# Theorem 2: J_u not in the Peirce Lie algebra spin(9).
# Theorem 3: Weakest sufficient condition is choice of u in S^6.
#
# References:
#   Lawson-Michelsohn, Spin Geometry (1989), Table I.4.3
#   Krasnov, J. Math. Phys. 62 (2021) 021703, arXiv:1912.11282
#   Phase 29 results (29-01-SUMMARY.md, 29-02-SUMMARY.md)
#
# Reproducibility: numpy 2.4.2, Python 3.14.2, macOS Darwin 24.6.0

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

import numpy as np
import pytest

from octonion_algebra import (
    compute_T_b_matrices, krasnov_J_u_matrix,
    rescale_to_clifford_generators,
    compute_grade_decomposition,
    compute_spin9_commutant,
    compute_grade2_stabilizer,
    compute_gsm_commutant,
    test_ju_uniqueness,
)

ATOL = 1e-14
ATOL_RANK = 1e-10


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture(scope="module")
def T_matrices():
    return compute_T_b_matrices()


@pytest.fixture(scope="module")
def J_u():
    return krasnov_J_u_matrix()


@pytest.fixture(scope="module")
def gamma_matrices(T_matrices):
    return rescale_to_clifford_generators(T_matrices)


# ============================================================================
# Theorem 1: No Spin(9)-equivariant complex structure
# (acceptance tests: test-schur-commutant, test-equivariant-endomorphism)
# ============================================================================

class TestTheorem1SchurCommutant:
    """Verify End_{Spin(9)}(S_9) = R via Schur's lemma computation."""

    def test_spin9_commutant_dim_is_1(self, gamma_matrices):
        """The commutant of the Spin(9) action on R^16 has dimension 1.

        This confirms End_{Spin(9)}(S_9) = R (real type), which is the
        core of Theorem 1. Benchmark: Lawson-Michelsohn Table I.4.3,
        Cl+(9,0) = M_16(R) irreducible.
        (acceptance test: test-schur-commutant)
        """
        result = compute_spin9_commutant(gamma_matrices)
        assert result['commutant_dim'] == 1, (
            f"Expected commutant dim = 1, got {result['commutant_dim']}")

    def test_commutant_is_identity(self, gamma_matrices):
        """The commutant is spanned by I_{16} (scalar multiples of identity).

        Any Spin(9)-equivariant endomorphism of S_9 is alpha * I for alpha in R.
        (acceptance test: test-equivariant-endomorphism)
        """
        result = compute_spin9_commutant(gamma_matrices)
        assert result['is_scalar_multiple_of_identity'], (
            f"Commutant basis is not a scalar multiple of identity; "
            f"max deviation = {result['max_deviation_from_identity']:.2e}")

    def test_commutant_deviation_from_identity(self, gamma_matrices):
        """The deviation of the commutant basis from I_{16} is at machine precision."""
        result = compute_spin9_commutant(gamma_matrices)
        assert result['max_deviation_from_identity'] < 1e-12, (
            f"Deviation from identity: {result['max_deviation_from_identity']:.2e}")

    def test_no_real_root_of_negative_one(self):
        """No real scalar alpha satisfies alpha^2 = -1.

        This is the trivial final step of Theorem 1: since End_{Spin(9)}(S_9) = R,
        any equivariant J has J = alpha*I, and alpha^2 = -1 has no real solution.
        """
        for alpha in np.linspace(-10, 10, 1000):
            assert alpha ** 2 >= 0, f"Found alpha with alpha^2 < 0: {alpha}"
            assert abs(alpha ** 2 - (-1)) > 0.9, (
                f"Found alpha close to alpha^2 = -1: alpha={alpha}, "
                f"alpha^2={alpha**2}")


# ============================================================================
# Theorem 2: J_u not in spin(9)
# (acceptance tests: test-grade3-nonzero, test-ju-projection-residual,
#  test-no-grade2-Ju)
# ============================================================================

class TestTheorem2GradeSeparation:
    """Verify J_u has nonzero grade-3 and is not in spin(9)."""

    def test_ju_grade3_norm(self, gamma_matrices, J_u):
        """J_u has grade-3 coefficient norm = sqrt(3)/2 = 0.866.

        Regression from Phase 29-01 (Eq. 29-01.3).
        (acceptance test: test-grade3-nonzero)
        """
        grade = compute_grade_decomposition(J_u, gamma_matrices)
        g3_norm_sq = sum(
            c ** 2 for s, c in grade['coefficients'].items() if len(s) == 3
        )
        g3_norm = np.sqrt(g3_norm_sq)
        expected = np.sqrt(3) / 2  # 0.866025...
        assert abs(g3_norm - expected) < 1e-12, (
            f"Grade-3 norm: {g3_norm:.6f}, expected {expected:.6f}")

    def test_ju_grade2_norm(self, gamma_matrices, J_u):
        """J_u has grade-2 coefficient norm = 0.500.

        Regression from Phase 29-01.
        """
        grade = compute_grade_decomposition(J_u, gamma_matrices)
        g2_norm_sq = sum(
            c ** 2 for s, c in grade['coefficients'].items() if len(s) == 2
        )
        g2_norm = np.sqrt(g2_norm_sq)
        assert abs(g2_norm - 0.5) < 1e-12, (
            f"Grade-2 norm: {g2_norm:.6f}, expected 0.500000")

    def test_ju_spin9_projection_residual(self, gamma_matrices, J_u):
        """Least-squares projection of J_u onto spin(9) has nonzero residual.

        The residual measures how far J_u is from the 36-dim spin(9) subspace.
        Since J_u has grade-3 components and spin(9) is grade-2 only, the
        residual should be nonzero.
        (acceptance test: test-ju-projection-residual)
        """
        # Build spin(9) basis
        spin9_gens = []
        for i in range(9):
            for j in range(i + 1, 9):
                spin9_gens.append(gamma_matrices[i] @ gamma_matrices[j])

        spin9_flat = np.array([g.flatten() for g in spin9_gens]).T
        coeffs, _, _, _ = np.linalg.lstsq(spin9_flat, J_u.flatten(), rcond=None)
        residual = np.linalg.norm(J_u.flatten() - spin9_flat @ coeffs)

        # Residual should be positive (J_u not in spin(9))
        assert residual > 0.1, (
            f"J_u projection residual = {residual:.6f}, expected > 0.1")

    def test_grade2_stabilizers_differ_from_ju(self, gamma_matrices, J_u):
        """No grade-2 element gamma_{ij} has stabilizer dim=10 with su(3)+u(1)^2.

        This confirms J_u's stabilizer structure is unique to its grade 2+3
        structure and cannot be replicated by any element of spin(9).
        (acceptance test: test-no-grade2-Ju)
        """
        # Check all 36 gamma_{ij}
        for i in range(9):
            for j in range(i + 1, 9):
                target = gamma_matrices[i] @ gamma_matrices[j]
                stab = compute_grade2_stabilizer(gamma_matrices, target)
                # None should have dim=10 with center=2
                if stab['stabilizer_dim'] == 10 and stab['center_dim'] == 2:
                    pytest.fail(
                        f"gamma_{i}{j} has same stabilizer structure as J_u: "
                        f"dim={stab['stabilizer_dim']}, "
                        f"semisimple={stab['semisimple_dim']}, "
                        f"center={stab['center_dim']}")

    def test_all_grade2_stabilizer_dim_22(self, gamma_matrices):
        """All 36 grade-2 elements gamma_{ij} have stabilizer dim = 22.

        This is much larger than J_u's stabilizer dim = 10, confirming that
        grade-2 complex structures break LESS symmetry than J_u.
        """
        for i in range(9):
            for j in range(i + 1, 9):
                target = gamma_matrices[i] @ gamma_matrices[j]
                stab = compute_grade2_stabilizer(gamma_matrices, target)
                assert stab['stabilizer_dim'] == 22, (
                    f"gamma_{i}{j} stabilizer dim = {stab['stabilizer_dim']}, "
                    f"expected 22")


# ============================================================================
# Theorem 3: Weakest sufficient condition (u in S^6)
# (acceptance tests: test-ju-uniqueness-recheck, test-stabilizer-recheck)
# ============================================================================

class TestTheorem3WeakestCondition:
    """Verify J_u uniqueness and stabilizer from Phase 29-02."""

    def test_ju_uniqueness_regression(self, gamma_matrices, J_u):
        """J_u is isolated in its 8-monomial subspace (tangent dim = 0).

        Regression from Phase 29-02 (Eq. 29-02.2).
        (acceptance test: test-ju-uniqueness-recheck)
        """
        result = test_ju_uniqueness(gamma_matrices, J_u)
        assert result['is_isolated'], (
            f"J_u not isolated: tangent dim = {result['tangent_dim_at_ju']}")
        assert result['monomial_subspace_dim'] == 8

    def test_ju_tangent_dim_0(self, gamma_matrices, J_u):
        """Tangent dim at J_u = 0 (Jacobian is full rank in 8-dim subspace)."""
        result = test_ju_uniqueness(gamma_matrices, J_u)
        assert result['tangent_dim_at_ju'] == 0, (
            f"Tangent dim = {result['tangent_dim_at_ju']}, expected 0")

    def test_stabilizer_dim_regression(self, gamma_matrices, J_u):
        """Stabilizer dim = 10 = su(3) + u(1)^2.

        Regression from Phase 29-02 (Eq. 29-02.3).
        (acceptance test: test-stabilizer-recheck)
        """
        result = compute_gsm_commutant(gamma_matrices, J_u)
        assert result['commutant_dim'] == 10, (
            f"Stabilizer dim = {result['commutant_dim']}, expected 10")
        assert result['semisimple_dim'] == 8, (
            f"Semisimple dim = {result['semisimple_dim']}, expected 8 (su(3))")
        assert result['center_dim'] == 2, (
            f"Center dim = {result['center_dim']}, expected 2 (u(1)^2)")


# ============================================================================
# Phase 29 regression
# ============================================================================

class TestPhase29Regression:
    """Verify Phase 29 tests still pass (subset -- full suite in test_observable_algebra.py)."""

    def test_T_b_count(self, T_matrices):
        """10 Peirce operators."""
        assert len(T_matrices) == 10

    def test_ju_squared(self, J_u):
        """J_u^2 = -I."""
        err = np.max(np.abs(J_u @ J_u + np.eye(16)))
        assert err < ATOL

    def test_ju_antisymmetric(self, J_u):
        """J_u is antisymmetric (J_u^T = -J_u)."""
        err = np.max(np.abs(J_u + J_u.T))
        assert err < ATOL

    def test_clifford_anticommutation(self, gamma_matrices):
        """Verify {gamma_i, gamma_j} = 2*delta_{ij}*I for rescaled generators."""
        for i in range(9):
            for j in range(i, 9):
                ac = gamma_matrices[i] @ gamma_matrices[j] + gamma_matrices[j] @ gamma_matrices[i]
                if i == j:
                    err = np.max(np.abs(ac - 2.0 * np.eye(16)))
                    assert err < ATOL, f"{{gamma_{i}, gamma_{i}}} != 2I: err = {err}"
                else:
                    err = np.max(np.abs(ac))
                    assert err < ATOL, f"{{gamma_{i}, gamma_{j}}} != 0: err = {err}"
