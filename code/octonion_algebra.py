# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   peirce_decomposition=under_E11,
#   v_half_basis=(x2_0..x2_7,x3_0..x3_7)
#
# Phase 28, Plan 01: Octonion arithmetic, h_3(O) Jordan product, Peirce
# projections, and L_{E_{11}} computation.
#
# ALGV-01 RESULT: L_{E_{11}} = (1/2)*I_{16} on V_{1/2} (exact, zero error).
# Confirms V_1 = R*E_{11} bottleneck from v6.0 Phase 22 and derivation 11.
#
# References:
#   Baez, "The Octonions," Bull. AMS 39 (2002), Sec. 3.4
#   Alfsen-Shultz, State Spaces of Operator Algebras (2001), Ch. 8-9
#
# Reproducibility: numpy 2.4.2, Python 3.14.2, macOS Darwin 24.6.0
# No random seeds needed for deterministic tests; random tests use explicit
# seeds passed by caller.

import numpy as np

# ============================================================================
# Octonion Arithmetic
# ============================================================================

# Fano multiplication table.
# Convention: e_1 * e_2 = e_4.
# The 7 Fano triples (i, j, k) with e_i * e_j = +e_k:
#   (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)
FANO_TRIPLES = [
    (1, 2, 4),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 7),
    (5, 6, 1),
    (6, 7, 2),
    (7, 1, 3),
]

# Build the full multiplication table for imaginary units.
# _MUL_TABLE[i][j] = (sign, index) meaning e_i * e_j = sign * e_{index}
# for i, j in {1,...,7}.  Index 0 means the real part.
_MUL_TABLE = {}
for i in range(1, 8):
    for j in range(1, 8):
        _MUL_TABLE[(i, j)] = (0, 0)  # will be filled

for i, j, k in FANO_TRIPLES:
    # e_i * e_j = +e_k
    _MUL_TABLE[(i, j)] = (+1, k)
    # e_j * e_i = -e_k  (anticommutativity of distinct imaginary units)
    _MUL_TABLE[(j, i)] = (-1, k)
    # Cyclic: e_j * e_k = +e_i
    _MUL_TABLE[(j, k)] = (+1, i)
    _MUL_TABLE[(k, j)] = (-1, i)
    # Cyclic: e_k * e_i = +e_j
    _MUL_TABLE[(k, i)] = (+1, j)
    _MUL_TABLE[(i, k)] = (-1, j)

# e_i * e_i = -1 (real part) for all i in {1,...,7}
for i in range(1, 8):
    _MUL_TABLE[(i, i)] = (-1, 0)


class Octonion:
    """Octonion represented as 8-component real array.

    a = a[0] + a[1]*e_1 + ... + a[7]*e_7

    Multiplication follows the Fano plane with e_1*e_2 = e_4.
    """

    __slots__ = ('c',)

    def __init__(self, components=None):
        if components is None:
            self.c = np.zeros(8, dtype=np.float64)
        else:
            self.c = np.asarray(components, dtype=np.float64).copy()
            if self.c.shape != (8,):
                raise ValueError(f"Octonion needs 8 components, got {self.c.shape}")

    @staticmethod
    def basis(i):
        """Return the i-th basis element (e_0=1, e_1, ..., e_7)."""
        c = np.zeros(8, dtype=np.float64)
        c[i] = 1.0
        return Octonion(c)

    @staticmethod
    def random(rng=None):
        """Random octonion with standard normal components."""
        if rng is None:
            rng = np.random.default_rng()
        return Octonion(rng.standard_normal(8))

    def __repr__(self):
        return f"Octonion({self.c})"

    def __add__(self, other):
        return Octonion(self.c + other.c)

    def __sub__(self, other):
        return Octonion(self.c - other.c)

    def __neg__(self):
        return Octonion(-self.c)

    def __rmul__(self, scalar):
        """Scalar multiplication: scalar * octonion."""
        return Octonion(scalar * self.c)

    def __mul__(self, other):
        """Octonion multiplication using the Fano table."""
        a, b = self.c, other.c
        result = np.zeros(8, dtype=np.float64)

        # Real * Real
        result[0] += a[0] * b[0]

        # Real * Imaginary and Imaginary * Real
        for i in range(1, 8):
            result[i] += a[0] * b[i]
            result[i] += a[i] * b[0]

        # Imaginary * Imaginary: use multiplication table
        for i in range(1, 8):
            if a[i] == 0.0:
                continue
            for j in range(1, 8):
                if b[j] == 0.0:
                    continue
                sign, k = _MUL_TABLE[(i, j)]
                result[k] += sign * a[i] * b[j]

        return Octonion(result)

    def conjugate(self):
        """Octonion conjugate: negate all imaginary parts."""
        c = self.c.copy()
        c[1:] = -c[1:]
        return Octonion(c)

    def norm_sq(self):
        """Squared norm: |a|^2 = sum(a_i^2) = a * conj(a) (real part)."""
        return np.dot(self.c, self.c)

    def norm(self):
        """Norm: |a| = sqrt(sum(a_i^2))."""
        return np.sqrt(self.norm_sq())

    def real_part(self):
        """Real (scalar) component a_0."""
        return self.c[0]

    def imag_part(self):
        """Imaginary part as Octonion (a_0 set to 0)."""
        c = self.c.copy()
        c[0] = 0.0
        return Octonion(c)

    def components(self):
        """Return the 8-component array (read-only view)."""
        return self.c


# ============================================================================
# h_3(O) Jordan Algebra
# ============================================================================

# Zero octonion for convenience.
O_ZERO = Octonion()


class H3O:
    """Element of h_3(O), the exceptional Jordan algebra.

    Represented as (alpha, beta, gamma, x1, x2, x3) where:
      alpha, beta, gamma: real scalars (diagonal entries)
      x1, x2, x3: Octonion (off-diagonal entries)

    The corresponding 3x3 Hermitian octonionic matrix is:
        | alpha    conj(x3)  x2       |
        | x3       beta      conj(x1) |
        | conj(x2) x1        gamma    |
    """

    __slots__ = ('alpha', 'beta', 'gamma', 'x1', 'x2', 'x3')

    def __init__(self, alpha=0.0, beta=0.0, gamma=0.0,
                 x1=None, x2=None, x3=None):
        self.alpha = float(alpha)
        self.beta = float(beta)
        self.gamma = float(gamma)
        self.x1 = x1 if x1 is not None else Octonion()
        self.x2 = x2 if x2 is not None else Octonion()
        self.x3 = x3 if x3 is not None else Octonion()

    @staticmethod
    def random(rng=None):
        """Random h_3(O) element with standard normal entries."""
        if rng is None:
            rng = np.random.default_rng()
        return H3O(
            alpha=rng.standard_normal(),
            beta=rng.standard_normal(),
            gamma=rng.standard_normal(),
            x1=Octonion.random(rng),
            x2=Octonion.random(rng),
            x3=Octonion.random(rng),
        )

    @staticmethod
    def E11():
        """The rank-1 idempotent E_{11} = diag(1,0,0)."""
        return H3O(alpha=1.0)

    def __add__(self, other):
        return H3O(
            self.alpha + other.alpha,
            self.beta + other.beta,
            self.gamma + other.gamma,
            self.x1 + other.x1,
            self.x2 + other.x2,
            self.x3 + other.x3,
        )

    def __sub__(self, other):
        return H3O(
            self.alpha - other.alpha,
            self.beta - other.beta,
            self.gamma - other.gamma,
            self.x1 - other.x1,
            self.x2 - other.x2,
            self.x3 - other.x3,
        )

    def __rmul__(self, scalar):
        """Scalar multiplication."""
        s = float(scalar)
        return H3O(
            s * self.alpha,
            s * self.beta,
            s * self.gamma,
            s * self.x1,
            s * self.x2,
            s * self.x3,
        )

    def norm(self):
        """Frobenius-like norm: sqrt(sum of squared components)."""
        return np.sqrt(
            self.alpha**2 + self.beta**2 + self.gamma**2
            + self.x1.norm_sq() + self.x2.norm_sq() + self.x3.norm_sq()
        )

    def to_vector(self):
        """Flatten to R^27 vector: (alpha, beta, gamma, x1[0:8], x2[0:8], x3[0:8])."""
        return np.concatenate([
            [self.alpha, self.beta, self.gamma],
            self.x1.c, self.x2.c, self.x3.c,
        ])

    @staticmethod
    def from_vector(v):
        """Reconstruct H3O from R^27 vector."""
        return H3O(
            alpha=v[0], beta=v[1], gamma=v[2],
            x1=Octonion(v[3:11]),
            x2=Octonion(v[11:19]),
            x3=Octonion(v[19:27]),
        )

    def __repr__(self):
        return (f"H3O(alpha={self.alpha}, beta={self.beta}, gamma={self.gamma}, "
                f"x1={self.x1}, x2={self.x2}, x3={self.x3})")


def _mat_mul_h3o(A, B):
    """Compute the 3x3 octonionic matrix product AB.

    Each entry (AB)_{ij} = sum_k A_{ik} * B_{kj} involves only single
    octonion products (2 factors), so Artin's theorem guarantees
    associativity is not an issue.

    We extract the 3x3 matrices from H3O representation:
        A = | A.alpha    conj(A.x3)  A.x2       |
            | A.x3       A.beta      conj(A.x1)  |
            | conj(A.x2) A.x1        A.gamma     |

    Returns the entries of the product as a tuple:
        (M11, M12, M13, M21, M22, M23, M31, M32, M33)
    where each Mij is an Octonion.
    """
    # Build real-valued diagonal octonions
    aA = Octonion(np.array([A.alpha, 0, 0, 0, 0, 0, 0, 0]))
    bA = Octonion(np.array([A.beta, 0, 0, 0, 0, 0, 0, 0]))
    gA = Octonion(np.array([A.gamma, 0, 0, 0, 0, 0, 0, 0]))
    aB = Octonion(np.array([B.alpha, 0, 0, 0, 0, 0, 0, 0]))
    bB = Octonion(np.array([B.beta, 0, 0, 0, 0, 0, 0, 0]))
    gB = Octonion(np.array([B.gamma, 0, 0, 0, 0, 0, 0, 0]))

    # Off-diagonal entries
    x1A, x2A, x3A = A.x1, A.x2, A.x3
    x1B, x2B, x3B = B.x1, B.x2, B.x3
    cx1A, cx2A, cx3A = x1A.conjugate(), x2A.conjugate(), x3A.conjugate()
    cx1B, cx2B, cx3B = x1B.conjugate(), x2B.conjugate(), x3B.conjugate()

    # Row 1: A[1,k] = (aA, cx3A, x2A)
    # Col j: B[k,j]
    # (1,1): aA*aB + cx3A*x3B + x2A*cx2B
    M11 = aA * aB + cx3A * x3B + x2A * cx2B
    # (1,2): aA*cx3B + cx3A*bB + x2A*x1B
    M12 = aA * cx3B + cx3A * bB + x2A * x1B
    # (1,3): aA*x2B + cx3A*cx1B + x2A*gB
    M13 = aA * x2B + cx3A * cx1B + x2A * gB

    # Row 2: A[2,k] = (x3A, bA, cx1A)
    # (2,1): x3A*aB + bA*x3B + cx1A*cx2B
    M21 = x3A * aB + bA * x3B + cx1A * cx2B
    # (2,2): x3A*cx3B + bA*bB + cx1A*x1B
    M22 = x3A * cx3B + bA * bB + cx1A * x1B
    # (2,3): x3A*x2B + bA*cx1B + cx1A*gB
    M23 = x3A * x2B + bA * cx1B + cx1A * gB

    # Row 3: A[3,k] = (cx2A, x1A, gA)
    # (3,1): cx2A*aB + x1A*x3B + gA*cx2B
    M31 = cx2A * aB + x1A * x3B + gA * cx2B
    # (3,2): cx2A*cx3B + x1A*bB + gA*x1B
    M32 = cx2A * cx3B + x1A * bB + gA * x1B
    # (3,3): cx2A*x2B + x1A*cx1B + gA*gB
    M33 = cx2A * x2B + x1A * cx1B + gA * gB

    return M11, M12, M13, M21, M22, M23, M31, M32, M33


def _extract_h3o(M11, M12, M13, M21, M22, M23, M31, M32, M33):
    """Extract the Hermitian part from a 3x3 octonionic matrix.

    For a product AB where A, B are Hermitian, the result AB is NOT
    generally Hermitian. But for the Jordan product (AB + BA)/2, the
    sum IS Hermitian.

    We extract the h_3(O) coordinates (alpha, beta, gamma, x1, x2, x3)
    from the matrix:
        | alpha    conj(x3)  x2       |
        | x3       beta      conj(x1) |
        | conj(x2) x1        gamma    |

    For the diagonal: take real part of M_{ii}.
    For off-diagonal: x3 = M_{21}, x2 = M_{13}, x1 = M_{32}.
    """
    alpha = M11.real_part()
    beta = M22.real_part()
    gamma = M33.real_part()
    # x3 lives at position (2,1), x2 at (1,3), x1 at (3,2)
    x1 = Octonion(M32.c.copy())
    x2 = Octonion(M13.c.copy())
    x3 = Octonion(M21.c.copy())
    return H3O(alpha, beta, gamma, x1, x2, x3)


def jordan_product(A, B):
    """Jordan product A . B = (1/2)(AB + BA) for A, B in h_3(O).

    The result is guaranteed to be in h_3(O) (Hermitian) because
    (AB + BA)^* = B^*A^* + A^*B^* = BA + AB for Hermitian A, B.
    """
    # Compute AB
    AB = _mat_mul_h3o(A, B)
    # Compute BA
    BA = _mat_mul_h3o(B, A)

    # Sum entry-by-entry and divide by 2
    S = []
    for ab_ij, ba_ij in zip(AB, BA):
        S.append(ab_ij + ba_ij)

    result = _extract_h3o(*S)

    # Apply the 1/2 factor
    return 0.5 * result


# ============================================================================
# Peirce Projections under E_{11}
# ============================================================================

def peirce_V1(X):
    """Project onto V_1 = R * E_{11}: extract alpha component."""
    return H3O(alpha=X.alpha)


def peirce_Vhalf(X):
    """Project onto V_{1/2} = O^2: extract (x2, x3) components."""
    return H3O(x2=Octonion(X.x2.c.copy()), x3=Octonion(X.x3.c.copy()))


def peirce_V0(X):
    """Project onto V_0 = h_2(O): extract (beta, gamma, x1) components."""
    return H3O(beta=X.beta, gamma=X.gamma, x1=Octonion(X.x1.c.copy()))


# ============================================================================
# L_{E_{11}} operator
# ============================================================================

def L_E11(X):
    """Multiplication operator L_{E_{11}}(X) = E_{11} . X."""
    return jordan_product(H3O.E11(), X)


def L_E11_matrix_on_Vhalf():
    """Compute the 16x16 matrix of L_{E_{11}} restricted to V_{1/2}.

    Basis of V_{1/2}: v_k^(2) has x2 = e_k (k=0..7), all else zero.
                      v_k^(3) has x3 = e_k (k=0..7), all else zero.
    Ordering: [v_0^(2), ..., v_7^(2), v_0^(3), ..., v_7^(3)].

    Returns: 16x16 numpy array M where M[:,j] is the coordinate vector
    of Pi_{1/2}(E_{11} . v_j) in the V_{1/2} basis.
    """
    M = np.zeros((16, 16), dtype=np.float64)

    for j in range(16):
        # Construct basis vector v_j
        if j < 8:
            # v_j^(2): x2 = e_j
            v_j = H3O(x2=Octonion.basis(j))
        else:
            # v_{j-8}^(3): x3 = e_{j-8}
            v_j = H3O(x3=Octonion.basis(j - 8))

        # Apply L_{E_{11}}
        Lv = L_E11(v_j)

        # Project onto V_{1/2}
        Lv_half = peirce_Vhalf(Lv)

        # Extract coordinates in V_{1/2} basis
        # First 8: x2 components, next 8: x3 components
        M[:8, j] = Lv_half.x2.c
        M[8:, j] = Lv_half.x3.c

    return M


def Vhalf_basis_vectors():
    """Return the 16 basis vectors of V_{1/2} as H3O elements."""
    basis = []
    for k in range(8):
        basis.append(H3O(x2=Octonion.basis(k)))
    for k in range(8):
        basis.append(H3O(x3=Octonion.basis(k)))
    return basis


# ============================================================================
# V_0 = h_2(O) Peirce operators on V_{1/2}  [Plan 02, ALGV-02]
# ============================================================================
#
# V_0 basis (Spin(9)-adapted, 10 elements):
#   b_1 = (1/2)(E_{22} + E_{33})  -- trace element of h_2(O)
#   b_2 = (1/2)(E_{22} - E_{33})  -- traceless diagonal
#   b_{k+3} for k=0,...,7: x_1 = e_k, all else zero (off-diagonal)
#
# T_b: V_{1/2} -> V_{1/2} defined by T_b(v) = Pi_{1/2}(b . v)
# where . is the Jordan product in h_3(O).


def V0_basis_elements():
    """Return the 10 Spin(9)-adapted basis elements of V_0 = h_2(O).

    Returns list of 10 H3O elements:
      b[0] = (1/2)(E_{22} + E_{33})  (trace)
      b[1] = (1/2)(E_{22} - E_{33})  (traceless diagonal)
      b[2..9] = x_1 = e_k for k=0,...,7  (off-diagonal)
    """
    basis = []
    # b_1: trace element (1/2)(E22 + E33)
    basis.append(H3O(beta=0.5, gamma=0.5))
    # b_2: traceless diagonal (1/2)(E22 - E33)
    basis.append(H3O(beta=0.5, gamma=-0.5))
    # b_3 through b_10: off-diagonal x_1 = e_k
    for k in range(8):
        basis.append(H3O(x1=Octonion.basis(k)))
    return basis


def compute_T_b_matrix(b):
    """Compute the 16x16 matrix of T_b: V_{1/2} -> V_{1/2}.

    T_b(v) = Pi_{1/2}(b . v) where b is in V_0 and v in V_{1/2}.

    Parameters:
        b: H3O element in V_0

    Returns:
        16x16 numpy array M where M[:,j] is T_b(v_j) in V_{1/2} basis.
    """
    vhalf_basis = Vhalf_basis_vectors()
    M = np.zeros((16, 16), dtype=np.float64)

    for j, v_j in enumerate(vhalf_basis):
        # Jordan product b . v_j
        prod = jordan_product(b, v_j)
        # Project onto V_{1/2}
        prod_half = peirce_Vhalf(prod)
        # Extract coordinates
        M[:8, j] = prod_half.x2.c
        M[8:, j] = prod_half.x3.c

    return M


def compute_T_b_matrices():
    """Compute all 10 Peirce operator matrices T_{b_i}: V_{1/2} -> V_{1/2}.

    Returns:
        List of 10 numpy arrays, each 16x16.
    """
    return [compute_T_b_matrix(b) for b in V0_basis_elements()]


def compute_T_b_full_products(b, vhalf_basis=None):
    """Compute full Jordan products b . v_j (before projection).

    Returns list of 16 H3O elements (the full products, not just V_{1/2} part).
    Useful for checking Peirce rule: V_1 and V_0 components should be zero.
    """
    if vhalf_basis is None:
        vhalf_basis = Vhalf_basis_vectors()
    return [jordan_product(b, v_j) for v_j in vhalf_basis]


def krasnov_J_u_matrix():
    """Construct Krasnov's J_u as a 16x16 matrix on V_{1/2}.

    J_u acts on V_{1/2} = O^2 by left multiplication by u = e_7:
        J_u(x_2, x_3) = (e_7 * x_2, e_7 * x_3)

    The matrix is expressed in the basis (x_2^0,...,x_2^7, x_3^0,...,x_3^7).

    Returns:
        16x16 numpy array.
    """
    e7 = Octonion.basis(7)
    M = np.zeros((16, 16), dtype=np.float64)

    for j in range(16):
        if j < 8:
            # Basis vector has x_2 = e_j, x_3 = 0
            # J_u maps to (e_7 * e_j, 0)
            result = e7 * Octonion.basis(j)
            M[:8, j] = result.c
        else:
            # Basis vector has x_2 = 0, x_3 = e_{j-8}
            # J_u maps to (0, e_7 * e_{j-8})
            result = e7 * Octonion.basis(j - 8)
            M[8:, j] = result.c

    return M


def search_j_squared_linear(T_matrices):
    """Search for J^2 = -Id in the span of T_b operators.

    The condition T(c)^2 = -Id becomes sum c_i c_j S_{ij} = -Id
    where S_{ij} = (1/2)(T_i T_j + T_j T_i).

    This function:
    1. Computes all S_{ij} (symmetric products)
    2. Checks the linear system feasibility
    3. Returns analysis results

    Parameters:
        T_matrices: list of 10 numpy arrays (16x16)

    Returns:
        dict with keys:
          'S_matrices': 10x10 array of 16x16 matrices
          'linear_feasible': bool (does A @ q = b have a solution?)
          'linear_residual': float (min ||A @ q - b||)
          'linear_solution': array or None
          'rank_A': int
    """
    n = len(T_matrices)
    # Compute S_{ij} = (1/2)(T_i T_j + T_j T_i) for upper triangle
    S = {}
    for i in range(n):
        for j in range(i, n):
            S[(i, j)] = 0.5 * (T_matrices[i] @ T_matrices[j]
                                + T_matrices[j] @ T_matrices[i])
            if i != j:
                S[(j, i)] = S[(i, j)]

    # Build the linear system: sum c_i c_j S_{ij} = -I_{16}
    # Flatten S_{ij} to 256-vectors.  Upper triangle indices for q.
    # q has n*(n+1)/2 = 55 independent components.
    n_upper = n * (n + 1) // 2
    A = np.zeros((256, n_upper), dtype=np.float64)
    col = 0
    index_map = []  # maps column to (i,j)
    for i in range(n):
        for j in range(i, n):
            # Coefficient: if i==j, c_i^2 contributes S_{ii};
            # if i!=j, c_i*c_j contributes 2*S_{ij} (since q_{ij}=c_i c_j
            # but we store only upper triangle with factor 2 for off-diag)
            if i == j:
                A[:, col] = S[(i, j)].flatten()
            else:
                A[:, col] = 2.0 * S[(i, j)].flatten()
            index_map.append((i, j))
            col += 1

    b = -np.eye(16).flatten()

    # Solve least-squares
    result_lstsq = np.linalg.lstsq(A, b, rcond=None)
    q_sol = result_lstsq[0]
    residual_vec = A @ q_sol - b
    residual = np.linalg.norm(residual_vec)
    rank_A = result_lstsq[2]

    return {
        'S_matrices': S,
        'linear_feasible': residual < 1e-10,
        'linear_residual': residual,
        'linear_solution': q_sol if residual < 1e-10 else None,
        'rank_A': int(rank_A),
        'A_matrix': A,
        'b_vector': b,
    }


def search_j_squared_individual(T_matrices):
    """Check if any individual T_{b_i}^2 = -Id.

    Returns:
        List of dicts, one per T_b, with eigenvalues of T_b^2.
    """
    results = []
    for i, T in enumerate(T_matrices):
        T_sq = T @ T
        evals = np.linalg.eigvalsh(T_sq) if np.allclose(T_sq, T_sq.T) else np.linalg.eigvals(T_sq)
        evals = np.sort(np.real(evals))
        is_minus_id = np.allclose(T_sq, -np.eye(16), atol=1e-12)
        results.append({
            'index': i,
            'eigenvalues_T_sq': evals,
            'is_minus_id': is_minus_id,
        })
    return results


def check_ju_in_span(T_matrices, J_u=None):
    """Test if Krasnov's J_u lies in span({T_b}).

    Solves min_c ||sum c_i T_i - J_u||_F via least-squares.

    Returns:
        dict with 'residual', 'coefficients', 'in_span' (bool)
    """
    if J_u is None:
        J_u = krasnov_J_u_matrix()

    # Flatten
    n = len(T_matrices)
    B = np.zeros((256, n), dtype=np.float64)
    for i, T in enumerate(T_matrices):
        B[:, i] = T.flatten()

    ju_flat = J_u.flatten()
    result = np.linalg.lstsq(B, ju_flat, rcond=None)
    c = result[0]
    residual_vec = B @ c - ju_flat
    residual = np.linalg.norm(residual_vec)

    return {
        'residual': residual,
        'coefficients': c,
        'in_span': residual < 1e-12,
    }


def compute_commutator_algebra(T_matrices, max_iterations=5):
    """Compute the Lie algebra generated by {T_b_i}.

    Iteratively computes commutators until the space closes.

    Returns:
        dict with 'dimension', 'basis' (list of 16x16 matrices),
        'closed' (bool), 'iterations' (int)
    """
    # Start with the T_b matrices themselves
    basis = []
    for T in T_matrices:
        basis.append(T.flatten())

    basis_matrix = np.array(basis).T  # 256 x n
    dim = np.linalg.matrix_rank(basis_matrix, tol=1e-10)

    # Orthonormalize
    U, s, Vt = np.linalg.svd(basis_matrix, full_matrices=False)
    current_basis = U[:, :dim]  # 256 x dim, orthonormal columns

    for iteration in range(max_iterations):
        new_elements = []
        n_basis = current_basis.shape[1]

        for i in range(n_basis):
            for j in range(i + 1, n_basis):
                Mi = current_basis[:, i].reshape(16, 16)
                Mj = current_basis[:, j].reshape(16, 16)
                comm = Mi @ Mj - Mj @ Mi
                comm_flat = comm.flatten()
                new_elements.append(comm_flat)

        if not new_elements:
            return {
                'dimension': current_basis.shape[1],
                'basis': current_basis,
                'closed': True,
                'iterations': iteration,
            }

        # Add new elements and re-check rank
        new_matrix = np.column_stack([current_basis] + [np.array(new_elements).T])
        new_dim = np.linalg.matrix_rank(new_matrix, tol=1e-10)

        if new_dim == current_basis.shape[1]:
            # Closed!
            return {
                'dimension': new_dim,
                'basis': current_basis,
                'closed': True,
                'iterations': iteration + 1,
            }

        # Expand basis
        U, s, Vt = np.linalg.svd(new_matrix, full_matrices=False)
        current_basis = U[:, :new_dim]

    return {
        'dimension': current_basis.shape[1],
        'basis': current_basis,
        'closed': False,
        'iterations': max_iterations,
    }
