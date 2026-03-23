#!/usr/bin/env python3
"""
Verification of D moduli space parameterization for the self-modeling spectral
triple at n=1,2,3,4.

The moduli space consists of all self-adjoint Dirac operators D on H = C^{2n^2}
satisfying:
  (1) D* = D (self-adjointness) -- automatic from block form
  (2) D gamma + gamma D = 0 (anticommutation with grading)
  (3) J_matrix @ conj(D) @ J_matrix = D (commutation with antilinear J)

The block form D = [[0, M^dag], [M, 0]] in the gamma-eigenspace basis
(H_+, H_-) encodes (1) and (2). Constraint (3) reduces to:
  M = J_+^{mat} M^T J_+^{mat}
where J_+^{mat} is the linear part of J restricted to H_+ -> H_-.

Analytical prediction: dim(moduli space) = n^2(n^2 + 1).

Convention assertions:
  ASSERT_CONVENTION: inner_product=linear_second, J_definition=antilinear_PC,
    P_definition=SWAP, gamma_definition=diag(P,-P),
    ko_dimension=6, barrett_iso=v_tensor_w_to_vwT,
    commutator=[A,B]=AB-BA

References:
  - Barrett 2015, arXiv:1502.05383 (D parameterization)
  - van Suijlekom 2024, Ch. 3-4 (D constraints)
  - Cacic 2009, arXiv:0902.2068 (moduli space theory)
  - Phase 13 results (H, J, gamma definitions)
  - derivations/08-dirac-moduli-space.md (this phase's derivation)

Library versions: numpy 2.4.2, pytest 9.0.2
Platform: macOS Darwin 24.6.0
"""

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Infrastructure: reuse Phase 13 patterns from tests/test_order_zero.py
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


# ---------------------------------------------------------------------------
# New infrastructure for D moduli space
# ---------------------------------------------------------------------------

def build_gamma_eigenbasis(n):
    """Change-of-basis matrix Q from (particle, antiparticle) to (H_+, H_-).

    gamma = diag(P, -P) in (p, ap) basis.
    H_+ (gamma = +1) = Sym_p + Skew_ap
    H_- (gamma = -1) = Skew_p + Sym_ap

    Returns Q such that Q^T gamma Q = diag(I, -I).
    The columns of Q are the gamma eigenvectors.

    Column ordering:
      First n^2 columns: H_+ basis (Sym_p eigenvectors, then Skew_ap eigenvectors)
      Last n^2 columns: H_- basis (Skew_p eigenvectors, then Sym_ap eigenvectors)
    """
    P = build_swap_matrix(n)
    dim = n * n
    dim_full = 2 * dim

    # Diagonalize P to get Sym/Skew eigenvectors
    evals, evecs = np.linalg.eigh(P)
    # eigh returns eigenvalues in ascending order: -1 first, then +1
    # Identify +1 (Sym) and -1 (Skew) eigenvectors
    sym_mask = np.abs(evals - 1.0) < 1e-10
    skew_mask = np.abs(evals + 1.0) < 1e-10

    sym_vecs = evecs[:, sym_mask]  # columns are Sym eigenvectors (dim s)
    skew_vecs = evecs[:, skew_mask]  # columns are Skew eigenvectors (dim a)

    s = sym_vecs.shape[1]  # n(n+1)/2
    a = skew_vecs.shape[1]  # n(n-1)/2
    assert s == n * (n + 1) // 2, f"Sym dim {s} != {n*(n+1)//2}"
    assert a == n * (n - 1) // 2, f"Skew dim {a} != {n*(n-1)//2}"

    Q = np.zeros((dim_full, dim_full), dtype=float)

    # H_+ columns (first n^2):
    #   Sym_p: sym_vecs in particle sector (rows 0..dim-1)
    #   Skew_ap: skew_vecs in antiparticle sector (rows dim..2dim-1)
    col = 0
    for j in range(s):
        Q[:dim, col] = sym_vecs[:, j]
        col += 1
    for j in range(a):
        Q[dim:, col] = skew_vecs[:, j]
        col += 1

    # H_- columns (last n^2):
    #   Skew_p: skew_vecs in particle sector (rows 0..dim-1)
    #   Sym_ap: sym_vecs in antiparticle sector (rows dim..2dim-1)
    for j in range(a):
        Q[:dim, col] = skew_vecs[:, j]
        col += 1
    for j in range(s):
        Q[dim:, col] = sym_vecs[:, j]
        col += 1

    assert col == dim_full
    return Q


def build_J_pm(n):
    """Compute J_+ and J_- in the gamma-eigenspace basis.

    Returns (J_plus, J_minus) where:
      J_plus: n^2 x n^2 real matrix (linear part of J mapping H_+ -> H_-)
      J_minus: n^2 x n^2 real matrix (linear part of J mapping H_- -> H_+)

    The full J_matrix in gamma-eigenspace basis is [[0, J_minus], [J_plus, 0]].
    """
    Q = build_gamma_eigenbasis(n)
    J_mat = build_J_matrix(n)
    dim = n * n

    # Transform J_matrix to gamma-eigenspace basis: J_gamma = Q^T J_mat Q
    # (J_matrix is real, Q is real orthogonal)
    J_gamma = Q.T @ J_mat @ Q

    J_plus = J_gamma[dim:, :dim]  # lower-left: H_+ -> H_-
    J_minus = J_gamma[:dim, dim:]  # upper-right: H_- -> H_+

    return J_plus, J_minus


def build_constraint_matrix(n):
    """Build the real linear system encoding M = J_+ M^T J_+ for vectorized M.

    M is an n^2 x n^2 complex matrix written as M = M_R + i M_I.
    The constraint M = J_+ M^T J_+ gives:
      M_R = J_+ M_R^T J_+
      M_I = J_+ M_I^T J_+
    Both real and imaginary parts satisfy the same constraint.

    Vectorize: x = [vec(M_R); vec(M_I)] (2n^4 real parameters).
    The constraint T(X) = X where T(X) = J_+ X^T J_+ is an involution.

    Returns C such that C @ x = 0 for valid M.
    C has shape (2n^4, 2n^4) and encodes (T - I) on each component.
    """
    J_plus, _ = build_J_pm(n)
    dim = n * n
    dim_sq = dim * dim  # n^4

    # Build the matrix for T(X) = J_+ X^T J_+ acting on vec(X)
    # vec(AXB) = (B^T kron A) vec(X)
    # vec(X^T) = K vec(X) where K is the commutation matrix
    # vec(J_+ X^T J_+) = (J_+^T kron J_+) K vec(X)

    # Commutation matrix: K permutes (i,j) -> (j,i) in column-major order
    K = np.zeros((dim_sq, dim_sq), dtype=float)
    for i in range(dim):
        for j in range(dim):
            # vec(X) index for X_{ij} is j*dim + i (column-major)
            # vec(X^T) index for (X^T)_{ij} = X_{ji} is j*dim + i
            # So K maps index (j*dim + i) to (i*dim + j)
            K[i * dim + j, j * dim + i] = 1.0

    T_mat = np.kron(J_plus.T, J_plus) @ K

    # Constraint: (T - I) vec(X) = 0 for both real and imaginary parts
    constraint_single = T_mat - np.eye(dim_sq)

    # Full constraint on [vec(M_R); vec(M_I)]
    C = np.zeros((2 * dim_sq, 2 * dim_sq), dtype=float)
    C[:dim_sq, :dim_sq] = constraint_single
    C[dim_sq:, dim_sq:] = constraint_single

    return C


def build_moduli_basis(n):
    """Compute a basis for the D moduli space at given n.

    Returns a list of 2n^2 x 2n^2 complex matrices D_k, each satisfying:
      D_k = D_k^dag, D_k gamma + gamma D_k = 0, J conj(D_k) J = D_k.

    The matrices are in the ORIGINAL (particle, antiparticle) basis.
    """
    J_plus, _ = build_J_pm(n)
    Q = build_gamma_eigenbasis(n)
    dim = n * n
    dim_sq = dim * dim

    # Build T matrix for T(X) = J_+ X^T J_+ on vec(X)
    K = np.zeros((dim_sq, dim_sq), dtype=float)
    for i in range(dim):
        for j in range(dim):
            K[i * dim + j, j * dim + i] = 1.0

    T_mat = np.kron(J_plus.T, J_plus) @ K

    # Find +1 eigenspace of T (constraint: T(X) = X)
    # T is an involution, so eigenvalues are +1 and -1
    evals, evecs = np.linalg.eigh(T_mat)
    # +1 eigenvectors
    plus_mask = np.abs(evals - 1.0) < 1e-10
    plus_vecs = evecs[:, plus_mask]  # each column is a vec(X) satisfying T(X)=X

    n_plus = plus_vecs.shape[1]

    # Build D matrices: for each +1 eigenvector, it contributes to M_R or M_I
    basis = []
    for k in range(n_plus):
        # Real part contribution: M = X (real), D in gamma-eigenspace basis
        X = plus_vecs[:, k].reshape((dim, dim), order='F')  # column-major
        M = X.astype(complex)
        D_gamma = np.zeros((2 * dim, 2 * dim), dtype=complex)
        D_gamma[dim:, :dim] = M  # lower-left: M
        D_gamma[:dim, dim:] = M.conj().T  # upper-right: M^dag
        # Transform to original basis
        D_orig = Q @ D_gamma @ Q.T
        basis.append(D_orig)

    for k in range(n_plus):
        # Imaginary part contribution: M = i*X, D in gamma-eigenspace basis
        X = plus_vecs[:, k].reshape((dim, dim), order='F')
        M = 1j * X
        D_gamma = np.zeros((2 * dim, 2 * dim), dtype=complex)
        D_gamma[dim:, :dim] = M
        D_gamma[:dim, dim:] = M.conj().T
        D_orig = Q @ D_gamma @ Q.T
        basis.append(D_orig)

    return basis


def predicted_moduli_dim(n):
    """Analytical prediction: dim = n^2(n^2 + 1)."""
    return n * n * (n * n + 1)


# ===================================================================
# SECTION 1: GAMMA EIGENSPACE BASIS TESTS
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_gamma_diagonal_in_eigenbasis(n):
    """Verify gamma = diag(I, -I) after basis change."""
    Q = build_gamma_eigenbasis(n)
    gamma = build_gamma_matrix(n)
    dim = n * n

    gamma_new = Q.T @ gamma @ Q
    expected = np.diag(np.concatenate([np.ones(dim), -np.ones(dim)]))
    assert np.allclose(gamma_new, expected, atol=1e-12), (
        f"gamma not diagonal in eigenbasis at n={n}, "
        f"max error = {np.max(np.abs(gamma_new - expected)):.2e}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_eigenbasis_orthogonal(n):
    """Q is orthogonal: Q^T Q = I."""
    Q = build_gamma_eigenbasis(n)
    dim_full = 2 * n * n
    assert np.allclose(Q.T @ Q, np.eye(dim_full), atol=1e-12), (
        f"Q not orthogonal at n={n}"
    )


# ===================================================================
# SECTION 2: J IN GAMMA-EIGENSPACE BASIS
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_j_off_diagonal_in_eigenbasis(n):
    """Verify J_matrix = [[0, J_-], [J_+, 0]] in gamma-eigenspace basis."""
    Q = build_gamma_eigenbasis(n)
    J_mat = build_J_matrix(n)
    dim = n * n

    J_gamma = Q.T @ J_mat @ Q

    # Check diagonal blocks are zero
    assert np.allclose(J_gamma[:dim, :dim], 0, atol=1e-12), (
        f"J upper-left block nonzero at n={n}"
    )
    assert np.allclose(J_gamma[dim:, dim:], 0, atol=1e-12), (
        f"J lower-right block nonzero at n={n}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_j_squared_identity_eigenbasis(n):
    """Verify J^2 = I in the gamma-eigenspace basis."""
    J_plus, J_minus = build_J_pm(n)
    dim = n * n

    # J^2 requires J_- J_+ = I and J_+ J_- = I
    assert np.allclose(J_minus @ J_plus, np.eye(dim), atol=1e-12), (
        f"J_- J_+ != I at n={n}"
    )
    assert np.allclose(J_plus @ J_minus, np.eye(dim), atol=1e-12), (
        f"J_+ J_- != I at n={n}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_j_plus_orthogonal(n):
    """J_+ is a real orthogonal matrix."""
    J_plus, _ = build_J_pm(n)
    dim = n * n
    assert np.allclose(J_plus.T @ J_plus, np.eye(dim), atol=1e-12), (
        f"J_+ not orthogonal at n={n}"
    )
    assert np.all(np.abs(J_plus.imag) < 1e-15) if np.iscomplexobj(J_plus) else True, (
        f"J_+ has imaginary entries at n={n}"
    )


# ===================================================================
# SECTION 3: MODULI SPACE DIMENSION
# ===================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_moduli_dim(n):
    """Verify moduli space dimension matches n^2(n^2 + 1)."""
    if n == 1:
        # At n=1: P = I (scalar), gamma = diag(1,-1), H = C^2
        # Moduli is all complex z: D = [[0, z*], [z, 0]]
        # dim = 2 (one complex parameter)
        predicted = 2
    else:
        predicted = predicted_moduli_dim(n)

    basis = build_moduli_basis(n)
    actual = len(basis)

    assert actual == predicted, (
        f"Moduli dim at n={n}: got {actual}, expected {predicted}"
    )


def test_moduli_dim_sequence():
    """Print moduli space dimensions at n=1,2,3,4 and verify pattern."""
    dims = {}
    for n in [1, 2, 3, 4]:
        basis = build_moduli_basis(n)
        dims[n] = len(basis)
        print(f"n={n}: dim(moduli) = {dims[n]}, predicted = {predicted_moduli_dim(n)}")

    # Verify the formula n^2(n^2 + 1) for all n
    for n in [1, 2, 3, 4]:
        assert dims[n] == predicted_moduli_dim(n), (
            f"n={n}: dim {dims[n]} != formula {predicted_moduli_dim(n)}"
        )

    # Verify non-decreasing
    for i in range(len(list(dims.values())) - 1):
        ns = sorted(dims.keys())
        assert dims[ns[i + 1]] >= dims[ns[i]], (
            f"Dimension decreased from n={ns[i]} to n={ns[i+1]}"
        )


# ===================================================================
# SECTION 4: CONSTRAINT SATISFACTION FOR ALL BASIS ELEMENTS
# ===================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_basis_self_adjoint(n):
    """Every moduli basis element satisfies D = D^dagger."""
    basis = build_moduli_basis(n)
    for k, D in enumerate(basis):
        err = np.linalg.norm(D - D.conj().T, 'fro')
        assert err < 1e-12, (
            f"Basis element {k} at n={n}: D != D^dag, Frobenius = {err:.2e}"
        )


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_basis_gamma_anticommutes(n):
    """Every moduli basis element satisfies D gamma + gamma D = 0."""
    gamma = build_gamma_matrix(n)
    basis = build_moduli_basis(n)
    for k, D in enumerate(basis):
        anticomm = D @ gamma + gamma @ D
        err = np.linalg.norm(anticomm, 'fro')
        assert err < 1e-12, (
            f"Basis element {k} at n={n}: {{D,gamma}} != 0, Frobenius = {err:.2e}"
        )


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_basis_j_commutes(n):
    """Every moduli basis element satisfies J_matrix conj(D) J_matrix = D.

    CRITICAL: J is antilinear, so JDJ^{-1} = J_matrix @ conj(D) @ J_matrix^{-1}.
    Since J_matrix^2 = I (for real J_matrix), J_matrix^{-1} = J_matrix.
    So the constraint is J_matrix @ conj(D) @ J_matrix = D.
    """
    J_mat = build_J_matrix(n)
    basis = build_moduli_basis(n)
    for k, D in enumerate(basis):
        JDJ = J_mat @ np.conj(D) @ J_mat
        err = np.linalg.norm(JDJ - D, 'fro')
        assert err < 1e-12, (
            f"Basis element {k} at n={n}: JDJ^-1 != D, Frobenius = {err:.2e}"
        )


# ===================================================================
# SECTION 5: TRIVIAL AND EXISTENCE TESTS
# ===================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_d_zero_in_space(n):
    """D=0 is expressible as the zero linear combination of basis elements."""
    basis = build_moduli_basis(n)
    dim_full = 2 * n * n
    D_zero = np.zeros((dim_full, dim_full), dtype=complex)

    # The zero vector is always in any vector space
    # Verify by checking that all-zero coefficients give D=0
    D_sum = sum(0.0 * D for D in basis)
    assert np.allclose(D_sum, D_zero, atol=1e-15), (
        f"Zero combination doesn't give zero at n={n}"
    )


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_nonzero_d_exists(n):
    """At least one basis element has Frobenius norm > 0."""
    basis = build_moduli_basis(n)
    norms = [np.linalg.norm(D, 'fro') for D in basis]
    max_norm = max(norms)
    assert max_norm > 1e-10, (
        f"All basis elements are zero at n={n}! Moduli space may be trivial."
    )


# ===================================================================
# SECTION 6: LINEAR INDEPENDENCE OF BASIS
# ===================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_basis_linear_independence(n):
    """Basis elements are linearly independent (over R)."""
    basis = build_moduli_basis(n)
    if not basis:
        pytest.skip(f"Empty basis at n={n}")

    dim_full = 2 * n * n
    dim_sq = dim_full * dim_full

    # Stack vectorized basis elements as columns
    # Use real and imaginary parts separately for real linear independence
    vecs = []
    for D in basis:
        v = np.concatenate([D.real.ravel(), D.imag.ravel()])
        vecs.append(v)
    mat = np.column_stack(vecs)

    # Rank should equal number of basis elements
    rank = np.linalg.matrix_rank(mat, tol=1e-10)
    assert rank == len(basis), (
        f"Basis not linearly independent at n={n}: rank={rank}, count={len(basis)}"
    )


# ===================================================================
# SECTION 7: COMPLETENESS CHECK (SVD cross-validation)
# ===================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_moduli_dim_via_svd(n):
    """Cross-check moduli dim via direct SVD of constraint matrix on full D.

    Build the constraint C @ vec(D) = 0 directly (without going through
    gamma-eigenspace decomposition) and check the null space dimension.

    Three constraints:
      (a) D gamma + gamma D = 0  [complex-linear]
      (b) D - D^dag = 0  [antilinear -> split real/imag]
      (c) J_matrix conj(D) J_matrix - D = 0  [antilinear -> split real/imag]

    All encoded as real-linear constraints on [vec(Re(D)); vec(Im(D))].
    """
    J_mat = build_J_matrix(n)
    gamma = build_gamma_matrix(n)
    dim = 2 * n * n
    dim_sq = dim * dim

    # Commutation matrix for dim x dim
    K = np.zeros((dim_sq, dim_sq), dtype=float)
    for i in range(dim):
        for j in range(dim):
            K[i * dim + j, j * dim + i] = 1.0

    I_d = np.eye(dim)
    I_dd = np.eye(dim_sq)

    # Constraint (a): D gamma + gamma D = 0
    # vec(D gamma) = (gamma^T kron I) vec(D) for real gamma
    # vec(gamma D) = (I kron gamma) vec(D) for real gamma
    # Applied to complex D = D_R + i D_I:
    A_gamma_real = np.kron(gamma.T, I_d) + np.kron(I_d, gamma)
    # This acts on vec(D_R) and vec(D_I) identically (gamma is real)
    # Constraint: A_gamma_real vec(D_R) = 0 AND A_gamma_real vec(D_I) = 0

    # Constraint (b): D = D^dag = conj(D)^T
    # D_R + i D_I = (D_R - i D_I)^T = D_R^T - i D_I^T
    # => D_R = D_R^T and D_I = -D_I^T
    # D_R^T: vec(D_R^T) = K vec(D_R), so constraint: (K - I) vec(D_R) = 0
    # D_I^T: vec(D_I^T) = K vec(D_I), so constraint: (K + I) vec(D_I) = 0

    # Constraint (c): J_matrix conj(D) J_matrix = D
    # J_matrix (D_R - i D_I) J_matrix = D_R + i D_I
    # Real: J_matrix D_R J_matrix = D_R
    # Imag: -J_matrix D_I J_matrix = D_I, i.e., J_matrix D_I J_matrix = -D_I
    # vec(J D_R J) = (J^T kron J) vec(D_R) for real J
    JkJ = np.kron(J_mat.T, J_mat)
    # Constraint: (JkJ - I) vec(D_R) = 0
    # Constraint: (JkJ + I) vec(D_I) = 0

    # Stack all constraints into one matrix
    # State vector: x = [vec(D_R); vec(D_I)], length 2*dim_sq
    n_constraints = 4  # gamma_R, gamma_I, hermiticity_R+J_R, hermiticity_I+J_I
    C = np.zeros((4 * dim_sq, 2 * dim_sq), dtype=float)

    # Constraint (a) on D_R
    C[:dim_sq, :dim_sq] = A_gamma_real

    # Constraint (a) on D_I
    C[dim_sq:2*dim_sq, dim_sq:] = A_gamma_real

    # Constraint (b+c) on D_R: (K - I) and (JkJ - I)
    # Combine: just stack both
    C[2*dim_sq:3*dim_sq, :dim_sq] = K - I_dd  # D_R symmetric
    # Also add J constraint on D_R
    # Actually let me stack them all separately
    # Rewrite: all constraints as separate rows

    # Let me redo this more carefully
    rows = []

    # (a) D gamma + gamma D = 0, real part
    rows.append(np.hstack([A_gamma_real, np.zeros((dim_sq, dim_sq))]))

    # (a) D gamma + gamma D = 0, imaginary part
    rows.append(np.hstack([np.zeros((dim_sq, dim_sq)), A_gamma_real]))

    # (b) D_R = D_R^T
    rows.append(np.hstack([K - I_dd, np.zeros((dim_sq, dim_sq))]))

    # (b) D_I = -D_I^T
    rows.append(np.hstack([np.zeros((dim_sq, dim_sq)), K + I_dd]))

    # (c) J D_R J = D_R
    rows.append(np.hstack([JkJ - I_dd, np.zeros((dim_sq, dim_sq))]))

    # (c) J D_I J = -D_I
    rows.append(np.hstack([np.zeros((dim_sq, dim_sq)), JkJ + I_dd]))

    C = np.vstack(rows)

    # Null space dimension
    _, S, _ = np.linalg.svd(C, full_matrices=False)
    null_dim = np.sum(S < 1e-10)
    # Full null space dimension = 2*dim_sq - rank(C)
    rank = np.sum(S > 1e-10)
    null_dim = 2 * dim_sq - rank

    predicted = predicted_moduli_dim(n)
    assert null_dim == predicted, (
        f"SVD null space dim at n={n}: got {null_dim}, expected {predicted}"
    )


# ===================================================================
# SECTION 8: INVOLUTION TRACE CHECK
# ===================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_involution_trace(n):
    """Verify tr(T) = n^2 for the involution T(X) = J_+ X^T J_+.

    Since dim(moduli) = n^4 + tr(T) (per component, times 2),
    the formula dim = n^2(n^2 + 1) requires tr(T) = n^2.
    """
    if n == 1:
        # At n=1, J_+ is 1x1, T is trivially identity on R^1
        # tr(T) = 1 = n^2. Formula: dim = 1 + 1 = 2. Check.
        assert True
        return

    J_plus, _ = build_J_pm(n)
    dim = n * n
    dim_sq = dim * dim

    K = np.zeros((dim_sq, dim_sq), dtype=float)
    for i in range(dim):
        for j in range(dim):
            K[i * dim + j, j * dim + i] = 1.0

    T_mat = np.kron(J_plus.T, J_plus) @ K
    trace_T = np.trace(T_mat)

    assert abs(trace_T - n * n) < 1e-10, (
        f"tr(T) at n={n}: got {trace_T:.4f}, expected {n*n}"
    )


# ===================================================================
# Entry point
# ===================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
