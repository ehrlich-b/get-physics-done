# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   peirce_decomposition=under_E11,
#   v_half_basis=(x2_0..x2_7,x3_0..x3_7),
#   clifford_signature=Cl(9,0)_gamma_i_sq=+I,
#   clifford_normalization=gamma_1=4*T_b[1]_gamma_k=2*T_b[k]_for_k=2..9
#
# Phase 28, Plan 01: Octonion arithmetic, h_3(O) Jordan product, Peirce
# projections, and L_{E_{11}} computation.
# Phase 28, Plan 02: V_0 channel operators, ALGV-02.
# Phase 29, Plan 01: Associative closure, volume element, J_u diagnostics.
# Phase 29, Plan 02: J_u polynomial, uniqueness, G_SM commutant, Spin(10).
#
# ALGV-01 RESULT: L_{E_{11}} = (1/2)*I_{16} on V_{1/2} (exact, zero error).
# ALGV-02 RESULT: V_0 channel NEGATIVE (T_b symmetric, J_u antisymmetric).
# ALGV-03 RESULT: Associative closure = M_16(R) (256-dim, full matrix algebra).
#
# References:
#   Baez, "The Octonions," Bull. AMS 39 (2002), Sec. 3.4
#   Alfsen-Shultz, State Spaces of Operator Algebras (2001), Ch. 8-9
#   Lawson-Michelsohn, Spin Geometry (1989), Table I.4.3
#   Krasnov, J. Math. Phys. 62 (2021) 021703, arXiv:1912.11282
#   Boyle, arXiv:2006.16265
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


# ============================================================================
# Phase 29, Plan 01: Associative closure, volume element, J_u diagnostics
# ============================================================================
#
# The associative algebra generated by {T_b} is the closure under matrix
# multiplication (not just commutators). For Cl(9,0) = M_16(R) + M_16(R),
# the irrep on R^16 is surjective onto M_16(R) = End(R^16), so the
# associative closure should be exactly 256-dimensional.
#
# Clifford rescaling (from Phase 28):
#   {T_b[1], T_b[1]} = (1/8)*I  =>  gamma_1 = 4*T_b[1]
#   {T_b[k], T_b[k]} = (1/2)*I  =>  gamma_k = 2*T_b[k] for k=2,...,9
#   Then {gamma_i, gamma_j} = 2*delta_{ij}*I_{16} (standard Cl(9,0)).


def rescale_to_clifford_generators(T_matrices):
    """Rescale the 9 traceless T_b operators to standard Clifford generators.

    gamma_1 = 4*T_b[1]  (diagonal traceless, eigenvalues +/-0.25)
    gamma_k = 2*T_b[k]  for k=2,...,9  (off-diagonal, eigenvalues +/-0.5)

    These satisfy {gamma_i, gamma_j} = 2*delta_{ij}*I_{16}, i.e., Cl(9,0).

    Parameters:
        T_matrices: list of 10 T_b matrices (T_matrices[0] = (1/4)*I trace element,
                    T_matrices[1..9] = 9 traceless generators)

    Returns:
        List of 9 numpy arrays (16x16), the Clifford generators.
    """
    gammas = [4.0 * T_matrices[1]]
    for k in range(2, 10):
        gammas.append(2.0 * T_matrices[k])
    return gammas


def compute_associative_closure(T_matrices, J_u=None, max_depth=10):
    """Compute the associative algebra generated by {T_b} on V_{1/2} = R^16.

    Starting from the 10 T_b matrices, iteratively computes all products
    A*B where A is a newly-added basis element and B is an original generator.
    Tracks dimension growth at each depth and optionally tests J_u membership.

    Parameters:
        T_matrices: list of 10 numpy arrays (16x16), the Peirce operators
        J_u: optional 16x16 matrix to test for membership at each depth
        max_depth: maximum iteration depth (default 10)

    Returns:
        dict with keys:
          'dimensions': list of int (dim at each depth)
          'ju_residuals': list of float (J_u residual at each depth, or [] if J_u is None)
          'ju_depth': int or None (first depth where J_u residual < 1e-12)
          'basis': numpy array of shape (rank, 256) -- orthonormal basis vectors (flattened 16x16)
          'converged_depth': int (depth at which dimension stabilized)
    """
    n_gen = len(T_matrices)
    generators_flat = [T.flatten() for T in T_matrices]
    ju_flat = J_u.flatten() if J_u is not None else None

    # Depth 0: span of the 10 generators
    all_vectors = np.array(generators_flat).T  # 256 x 10
    U, s, Vt = np.linalg.svd(all_vectors, full_matrices=False)
    rank = np.sum(s > 1e-10)
    current_basis = U[:, :rank]  # 256 x rank, orthonormal

    dimensions = [rank]
    ju_residuals = []
    ju_depth = None

    # Test J_u membership at depth 0
    if ju_flat is not None:
        coeffs, res, _, _ = np.linalg.lstsq(current_basis, ju_flat, rcond=None)
        residual = np.linalg.norm(ju_flat - current_basis @ coeffs)
        ju_residuals.append(residual)
        if residual < 1e-12:
            ju_depth = 0

    # Track which basis vectors are "new" at each depth
    # At depth 0, all basis vectors are new
    new_start_col = 0
    new_end_col = rank

    for depth in range(1, max_depth + 1):
        # Multiply NEW basis vectors (columns new_start_col..new_end_col-1)
        # by all 10 original generators
        new_products = []
        for col_idx in range(new_start_col, new_end_col):
            basis_mat = current_basis[:, col_idx].reshape(16, 16)
            for gen_idx in range(n_gen):
                gen_mat = T_matrices[gen_idx]
                # Product A*B
                prod = (basis_mat @ gen_mat).flatten()
                new_products.append(prod)
                # Product B*A
                prod2 = (gen_mat @ basis_mat).flatten()
                new_products.append(prod2)

        if not new_products:
            break

        # Add new products to current basis and re-compute rank
        new_matrix = np.column_stack(
            [current_basis] + [np.array(new_products).T]
        )
        U, s, Vt = np.linalg.svd(new_matrix, full_matrices=False)
        new_rank = np.sum(s > 1e-10)

        if new_rank == rank:
            # Converged -- no new dimensions added
            dimensions.append(new_rank)
            if ju_flat is not None:
                coeffs, res, _, _ = np.linalg.lstsq(current_basis, ju_flat, rcond=None)
                residual = np.linalg.norm(ju_flat - current_basis @ coeffs)
                ju_residuals.append(residual)
                if residual < 1e-12 and ju_depth is None:
                    ju_depth = depth
            break

        # Update basis
        old_rank = rank
        rank = new_rank
        current_basis = U[:, :rank]
        dimensions.append(rank)

        # New basis vectors are columns old_rank..rank-1
        new_start_col = old_rank
        new_end_col = rank

        # Test J_u membership
        if ju_flat is not None:
            coeffs, res, _, _ = np.linalg.lstsq(current_basis, ju_flat, rcond=None)
            residual = np.linalg.norm(ju_flat - current_basis @ coeffs)
            ju_residuals.append(residual)
            if residual < 1e-12 and ju_depth is None:
                ju_depth = depth

    converged_depth = len(dimensions) - 1

    return {
        'dimensions': dimensions,
        'ju_residuals': ju_residuals,
        'ju_depth': ju_depth,
        'basis': current_basis,
        'converged_depth': converged_depth,
    }


def compute_volume_element(gamma_matrices):
    """Compute the Cl(9,0) volume element omega = gamma_1 * ... * gamma_9.

    For Cl(9,0) on R^16, omega^2 = (-1)^{9*8/2} * I = (-1)^{36} * I = +I.
    Since the representation is irreducible and n=9 is odd, omega = +I or -I
    on the irrep.

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16), the Clifford generators

    Returns:
        dict with keys:
          'omega': 16x16 matrix (the volume element)
          'omega_squared_error': float (Frobenius norm of omega^2 - I)
          'eigenvalues': sorted array of eigenvalues
          'which_factor': "+1" if all eigenvalues +1, "-1" if all -1, "mixed" otherwise
    """
    omega = np.eye(16, dtype=np.float64)
    for g in gamma_matrices:
        omega = omega @ g

    omega_sq = omega @ omega
    omega_sq_error = np.linalg.norm(omega_sq - np.eye(16), 'fro')

    eigenvalues = np.sort(np.linalg.eigvalsh(omega))

    if np.allclose(eigenvalues, 1.0, atol=1e-12):
        which_factor = "+1"
    elif np.allclose(eigenvalues, -1.0, atol=1e-12):
        which_factor = "-1"
    else:
        which_factor = "mixed"

    return {
        'omega': omega,
        'omega_squared_error': omega_sq_error,
        'eigenvalues': eigenvalues,
        'which_factor': which_factor,
    }


def compute_ju_anticommutation(gamma_matrices, J_u):
    """Compute anticommutation and commutation of J_u with all Clifford generators.

    For each gamma_i (i=1,...,9):
      anticommutator: {J_u, gamma_i} = J_u @ gamma_i + gamma_i @ J_u
      commutator:     [J_u, gamma_i] = J_u @ gamma_i - gamma_i @ J_u

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16)
        J_u: 16x16 numpy array

    Returns:
        dict with keys:
          'anticommutators': list of 9 matrices
          'anticommutator_norms': list of 9 floats (Frobenius norms)
          'commutators': list of 9 matrices
          'commutator_norms': list of 9 floats
          'all_anticommute': True if all anticommutator norms < 1e-14
          'pattern': list of "anticommutes" / "commutes" / "neither" for each
    """
    anticommutators = []
    anticomm_norms = []
    commutators = []
    comm_norms = []
    pattern = []

    for g in gamma_matrices:
        ac = J_u @ g + g @ J_u
        cm = J_u @ g - g @ J_u
        ac_norm = np.linalg.norm(ac, 'fro')
        cm_norm = np.linalg.norm(cm, 'fro')

        anticommutators.append(ac)
        anticomm_norms.append(ac_norm)
        commutators.append(cm)
        comm_norms.append(cm_norm)

        if ac_norm < 1e-14:
            pattern.append("anticommutes")
        elif cm_norm < 1e-14:
            pattern.append("commutes")
        else:
            pattern.append("neither")

    return {
        'anticommutators': anticommutators,
        'anticommutator_norms': anticomm_norms,
        'commutators': commutators,
        'commutator_norms': comm_norms,
        'all_anticommute': all(n < 1e-14 for n in anticomm_norms),
        'pattern': pattern,
    }


def compute_grade_decomposition(target_matrix, gamma_matrices):
    """Decompose a 16x16 matrix into Clifford grade components.

    For Cl(9,0) with 9 generators on R^16, the volume element omega =
    gamma_1*...*gamma_9 satisfies omega = +I (verified numerically).
    This means gamma_{S^c} = epsilon_S * gamma_S, so monomials of grades
    k and 9-k are identified, giving 256 independent matrices (grades 0-4).

    Since omega = +I, the 256 monomials of grade 0 through 4 form a basis
    for M_16(R). The decomposition solves the linear system directly.

    For grade reporting, we report grades 0-4 from the linear solve plus
    the implied grades 5-9 (which are determined by the omega identification).

    Parameters:
        target_matrix: 16x16 numpy array to decompose
        gamma_matrices: list of 9 numpy arrays (16x16), the Clifford generators

    Returns:
        dict with keys:
          'coefficients': dict mapping frozenset(S) -> float (for |S| = 0..4)
          'grade_norms': list of 5 floats (L2 norm of coefficients at each grade 0..4)
          'dominant_grade': int (grade 0-4 with largest coefficient norm)
          'reconstruction_error': float (|target - reconstruction|)
          'nonzero_grades': list of (grade, count) for grades with nonzero coefficients
    """
    from itertools import combinations

    n = len(gamma_matrices)  # 9

    # Build basis from grade 0-4 monomials (256 total = sum C(9,k) for k=0..4)
    basis_matrices = []
    basis_labels = []
    grade_ranges = []  # (start, end) index for each grade

    idx = 0
    for k in range(5):
        start = idx
        for subset in combinations(range(n), k):
            S = frozenset(subset)
            gamma_S = np.eye(16, dtype=np.float64)
            for i in sorted(subset):
                gamma_S = gamma_S @ gamma_matrices[i]
            basis_matrices.append(gamma_S)
            basis_labels.append(S)
            idx += 1
        grade_ranges.append((start, idx))

    # Stack as columns: B is 256 x 256
    B = np.array([m.flatten() for m in basis_matrices]).T

    # Solve for coefficients
    coeffs = np.linalg.solve(B, target_matrix.flatten())

    # Reconstruction check
    reconstruction = (B @ coeffs).reshape(16, 16)
    reconstruction_error = np.linalg.norm(
        target_matrix - reconstruction, 'fro')

    # Build coefficient dict and grade norms
    coefficients = {}
    grade_norms = []
    nonzero_grades = []

    for k in range(5):
        start, end = grade_ranges[k]
        for i in range(start, end):
            coefficients[basis_labels[i]] = coeffs[i]

        grade_coeffs = coeffs[start:end]
        norm = np.linalg.norm(grade_coeffs)
        grade_norms.append(norm)

        n_nonzero = int(np.sum(np.abs(grade_coeffs) > 1e-14))
        if n_nonzero > 0:
            nonzero_grades.append((k, n_nonzero))

    dominant_grade = int(np.argmax(grade_norms))

    return {
        'coefficients': coefficients,
        'grade_norms': grade_norms,
        'dominant_grade': dominant_grade,
        'reconstruction_error': reconstruction_error,
        'nonzero_grades': nonzero_grades,
    }


def find_ju_depth(T_matrices, J_u=None):
    """Find the minimal associative closure depth at which J_u first appears.

    Wrapper around compute_associative_closure.

    Parameters:
        T_matrices: list of 10 T_b matrices
        J_u: optional 16x16 matrix (default: krasnov_J_u_matrix())

    Returns:
        int or None: the depth at which J_u joins the closure, or None if not found.
    """
    if J_u is None:
        J_u = krasnov_J_u_matrix()
    result = compute_associative_closure(T_matrices, J_u=J_u)
    return result['ju_depth']


# ============================================================================
# Phase 29, Plan 02: J_u polynomial, uniqueness, G_SM commutant, Spin(10)
# ============================================================================


def express_ju_as_clifford_polynomial(gamma_matrices, J_u):
    """Express J_u as an explicit polynomial in the Clifford generators.

    Uses compute_grade_decomposition to expand J_u = sum_S c_S gamma_S
    where gamma_S = ordered product of gamma_i for i in S, then extracts
    the nonzero terms and formats them as a polynomial.

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16)
        J_u: 16x16 numpy array

    Returns:
        dict with keys:
          'terms': list of (coefficient, sorted_subset_tuple) for |c_S| > 1e-10
          'n_nonzero': int (number of nonzero terms)
          'reconstruction_error': float
          'grade_2_terms': list of (coefficient, subset) for grade-2 terms
          'grade_3_terms': list of (coefficient, subset) for grade-3 terms
          'dominant_term': (coefficient, subset) with largest |c_S|
    """
    grade_result = compute_grade_decomposition(J_u, gamma_matrices)
    terms = []
    for S, c in grade_result['coefficients'].items():
        if abs(c) > 1e-10:
            terms.append((c, tuple(sorted(S))))
    terms.sort(key=lambda x: (len(x[1]), x[1]))

    grade_2 = [(c, s) for c, s in terms if len(s) == 2]
    grade_3 = [(c, s) for c, s in terms if len(s) == 3]
    dominant = max(terms, key=lambda x: abs(x[0])) if terms else None

    return {
        'terms': terms,
        'n_nonzero': len(terms),
        'reconstruction_error': grade_result['reconstruction_error'],
        'grade_2_terms': grade_2,
        'grade_3_terms': grade_3,
        'dominant_term': dominant,
    }


def test_ju_uniqueness(gamma_matrices, J_u):
    """Test uniqueness of J_u among elements sharing its algebraic properties.

    Finds all X in span{M_1,...,M_8} (the 8 Clifford monomials appearing
    in J_u's polynomial) satisfying X^2 = -I. The monomials are orthogonal
    under Tr(A^T B)/16 and all square to -I, but they do NOT mutually
    anticommute. So the constraint X^2 = -I for X = sum a_k M_k is:

      X^2 = -|a|^2 I + sum_{i<j} a_i a_j {M_i, M_j} = -I

    This requires |a|^2 = 1 AND sum_{i<j} a_i a_j {M_i, M_j} = 0.

    The Jacobian analysis at J_u's coefficients determines whether J_u
    is locally isolated (0-dim tangent space) or part of a family.

    Also computes the stabilizer of J_u in spin(9) = span{gamma_i gamma_j}.

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16)
        J_u: 16x16 numpy array

    Returns:
        dict with keys:
          'monomial_subspace_dim': 8 (number of monomials in J_u's polynomial)
          'tangent_dim_at_ju': int (local dimension of solution manifold)
          'is_isolated': bool (True if tangent_dim = 0)
          'ju_coefficients': array of 8 coefficients
          'norm_squared': float (should be 1.0)
          'constraint_residual': float (should be 0.0)
          'stabilizer_dim_spin9': int (dim of centralizer of J_u in spin(9))
    """
    from itertools import combinations

    # Build the 8 monomials from J_u's polynomial
    poly = express_ju_as_clifford_polynomial(gamma_matrices, J_u)
    terms = poly['terms']
    monomials = []
    coeffs_ju = []
    for c, subset in terms:
        M = np.eye(16, dtype=np.float64)
        for i in subset:
            M = M @ gamma_matrices[i]
        monomials.append(M)
        coeffs_ju.append(c)
    n_mono = len(monomials)
    a0 = np.array(coeffs_ju)

    # Verify |a|^2 = 1
    norm_sq = np.sum(a0**2)

    # Verify constraint: sum_{i<j} a_i a_j {M_i, M_j} = 0
    F_a0 = np.zeros((16, 16))
    for i in range(n_mono):
        for j in range(i + 1, n_mono):
            ac = monomials[i] @ monomials[j] + monomials[j] @ monomials[i]
            F_a0 += a0[i] * a0[j] * ac
    constraint_residual = np.linalg.norm(F_a0, 'fro')

    # Jacobian of the constraint at a0
    # F_k(a) = sum_{j != k} a_j {M_k, M_j}  (256 conditions per k)
    Jac = np.zeros((256, n_mono))
    for k in range(n_mono):
        deriv = np.zeros((16, 16))
        for j in range(n_mono):
            if j != k:
                deriv += a0[j] * (monomials[k] @ monomials[j]
                                  + monomials[j] @ monomials[k])
        Jac[:, k] = deriv.flatten()

    # Add unit sphere constraint: a . da = 0
    Jac_full = np.vstack([Jac, 2 * a0.reshape(1, -1)])
    rank_jac = np.linalg.matrix_rank(Jac_full, tol=1e-10)
    tangent_dim = n_mono - rank_jac

    # Stabilizer dimension in spin(9)
    spin9_gens = []
    for i in range(len(gamma_matrices)):
        for j in range(i + 1, len(gamma_matrices)):
            spin9_gens.append(gamma_matrices[i] @ gamma_matrices[j])

    comm_action = np.zeros((256, len(spin9_gens)))
    for k, L in enumerate(spin9_gens):
        comm = J_u @ L - L @ J_u
        comm_action[:, k] = comm.flatten()

    _, s_comm, _ = np.linalg.svd(comm_action, full_matrices=False)
    stab_dim = len(spin9_gens) - np.sum(s_comm > 1e-10)

    return {
        'monomial_subspace_dim': n_mono,
        'tangent_dim_at_ju': tangent_dim,
        'is_isolated': tangent_dim == 0,
        'ju_coefficients': a0,
        'norm_squared': norm_sq,
        'constraint_residual': constraint_residual,
        'stabilizer_dim_spin9': stab_dim,
    }


def compute_gsm_commutant(gamma_matrices, J_u):
    """Compute the commutant of J_u in the Lie algebra spin(9).

    spin(9) = span{gamma_i gamma_j : i < j}, dim = 36.
    The commutant (centralizer) is {L in spin(9) : [J_u, L] = 0}.
    This is the Lie algebra of G_SM = Stab_{Spin(9)}(J_u).

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16)
        J_u: 16x16 numpy array

    Returns:
        dict with keys:
          'commutant_dim': int (dimension of the centralizer)
          'individual_commuting': list of (i,j) pairs where gamma_i gamma_j
                                   individually commutes with J_u
          'n_individual': int (count of individually commuting generators)
          'is_closed': bool (commutant is a Lie subalgebra)
          'semisimple_dim': int (dim of semisimple part, from Killing form)
          'center_dim': int (dim of center)
          'casimir_eigenvalues': array (Casimir eigenvalues on R^16)
          'casimir_multiplicities': list of (eigenvalue, multiplicity) pairs
          'r16_decomposition': str (description of R^16 decomposition)
    """
    n = len(gamma_matrices)  # 9

    # Build all 36 spin(9) generators
    spin9_gens = []
    spin9_labels = []
    for i in range(n):
        for j in range(i + 1, n):
            spin9_gens.append(gamma_matrices[i] @ gamma_matrices[j])
            spin9_labels.append((i, j))

    n_gens = len(spin9_gens)

    # Find individual commuting generators
    individual_comm = []
    for k, (L, label) in enumerate(zip(spin9_gens, spin9_labels)):
        comm = J_u @ L - L @ J_u
        if np.linalg.norm(comm, 'fro') < 1e-12:
            individual_comm.append(label)

    # Compute full commutant via SVD
    comm_action = np.zeros((256, n_gens))
    for k, L in enumerate(spin9_gens):
        comm = J_u @ L - L @ J_u
        comm_action[:, k] = comm.flatten()

    U_svd, s_svd, Vt_svd = np.linalg.svd(comm_action, full_matrices=True)
    rank = np.sum(s_svd > 1e-10)
    null_vecs = Vt_svd[rank:]  # (commutant_dim x n_gens)
    commutant_dim = null_vecs.shape[0]

    # Build commutant matrices
    stab_mats = []
    for idx in range(commutant_dim):
        v = null_vecs[idx]
        L = sum(v[k] * spin9_gens[k] for k in range(n_gens))
        stab_mats.append(L)

    stab_flat = np.array([L.flatten() for L in stab_mats]).T

    # Check Lie algebra closure
    is_closed = True
    for a in range(commutant_dim):
        for b in range(a + 1, commutant_dim):
            bracket = stab_mats[a] @ stab_mats[b] - stab_mats[b] @ stab_mats[a]
            coeffs, _, _, _ = np.linalg.lstsq(
                stab_flat, bracket.flatten(), rcond=None)
            resid = np.linalg.norm(bracket.flatten() - stab_flat @ coeffs)
            if resid > 1e-10:
                is_closed = False
                break
        if not is_closed:
            break

    # Structure constants and Killing form
    ad_mats = np.zeros((commutant_dim, commutant_dim, commutant_dim))
    for a in range(commutant_dim):
        for b in range(commutant_dim):
            bracket = (stab_mats[a] @ stab_mats[b]
                       - stab_mats[b] @ stab_mats[a])
            coeffs, _, _, _ = np.linalg.lstsq(
                stab_flat, bracket.flatten(), rcond=None)
            ad_mats[a, b] = coeffs

    killing = np.zeros((commutant_dim, commutant_dim))
    for a in range(commutant_dim):
        for b in range(commutant_dim):
            killing[a, b] = np.trace(ad_mats[a] @ ad_mats[b])

    evals_k = np.sort(np.linalg.eigvalsh(killing))
    semisimple_dim = int(np.sum(np.abs(evals_k) > 1e-6))
    center_dim = commutant_dim - semisimple_dim

    # Find center elements (commute with everything in the stabilizer)
    evals_k_full, evecs_k = np.linalg.eigh(killing)
    new_basis = []
    for i in range(commutant_dim):
        L = sum(evecs_k[j, i] * stab_mats[j] for j in range(commutant_dim))
        new_basis.append(L)

    center_idx = [i for i in range(commutant_dim)
                  if np.abs(evals_k_full[i]) < 1e-6]
    center_elements = []
    for idx in center_idx:
        max_bracket = 0
        for s in range(commutant_dim):
            bracket = new_basis[idx] @ new_basis[s] - new_basis[s] @ new_basis[idx]
            max_bracket = max(max_bracket, np.linalg.norm(bracket, 'fro'))
        if max_bracket < 1e-10:
            center_elements.append(idx)

    center_dim = len(center_elements)
    semisimple_dim = commutant_dim - center_dim

    # Casimir on R^16 (using orthonormal basis)
    G_spin9 = np.zeros((n_gens, n_gens))
    for i in range(n_gens):
        for j in range(n_gens):
            G_spin9[i, j] = np.trace(spin9_gens[i].T @ spin9_gens[j])
    ip_stab = null_vecs @ G_spin9 @ null_vecs.T
    evals_ip, evecs_ip = np.linalg.eigh(ip_stab)
    ortho_coeffs = (evecs_ip @ np.diag(1.0 / np.sqrt(np.maximum(evals_ip, 1e-15)))
                    @ evecs_ip.T @ null_vecs)
    ortho_mats = []
    for idx in range(commutant_dim):
        v = ortho_coeffs[idx]
        L = sum(v[k] * spin9_gens[k] for k in range(n_gens))
        ortho_mats.append(L)

    casimir = sum(L @ L for L in ortho_mats)
    cas_evals = np.sort(np.linalg.eigvalsh(casimir))
    unique_cas = np.unique(np.round(cas_evals, 4))
    cas_mults = [(float(e), int(np.sum(np.abs(cas_evals - e) < 0.01)))
                 for e in unique_cas]

    # R^16 decomposition description
    r16_desc = "; ".join(
        [f"eigenvalue {e:.4f}, multiplicity {m}" for e, m in cas_mults])

    return {
        'commutant_dim': commutant_dim,
        'individual_commuting': individual_comm,
        'n_individual': len(individual_comm),
        'is_closed': is_closed,
        'semisimple_dim': semisimple_dim,
        'center_dim': center_dim,
        'killing_eigenvalues': evals_k,
        'casimir_eigenvalues': cas_evals,
        'casimir_multiplicities': cas_mults,
        'r16_decomposition': r16_desc,
    }
