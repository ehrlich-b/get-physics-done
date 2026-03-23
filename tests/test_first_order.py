#!/usr/bin/env python3
"""
Verification of first-order condition [[D, pi(a)], pi_o(b)] = 0
for Barrett-form Dirac operator D_K with K in M_n(R)^sym.

Tests verify:
  A. Double commutator zero for all basis element pairs (n=2,3,4)
  B. Constraint matrix null space dimension = n^2 (A_F = full algebra)
  C. *-subalgebra closure of A_F
  D. K-independence of A_F dimension
  E. Limiting cases K=0 and K=I

Convention assertions:
  ASSERT_CONVENTION: inner_product=linear_second, J_definition=antilinear_PC,
    P_definition=SWAP, gamma_definition=diag(P,-P),
    ko_dimension=6, barrett_iso=v_tensor_w_to_vwT,
    commutator=[A,B]=AB-BA, jordan_product=K*X=(1/2)(KX+XK)

References:
  - Barrett 2015, arXiv:1502.05383
  - van Suijlekom 2024, Ch. 8-11
  - derivations/09-first-order-condition.md
  - Phase 13 (pi, pi_o), Phase 14 (Barrett-form D)

Library versions: numpy 2.4.2, pytest 9.0.2
Platform: macOS Darwin 24.6.0
Random seed: 20260323 (fixed for reproducibility)
"""

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Infrastructure: reused from test_dirac_moduli.py (Phase 13-14 patterns)
# ---------------------------------------------------------------------------

def build_swap_matrix(n):
    """SWAP operator P on C^n x C^n: P|i>|j> = |j>|i>."""
    dim = n * n
    P = np.zeros((dim, dim), dtype=float)
    for i in range(n):
        for j in range(n):
            P[i * n + j, j * n + i] = 1.0
    return P


def build_J_matrix(n):
    """Linear part of J on H = C^{2n^2}: J_matrix = [[0, P], [P, 0]]."""
    P = build_swap_matrix(n)
    dim = n * n
    J = np.zeros((2 * dim, 2 * dim), dtype=float)
    J[:dim, dim:] = P
    J[dim:, :dim] = P
    return J


def build_gamma_matrix(n):
    """Chirality: gamma = [[P, 0], [0, -P]] on H = C^{2n^2}."""
    P = build_swap_matrix(n)
    dim = n * n
    gamma = np.zeros((2 * dim, 2 * dim), dtype=float)
    gamma[:dim, :dim] = P
    gamma[dim:, dim:] = -P
    return gamma


def build_barrett_D(n, K):
    """Build Barrett-form D on the doubled space.

    D(X_p, X_ap) = (D_1(X_ap), D_1(X_p)) where D_1(X) = KX + XK^*.
    For K real symmetric, K^* = K, so D_1(X) = KX + XK.

    Parameters:
        n: algebra dimension
        K: n x n complex matrix (should be real symmetric for Barrett-form)
    Returns:
        D: 2n^2 x 2n^2 complex matrix
    """
    dim = n * n
    I_n = np.eye(n, dtype=complex)
    # D_1(X) = KX + XK^* as linear map on vec(X)
    # vec(KX) = (I kron K) vec(X)
    # vec(XK^*) = (K^{*T} kron I) vec(X) = (conj(K)^T kron I) vec(X)
    D1 = np.kron(I_n, K) + np.kron(np.conj(K).T, I_n)

    # sigma_1 structure: D(X_p, X_ap) = (D_1(X_ap), D_1(X_p))
    D = np.zeros((2 * dim, 2 * dim), dtype=complex)
    D[:dim, dim:] = D1   # particle row, antiparticle col
    D[dim:, :dim] = D1   # antiparticle row, particle col
    return D


def build_pi_a(n, a):
    """Build pi(a) on doubled space: pi(a)(X_p, X_ap) = (aX_p, aX_ap).

    Under Barrett iso, left multiplication L_a: vec(aX) = (I kron a) vec(X).

    Returns: 2n^2 x 2n^2 complex matrix.
    """
    dim = n * n
    I_n = np.eye(n, dtype=complex)
    La = np.kron(I_n, a)  # left multiplication by a

    pi = np.zeros((2 * dim, 2 * dim), dtype=complex)
    pi[:dim, :dim] = La
    pi[dim:, dim:] = La
    return pi


def build_pi_o_b(n, b):
    """Build pi_o(b) on doubled space: pi_o(b)(X_p, X_ap) = (X_p b, X_ap b).

    Under Barrett iso, right multiplication R_b: vec(Xb) = (b^T kron I) vec(X).

    Returns: 2n^2 x 2n^2 complex matrix.
    """
    dim = n * n
    I_n = np.eye(n, dtype=complex)
    Rb = np.kron(b.T, I_n)  # right multiplication by b

    pi_o = np.zeros((2 * dim, 2 * dim), dtype=complex)
    pi_o[:dim, :dim] = Rb
    pi_o[dim:, dim:] = Rb
    return pi_o


def matrix_unit(n, i, j):
    """Standard basis element E_{ij} of M_n(C)."""
    E = np.zeros((n, n), dtype=complex)
    E[i, j] = 1.0
    return E


def random_symmetric_real(n, rng):
    """Generate a random real symmetric n x n matrix."""
    A = rng.standard_normal((n, n))
    return (A + A.T) / 2


def double_commutator(D, pi_a, pi_o_b):
    """Compute [[D, pi(a)], pi_o(b)]."""
    comm1 = D @ pi_a - pi_a @ D
    comm2 = comm1 @ pi_o_b - pi_o_b @ comm1
    return comm2


# ---------------------------------------------------------------------------
# A. Double commutator zero tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 3, 4])
def test_double_comm_zero_barrett_diag(n):
    """[[D_K, L_a], R_b] = 0 for K = diag(1,0,...,0) and all basis a, b."""
    K = np.zeros((n, n), dtype=float)
    K[0, 0] = 1.0
    D = build_barrett_D(n, K)

    for i in range(n):
        for j in range(n):
            a = matrix_unit(n, i, j)
            pi_a = build_pi_a(n, a)
            for k in range(n):
                for l in range(n):
                    b = matrix_unit(n, k, l)
                    pi_o_b = build_pi_o_b(n, b)
                    dc = double_commutator(D, pi_a, pi_o_b)
                    err = np.linalg.norm(dc, 'fro')
                    assert err < 1e-12, (
                        f"n={n}, K=diag, a=E_{i}{j}, b=E_{k}{l}: "
                        f"||[[D,L_a],R_b]|| = {err}"
                    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_double_comm_zero_barrett_identity(n):
    """[[D_K, L_a], R_b] = 0 for K = I and all basis a, b."""
    K = np.eye(n, dtype=float)
    D = build_barrett_D(n, K)

    for i in range(n):
        for j in range(n):
            a = matrix_unit(n, i, j)
            pi_a = build_pi_a(n, a)
            for k in range(n):
                for l in range(n):
                    b = matrix_unit(n, k, l)
                    pi_o_b = build_pi_o_b(n, b)
                    dc = double_commutator(D, pi_a, pi_o_b)
                    err = np.linalg.norm(dc, 'fro')
                    assert err < 1e-12, (
                        f"n={n}, K=I, a=E_{i}{j}, b=E_{k}{l}: "
                        f"||[[D,L_a],R_b]|| = {err}"
                    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_double_comm_zero_barrett_random(n):
    """[[D_K, L_a], R_b] = 0 for random symmetric K and all basis a, b."""
    rng = np.random.default_rng(20260323)
    K = random_symmetric_real(n, rng)
    D = build_barrett_D(n, K)

    for i in range(n):
        for j in range(n):
            a = matrix_unit(n, i, j)
            pi_a = build_pi_a(n, a)
            for k in range(n):
                for l in range(n):
                    b = matrix_unit(n, k, l)
                    pi_o_b = build_pi_o_b(n, b)
                    dc = double_commutator(D, pi_a, pi_o_b)
                    err = np.linalg.norm(dc, 'fro')
                    assert err < 1e-12, (
                        f"n={n}, K=random, a=E_{i}{j}, b=E_{k}{l}: "
                        f"||[[D,L_a],R_b]|| = {err}"
                    )


# ---------------------------------------------------------------------------
# B. Constraint matrix null space tests (A_F dimension)
# ---------------------------------------------------------------------------

def build_first_order_constraint_matrix(n, K):
    """Build the constraint matrix for the first-order condition.

    For candidate a = sum_{p,q} alpha_{pq} E_{pq} (vectorized as C^{n^2}),
    the first-order condition [[D_K, L_a], R_{E_{kl}}] = 0 for all k, l
    gives a linear system in the n^2 unknowns alpha_{pq}.

    Each choice of (k, l) gives an n x n matrix equation (n^2 scalar eqns).
    Total constraints: n^2 (choices of b) * n^2 (output components) = n^4.
    Unknowns: n^2 (components of a).

    Returns: constraint matrix C of shape (n^4, n^2) such that C @ alpha = 0
    iff a = sum alpha_{pq} E_{pq} satisfies [[D_K, L_a], R_b] = 0 for all b.
    """
    D = build_barrett_D(n, K)
    dim = n * n

    # For each basis element a = E_{pq}, compute [[D, L_{E_{pq}}], R_{E_{kl}}]
    # for all (k,l). This gives a 2n^2 x 2n^2 matrix for each (pq, kl).
    # We vectorize the output and stack.

    rows = []
    for k in range(n):
        for l in range(n):
            b = matrix_unit(n, k, l)
            pi_o_b = build_pi_o_b(n, b)
            # For each pq, compute [[D, L_{E_{pq}}], R_b]
            # acting on a test vector. Since we want to check the operator
            # is zero, we can extract any column. Use all of them by
            # computing the full operator.
            row_block = []
            for p in range(n):
                for q in range(n):
                    a = matrix_unit(n, p, q)
                    pi_a = build_pi_a(n, a)
                    dc = double_commutator(D, pi_a, pi_o_b)
                    # dc is 2n^2 x 2n^2. For [[D,L_a],R_b] = 0, the entire
                    # operator must be zero. Take its Frobenius norm as a
                    # scalar constraint, but for the null space we need
                    # the LINEAR system.
                    #
                    # Actually: [[D, L_a], R_b] is linear in a. So for
                    # a = sum alpha_{pq} E_{pq}, we have
                    # [[D, L_a], R_b] = sum alpha_{pq} [[D, L_{E_{pq}}], R_b].
                    # For this to be zero AS AN OPERATOR, every matrix element
                    # of the sum must be zero. So we vectorize the operator.
                    row_block.append(dc.ravel())
            # row_block is a list of n^2 column vectors (each of length (2n^2)^2)
            # Stack as columns -> matrix of shape ((2n^2)^2, n^2)
            block = np.column_stack(row_block)
            rows.append(block)

    # Stack all (k,l) blocks vertically
    C = np.vstack(rows)
    return C


@pytest.mark.parametrize("n", [2, 3, 4])
def test_af_dimension_barrett_diag(n):
    """A_F dimension = n^2 for K = diag(1,0,...,0)."""
    K = np.zeros((n, n), dtype=float)
    K[0, 0] = 1.0
    C = build_first_order_constraint_matrix(n, K)
    sv = np.linalg.svd(C, compute_uv=False)
    null_dim = np.sum(sv < 1e-10)
    assert null_dim == n * n, (
        f"n={n}, K=diag: null space dim = {null_dim}, expected {n*n}. "
        f"Smallest SVs: {sv[-5:]}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_af_dimension_barrett_identity(n):
    """A_F dimension = n^2 for K = I."""
    K = np.eye(n, dtype=float)
    C = build_first_order_constraint_matrix(n, K)
    sv = np.linalg.svd(C, compute_uv=False)
    null_dim = np.sum(sv < 1e-10)
    assert null_dim == n * n, (
        f"n={n}, K=I: null space dim = {null_dim}, expected {n*n}. "
        f"Smallest SVs: {sv[-5:]}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_af_dimension_barrett_random(n):
    """A_F dimension = n^2 for random symmetric K."""
    rng = np.random.default_rng(20260323)
    K = random_symmetric_real(n, rng)
    C = build_first_order_constraint_matrix(n, K)
    sv = np.linalg.svd(C, compute_uv=False)
    null_dim = np.sum(sv < 1e-10)
    assert null_dim == n * n, (
        f"n={n}, K=random: null space dim = {null_dim}, expected {n*n}. "
        f"Smallest SVs: {sv[-5:]}"
    )


# ---------------------------------------------------------------------------
# C. *-subalgebra closure tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 3, 4])
def test_subalgebra_closure_product(n):
    """A_F is closed under matrix multiplication."""
    rng = np.random.default_rng(20260323 + n)
    K = random_symmetric_real(n, rng)
    D = build_barrett_D(n, K)

    # Take 3 random elements a, b in M_n(C)
    for _ in range(3):
        a = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        b_mat = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        ab = a @ b_mat  # product

        # Verify [[D, L_{ab}], R_c] = 0 for random c
        c = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        pi_ab = build_pi_a(n, ab)
        pi_o_c = build_pi_o_b(n, c)
        dc = double_commutator(D, pi_ab, pi_o_c)
        err = np.linalg.norm(dc, 'fro')
        assert err < 1e-10, (
            f"n={n}: product closure failed, ||[[D,L_{{ab}},R_c]]|| = {err}"
        )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_subalgebra_closure_adjoint(n):
    """A_F is closed under adjoint (dagger)."""
    rng = np.random.default_rng(20260323 + n + 100)
    K = random_symmetric_real(n, rng)
    D = build_barrett_D(n, K)

    for _ in range(3):
        a = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        a_dag = a.conj().T

        c = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        pi_a_dag = build_pi_a(n, a_dag)
        pi_o_c = build_pi_o_b(n, c)
        dc = double_commutator(D, pi_a_dag, pi_o_c)
        err = np.linalg.norm(dc, 'fro')
        assert err < 1e-10, (
            f"n={n}: adjoint closure failed, ||[[D,L_{{a^dag}},R_c]]|| = {err}"
        )


# ---------------------------------------------------------------------------
# D. K-independence tests
# ---------------------------------------------------------------------------

def test_af_independent_of_k():
    """dim(A_F) = n^2 for 10 random symmetric K at n=2."""
    n = 2
    rng = np.random.default_rng(20260323)
    for trial in range(10):
        K = random_symmetric_real(n, rng)
        C = build_first_order_constraint_matrix(n, K)
        sv = np.linalg.svd(C, compute_uv=False)
        null_dim = np.sum(sv < 1e-10)
        assert null_dim == n * n, (
            f"Trial {trial}: K={K}, null space dim = {null_dim}, expected {n*n}"
        )


# ---------------------------------------------------------------------------
# E. Limiting case tests
# ---------------------------------------------------------------------------

def test_k_zero():
    """K = 0: D = 0, first-order condition is vacuous."""
    n = 2
    K = np.zeros((n, n), dtype=float)
    D = build_barrett_D(n, K)

    # D should be zero
    assert np.linalg.norm(D, 'fro') < 1e-15, "D should be zero for K=0"

    # Double commutator trivially zero
    for i in range(n):
        for j in range(n):
            a = matrix_unit(n, i, j)
            b = matrix_unit(n, (i + 1) % n, j)
            pi_a = build_pi_a(n, a)
            pi_o_b = build_pi_o_b(n, b)
            dc = double_commutator(D, pi_a, pi_o_b)
            assert np.linalg.norm(dc, 'fro') < 1e-15


def test_k_identity():
    """K = I: [K, a] = 0 for all a, so [D, L_a] = 0."""
    n = 2
    K = np.eye(n, dtype=float)
    D = build_barrett_D(n, K)

    # Check [D, L_a] = 0 for all basis a
    for i in range(n):
        for j in range(n):
            a = matrix_unit(n, i, j)
            pi_a = build_pi_a(n, a)
            comm = D @ pi_a - pi_a @ D
            err = np.linalg.norm(comm, 'fro')
            assert err < 1e-12, (
                f"K=I: [D, L_{{E_{i}{j}}}] should be zero, "
                f"got norm {err}"
            )


def test_k_identity_commutator_structure():
    """K = I: verify [K, E_{ij}] = 0 for all i, j."""
    n = 3
    K = np.eye(n, dtype=float)
    for i in range(n):
        for j in range(n):
            E = matrix_unit(n, i, j)
            comm = K @ E - E @ K
            assert np.linalg.norm(comm, 'fro') < 1e-15, (
                f"[I, E_{i}{j}] should be zero"
            )


# ---------------------------------------------------------------------------
# F. Analytical intermediate result: [D_1, L_a] = L_{[K,a]}
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 3, 4])
def test_first_commutator_is_left_mult(n):
    """Verify [D_1, L_a] = L_{[K,a]} as operators on C^{n^2}."""
    rng = np.random.default_rng(20260323 + 200 + n)
    K = random_symmetric_real(n, rng)

    I_n = np.eye(n, dtype=complex)
    D1 = np.kron(I_n, K) + np.kron(K.T, I_n)  # K real sym: K^* = K, K^{*T} = K^T = K

    for i in range(n):
        for j in range(n):
            a = matrix_unit(n, i, j)
            La = np.kron(I_n, a)
            comm_Ka = K @ a - a @ K  # [K, a]
            L_comm = np.kron(I_n, comm_Ka)  # L_{[K,a]}

            # [D_1, L_a] = D_1 L_a - L_a D_1
            actual = D1 @ La - La @ D1
            err = np.linalg.norm(actual - L_comm, 'fro')
            assert err < 1e-12, (
                f"n={n}, a=E_{i}{j}: [D_1, L_a] != L_{{[K,a]}}, err={err}"
            )


# ---------------------------------------------------------------------------
# G. Barrett-form D still satisfies all 3 axiom constraints
#    (cross-check from Phase 14)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 3, 4])
def test_barrett_d_satisfies_axioms(n):
    """Barrett-form D with random symmetric K passes D*=D, Dgamma=-gammaD, JDJ=D."""
    rng = np.random.default_rng(20260323 + 300 + n)
    K = random_symmetric_real(n, rng)
    D = build_barrett_D(n, K)
    gamma = build_gamma_matrix(n)
    J_mat = build_J_matrix(n)

    # D = D^dag
    sa_err = np.linalg.norm(D - D.conj().T, 'fro')
    assert sa_err < 1e-12, f"D not self-adjoint: err={sa_err}"

    # D gamma + gamma D = 0
    anticomm = D @ gamma + gamma @ D
    gamma_err = np.linalg.norm(anticomm, 'fro')
    assert gamma_err < 1e-12, f"{{D, gamma}} != 0: err={gamma_err}"

    # J D J = D (antilinear: J_mat @ conj(D) @ J_mat)
    JDJ = J_mat @ np.conj(D) @ J_mat
    j_err = np.linalg.norm(JDJ - D, 'fro')
    assert j_err < 1e-12, f"JDJ != D: err={j_err}"


# ===========================================================================
# H. General D from full moduli space -- Plan 15-02
# ===========================================================================
# Import moduli space basis from test_dirac_moduli
import importlib
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from test_dirac_moduli import build_moduli_basis


def build_general_D(n, rng):
    """Build a random D from the full n^2(n^2+1)-dim moduli space."""
    basis = build_moduli_basis(n)
    coeffs = rng.standard_normal(len(basis))
    return sum(c * B for c, B in zip(coeffs, basis))


def build_first_order_constraint_general(n, D):
    """Build constraint matrix for first-order condition with arbitrary D.

    Returns matrix C such that C @ alpha = 0 iff a = sum alpha_{pq} E_{pq}
    satisfies [[D, L_a], R_b] = 0 for all b.
    """
    dim = n * n
    rows = []
    for k in range(n):
        for l in range(n):
            b = matrix_unit(n, k, l)
            pi_o_b = build_pi_o_b(n, b)
            row_block = []
            for p in range(n):
                for q in range(n):
                    a = matrix_unit(n, p, q)
                    pi_a = build_pi_a(n, a)
                    dc = double_commutator(D, pi_a, pi_o_b)
                    row_block.append(dc.ravel())
            block = np.column_stack(row_block)
            rows.append(block)
    C = np.vstack(rows)
    return C


def compute_af_dim(n, D, tol=1e-10):
    """Compute dim(A_F) for given D via constraint matrix null space."""
    C = build_first_order_constraint_general(n, D)
    sv = np.linalg.svd(C, compute_uv=False)
    return int(np.sum(sv < tol))


# ---------------------------------------------------------------------------
# H1. General D gives dim(A_F) = 1 at n=2
# ---------------------------------------------------------------------------

def test_general_d_af_dim_n2():
    """For 20 random D from full moduli at n=2, dim(A_F) = 1."""
    n = 2
    rng = np.random.default_rng(42)
    for trial in range(20):
        D = build_general_D(n, rng)
        af_dim = compute_af_dim(n, D)
        assert af_dim == 1, (
            f"n=2, trial {trial}: dim(A_F) = {af_dim}, expected 1"
        )


def test_general_d_af_dim_n3():
    """For 10 random D from full moduli at n=3, dim(A_F) = 1."""
    n = 3
    rng = np.random.default_rng(42)
    for trial in range(10):
        D = build_general_D(n, rng)
        af_dim = compute_af_dim(n, D)
        assert af_dim == 1, (
            f"n=3, trial {trial}: dim(A_F) = {af_dim}, expected 1"
        )


def test_general_d_af_dim_n4():
    """For 10 random D from full moduli at n=4, dim(A_F) = 1."""
    n = 4
    rng = np.random.default_rng(42)
    for trial in range(10):
        D = build_general_D(n, rng)
        af_dim = compute_af_dim(n, D)
        assert af_dim == 1, (
            f"n=4, trial {trial}: dim(A_F) = {af_dim}, expected 1"
        )


# ---------------------------------------------------------------------------
# H2. Barrett D from full moduli gives dim(A_F) = n^2 (consistency)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 3, 4])
def test_barrett_d_af_full_algebra_general_code(n):
    """Barrett D gives dim(A_F) = n^2 using the general constraint code."""
    rng = np.random.default_rng(20260323 + 500 + n)
    K = random_symmetric_real(n, rng)
    D = build_barrett_D(n, K)
    af_dim = compute_af_dim(n, D)
    assert af_dim == n * n, (
        f"n={n}, Barrett D: dim(A_F) = {af_dim}, expected {n*n}"
    )


# ---------------------------------------------------------------------------
# H3. Null space is C*I for general D
# ---------------------------------------------------------------------------

def test_general_d_null_space_is_identity():
    """The 1-dim null space for general D is spanned by the identity."""
    n = 2
    rng = np.random.default_rng(42)
    D = build_general_D(n, rng)
    C = build_first_order_constraint_general(n, D)
    U, sv, Vh = np.linalg.svd(C)
    null_mask = sv < 1e-10
    null_dim = int(np.sum(null_mask))
    assert null_dim == 1

    # The null vector is the last row of Vh
    null_vec = Vh[-1, :]
    a_mat = null_vec.reshape((n, n))

    # Check proportional to identity
    off_diag = a_mat - a_mat[0, 0] * np.eye(n)
    err = np.linalg.norm(off_diag, 'fro') / np.linalg.norm(a_mat, 'fro')
    assert err < 1e-10, (
        f"Null space not proportional to I: relative error {err:.2e}"
    )


# ---------------------------------------------------------------------------
# H4. SVD tolerance stability
# ---------------------------------------------------------------------------

def test_svd_tolerance_stability():
    """dim(A_F) = 1 is stable under SVD threshold variation."""
    n = 2
    rng = np.random.default_rng(42)
    D = build_general_D(n, rng)
    for tol in [1e-8, 1e-10, 1e-12]:
        af_dim = compute_af_dim(n, D, tol=tol)
        assert af_dim == 1, (
            f"n=2, tol={tol:.0e}: dim(A_F) = {af_dim}, expected 1"
        )


# ---------------------------------------------------------------------------
# H5. Barrett mixing: any non-Barrett perturbation drops A_F to C
# ---------------------------------------------------------------------------

def test_barrett_mixing_drops_af():
    """Adding epsilon * (random D) to Barrett D drops dim(A_F) from n^2 to 1."""
    n = 2
    rng = np.random.default_rng(42)
    K = random_symmetric_real(n, rng)
    D_barrett = build_barrett_D(n, K)

    # Pure Barrett: dim(A_F) = 4
    assert compute_af_dim(n, D_barrett) == n * n

    # With perturbation: dim(A_F) = 1
    D_rand = build_general_D(n, rng)
    for eps in [0.01, 0.1, 1.0]:
        D_mixed = D_barrett + eps * D_rand
        af_dim = compute_af_dim(n, D_mixed)
        assert af_dim == 1, (
            f"eps={eps}: dim(A_F) = {af_dim}, expected 1"
        )


# ---------------------------------------------------------------------------
# H6. Barrett vs non-Barrett comparison test
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 3, 4])
def test_barrett_vs_general_d(n):
    """Compare dim(A_F) for Barrett D vs general D at each n."""
    rng = np.random.default_rng(20260323 + 600 + n)

    # Barrett: expect n^2
    for _ in range(5):
        K = random_symmetric_real(n, rng)
        D_b = build_barrett_D(n, K)
        assert compute_af_dim(n, D_b) == n * n, (
            f"n={n}: Barrett D gives wrong dim(A_F)"
        )

    # General: expect 1
    for _ in range(5):
        D_g = build_general_D(n, rng)
        assert compute_af_dim(n, D_g) == 1, (
            f"n={n}: General D gives wrong dim(A_F)"
        )


# ===========================================================================
# I. Phase synthesis tests -- Plan 15-02 Task 2
# ===========================================================================

def test_synthesis_table():
    """Generate and verify the n vs dim(A_F) synthesis table."""
    rng = np.random.default_rng(20260323 + 700)
    results = {}
    for n in [2, 3, 4]:
        # Barrett
        K = random_symmetric_real(n, rng)
        D_b = build_barrett_D(n, K)
        af_barrett = compute_af_dim(n, D_b)

        # General
        D_g = build_general_D(n, rng)
        af_general = compute_af_dim(n, D_g)

        results[n] = {
            'moduli_dim': n * n * (n * n + 1),
            'barrett_dim': n * (n + 1) // 2,
            'af_barrett': af_barrett,
            'af_general': af_general,
        }

    # Verify table entries
    for n in [2, 3, 4]:
        r = results[n]
        assert r['moduli_dim'] == n * n * (n * n + 1)
        assert r['barrett_dim'] == n * (n + 1) // 2
        assert r['af_barrett'] == n * n, f"n={n}: Barrett af={r['af_barrett']}"
        assert r['af_general'] == 1, f"n={n}: General af={r['af_general']}"


def test_af_is_star_subalgebra_general_d():
    """A_F = C*I is a *-subalgebra: closed under product and adjoint."""
    n = 2
    rng = np.random.default_rng(42)
    D = build_general_D(n, rng)

    # a = alpha * I for various alpha
    for alpha in [1.0 + 0j, 1j, 2.0 + 3j]:
        a = alpha * np.eye(n, dtype=complex)
        pi_a = build_pi_a(n, a)
        for k in range(n):
            for l in range(n):
                b = matrix_unit(n, k, l)
                pi_o_b = build_pi_o_b(n, b)
                dc = double_commutator(D, pi_a, pi_o_b)
                err = np.linalg.norm(dc, 'fro')
                assert err < 1e-12, (
                    f"alpha={alpha}, b=E_{k}{l}: ||dc|| = {err}"
                )


def test_non_identity_violates_first_order_general_d():
    """For general D, a = E_{01} (non-scalar) violates first-order condition."""
    n = 2
    rng = np.random.default_rng(42)
    D = build_general_D(n, rng)

    a = matrix_unit(n, 0, 1)  # E_{01}, not a scalar
    pi_a = build_pi_a(n, a)

    max_err = 0.0
    for k in range(n):
        for l in range(n):
            b = matrix_unit(n, k, l)
            pi_o_b = build_pi_o_b(n, b)
            dc = double_commutator(D, pi_a, pi_o_b)
            err = np.linalg.norm(dc, 'fro')
            max_err = max(max_err, err)

    assert max_err > 0.1, (
        f"E_01 should violate first-order for general D, "
        f"but max ||dc|| = {max_err:.4f}"
    )


def test_case_consistency():
    """Verify characterization is internally consistent at all n."""
    rng = np.random.default_rng(20260323 + 800)
    for n in [2, 3, 4]:
        # For general D: A_F = C (dim 1) is a *-subalgebra of M_n(C)
        # Its gauge group = U(1)

        # For Barrett D: A_F = M_n(C) (dim n^2) is a *-subalgebra
        # Its gauge group = U(n)

        # Containment: C subset M_n(C) -- correct
        # Union: {Barrett D} union {general D} = full moduli -- the
        # Barrett subspace is the ONLY locus with A_F = M_n(C)

        # Verify: D = 0 (in both subspaces) gives A_F = M_n(C)
        D_zero = np.zeros((2 * n * n, 2 * n * n), dtype=complex)
        af_zero = compute_af_dim(n, D_zero)
        assert af_zero == n * n, (
            f"n={n}: D=0 should give A_F = M_n(C) (vacuous condition)"
        )

        # Verify: random Barrett gives n^2, random general gives 1
        K = random_symmetric_real(n, rng)
        D_b = build_barrett_D(n, K)
        assert compute_af_dim(n, D_b) == n * n

        D_g = build_general_D(n, rng)
        assert compute_af_dim(n, D_g) == 1
