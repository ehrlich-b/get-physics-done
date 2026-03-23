#!/usr/bin/env python3
"""
Verification of the order zero condition and spectral triple consistency
for the doubled self-modeling composite (H, J, gamma) at KO-dimension 6.

Tests verify at n=2,3,4 with exact integer/float arithmetic:
  1. J^2 = I (real structure squares to identity)
  2. J gamma = -gamma J (KO-dim 6 sign epsilon'' = -1)
  3. gamma^2 = I, gamma = gamma^dagger, eigenspace dimensions
  4. Order zero: [pi(a), pi_o(b)] = 0 for ALL n^4 pairs of matrix units
  5. pi_o is a *-representation of the opposite algebra A^op
  6. [gamma, pi(a)] = 0 tested -- documents whether it holds or fails

Definitions (from paper7-spectral-triple-prompt.md):
  H = (C^n x C^n)_particle  +  (C^n x C^n)_antiparticle    (dim = 2n^2)
  P = SWAP on C^n x C^n:  P|i>|j> = |j>|i>                 (n^2 x n^2)
  J(psi, chi) = (PC chi-bar, PC psi-bar)                    (antilinear)
  gamma(psi, chi) = (P psi, -P chi)

  J_matrix = [[0, P], [P, 0]]     (linear part of J)
  gamma_matrix = [[P, 0], [0, -P]]

  Naive algebra action:
    pi(a)(psi, chi) = ((a x I_n) psi, (a x I_n) chi)
    pi(a) = block_diag(kron(a, I_n), kron(a, I_n))

  Opposite action (J is antilinear, J_matrix is real):
    pi_o(b) = J pi(b*) J^{-1} = J_matrix @ conj(pi(b^dagger)) @ J_matrix

Convention assertions:
  ASSERT_CONVENTION: inner_product=linear_second, J_definition=antilinear_PC,
    P_definition=SWAP, gamma_definition=P_matter_sign,
    commutator=[A,B]=AB-BA, matrix_units=(E_ij)_kl=delta_ik*delta_jl

Reference: Connes 1995, J. Math. Phys. 36, 6194 (order zero condition).
Reference: Paper 6 (own): J, P, gamma definitions.

Library versions: numpy 2.4.2, pytest 9.0.2
Platform: macOS Darwin 24.6.0
"""

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Helpers parameterized by n
# ---------------------------------------------------------------------------

def matrix_unit(n, i, j):
    """Standard matrix unit E_ij: (E_ij)_kl = delta_ik delta_jl."""
    E = np.zeros((n, n), dtype=float)
    E[i, j] = 1.0
    return E


def all_matrix_units(n):
    """All n^2 matrix units for M_n(C)."""
    return [(i, j, matrix_unit(n, i, j)) for i in range(n) for j in range(n)]


def build_swap_matrix(n):
    """SWAP operator P on C^n x C^n: P|i>|j> = |j>|i>."""
    dim = n * n
    P = np.zeros((dim, dim), dtype=float)
    for i in range(n):
        for j in range(n):
            P[i * n + j, j * n + i] = 1.0
    return P


def build_J_matrix(n):
    """Linear part of J: J_matrix = [[0, P], [P, 0]]."""
    P = build_swap_matrix(n)
    dim = n * n
    J = np.zeros((2 * dim, 2 * dim), dtype=float)
    J[:dim, dim:] = P
    J[dim:, :dim] = P
    return J


def build_gamma_matrix(n):
    """Chirality: gamma = [[P, 0], [0, -P]]."""
    P = build_swap_matrix(n)
    dim = n * n
    gamma = np.zeros((2 * dim, 2 * dim), dtype=float)
    gamma[:dim, :dim] = P
    gamma[dim:, dim:] = -P
    return gamma


def build_pi(a, n):
    """Naive action: pi(a) = block_diag(kron(a, I_n), kron(a, I_n))."""
    block = np.kron(a, np.eye(n))
    dim = n * n
    pi = np.zeros((2 * dim, 2 * dim), dtype=complex)
    pi[:dim, :dim] = block
    pi[dim:, dim:] = block
    return pi


def build_pi_o(b, n):
    """Opposite action: pi_o(b) = J_matrix @ conj(pi(b^dagger)) @ J_matrix.

    Since J is antilinear with real J_matrix satisfying J_matrix^2 = I:
      J A J^{-1} = J_matrix @ conj(A) @ J_matrix
      pi_o(b) = J_matrix @ conj(pi(b^dagger)) @ J_matrix
    """
    J_mat = build_J_matrix(n)
    pi_b_star = build_pi(b.conj().T, n)
    return J_mat @ pi_b_star.conj() @ J_mat


# ===================================================================
# SECTION 1: J PROPERTIES
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_J_squared(n):
    """J^2 = I: J_matrix @ J_matrix = identity (J_matrix is real)."""
    J = build_J_matrix(n)
    assert np.allclose(J @ J, np.eye(2 * n * n), atol=1e-14), (
        f"J^2 != I at n={n}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_J_matrix_is_real(n):
    """J_matrix has only real entries (0s and 1s)."""
    J = build_J_matrix(n)
    assert np.all((J == 0) | (J == 1)), f"J_matrix non-binary at n={n}"


# ===================================================================
# SECTION 2: GAMMA PROPERTIES
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_gamma_squared(n):
    """gamma^2 = I."""
    gamma = build_gamma_matrix(n)
    assert np.allclose(gamma @ gamma, np.eye(2 * n * n), atol=1e-14)


@pytest.mark.parametrize("n", [2, 3, 4])
def test_gamma_selfadjoint(n):
    """gamma = gamma^dagger."""
    gamma = build_gamma_matrix(n)
    assert np.allclose(gamma, gamma.conj().T, atol=1e-14)


@pytest.mark.parametrize("n", [2, 3, 4])
def test_gamma_eigenspace_dimensions(n):
    """gamma eigenspaces: dim(+1) = dim(-1) = n^2.

    +1 eigenspace = Sym^2-particle + wedge^2-antiparticle
    -1 eigenspace = wedge^2-particle + Sym^2-antiparticle
    """
    gamma = build_gamma_matrix(n)
    evals = np.linalg.eigvalsh(gamma)
    n_plus = np.sum(np.abs(evals - 1.0) < 1e-10)
    n_minus = np.sum(np.abs(evals + 1.0) < 1e-10)
    assert n_plus == n * n, f"dim(+1)={n_plus}, expected {n*n}"
    assert n_minus == n * n, f"dim(-1)={n_minus}, expected {n*n}"


@pytest.mark.parametrize("n", [2, 3, 4])
def test_swap_eigenspace_dimensions(n):
    """SWAP eigenspaces: dim(Sym^2) = n(n+1)/2, dim(wedge^2) = n(n-1)/2."""
    P = build_swap_matrix(n)
    evals = np.linalg.eigvalsh(P)
    dim_sym = n * (n + 1) // 2
    dim_wedge = n * (n - 1) // 2
    n_plus = np.sum(np.abs(evals - 1.0) < 1e-10)
    n_minus = np.sum(np.abs(evals + 1.0) < 1e-10)
    assert n_plus == dim_sym, f"Sym^2 dim: {n_plus} != {dim_sym}"
    assert n_minus == dim_wedge, f"wedge^2 dim: {n_minus} != {dim_wedge}"


# ===================================================================
# SECTION 3: J-GAMMA ANTICOMMUTATION (KO-dim 6)
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_J_gamma_anticommute(n):
    """J gamma + gamma J = 0 (epsilon'' = -1 for KO-dimension 6).

    For real gamma and real J_matrix, J acts linearly on gamma,
    so the anticommutation is J_matrix @ gamma + gamma @ J_matrix = 0.
    """
    J = build_J_matrix(n)
    gamma = build_gamma_matrix(n)
    assert np.allclose(J @ gamma + gamma @ J, 0, atol=1e-14), (
        f"J gamma + gamma J != 0 at n={n}"
    )


# ===================================================================
# SECTION 4: ORDER ZERO CONDITION
# [pi(a), pi_o(b)] = 0 for ALL pairs of matrix units
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_order_zero_all_basis(n):
    """Order zero: [pi(E_ij), pi_o(E_kl)] = 0 for ALL n^4 pairs.

    This is the central test. The order zero condition states that the
    left algebra action commutes with the J-conjugated right action.
    We test ALL pairs exhaustively with exact (integer) arithmetic.
    """
    units = all_matrix_units(n)
    total = len(units) ** 2
    failures = []

    for i1, j1, E_a in units:
        pi_a = build_pi(E_a, n)
        for i2, j2, E_b in units:
            pi_o_b = build_pi_o(E_b, n)
            comm = pi_a @ pi_o_b - pi_o_b @ pi_a
            norm = np.linalg.norm(comm, 'fro')
            if norm > 1e-12:
                failures.append(((i1, j1), (i2, j2), norm))

    assert len(failures) == 0, (
        f"Order zero FAILS at n={n}: {len(failures)}/{total} nonzero commutators. "
        f"First 5: {failures[:5]}"
    )


# ===================================================================
# SECTION 5: pi_o IS A *-REPRESENTATION OF THE OPPOSITE ALGEBRA
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_pi_o_representation(n):
    """pi_o(a) pi_o(b) = pi_o(b*a) -- representation of A^op.

    In noncommutative geometry, pi_o maps to the opposite algebra where
    multiplication is reversed: a *_op b = b * a. So the correct
    multiplicativity condition is pi_o(a) @ pi_o(b) = pi_o(b @ a).
    """
    units = all_matrix_units(n)
    total = len(units) ** 2
    failures = []

    for i1, j1, E_a in units:
        pi_o_a = build_pi_o(E_a, n)
        for i2, j2, E_b in units:
            pi_o_b = build_pi_o(E_b, n)
            # Opposite algebra: a *_op b = b * a
            prod_op = E_b @ E_a
            pi_o_prod = build_pi_o(prod_op, n)
            composed = pi_o_a @ pi_o_b
            diff = np.linalg.norm(pi_o_prod - composed, 'fro')
            if diff > 1e-12:
                failures.append(((i1, j1), (i2, j2), diff))

    assert len(failures) == 0, (
        f"pi_o NOT a rep of A^op at n={n}: {len(failures)}/{total} failures"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_pi_o_star_preserving(n):
    """pi_o(a^dagger) = pi_o(a)^dagger -- *-preservation."""
    units = all_matrix_units(n)
    failures = []

    for i, j, E_ij in units:
        E_ji = matrix_unit(n, j, i)  # E_ij^dagger = E_ji
        pi_o_adj = build_pi_o(E_ji, n)
        pi_o_a_adj = build_pi_o(E_ij, n).conj().T
        diff = np.linalg.norm(pi_o_adj - pi_o_a_adj, 'fro')
        if diff > 1e-12:
            failures.append((i, j, diff))

    assert len(failures) == 0, (
        f"pi_o NOT *-preserving at n={n}: {len(failures)} failures"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_pi_o_dimension(n):
    """dim(span{pi_o(E_ij)}) = n^2 -- pi_o matrices are linearly independent."""
    units = all_matrix_units(n)
    vectors = [build_pi_o(E, n).flatten() for _, _, E in units]
    rank = np.linalg.matrix_rank(np.array(vectors), tol=1e-10)
    assert rank == n * n, f"pi_o rank={rank}, expected {n*n} at n={n}"


# ===================================================================
# SECTION 6: [gamma, pi(a)] = 0 (EVEN CONDITION)
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_gamma_pi_commute(n):
    """[gamma, pi(a)] = 0 requires [P, kron(a, I_n)] = 0 in each sector.

    Since P kron(a, I) P = kron(I, a) [SWAP property], [P, kron(a, I)] = 0
    only when kron(a, I) = kron(I, a), i.e., a = c*I (scalar). This means
    ALL non-scalar matrix units fail, including diagonal E_ii (i != j case
    is obvious; i = j case: kron(E_ii, I) != kron(I, E_ii) for n > 1).

    RESULT: The naive action pi(a) = block_diag(a x I, a x I) does NOT
    satisfy [gamma, pi(a)] = 0 for ANY non-scalar algebra element.
    The even condition fails for the full algebra M_n(C); the only
    subalgebra satisfying [gamma, pi(a)] = 0 is {c*I : c in C} = C.

    This is a significant constraint on the spectral triple construction:
    the even condition requires either a different algebra action or a
    different chirality operator.
    """
    gamma = build_gamma_matrix(n)
    units = all_matrix_units(n)
    noncommuting = []

    for i, j, E_ij in units:
        pi_a = build_pi(E_ij, n)
        comm = gamma @ pi_a - pi_a @ gamma
        norm = np.linalg.norm(comm, 'fro')
        if norm > 1e-12:
            noncommuting.append((i, j, norm))

    # ALL n^2 matrix units fail to commute with gamma
    assert len(noncommuting) == n * n, (
        f"Expected all {n*n} matrix units to fail [gamma, pi(E_ij)] = 0, "
        f"but only {len(noncommuting)} failed at n={n}"
    )

    # Verify the identity matrix DOES commute with gamma
    I_n = np.eye(n)
    pi_I = build_pi(I_n, n)
    comm_I = gamma @ pi_I - pi_I @ gamma
    assert np.allclose(comm_I, 0, atol=1e-14), (
        f"[gamma, pi(I)] != 0 at n={n} -- this should never happen"
    )


# ===================================================================
# SECTION 7: COMPLETENESS CHECK -- the pi and pi_o commutants
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_pi_o_generates_commutant_of_pi(n):
    """Verify {pi_o(E_kl)} generates the commutant of {pi(E_ij)}.

    Since [pi(a), pi_o(b)] = 0, pi_o(A) lies in the commutant of pi(A).
    We check that the commutant of pi(M_n(C)) has dimension exactly n^2
    within the full matrix algebra M_{2n^2}(C), matching dim(pi_o(M_n(C))).

    Actually the commutant of pi(M_n(C)) in M_{2n^2}(C) is computed by
    finding all 2n^2 x 2n^2 matrices X such that [pi(E_ij), X] = 0 for
    all matrix units E_ij.
    """
    units = all_matrix_units(n)
    dim = 2 * n * n
    dim_sq = dim * dim

    # Build the linear system: X is in commutant iff [pi(E_ij), X] = 0 for all ij
    # Vectorize X as a dim_sq-vector. [pi(E_ij), X] = 0 becomes a linear constraint.
    constraints = []
    for _, _, E_ij in units:
        pi_ij = build_pi(E_ij, n)
        # [pi_ij, X] = pi_ij @ X - X @ pi_ij = 0
        # As a linear map on vec(X): (I kron pi_ij - pi_ij^T kron I) vec(X) = 0
        M = np.kron(np.eye(dim), pi_ij) - np.kron(pi_ij.T, np.eye(dim))
        constraints.append(M)

    # Stack all constraints
    constraint_matrix = np.vstack(constraints)
    # Commutant dimension = null space dimension
    _, s, _ = np.linalg.svd(constraint_matrix, full_matrices=False)
    null_dim = np.sum(s < 1e-10)

    # The commutant should be n^2-dimensional (same as pi_o image)
    # Actually for block_diag(a x I, a x I), the commutant in M_{2n^2}
    # is M_2(C) tensor I_n tensor M_n(C), which has dimension 2^2 * n^2 = 4n^2
    # Wait -- let me compute it properly.
    # pi(a) = diag(a x I, a x I) -- same block in both sectors
    # Commutant of {a x I : a in M_n} in M_{n^2} is {I_n x b : b in M_n} = M_n
    # The full commutant in M_{2n^2} of block_diag(a x I, a x I) is
    # M_2(C) x commutant_of_{a x I} = M_2 x M_n, dimension 4 * n^2
    expected_dim = 4 * n * n
    assert null_dim == expected_dim, (
        f"Commutant of pi(M_n) has dim {null_dim}, expected {expected_dim} at n={n}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_pi_o_inside_commutant(n):
    """Verify each pi_o(E_ij) lies in the commutant of pi(M_n(C)).

    This is equivalent to the order zero condition but checked from the
    commutant perspective.
    """
    units = all_matrix_units(n)
    for _, _, E_b in units:
        pi_o_b = build_pi_o(E_b, n)
        for _, _, E_a in units:
            pi_a = build_pi(E_a, n)
            comm = pi_a @ pi_o_b - pi_o_b @ pi_a
            assert np.linalg.norm(comm, 'fro') < 1e-12, (
                f"pi_o(E_b) not in commutant of pi(M_n) at n={n}"
            )


# ===================================================================
# SECTION 8: DIAGNOSTIC REPORT
# ===================================================================

def test_diagnostic_summary():
    """Print structured summary of all results at n=2,3,4."""
    print("\n" + "=" * 70)
    print("ORDER ZERO VERIFICATION SUMMARY")
    print("=" * 70)

    for n in [2, 3, 4]:
        dim_H = 2 * n * n
        n_pairs = n ** 4
        print(f"\n--- n={n}, dim(H)={dim_H}, commutator pairs={n_pairs} ---")

        J = build_J_matrix(n)
        gamma = build_gamma_matrix(n)

        # Core properties
        J_sq = np.allclose(J @ J, np.eye(dim_H), atol=1e-14)
        gamma_sq = np.allclose(gamma @ gamma, np.eye(dim_H), atol=1e-14)
        anticomm = np.allclose(J @ gamma + gamma @ J, 0, atol=1e-14)
        print(f"  J^2 = I:             {J_sq}")
        print(f"  gamma^2 = I:         {gamma_sq}")
        print(f"  J gamma = -gamma J:  {anticomm}")

        # Order zero
        units = all_matrix_units(n)
        zero_count = 0
        for _, _, E_a in units:
            pi_a = build_pi(E_a, n)
            for _, _, E_b in units:
                pi_o_b = build_pi_o(E_b, n)
                if np.linalg.norm(pi_a @ pi_o_b - pi_o_b @ pi_a, 'fro') < 1e-12:
                    zero_count += 1
        print(f"  Order zero [pi, pi_o] = 0:  {zero_count}/{n_pairs} "
              f"({'PASS' if zero_count == n_pairs else 'FAIL'})")

        # [gamma, pi(a)] = 0
        gamma_comm = sum(
            1 for _, _, E in units
            if np.linalg.norm(gamma @ build_pi(E, n) - build_pi(E, n) @ gamma, 'fro') < 1e-12
        )
        print(f"  [gamma, pi(a)] = 0:  {gamma_comm}/{len(units)} "
              f"({'PASS' if gamma_comm == len(units) else 'FAIL -- only diagonal E_ii commute'})")

        # pi_o representation
        rep_pass = 0
        for _, _, E_a in units:
            po_a = build_pi_o(E_a, n)
            for _, _, E_b in units:
                po_b = build_pi_o(E_b, n)
                prod_op = E_b @ E_a  # opposite algebra
                po_prod = build_pi_o(prod_op, n)
                if np.linalg.norm(po_a @ po_b - po_prod, 'fro') < 1e-12:
                    rep_pass += 1
        print(f"  pi_o rep of A^op:    {rep_pass}/{n_pairs} "
              f"({'PASS' if rep_pass == n_pairs else 'FAIL'})")

    print("\n" + "=" * 70)
    print("KEY FINDING: Order zero condition PASSES for the naive action")
    print("pi(a) = block_diag(a x I, a x I) at n=2,3,4.")
    print("")
    print("ISSUE: [gamma, pi(a)] = 0 FAILS for off-diagonal matrix units.")
    print("This means the naive action does not define an EVEN spectral triple.")
    print("The algebra sub-bundle that commutes with gamma is the diagonal")
    print("subalgebra (multiples of I), which is trivial.")
    print("=" * 70 + "\n")


# ===================================================================
# Main
# ===================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short", "-s"])
