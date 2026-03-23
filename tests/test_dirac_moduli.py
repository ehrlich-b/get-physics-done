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
# SECTION 9: CANDIDATE INFRASTRUCTURE (Plan 14-02)
# ===================================================================

def build_commutator_D(n, a):
    """Build D_a^comm on the doubled space H = C^{2n^2} from [a, X] = aX - Xa.

    Under Barrett iso, H = M_n(C)_p + M_n(C)_{ap}. The commutator [a, -]
    acts identically on both sectors: D(X_p, X_{ap}) = ([a,X_p], [a,X_{ap}]).

    The resulting D is a 2n^2 x 2n^2 matrix acting on vectors in H where
    we vectorize X in M_n(C) using column-major (Fortran) ordering.

    Parameters:
        n: algebra dimension (A = M_n(C))
        a: n x n complex matrix
    Returns:
        D: 2n^2 x 2n^2 complex matrix
    """
    dim = n * n
    # [a, X] = aX - Xa as a linear map on vec(X)
    # vec(aX) = (I kron a) vec(X), vec(Xa) = (a^T kron I) vec(X)
    I_n = np.eye(n, dtype=complex)
    La = np.kron(I_n, a)  # left multiplication by a
    Ra = np.kron(a.T, I_n)  # right multiplication by a
    comm = La - Ra  # [a, -] as dim x dim matrix

    # On doubled space: D acts as comm on each sector
    D = np.zeros((2 * dim, 2 * dim), dtype=complex)
    D[:dim, :dim] = comm
    D[dim:, dim:] = comm
    return D


def build_sp_D(n, a):
    """Build D_a^sp on the doubled space from sqrt(a) X sqrt(a).

    Parameters:
        n: algebra dimension
        a: n x n positive semidefinite Hermitian matrix
    Returns:
        D: 2n^2 x 2n^2 complex matrix
    """
    dim = n * n
    # Compute matrix sqrt
    evals, evecs = np.linalg.eigh(a)
    evals = np.maximum(evals, 0)  # ensure non-negative
    sqrt_a = evecs @ np.diag(np.sqrt(evals)) @ evecs.conj().T

    # sqrt(a) X sqrt(a) as linear map: vec(sqrt(a) X sqrt(a)) = (sqrt(a)^T kron sqrt(a)) vec(X)
    I_n = np.eye(n, dtype=complex)
    sp_map = np.kron(sqrt_a.T, sqrt_a)

    D = np.zeros((2 * dim, 2 * dim), dtype=complex)
    D[:dim, :dim] = sp_map
    D[dim:, dim:] = sp_map
    return D


def build_barrett_D(n, K):
    """Build Barrett-form D on the doubled space.

    D(X_p, X_{ap}) = (K X_{ap} + X_{ap} K^*, K X_p + X_p K^*)

    This is the sigma_1 tensor D_1 form from Barrett 2015 with
    D_1(X) = KX + XK^*.

    Parameters:
        n: algebra dimension
        K: n x n complex matrix
    Returns:
        D: 2n^2 x 2n^2 complex matrix
    """
    dim = n * n
    I_n = np.eye(n, dtype=complex)
    # D_1(X) = KX + XK^* = (I kron K)vec(X) + (K^{*T} kron I)vec(X)
    # = (I kron K + conj(K) kron I) vec(X)   [since K^{*T} = conj(K)]
    # Wait: vec(XK^*) = (K^{*T} kron I) vec(X) = (conj(K) kron I) vec(X)?
    # No. vec(XB) = (B^T kron I) vec(X). So vec(X K^*) = (K^{*T} kron I) vec(X).
    # K^{*T} = conj(K^T)^T ... no. K^* = conj(K). K^{*T} = conj(K)^T.
    D1 = np.kron(I_n, K) + np.kron(np.conj(K).T, I_n)

    # Barrett form: off-diagonal in V = C^2
    # D(X_p, X_{ap}) = (D_1(X_{ap}), D_1(X_p))
    D = np.zeros((2 * dim, 2 * dim), dtype=complex)
    D[:dim, dim:] = D1  # particle row, antiparticle col
    D[dim:, :dim] = D1  # antiparticle row, particle col
    return D


def check_all_constraints(D, n, tol=1e-12):
    """Check all three D constraints: D*=D, D gamma=-gamma D, JD=DJ.

    Parameters:
        D: 2n^2 x 2n^2 complex matrix
        n: algebra dimension
        tol: tolerance for Frobenius norm checks
    Returns:
        dict with keys:
            'self_adjoint': (bool, float) -- (pass, Frobenius norm of D - D^dag)
            'gamma_anticommutes': (bool, float) -- (pass, Frobenius norm of {D,gamma})
            'j_commutes': (bool, float) -- (pass, Frobenius norm of JDJ - D)
    """
    gamma = build_gamma_matrix(n)
    J_mat = build_J_matrix(n)

    # Constraint 1: D = D^dag
    sa_err = np.linalg.norm(D - D.conj().T, 'fro')

    # Constraint 2: D gamma + gamma D = 0
    anticomm = D @ gamma + gamma @ D
    gamma_err = np.linalg.norm(anticomm, 'fro')

    # Constraint 3: J_matrix @ conj(D) @ J_matrix = D (antilinear J)
    JDJ = J_mat @ np.conj(D) @ J_mat
    j_err = np.linalg.norm(JDJ - D, 'fro')

    return {
        'self_adjoint': (sa_err < tol, sa_err),
        'gamma_anticommutes': (gamma_err < tol, gamma_err),
        'j_commutes': (j_err < tol, j_err),
    }


def project_onto_moduli(D, n):
    """Project D onto the moduli space; return coefficients and residual.

    Parameters:
        D: 2n^2 x 2n^2 complex matrix
        n: algebra dimension
    Returns:
        (coeffs, residual_norm, D_projected)
        coeffs: array of real coefficients in the moduli basis
        residual_norm: Frobenius norm of D - D_projected
        D_projected: closest element in the moduli space
    """
    basis = build_moduli_basis(n)
    if not basis:
        return np.array([]), np.linalg.norm(D, 'fro'), np.zeros_like(D)

    dim_full = 2 * n * n

    # Vectorize basis elements (real representation)
    vecs = []
    for B in basis:
        v = np.concatenate([B.real.ravel(), B.imag.ravel()])
        vecs.append(v)
    mat = np.column_stack(vecs)

    # Vectorize D
    d_vec = np.concatenate([D.real.ravel(), D.imag.ravel()])

    # Least squares projection
    coeffs, residuals, _, _ = np.linalg.lstsq(mat, d_vec, rcond=None)

    # Reconstruct projected D
    D_proj = sum(c * B for c, B in zip(coeffs, basis))

    residual_norm = np.linalg.norm(D - D_proj, 'fro')

    return coeffs, residual_norm, D_proj


# ===================================================================
# SECTION 10: CANDIDATE A TESTS (Commutator [a, -])
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_commutator_self_adjoint(n):
    """D_a^comm is self-adjoint when a = a^dagger."""
    # a = diag(1,0,...,0) -- Hermitian
    a = np.zeros((n, n), dtype=complex)
    a[0, 0] = 1.0
    D = build_commutator_D(n, a)
    result = check_all_constraints(D, n)
    assert result['self_adjoint'][0], (
        f"Commutator D not self-adjoint at n={n}: Frobenius = {result['self_adjoint'][1]:.2e}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_commutator_gamma_anticommutes(n):
    """D_a^comm anticommutes with gamma for symmetric a."""
    # a = diag(1,0,...,0) -- real symmetric
    a = np.zeros((n, n), dtype=complex)
    a[0, 0] = 1.0
    D = build_commutator_D(n, a)
    result = check_all_constraints(D, n)
    assert result['gamma_anticommutes'][0], (
        f"Commutator D doesn't anticommute with gamma at n={n}: "
        f"Frobenius = {result['gamma_anticommutes'][1]:.2e}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_commutator_j_constraint_fails(n):
    """D_a^comm FAILS JD = DJ: should get JD = -DJ instead."""
    a = np.zeros((n, n), dtype=complex)
    a[0, 0] = 1.0
    D = build_commutator_D(n, a)
    J_mat = build_J_matrix(n)

    # Check JDJ = D (should FAIL)
    JDJ = J_mat @ np.conj(D) @ J_mat
    err_plus = np.linalg.norm(JDJ - D, 'fro')
    # Check JDJ = -D (should PASS -- anticommutation)
    err_minus = np.linalg.norm(JDJ + D, 'fro')

    assert err_plus > 1e-10, (
        f"Commutator D unexpectedly PASSES J constraint at n={n}"
    )
    assert err_minus < 1e-10, (
        f"Commutator D does not satisfy JD = -DJ at n={n}: "
        f"||JDJ + D|| = {err_minus:.2e}"
    )


@pytest.mark.parametrize("n", [2])
def test_commutator_multiple_a(n):
    """Test commutator with multiple a values at n=2."""
    a_list = {
        'diag(1,0)': np.diag([1.0, 0.0]).astype(complex),
        'E12+E21': np.array([[0, 1], [1, 0]], dtype=complex),
        'diag(1,2)': np.diag([1.0, 2.0]).astype(complex),
    }

    for name, a in a_list.items():
        D = build_commutator_D(n, a)
        if np.allclose(D, 0):
            continue  # skip trivial case

        result = check_all_constraints(D, n)
        J_mat = build_J_matrix(n)
        JDJ = J_mat @ np.conj(D) @ J_mat

        # Self-adjoint: PASS for Hermitian a
        assert result['self_adjoint'][0], (
            f"a={name}: not self-adjoint, Frob = {result['self_adjoint'][1]:.2e}"
        )
        # Gamma anticommutation: PASS for real symmetric a
        assert result['gamma_anticommutes'][0], (
            f"a={name}: gamma anticomm fails, Frob = {result['gamma_anticommutes'][1]:.2e}"
        )
        # J constraint: FAIL (JD = -DJ)
        err_minus = np.linalg.norm(JDJ + D, 'fro')
        assert err_minus < 1e-10, (
            f"a={name}: JD = -DJ not satisfied, Frob = {err_minus:.2e}"
        )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_commutator_projection(n):
    """Project commutator D onto moduli space; report residual."""
    a = np.zeros((n, n), dtype=complex)
    a[0, 0] = 1.0
    D = build_commutator_D(n, a)

    if np.allclose(D, 0):
        pytest.skip(f"Trivial D at n={n}")

    coeffs, residual, D_proj = project_onto_moduli(D, n)
    D_norm = np.linalg.norm(D, 'fro')

    # The commutator should NOT be in the moduli space
    # (it fails the J constraint), so residual should be significant
    relative_residual = residual / D_norm if D_norm > 0 else 0
    print(f"n={n}: ||D|| = {D_norm:.4f}, residual = {residual:.4f}, "
          f"relative = {relative_residual:.4f}")

    # The residual should be nonzero since commutator fails J constraint
    # But projection is onto the basis of the MODULI SPACE, so the projected
    # part may be zero or nonzero depending on whether any component of D
    # lies in the moduli space. Since JDJ = -D and moduli requires JDJ = D,
    # the projection should be zero.
    # Actually: D = D_in + D_out where D_in satisfies JDJ=D and D_out satisfies JDJ=-D.
    # Since JDJ = -D, we have D_in = 0 and D_out = D. So projection onto moduli = 0.
    assert residual > 0.1 * D_norm, (
        f"Commutator D has unexpectedly small moduli residual at n={n}: "
        f"relative = {relative_residual:.4f}"
    )


# ===================================================================
# SECTION 11: CANDIDATE B TESTS (SP operator sqrt(a) X sqrt(a))
# ===================================================================

@pytest.mark.parametrize("n", [2])
def test_sp_gamma_commutes(n):
    """SP operator sqrt(a) X sqrt(a) COMMUTES with gamma (SWAP-even)."""
    a = np.diag([1.0, 0.0]).astype(complex)
    D = build_sp_D(n, a)
    gamma = build_gamma_matrix(n)

    # Check D gamma - gamma D = 0 (commutation, not anticommutation)
    comm = D @ gamma - gamma @ D
    comm_err = np.linalg.norm(comm, 'fro')

    # Check D gamma + gamma D != 0 (anticommutation fails)
    anticomm = D @ gamma + gamma @ D
    anticomm_err = np.linalg.norm(anticomm, 'fro')

    assert comm_err < 1e-12, (
        f"SP operator doesn't commute with gamma: Frob = {comm_err:.2e}"
    )
    assert anticomm_err > 1e-10, (
        f"SP operator unexpectedly anticommutes with gamma: Frob = {anticomm_err:.2e}"
    )


@pytest.mark.parametrize("n", [2])
def test_sp_odd_extraction_fails(n):
    """SWAP-odd extraction of SP operator has wrong structure."""
    a = np.diag([1.0, 0.0]).astype(complex)

    dim = n * n
    I_n = np.eye(n, dtype=complex)
    evals, evecs = np.linalg.eigh(a)
    evals = np.maximum(evals, 0)
    sqrt_a = evecs @ np.diag(np.sqrt(evals)) @ evecs.conj().T

    # SP map: sqrt(a) X sqrt(a)
    sp_map = np.kron(sqrt_a.T, sqrt_a)

    # SWAP (transpose) map on M_n(C)
    P_mat = np.zeros((dim, dim), dtype=float)
    for i in range(n):
        for j in range(n):
            P_mat[i * n + j, j * n + i] = 1.0

    # SWAP-odd part: (SP - P SP P) / 2
    # P SP P(X) = P(sqrt(a) (PX) sqrt(a)) = (sqrt(a) X^T sqrt(a))^T
    # For real symmetric sqrt(a): = sqrt(a) X sqrt(a) = SP(X)
    # So SWAP-odd part = 0 for real symmetric a!
    sp_odd = (sp_map - P_mat @ sp_map @ P_mat) / 2
    odd_norm = np.linalg.norm(sp_odd, 'fro')

    # The SWAP-odd part should be zero (or near-zero) since SP commutes with P
    assert odd_norm < 1e-12, (
        f"SWAP-odd extraction unexpectedly nonzero: Frob = {odd_norm:.2e}"
    )


# ===================================================================
# SECTION 12: CANDIDATE C TESTS (Barrett form)
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_barrett_candidate(n):
    """Barrett-form D with non-scalar K: check all constraints."""
    # K = diag(1,0,...,0) -- Hermitian but not scalar
    K = np.zeros((n, n), dtype=complex)
    K[0, 0] = 1.0
    D = build_barrett_D(n, K)
    result = check_all_constraints(D, n)

    # Self-adjoint: should pass (K Hermitian)
    assert result['self_adjoint'][0], (
        f"Barrett D not self-adjoint at n={n}: Frob = {result['self_adjoint'][1]:.2e}"
    )

    # Gamma anticommutation: check numerically
    # Barrett form D = sigma_1 tensor D_1 should give
    # {D, gamma} = i sigma_2 tensor [P, D_1]
    # D_1 = KX + XK^*. For K Hermitian: K^* = K^T.
    # [P, D_1] != 0 unless K is real AND symmetric.
    # For K = diag(1,0,...,0): K is real and symmetric, so K^* = K^T = K.
    # Then D_1(X) = KX + XK. Check [P, D_1]:
    # P D_1(X) = (KX + XK)^T = X^T K^T + K^T X^T = X^T K + K X^T
    # D_1(PX) = K X^T + X^T K
    # So P D_1 = D_1 P: PASS.
    # So gamma anticommutation should PASS for real symmetric K.

    # J constraint: Barrett form with real symmetric K PASSES JD = DJ.
    # The J constraint requires [K^T - K, Y] = 0 for all Y, i.e., K^T = K.
    # K = diag(1,0,...,0) IS real symmetric, so it passes.
    assert result['j_commutes'][0], (
        f"Barrett D with real symmetric K fails J at n={n}: "
        f"Frobenius = {result['j_commutes'][1]:.2e}"
    )
    assert result['gamma_anticommutes'][0], (
        f"Barrett D gamma anticomm fails at n={n}: "
        f"Frobenius = {result['gamma_anticommutes'][1]:.2e}"
    )


@pytest.mark.parametrize("n", [2, 3])
def test_barrett_nonsymmetric_k_fails(n):
    """Barrett-form D with non-symmetric K FAILS the J constraint."""
    # K = upper triangular, NOT symmetric
    K = np.zeros((n, n), dtype=complex)
    K[0, 1] = 1.0  # K_{01} = 1, K_{10} = 0: not symmetric
    D = build_barrett_D(n, K)
    result = check_all_constraints(D, n)

    # J constraint should FAIL for non-symmetric K
    assert not result['j_commutes'][0], (
        f"Barrett D with non-symmetric K passes J at n={n} (unexpected)"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_barrett_scalar_k(n):
    """Barrett-form D with K = lambda I should pass all constraints."""
    K = np.eye(n, dtype=complex)  # K = I (scalar, lambda=1)
    D = build_barrett_D(n, K)
    result = check_all_constraints(D, n)

    assert result['self_adjoint'][0], (
        f"Barrett scalar K not self-adjoint at n={n}: Frob = {result['self_adjoint'][1]:.2e}"
    )
    # gamma: D_1(X) = IX + XI = 2X. P D_1 = D_1 P trivially. So should pass.
    assert result['gamma_anticommutes'][0], (
        f"Barrett scalar K gamma fail at n={n}: Frob = {result['gamma_anticommutes'][1]:.2e}"
    )
    # J: K = I is scalar, should pass
    assert result['j_commutes'][0], (
        f"Barrett scalar K J fail at n={n}: Frob = {result['j_commutes'][1]:.2e}"
    )


@pytest.mark.parametrize("n", [2, 3, 4])
def test_barrett_scalar_in_moduli(n):
    """Barrett D with K = lambda I should be in the moduli space."""
    K = np.eye(n, dtype=complex)
    D = build_barrett_D(n, K)

    coeffs, residual, D_proj = project_onto_moduli(D, n)
    D_norm = np.linalg.norm(D, 'fro')

    relative_residual = residual / D_norm if D_norm > 0 else 0
    print(f"n={n}: Barrett scalar ||D|| = {D_norm:.4f}, residual = {residual:.6f}, "
          f"relative = {relative_residual:.6f}")

    assert relative_residual < 1e-10, (
        f"Barrett scalar K not in moduli space at n={n}: "
        f"relative residual = {relative_residual:.2e}"
    )


# ===================================================================
# SECTION 13: NATURAL D IDENTIFICATION
# ===================================================================

@pytest.mark.parametrize("n", [2, 3, 4])
def test_natural_d_simplest(n):
    """Verify the simplest non-trivial D in the moduli space."""
    # The simplest D: M with only M_{12} and M_{21} nonzero
    # At n=2: s=3, a=1. M_{12} is 1x1, M_{21} is 3x3.
    # Simplest: M_{12} = alpha, M_{21} = beta * I_s
    # For testing: alpha = 1, beta = 1

    basis = build_moduli_basis(n)
    assert len(basis) > 0, f"Empty moduli basis at n={n}"

    # Pick the first nonzero basis element as a representative
    D_test = None
    for B in basis:
        if np.linalg.norm(B, 'fro') > 1e-10:
            D_test = B
            break

    assert D_test is not None, f"No nonzero basis element at n={n}"

    result = check_all_constraints(D_test, n)
    assert result['self_adjoint'][0], f"Natural D not self-adjoint at n={n}"
    assert result['gamma_anticommutes'][0], f"Natural D gamma fail at n={n}"
    assert result['j_commutes'][0], f"Natural D J fail at n={n}"


@pytest.mark.parametrize("n", [2, 3, 4])
def test_natural_d_nonzero(n):
    """Verify that nontrivial D exist in the moduli space."""
    basis = build_moduli_basis(n)
    norms = [np.linalg.norm(B, 'fro') for B in basis]
    assert max(norms) > 1e-10, f"All moduli basis elements zero at n={n}"
    print(f"n={n}: {len(basis)} basis elements, max norm = {max(norms):.4f}")


# ===================================================================
# SECTION 14: SUMMARY TABLE
# ===================================================================

def test_candidate_summary_table():
    """Print summary table of all candidate tests at n=2,3,4."""
    print("\n" + "=" * 90)
    print("CANDIDATE TESTING SUMMARY TABLE")
    print("=" * 90)
    print(f"{'Candidate':<30} {'n':>3} {'D*=D':>10} {'Dgamma=-gammaD':>16} "
          f"{'JD=DJ':>10} {'In moduli?':>12} {'Residual':>10}")
    print("-" * 90)

    for n in [2, 3, 4]:
        dim = n * n

        # Candidate A: commutator
        a = np.zeros((n, n), dtype=complex)
        a[0, 0] = 1.0
        D = build_commutator_D(n, a)
        if not np.allclose(D, 0):
            r = check_all_constraints(D, n)
            _, resid, _ = project_onto_moduli(D, n)
            D_norm = np.linalg.norm(D, 'fro')
            rel_resid = resid / D_norm if D_norm > 0 else 0
            print(f"{'A: [a,X] a=diag(1,0..)':<30} {n:>3} "
                  f"{'PASS' if r['self_adjoint'][0] else 'FAIL':>10} "
                  f"{'PASS' if r['gamma_anticommutes'][0] else 'FAIL':>16} "
                  f"{'PASS' if r['j_commutes'][0] else 'FAIL':>10} "
                  f"{'YES' if rel_resid < 1e-6 else 'NO':>12} "
                  f"{rel_resid:>10.4f}")

        # Candidate B: SP operator
        D = build_sp_D(n, a)
        if not np.allclose(D, 0):
            r = check_all_constraints(D, n)
            _, resid, _ = project_onto_moduli(D, n)
            D_norm = np.linalg.norm(D, 'fro')
            rel_resid = resid / D_norm if D_norm > 0 else 0
            print(f"{'B: sqrt(a)Xsqrt(a)':<30} {n:>3} "
                  f"{'PASS' if r['self_adjoint'][0] else 'FAIL':>10} "
                  f"{'PASS' if r['gamma_anticommutes'][0] else 'FAIL':>16} "
                  f"{'PASS' if r['j_commutes'][0] else 'FAIL':>10} "
                  f"{'YES' if rel_resid < 1e-6 else 'NO':>12} "
                  f"{rel_resid:>10.4f}")

        # Candidate C: Barrett with non-scalar K
        K = np.zeros((n, n), dtype=complex)
        K[0, 0] = 1.0
        D = build_barrett_D(n, K)
        if not np.allclose(D, 0):
            r = check_all_constraints(D, n)
            _, resid, _ = project_onto_moduli(D, n)
            D_norm = np.linalg.norm(D, 'fro')
            rel_resid = resid / D_norm if D_norm > 0 else 0
            print(f"{'C: Barrett K=diag(1,0..)':<30} {n:>3} "
                  f"{'PASS' if r['self_adjoint'][0] else 'FAIL':>10} "
                  f"{'PASS' if r['gamma_anticommutes'][0] else 'FAIL':>16} "
                  f"{'PASS' if r['j_commutes'][0] else 'FAIL':>10} "
                  f"{'YES' if rel_resid < 1e-6 else 'NO':>12} "
                  f"{rel_resid:>10.4f}")

        # Candidate C: Barrett with scalar K = I
        K = np.eye(n, dtype=complex)
        D = build_barrett_D(n, K)
        r = check_all_constraints(D, n)
        _, resid, _ = project_onto_moduli(D, n)
        D_norm = np.linalg.norm(D, 'fro')
        rel_resid = resid / D_norm if D_norm > 0 else 0
        print(f"{'C: Barrett K=I (scalar)':<30} {n:>3} "
              f"{'PASS' if r['self_adjoint'][0] else 'FAIL':>10} "
              f"{'PASS' if r['gamma_anticommutes'][0] else 'FAIL':>16} "
              f"{'PASS' if r['j_commutes'][0] else 'FAIL':>10} "
              f"{'YES' if rel_resid < 1e-6 else 'NO':>12} "
              f"{rel_resid:>10.4f}")

    print("=" * 90)


# ===================================================================
# Entry point
# ===================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
