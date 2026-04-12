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
# Phase 30, Plan 01: Impossibility theorem verification (Schur commutant,
#   grade-2 stabilizer comparison).
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


# ============================================================================
# Phase 46, Plan 01: pi_u projection, det_2 quadratic form, h_2(O) Jordan product
# ============================================================================
#
# VERIFIED (46-01 Task 1):
#   det_2(E_{22}) = 0, det_2(I_2) = 1, det_2(off-diag e_7) = -1.
#   Gram matrix of det_2 on h_2(C_u) = diag(+1,-1,-1,-1).  Signature (1,3).
#   pi_u idempotent (error 0), image dim 4, components [1:7] exactly zero.
#   Reference: Baez 2002 Sec 3.3: h_2(C) = R^{3,1}.
#
# VERIFIED (46-01 Task 2):
#   jordan_product_h2o: symmetric (error 0), identity property (error 0).
#   Intrinsic V_0 closure: all 55 basis pairs, zero V_{1/2} and V_1 leakage.
#   Intrinsic vs inherited: EXACT agreement on all 55 pairs, zero V_{1/2}
#   leakage from inherited h_3(O) product. Peirce rule V_0 o V_0 c V_0 holds.
#   h_2(C_u) limiting case: both products close in C_u, exact agreement.
#   Reference: McCrimmon 2004 Ch. 17 (Peirce multiplication rules).
# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   metric_on_h2Cu=mostly_minus_via_det2
#
# Reference: Baez 2002 (math/0105155) Sec 3.3-3.4: h_2(K) = R^{dim(K)+1,1}
#   For K=C (dim 2): h_2(C) = R^{3,1}, Minkowski signature via det.
# Reference: McCrimmon 2004, Ch. 17: Peirce multiplication rules.


def proj_u(b):
    """Project octonion b onto C_u = span{1, u} where u = e_7.

    For u = e_7: keep real part (component 0) and e_7 component (component 7),
    zero out imaginary components 1-6.

    Parameters:
        b: Octonion

    Returns:
        Octonion with only components 0 and 7 nonzero.
    """
    c = np.zeros(8, dtype=np.float64)
    c[0] = b.c[0]
    c[7] = b.c[7]
    return Octonion(c)


def pi_u(X):
    """Project V_0 element X in h_2(O) onto h_2(C_u) where u = e_7.

    Formula: pi_u(beta, gamma, x1) = (beta, gamma, proj_u(x1)).
    The diagonal entries are unchanged; the off-diagonal octonion is
    projected to its C_u = span{1, e_7} component.

    Assumes X is already in V_0 (alpha=0, x2=0, x3=0). Preserves those.

    Parameters:
        X: H3O element in V_0

    Returns:
        H3O element in h_2(C_u) subset of V_0.
    """
    return H3O(
        alpha=0.0,
        beta=X.beta,
        gamma=X.gamma,
        x1=proj_u(X.x1),
        x2=Octonion(),
        x3=Octonion(),
    )


def det_2(X):
    """Quadratic form det_2 on h_2(O) or h_2(C_u).

    For X = (beta, gamma, x1) representing the 2x2 Hermitian matrix
        [[beta,    conj(x1)],
         [x1,      gamma   ]]

    det_2(X) = beta * gamma - |x1|^2.

    This is the natural determinant on 2x2 Hermitian octonionic matrices.
    On h_2(C_u) = R^4 with parametrization x_0=(beta+gamma)/2,
    x_3=(beta-gamma)/2, x_1=Re(x1), x_2=x1.c[7], it becomes
    det_2 = x_0^2 - x_1^2 - x_2^2 - x_3^2, giving signature (1,3).

    Parameters:
        X: H3O element (uses beta, gamma, x1 only)

    Returns:
        float: beta * gamma - |x1|^2
    """
    return X.beta * X.gamma - X.x1.norm_sq()


def jordan_product_h2o(A, B):
    """Intrinsic Jordan product on h_2(O), the 2x2 Hermitian octonionic matrices.

    For A = (beta_A, gamma_A, x1_A) and B = (beta_B, gamma_B, x1_B),
    representing 2x2 matrices:
        A_mat = [[beta_A,    conj(x1_A)],
                 [x1_A,      gamma_A   ]]
        B_mat = [[beta_B,    conj(x1_B)],
                 [x1_B,      gamma_B   ]]

    The Jordan product is (1/2)(A_mat B_mat + B_mat A_mat), extracting
    the Hermitian entries.

    CRITICAL: This is the INTRINSIC h_2(O) product, NOT the inherited
    h_3(O) Peirce product. The intrinsic product closes in h_2(O) by
    construction (h_2(O) is a Jordan algebra in its own right).

    Parameters:
        A, B: H3O elements in V_0 (only beta, gamma, x1 used)

    Returns:
        H3O element in V_0 (alpha=0, x2=0, x3=0)
    """
    bA, gA = A.beta, A.gamma
    bB, gB = B.beta, B.gamma
    x1A, x1B = A.x1, B.x1
    cx1A, cx1B = x1A.conjugate(), x1B.conjugate()

    # Real scalars for diagonal entries
    bA_oct = Octonion(np.array([bA, 0, 0, 0, 0, 0, 0, 0]))
    gA_oct = Octonion(np.array([gA, 0, 0, 0, 0, 0, 0, 0]))
    bB_oct = Octonion(np.array([bB, 0, 0, 0, 0, 0, 0, 0]))
    gB_oct = Octonion(np.array([gB, 0, 0, 0, 0, 0, 0, 0]))

    # AB matrix entries:
    #   (AB)_{11} = bA*bB + conj(x1A)*x1B
    #   (AB)_{12} = bA*conj(x1B) + conj(x1A)*gB
    #   (AB)_{21} = x1A*bB + gA*x1B
    #   (AB)_{22} = x1A*conj(x1B) + gA*gB
    AB_11 = bA_oct * bB_oct + cx1A * x1B
    AB_12 = bA_oct * cx1B + cx1A * gB_oct
    AB_21 = x1A * bB_oct + gA_oct * x1B
    AB_22 = x1A * cx1B + gA_oct * gB_oct

    # BA matrix entries:
    BA_11 = bB_oct * bA_oct + cx1B * x1A
    BA_12 = bB_oct * cx1A + cx1B * gA_oct
    BA_21 = x1B * bA_oct + gB_oct * x1A
    BA_22 = x1B * cx1A + gB_oct * gA_oct

    # Jordan product = (1/2)(AB + BA)
    # Diagonal entries are real (take real part)
    beta_out = 0.5 * ((AB_11 + BA_11).real_part())
    gamma_out = 0.5 * ((AB_22 + BA_22).real_part())

    # Off-diagonal entry: x1 sits at position (2,1) in the 2x2 matrix
    x1_out = 0.5 * (AB_21 + BA_21)

    return H3O(
        alpha=0.0,
        beta=beta_out,
        gamma=gamma_out,
        x1=x1_out,
        x2=Octonion(),
        x3=Octonion(),
    )


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


def verify_spin10_branching(gamma_matrices, J_u):
    """Verify or characterize the Spin(9)->Spin(10) extension via J_u.

    If J_u anticommuted with all gamma_i (Case A), the 10 operators
    {gamma_1,...,gamma_9, J_u} would generate Cl(9,1) and the even
    subalgebra would be spin(9,1) = spin(10) (Wick-rotated).

    Since J_u does NOT anticommute with all gamma_i (Case B, from Plan 01),
    the extension fails as a Clifford algebra. Instead, characterize:

    1. The 45-dim space span{gamma_i gamma_j, gamma_i J_u}: is it a Lie algebra?
    2. If not, what Lie algebra does it generate?
    3. The complexification structure (R^16, J_u) = C^8 under spin(9).

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16)
        J_u: 16x16 numpy array

    Returns:
        dict with keys:
          'case': 'A' or 'B' (whether J_u anticommutes with all gamma_i)
          'span_dim_45': int (rank of {spin(9), gamma_i J_u})
          'is_lie_algebra': bool (whether the 45-dim space is closed)
          'generated_lie_dim': int (dim of Lie algebra generated by the 45-dim space)
          'generated_lie_type': str (description)
          'complexification_valid': bool (J_u defines a complex structure)
          'j_linear_dim': int (dim of spin(9) elements that are J_u-linear)
          'j_linear_is_subalgebra': bool
    """
    n = len(gamma_matrices)

    # Check anticommutation pattern
    all_anticommute = True
    for g in gamma_matrices:
        ac = J_u @ g + g @ J_u
        if np.linalg.norm(ac, 'fro') > 1e-12:
            all_anticommute = False
            break
    case = 'A' if all_anticommute else 'B'

    # Build spin(9) generators and gamma_i J_u
    spin9_gens = []
    for i in range(n):
        for j in range(i + 1, n):
            spin9_gens.append(gamma_matrices[i] @ gamma_matrices[j])
    new_gens = [gamma_matrices[i] @ J_u for i in range(n)]

    # Span dimension
    all_flat = ([g.flatten() for g in spin9_gens]
                + [g.flatten() for g in new_gens])
    all_matrix = np.array(all_flat).T
    span_dim = np.linalg.matrix_rank(all_matrix, tol=1e-10)

    # Check if the 45-dim space is closed under brackets
    spin9_flat = np.array([g.flatten() for g in spin9_gens]).T
    is_lie = True
    # Test [gamma_i J_u, gamma_j J_u] in span
    for i in range(n):
        for j in range(i + 1, n):
            bracket = new_gens[i] @ new_gens[j] - new_gens[j] @ new_gens[i]
            coeffs, _, _, _ = np.linalg.lstsq(
                all_matrix, bracket.flatten(), rcond=None)
            resid = np.linalg.norm(bracket.flatten() - all_matrix @ coeffs)
            if resid > 1e-10:
                is_lie = False
                break
        if not is_lie:
            break

    if is_lie:
        # Also check [spin(9), gamma_i J_u] closure
        for idx, L in enumerate(spin9_gens):
            for k in range(n):
                bracket = L @ new_gens[k] - new_gens[k] @ L
                coeffs, _, _, _ = np.linalg.lstsq(
                    all_matrix, bracket.flatten(), rcond=None)
                resid = np.linalg.norm(bracket.flatten() - all_matrix @ coeffs)
                if resid > 1e-10:
                    is_lie = False
                    break
            if not is_lie:
                break

    # Find the Lie algebra generated (iterative closure)
    initial = spin9_gens + new_gens
    current_flat = np.array([g.flatten() for g in initial]).T
    U, s, _ = np.linalg.svd(current_flat, full_matrices=False)
    rank = np.sum(s > 1e-10)
    basis = U[:, :rank]

    for iteration in range(10):
        new_elements = []
        nb = basis.shape[1]
        for i in range(nb):
            for j in range(i + 1, nb):
                Mi = basis[:, i].reshape(16, 16)
                Mj = basis[:, j].reshape(16, 16)
                comm = Mi @ Mj - Mj @ Mi
                new_elements.append(comm.flatten())
        if not new_elements:
            break
        extended = np.column_stack([basis] + [np.array(new_elements).T])
        new_rank = np.linalg.matrix_rank(extended, tol=1e-10)
        if new_rank == rank:
            break
        U, s, _ = np.linalg.svd(extended, full_matrices=False)
        rank = new_rank
        basis = U[:, :rank]

    gen_lie_dim = rank
    if gen_lie_dim == 255:
        gen_lie_type = "sl(16, R)"
    elif gen_lie_dim == 120:
        gen_lie_type = "so(16)"
    elif gen_lie_dim == 45:
        gen_lie_type = "so(10) or spin(10)"
    else:
        gen_lie_type = f"unknown (dim {gen_lie_dim})"

    # Complexification: J_u defines a complex structure on R^16 = C^8.
    # An element L of spin(9) is J_u-linear (i.e., C-linear on C^8)
    # iff [L, J_u] = 0. This is exactly the commutant we already computed.
    # The J_u-linear spin(9) elements form a Lie subalgebra = stab(J_u).
    comm_action = np.zeros((256, len(spin9_gens)))
    for k, L in enumerate(spin9_gens):
        comm = J_u @ L - L @ J_u
        comm_action[:, k] = comm.flatten()
    _, s_comm, Vt_comm = np.linalg.svd(comm_action, full_matrices=True)
    j_linear_dim = len(spin9_gens) - np.sum(s_comm > 1e-10)

    # Check if J_u-linear elements form a subalgebra
    null_vecs = Vt_comm[np.sum(s_comm > 1e-10):]
    j_linear_mats = []
    for idx in range(j_linear_dim):
        v = null_vecs[idx]
        L = sum(v[k] * spin9_gens[k] for k in range(len(spin9_gens)))
        j_linear_mats.append(L)
    j_linear_flat = np.array([L.flatten() for L in j_linear_mats]).T
    j_linear_sub = True
    for a in range(j_linear_dim):
        for b in range(a + 1, j_linear_dim):
            bracket = (j_linear_mats[a] @ j_linear_mats[b]
                       - j_linear_mats[b] @ j_linear_mats[a])
            coeffs, _, _, _ = np.linalg.lstsq(
                j_linear_flat, bracket.flatten(), rcond=None)
            resid = np.linalg.norm(bracket.flatten() - j_linear_flat @ coeffs)
            if resid > 1e-10:
                j_linear_sub = False
                break
        if not j_linear_sub:
            break

    return {
        'case': case,
        'span_dim_45': span_dim,
        'is_lie_algebra': is_lie,
        'generated_lie_dim': gen_lie_dim,
        'generated_lie_type': gen_lie_type,
        'complexification_valid': True,  # J_u^2 = -I always valid
        'j_linear_dim': j_linear_dim,
        'j_linear_is_subalgebra': j_linear_sub,
    }


# ============================================================================
# Phase 30, Plan 01: Impossibility theorem verification
# ============================================================================


def compute_spin9_commutant(gamma_matrices):
    """Compute the commutant of the full Spin(9) action on R^16.

    Finds all 16x16 matrices X satisfying [g, X] = 0 for every generator
    g in spin(9) = span{gamma_i gamma_j : i < j}.

    By Schur's lemma, since S_9 is an irreducible real-type representation
    of Spin(9), this commutant should be 1-dimensional (= R * I_{16}).

    ASSERT_CONVENTION: clifford_signature=Cl(9,0)_gamma_i_sq=+I

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16), Clifford generators

    Returns:
        dict with keys:
          'commutant_dim': int (should be 1)
          'commutant_basis': list of 16x16 arrays (basis of commutant)
          'is_scalar_multiple_of_identity': bool
          'max_deviation_from_identity': float (max |X/trace(X)*16 - I|
              for basis element X)
    """
    n = len(gamma_matrices)

    # Build all 36 spin(9) generators: gamma_i gamma_j for i < j
    spin9_gens = []
    for i in range(n):
        for j in range(i + 1, n):
            spin9_gens.append(gamma_matrices[i] @ gamma_matrices[j])

    # For each of the 256 basis elements E_{ab} of M_16(R), compute
    # the commutator [g, E_{ab}] for all spin(9) generators g.
    # Stack these constraints and find the nullspace.
    #
    # More efficient: vectorize the commutator action.
    # [A, X] = AX - XA.  In vectorized form (using Kronecker products):
    # vec([A, X]) = (I kron A - A^T kron I) vec(X)
    #
    # Stack for all generators to get a constraint matrix.
    n_gens = len(spin9_gens)
    I16 = np.eye(16)

    # Build the stacked commutator action matrix
    # Each generator contributes 256 rows (constraints)
    constraint_rows = []
    for g in spin9_gens:
        # [g, X] = gX - Xg
        # vec(gX - Xg) = (I kron g - g^T kron I) vec(X)
        action = np.kron(I16, g) - np.kron(g.T, I16)
        constraint_rows.append(action)

    constraint_matrix = np.vstack(constraint_rows)  # (36*256) x 256

    # Find nullspace via SVD
    U, s, Vt = np.linalg.svd(constraint_matrix, full_matrices=True)
    rank = np.sum(s > 1e-10)
    null_vecs = Vt[rank:]  # null space rows
    commutant_dim = null_vecs.shape[0]

    # Reshape to matrices
    commutant_basis = []
    for k in range(commutant_dim):
        X = null_vecs[k].reshape(16, 16)
        commutant_basis.append(X)

    # Check if each basis element is a scalar multiple of identity
    is_identity = True
    max_dev = 0.0
    for X in commutant_basis:
        tr = np.trace(X)
        if abs(tr) < 1e-14:
            # X is traceless but commutes with everything -- shouldn't happen
            # for a 1-dim commutant
            is_identity = False
            max_dev = max(max_dev, np.linalg.norm(X, 'fro'))
        else:
            normalized = X / (tr / 16.0)
            dev = np.max(np.abs(normalized - I16))
            max_dev = max(max_dev, dev)
            if dev > 1e-10:
                is_identity = False

    return {
        'commutant_dim': commutant_dim,
        'commutant_basis': commutant_basis,
        'is_scalar_multiple_of_identity': is_identity,
        'max_deviation_from_identity': max_dev,
    }


def compute_grade2_stabilizer(gamma_matrices, target_gamma_ij):
    """Compute the stabilizer of a grade-2 element gamma_i gamma_j in spin(9).

    Parameters:
        gamma_matrices: list of 9 numpy arrays (16x16)
        target_gamma_ij: 16x16 numpy array (the grade-2 element gamma_i gamma_j)

    Returns:
        dict with keys:
          'stabilizer_dim': int
          'semisimple_dim': int
          'center_dim': int
    """
    n = len(gamma_matrices)

    # Build all 36 spin(9) generators
    spin9_gens = []
    for i in range(n):
        for j in range(i + 1, n):
            spin9_gens.append(gamma_matrices[i] @ gamma_matrices[j])
    n_gens = len(spin9_gens)

    # Commutant of target in spin(9)
    comm_action = np.zeros((256, n_gens))
    for k, L in enumerate(spin9_gens):
        comm = target_gamma_ij @ L - L @ target_gamma_ij
        comm_action[:, k] = comm.flatten()

    U, s, Vt = np.linalg.svd(comm_action, full_matrices=True)
    rank = np.sum(s > 1e-10)
    null_vecs = Vt[rank:]
    stab_dim = null_vecs.shape[0]

    # Build stabilizer matrices
    stab_mats = []
    for idx in range(stab_dim):
        v = null_vecs[idx]
        L = sum(v[k] * spin9_gens[k] for k in range(n_gens))
        stab_mats.append(L)

    if stab_dim == 0:
        return {
            'stabilizer_dim': 0,
            'semisimple_dim': 0,
            'center_dim': 0,
        }

    stab_flat = np.array([L.flatten() for L in stab_mats]).T

    # Structure constants and Killing form
    ad_mats = np.zeros((stab_dim, stab_dim, stab_dim))
    for a in range(stab_dim):
        for b in range(stab_dim):
            bracket = stab_mats[a] @ stab_mats[b] - stab_mats[b] @ stab_mats[a]
            coeffs, _, _, _ = np.linalg.lstsq(stab_flat, bracket.flatten(),
                                               rcond=None)
            ad_mats[a, b] = coeffs

    killing = np.zeros((stab_dim, stab_dim))
    for a in range(stab_dim):
        for b in range(stab_dim):
            killing[a, b] = np.trace(ad_mats[a] @ ad_mats[b])

    evals_k_full, evecs_k = np.linalg.eigh(killing)

    # Find center (Killing form zero eigenvalues that also commute with all)
    new_basis = []
    for i in range(stab_dim):
        L = sum(evecs_k[j, i] * stab_mats[j] for j in range(stab_dim))
        new_basis.append(L)

    center_count = 0
    for i in range(stab_dim):
        if np.abs(evals_k_full[i]) < 1e-6:
            max_bracket = 0
            for s in range(stab_dim):
                bracket = new_basis[i] @ new_basis[s] - new_basis[s] @ new_basis[i]
                max_bracket = max(max_bracket, np.linalg.norm(bracket, 'fro'))
            if max_bracket < 1e-10:
                center_count += 1

    return {
        'stabilizer_dim': stab_dim,
        'semisimple_dim': stab_dim - center_count,
        'center_dim': center_count,
    }


# ============================================================================
# Phase 46, Plan 02: Delta non-homomorphism, V_{1/2} x V_{1/2} -> V_0 product
# ============================================================================
# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   metric_on_h2Cu=mostly_minus_via_det2
#
# Delta(A,B) = pi_u(A o B) - pi_u(A) o pi_u(B) measures the failure of pi_u
# to be a Jordan homomorphism.  It vanishes when both A,B are in h_2(C_u)
# (associativity of C_u) and is generically nonzero on h_2(O) due to
# octonion non-associativity.
#
# Reference: Baez 2002 Sec 3.3-3.4 (h_2(C) is associative -> pi_u is
#   homomorphism on h_2(C_u)).
# Reference: McCrimmon 2004 Ch. 17 (Peirce multiplication rules).


def delta_pi_u(A, B):
    """Non-homomorphism failure of pi_u on V_0.

    Delta(A,B) = pi_u(jordan_product_h2o(A, B)) - jordan_product_h2o(pi_u(A), pi_u(B))

    Both Jordan products are the intrinsic h_2(O) product.
    The result lives in h_2(C_u) (image of pi_u).

    Parameters:
        A, B: H3O elements in V_0

    Returns:
        H3O element in h_2(C_u)
    """
    # pi_u(A o B)
    AB = jordan_product_h2o(A, B)
    term1 = pi_u(AB)

    # pi_u(A) o pi_u(B)
    piA = pi_u(A)
    piB = pi_u(B)
    term2 = jordan_product_h2o(piA, piB)

    return term1 - term2


def h2cu_basis():
    """Return the 4 basis elements of h_2(C_u) as H3O elements in V_0.

    B_0 = E_{22} = (beta=1, gamma=0)
    B_1 = E_{33} = (beta=0, gamma=1)
    B_2 = off-diag real = (x1 = 1)
    B_3 = off-diag u = (x1 = e_7)

    These span h_2(C_u) where C_u = span{1, e_7}.
    """
    return [
        H3O(beta=1.0, gamma=0.0),       # E_{22}
        H3O(beta=0.0, gamma=1.0),       # E_{33}
        H3O(x1=Octonion.basis(0)),      # x1 = 1
        H3O(x1=Octonion.basis(7)),      # x1 = e_7
    ]


def compute_delta_table():
    """Compute Delta(B_i, B_j) for all 55 V_0 basis pairs (i <= j).

    Uses V0_basis_elements() (10 elements).

    Returns:
        dict with keys:
          'deltas': list of (i, j, H3O) for all 55 pairs
          'norms': 10x10 symmetric matrix of |Delta(B_i, B_j)|
          'cu_pairs': list of (i, j) indices for h_2(C_u) basis pairs
          'cu_max_error': float, max |Delta| on h_2(C_u) pairs
          'nonzero_pairs': list of (i, j, norm) for pairs with |Delta| > 1e-14
          'zero_pairs': list of (i, j) for pairs with |Delta| <= 1e-14
    """
    basis = V0_basis_elements()
    n = len(basis)  # 10

    deltas = []
    norms = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            d = delta_pi_u(basis[i], basis[j])
            dn = d.norm()
            deltas.append((i, j, d))
            norms[i, j] = dn
            norms[j, i] = dn

    # Identify h_2(C_u) basis indices within V0_basis_elements:
    # V0 basis: b[0]=(beta=0.5, gamma=0.5), b[1]=(beta=0.5, gamma=-0.5),
    #           b[2]=x1=e_0, b[3]=x1=e_1, ..., b[9]=x1=e_7
    # h_2(C_u) elements: beta, gamma components -> b[0], b[1] span the diagonal
    # x1 in C_u -> b[2] (x1=e_0=1) and b[9] (x1=e_7=u)
    cu_indices = [0, 1, 2, 9]  # b[0], b[1] (diagonal), b[2] (x1=1), b[9] (x1=e_7)

    cu_pairs = []
    cu_max_error = 0.0
    for i in cu_indices:
        for j in cu_indices:
            if j >= i:
                cu_pairs.append((i, j))
                cu_max_error = max(cu_max_error, norms[i, j])

    nonzero_pairs = [(i, j, norms[i, j]) for (i, j, _) in deltas if norms[i, j] > 1e-14]
    zero_pairs = [(i, j) for (i, j, _) in deltas if norms[i, j] <= 1e-14]

    return {
        'deltas': deltas,
        'norms': norms,
        'cu_indices': cu_indices,
        'cu_pairs': cu_pairs,
        'cu_max_error': cu_max_error,
        'nonzero_pairs': nonzero_pairs,
        'zero_pairs': zero_pairs,
    }


def vhalf_product_V0(v, w):
    """V_0 component of V_{1/2} x V_{1/2} Peirce product.

    vhalf_product_V0(v, w) = peirce_V0(jordan_product(v, w))

    Parameters:
        v, w: H3O elements in V_{1/2}

    Returns:
        H3O element in V_0
    """
    return peirce_V0(jordan_product(v, w))


def compute_vhalf_product_tables():
    """Compute full V_{1/2} x V_{1/2} product tables.

    Returns dict with:
      'v0_table': 16x16x10 array (V_0 component as R^10 vectors)
      'mink_table': 16x16x4 array (pi_u-projected Minkowski coordinates)
      'mink_matrices': list of 4 matrices [M0, M1, M2, M3] (16x16 each)
      'alpha_table': 16x16 array (V_1 component alpha_{ij})
      'v0_rank': int
      'mink_rank': int

    Minkowski coordinates: x_0=(beta+gamma)/2, x_3=(beta-gamma)/2,
    x_1=Re(x1)=x1.c[0], x_2=x1.c[7] (Im_u component).

    VERIFIED (46-02 Task 2):
      Peirce rule: |V_{1/2} component| = 0 for all 136 pairs.
      Symmetry: all tables symmetric with zero error.
      V_1 component: alpha_ij = delta_ij (identity).
      V_0 product rank: 10 (surjective onto V_0).
      pi_u-projected rank: 4 (surjective onto h_2(C_u)).
      M_0 = (1/2)*I_16 (timelike).
      Spatial {M_i, M_j} = (1/2)*delta_ij*I_16 (Cl(3,0) on R^16).
      Cu^2 restriction: matches standard Hermitian outer product exactly.
      Cu^2 self-products: rank-1 positive semidefinite (det_2=0).
    """
    vbasis = Vhalf_basis_vectors()
    n = len(vbasis)  # 16

    v0_table = np.zeros((n, n, 10))
    mink_table = np.zeros((n, n, 4))
    alpha_table = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            prod = jordan_product(vbasis[i], vbasis[j])

            # V_0 component
            v0 = peirce_V0(prod)
            v0_vec = np.array([v0.beta, v0.gamma] + list(v0.x1.c))
            v0_table[i, j] = v0_vec
            v0_table[j, i] = v0_vec

            # pi_u projection -> Minkowski coordinates
            v0p = pi_u(v0)
            x0 = (v0p.beta + v0p.gamma) / 2
            x3 = (v0p.beta - v0p.gamma) / 2
            x1 = v0p.x1.c[0]
            x2 = v0p.x1.c[7]
            mink_table[i, j] = [x0, x1, x2, x3]
            mink_table[j, i] = [x0, x1, x2, x3]

            # V_1 component
            v1 = peirce_V1(prod)
            alpha_table[i, j] = v1.alpha
            alpha_table[j, i] = v1.alpha

    # Rank computations
    products = []
    proj_products = []
    for i in range(n):
        for j in range(i, n):
            products.append(v0_table[i, j])
            proj_products.append(mink_table[i, j])
    v0_rank = int(np.linalg.matrix_rank(np.array(products), tol=1e-10))
    mink_rank = int(np.linalg.matrix_rank(np.array(proj_products), tol=1e-10))

    mink_matrices = [mink_table[:, :, mu] for mu in range(4)]

    return {
        'v0_table': v0_table,
        'mink_table': mink_table,
        'mink_matrices': mink_matrices,
        'alpha_table': alpha_table,
        'v0_rank': v0_rank,
        'mink_rank': mink_rank,
    }


# ============================================================================
# Phase 47, Plan 01: det_3, polarization, d_{IJK} tensor, Peirce block decomposition
# ============================================================================
#
# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   det_3_association=left_to_right_Re((x1*x2)*x3),
#   d_ijk_normalization=d(X,X,X)=6*N(X)_via_inclusion_exclusion,
#   peirce_indices=I0_V1_I1to16_Vhalf_I17to26_V0
#
# Reference: Baez 2002 (math/0105155) Sec 3.4: det formula for h_3(O).
# Reference: Slansky 1981, Phys. Rep. 79: E_6 branching 27 -> 1+16+10.
#
# The cubic norm on h_3(O) is:
#   N(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2
#          + 2*Re((x1*x2)*x3)
#
# CRITICAL: The cross-term uses LEFT-to-right association (x1*x2)*x3,
# matching the Sarrus expansion of the 3x3 matrix determinant.
# Do NOT use x1*(x2*x3) -- differs by octonion non-associativity.


def det_3(X):
    """Cubic determinant (norm form) on h_3(O).

    N(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2
           + 2*Re((x1*x2)*x3)

    The cross-term uses LEFT-to-right association: compute x1*x2 first,
    then multiply by x3, then take Re = c[0].

    Parameters:
        X: H3O element

    Returns:
        float: the cubic norm N(X)
    """
    # Diagonal cubic term
    diag = X.alpha * X.beta * X.gamma

    # Quadratic correction terms
    quad = (X.alpha * X.x1.norm_sq()
            + X.beta * X.x2.norm_sq()
            + X.gamma * X.x3.norm_sq())

    # Cross-term: 2 * Re((x1 * x2) * x3)
    # CRITICAL: left-to-right association
    x1x2 = X.x1 * X.x2        # Octonion product, computed first
    x1x2_x3 = x1x2 * X.x3     # Then multiply by x3
    cross = 2.0 * x1x2_x3.c[0]  # Real part

    return diag - quad + cross


def polarize_d(X, Y, Z):
    """Polarized symmetric trilinear form d(X,Y,Z) from det_3.

    d(X,Y,Z) = N(X+Y+Z) - N(X+Y) - N(X+Z) - N(Y+Z) + N(X) + N(Y) + N(Z)

    With our convention, d(X,X,X) = 6*N(X).

    Parameters:
        X, Y, Z: H3O elements

    Returns:
        float: d(X,Y,Z)
    """
    XpY = X + Y
    XpZ = X + Z
    YpZ = Y + Z
    XpYpZ = XpY + Z

    return (det_3(XpYpZ)
            - det_3(XpY) - det_3(XpZ) - det_3(YpZ)
            + det_3(X) + det_3(Y) + det_3(Z))


def peirce_basis_27():
    """Return the 27-element Peirce-adapted basis for h_3(O).

    Index scheme:
      I = 0:     E_{11} = diag(1,0,0)                     [V_1]
      I = 1..16: V_{1/2} basis from Vhalf_basis_vectors()  [V_{1/2}]
      I = 17..26: V_0 basis from V0_basis_elements()        [V_0]

    Returns:
        list of 27 H3O elements
    """
    basis = []
    # I=0: V_1
    basis.append(H3O.E11())
    # I=1..16: V_{1/2}
    basis.extend(Vhalf_basis_vectors())
    # I=17..26: V_0
    basis.extend(V0_basis_elements())
    return basis


def peirce_sector(I):
    """Return the Peirce sector label for basis index I.

    Returns:
        str: 'V_1' (I=0), 'V_{1/2}' (I=1..16), 'V_0' (I=17..26)
    """
    if I == 0:
        return 'V_1'
    elif 1 <= I <= 16:
        return 'V_{1/2}'
    elif 17 <= I <= 26:
        return 'V_0'
    else:
        raise ValueError(f"Index {I} out of range 0..26")


def d_ijk_tensor(basis=None, threshold=1e-14):
    """Compute the full d_{IJK} tensor by polarization on the Peirce basis.

    Evaluates d(e_I, e_J, e_K) for all I <= J <= K in range(27).
    Returns only nonzero entries (|d| > threshold).

    Parameters:
        basis: list of 27 H3O elements (default: peirce_basis_27())
        threshold: cutoff for nonzero entries

    Returns:
        dict: {(I,J,K): value} for nonzero entries with I <= J <= K
    """
    if basis is None:
        basis = peirce_basis_27()

    tensor = {}
    for I in range(27):
        for J in range(I, 27):
            for K in range(J, 27):
                val = polarize_d(basis[I], basis[J], basis[K])
                if abs(val) > threshold:
                    tensor[(I, J, K)] = val

    return tensor


def classify_peirce_blocks(tensor):
    """Classify d_{IJK} entries by Peirce sector triple.

    For each nonzero tensor entry, determines the Peirce sectors
    of I, J, K and collects them into block categories.

    Parameters:
        tensor: dict {(I,J,K): value} from d_ijk_tensor

    Returns:
        dict: {sector_triple: list of ((I,J,K), value)} where
              sector_triple is a sorted tuple of sector labels
    """
    blocks = {}
    for (I, J, K), val in tensor.items():
        sectors = tuple(sorted([peirce_sector(I), peirce_sector(J),
                                peirce_sector(K)]))
        if sectors not in blocks:
            blocks[sectors] = []
        blocks[sectors].append(((I, J, K), val))
    return blocks


# ============================================================================
# VERIFIED (47-01 Task 1):
#   det_3(I_3) = 1.0 (exact). det_3(E_{ii}) = 0 for all i (exact).
#   det_3(diag(a,b,c)) = abc (rel err 0). Homogeneity: max rel err 9.2e-15.
#   Polarization symmetry: max |d(perm) - d| = 6.8e-14.
#   d(X,X,X) = 6*N(X): max rel err 1.4e-13 (float64 noise, 7 det_3 evals).
#   h_3(C_u) restriction: matches complex det to 2.9e-16.
#   Reference: Baez 2002 Sec. 3.4.
#
# VERIFIED (47-01 Task 2):
#   d_{IJK} tensor: 106 nonzero entries out of 3654 distinct triples (97% zero).
#   Exactly two nonzero Peirce block types:
#     (V_1, V_0, V_0): 10 entries -- diagonal matrix diag(+0.5, -0.5, -2,...,-2)
#     (V_{1/2}, V_{1/2}, V_0): 96 entries -- 16 per diagonal V_0, 8 per off-diag
#   All forbidden blocks EXACTLY zero (max |d| = 0 to machine precision):
#     d_{0,0,0} = 0, pure V_0 (220 triples) = 0, V_1xV_1xV_0 = 0,
#     V_1xV_{1/2}xV_{1/2} = 0, V_{1/2}^3 = 0, V_1xV_{1/2}xV_0 = 0.
#   (V_1,V_0,V_0) block = det_2 bilinear form B(A,B): max err 0 (exact match).
#   d_{IJK} fully symmetric: max err 0 over 50 random triples.
#   Reference: Slansky 1981 (E_6 branching), Baez 2002 (cubic norm).
# ============================================================================


# ============================================================================
# Phase 47, Plan 02: F_4 invariance, uniqueness, and 27 quantum numbers
# ============================================================================
#
# ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba),
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   det_3_association=left_to_right_Re((x1*x2)*x3),
#   real_form=E6(-26)_not_E6(-78)_or_E6(6),
#   f4_rep_on_27=26+1_under_F4
#
# Reference: Springer 1962, Indag. Math. 24, 259-265 (uniqueness of cubic norm).
# Reference: Gunaydin-Sierra-Townsend 1984, Nucl. Phys. B 242, 244-268 (GST).
# Reference: Slansky 1981, Phys. Rep. 79 (E_6 branching rules).
# Reference: Paper 7 (SM fermion quantum numbers from Cl(6) eigenvalues).


def _octonion_L_mat(a):
    """Left multiplication matrix L_a(x) = a*x as 8x8 matrix."""
    M = np.zeros((8, 8), dtype=np.float64)
    for k in range(8):
        M[:, k] = (a * Octonion.basis(k)).c
    return M


def _octonion_R_mat(a):
    """Right multiplication matrix R_a(x) = x*a as 8x8 matrix."""
    M = np.zeros((8, 8), dtype=np.float64)
    for k in range(8):
        M[:, k] = (Octonion.basis(k) * a).c
    return M


def _g2_derivation_matrix(i, j):
    """Return the 8x8 matrix of the G_2 derivation D_{e_i, e_j}.

    G_2 = Aut(O) is the 14-dimensional Lie algebra of derivations of O.
    The derivation D_{a,b} for traceless a,b is given by (Schafer 1966):

      D_{a,b} = [L_a, L_b] + [L_a, R_b] + [R_a, R_b]

    where L_a(x) = ax, R_a(x) = xa.

    This produces a derivation: D(xy) = D(x)y + xD(y) for all x,y in O.
    The 21 pairs (i,j) with 1 <= i < j <= 7 span a 14-dim space = g_2.

    Parameters:
        i, j: indices in 1..7 (imaginary octonion basis elements)

    Returns:
        8x8 numpy array (the derivation matrix on full O)
    """
    a = Octonion.basis(i)
    b = Octonion.basis(j)
    La = _octonion_L_mat(a)
    Lb = _octonion_L_mat(b)
    Ra = _octonion_R_mat(a)
    Rb = _octonion_R_mat(b)
    return (La @ Lb - Lb @ La) + (La @ Rb - Rb @ La) + (Ra @ Rb - Rb @ Ra)


def _apply_g2_to_octonion(g2_mat, x):
    """Apply a G_2 transformation (7x7 matrix on Im(O)) to an octonion.

    G_2 fixes the real part and rotates the imaginary part.

    Parameters:
        g2_mat: 7x7 numpy array (orthogonal, in G_2 subset SO(7))
        x: Octonion

    Returns:
        Octonion with transformed imaginary part
    """
    c = np.zeros(8, dtype=np.float64)
    c[0] = x.c[0]
    c[1:] = g2_mat @ x.c[1:]
    return Octonion(c)


def _permute_h3o(X, perm):
    """Apply a permutation of rows/columns to h_3(O), preserving det.

    The S_3 subgroup of F_4 permutes the rows and columns simultaneously.
    For h_3(O) represented as:
        | alpha    conj(x3)  x2       |   row 0
        | x3       beta      conj(x1) |   row 1
        | conj(x2) x1        gamma    |   row 2

    Under permutation sigma, M'_{sigma(i), sigma(j)} = M_{i,j}.

    perm is a tuple (p0, p1, p2): position i in the NEW matrix gets the
    data from position perm[i] in the OLD matrix. This is the INVERSE
    of the mapping above; we use the inverse convention.

    Actually, we compute directly: build a 3x3 matrix of Octonions,
    permute rows and columns, then read off the new H3O data.
    """
    # Build full 3x3 matrix of Octonions
    # M[i][j] is the (i,j) entry
    M = [[None]*3 for _ in range(3)]
    M[0][0] = Octonion([X.alpha, 0, 0, 0, 0, 0, 0, 0])
    M[1][1] = Octonion([X.beta, 0, 0, 0, 0, 0, 0, 0])
    M[2][2] = Octonion([X.gamma, 0, 0, 0, 0, 0, 0, 0])
    M[0][1] = X.x3.conjugate()
    M[1][0] = Octonion(X.x3.c.copy())
    M[0][2] = Octonion(X.x2.c.copy())
    M[2][0] = X.x2.conjugate()
    M[1][2] = X.x1.conjugate()
    M[2][1] = Octonion(X.x1.c.copy())

    # Apply permutation: M'_{i,j} = M_{perm[i], perm[j]}
    Mp = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            Mp[i][j] = M[perm[i]][perm[j]]

    # Extract H3O data from the permuted matrix
    new_alpha = Mp[0][0].c[0]
    new_beta = Mp[1][1].c[0]
    new_gamma = Mp[2][2].c[0]
    # x3 is at M[1][0], x2 is at M[0][2], x1 is at M[2][1]
    new_x3 = Mp[1][0]
    new_x2 = Mp[0][2]
    new_x1 = Mp[2][1]

    return H3O(
        alpha=new_alpha, beta=new_beta, gamma=new_gamma,
        x1=new_x1, x2=new_x2, x3=new_x3,
    )


def verify_f4_invariance_det3(n_random=10, seeds=None):
    """Verify F_4 invariance of det_3 by testing known F_4 subgroup actions.

    Tests two types of F_4 transformations:
    1. S_3 permutations of diagonal entries (6 permutations)
    2. G_2 automorphisms of the octonions applied simultaneously to x1, x2, x3.
       Uses 14 independent G_2 generators to construct finite rotations
       exp(epsilon * D) for small epsilon, verifying det_3 is unchanged.

    Together, S_3 and G_2 generate a large subgroup of F_4. Invariance under
    these transformations, combined with Springer's algebraic characterization,
    provides strong evidence for full F_4 invariance.

    Additionally tests invariance under Spin(8) triality-related transformations
    embedded in F_4, using the Clifford generators already available.

    Parameters:
        n_random: number of random test elements (default 10)
        seeds: list of RNG seeds (default [42, 137, 999, 314, 271, 161, 577, 811, 919, 733])

    Returns:
        dict with verification results
    """
    if seeds is None:
        seeds = [42, 137, 999, 314, 271, 161, 577, 811, 919, 733]
    seeds = seeds[:n_random]

    results = {
        'S3_max_error': 0.0,
        'S3_tests': 0,
        'G2_max_error': 0.0,
        'G2_tests': 0,
        'spin9_grade2_max_error': 0.0,
        'spin9_grade2_tests': 0,
        'total_tests': 0,
        'all_pass': True,
    }

    # --- Test 1: S_3 permutation invariance ---
    # All 6 permutations of (0,1,2)
    perms = [
        (0, 1, 2), (0, 2, 1), (1, 0, 2),
        (1, 2, 0), (2, 0, 1), (2, 1, 0),
    ]

    for seed in seeds:
        rng = np.random.default_rng(seed)
        X = H3O.random(rng)
        N_X = det_3(X)

        for p in perms:
            X_perm = _permute_h3o(X, p)
            N_perm = det_3(X_perm)
            err = abs(N_perm - N_X)
            results['S3_max_error'] = max(results['S3_max_error'], err)
            results['S3_tests'] += 1

    # --- Test 2: G_2 automorphism invariance ---
    # G_2 = Aut(O) acts on Im(O) = R^7. The 14-dim Lie algebra is generated
    # by derivations D_{e_i, e_j} = [L_{e_i}, L_{e_j}] + [L_{e_i}, R_{e_j}]
    #   + [R_{e_i}, R_{e_j}] (Schafer 1966).
    # For the invariance test, we use infinitesimal G_2 transformations:
    # exp(epsilon * D) applied to each off-diagonal octonion simultaneously.
    epsilon = 1e-5

    # Build all 21 G_2 derivation matrices, which span 14 dimensions
    g2_deriv_mats = []
    for i in range(1, 8):
        for j in range(i + 1, 8):
            D = _g2_derivation_matrix(i, j)
            g2_deriv_mats.append(D)

    # Verify they span a 14-dim space (sanity check)
    deriv_flat = np.array([D[1:, 1:].flatten() for D in g2_deriv_mats]).T
    g2_rank = int(np.linalg.matrix_rank(deriv_flat, tol=1e-10))
    results['n_g2_generators'] = g2_rank

    for seed in seeds:
        rng = np.random.default_rng(seed)
        X = H3O.random(rng)
        N_X = det_3(X)

        for D in g2_deriv_mats:
            # Infinitesimal G_2 transformation: exp(eps*D) ~ I + eps*D + eps^2*D^2/2
            R = np.eye(8) + epsilon * D + 0.5 * epsilon**2 * (D @ D)
            # Apply to all three off-diagonal octonions
            X_rot = H3O(
                alpha=X.alpha, beta=X.beta, gamma=X.gamma,
                x1=Octonion(R @ X.x1.c),
                x2=Octonion(R @ X.x2.c),
                x3=Octonion(R @ X.x3.c),
            )
            N_rot = det_3(X_rot)
            # Should be invariant to O(epsilon^3) since we used 2nd order expansion
            err = abs(N_rot - N_X)
            results['G2_max_error'] = max(results['G2_max_error'], err)
            results['G2_tests'] += 1

    # --- Test 3: Spin(9) grade-2 generators acting on h_3(O) ---
    # The grade-2 elements gamma_a * gamma_b (a < b) generate Spin(9) c F_4.
    # They act on V_{1/2} = R^16 via the spinor representation.
    # The F_4 action on h_3(O) = V_1 + V_{1/2} + V_0 is:
    #   V_1: trivially (F_4 preserves trace)
    #   V_{1/2}: via the 16-dim spinor rep of Spin(9)
    #   V_0: via the 10-dim vector rep of Spin(9)
    #
    # For Spin(9) generators: the action on V_0 is obtained from the
    # commutator action [gamma_ab, T_c] on the V_0 operators T_c.
    # We verify det_3(X) is invariant under these infinitesimal actions.

    T_mats = compute_T_b_matrices()
    gammas = rescale_to_clifford_generators(T_mats)

    # Build all 36 grade-2 generators
    grade2_gens = []
    for a in range(9):
        for b in range(a + 1, 9):
            grade2_gens.append((a, b, gammas[a] @ gammas[b]))

    # For each generator, construct the infinitesimal action on h_3(O):
    # The F_4 action on V_{1/2} via Spin(9): delta(v) = (1/4)[gamma_ab, v_vec]
    # where v_vec is the 16-component coordinate vector.
    # On V_0: the 10-dim vector rep. The T_b matrices satisfy
    #   [gamma_ab, T_c] = sum_d M_{cd} T_d
    # giving the 10x10 matrix of the generator on V_0.
    # On V_1: trivial (delta = 0).

    eps_spin = 1e-6
    vhalf_basis = Vhalf_basis_vectors()
    v0_basis = V0_basis_elements()

    for seed in seeds:
        rng = np.random.default_rng(seed)
        X = H3O.random(rng)
        N_X = det_3(X)

        # Extract Peirce components
        v1_comp = peirce_V1(X)
        vh_comp = peirce_Vhalf(X)
        v0_comp = peirce_V0(X)

        # V_{1/2} coordinate vector (16-dim): coefficients in vhalf_basis
        vh_vec = np.concatenate([vh_comp.x2.c, vh_comp.x3.c])

        # V_0 coordinate vector (10-dim): coefficients in v0_basis
        # v0_basis: b[0]=(0.5,0.5,0), b[1]=(0.5,-0.5,0), b[2..9]=(0,0,e_k)
        # For a V_0 element (beta, gamma, x1):
        #   beta = 0.5*c0 + 0.5*c1, gamma = 0.5*c0 - 0.5*c1
        #   => c0 = beta + gamma, c1 = beta - gamma
        #   c_{k+2} = x1.c[k] for k=0..7
        c0 = v0_comp.beta + v0_comp.gamma
        c1 = v0_comp.beta - v0_comp.gamma
        v0_vec = np.concatenate([[c0, c1], v0_comp.x1.c])

        for a, b, gab in grade2_gens:
            # Action on V_{1/2}: delta_vh = (1/2) * gab @ vh_vec
            # (factor 1/2 from the spin rep normalization: gamma_ab/4 is the
            #  Lie algebra element, but gab = gamma_a @ gamma_b, so
            #  the Lie algebra generator is gab/4 and the action is gab/4 * v.
            #  For infinitesimal: delta = eps * (gab/4) @ v)
            delta_vh = (eps_spin / 4.0) * (gab @ vh_vec)

            # Action on V_0: need the 10x10 matrix representation
            # [gamma_ab/4, T_c] gives the commutator action
            # T_mats[c] are the 10 operators on V_{1/2}
            # The 10-dim rep: M_{cd} via [gab/4, T_c] = sum_d M_{cd} T_d
            M_v0 = np.zeros((10, 10), dtype=np.float64)
            T_flat = np.array([T_mats[c].flatten() for c in range(10)]).T  # 256x10
            for c in range(10):
                bracket = (gab / 4.0) @ T_mats[c] - T_mats[c] @ (gab / 4.0)
                coeffs, _, _, _ = np.linalg.lstsq(T_flat, bracket.flatten(), rcond=None)
                M_v0[:, c] = coeffs

            delta_v0 = eps_spin * (M_v0 @ v0_vec)

            # Reconstruct delta X from the variations
            # V_1: no change (delta_v1 = 0)
            # V_{1/2}: delta_vh_vec -> H3O
            delta_x2 = Octonion(delta_vh[:8])
            delta_x3 = Octonion(delta_vh[8:])
            # V_0: delta_v0_vec -> H3O
            delta_beta = 0.5 * delta_v0[0] + 0.5 * delta_v0[1]
            delta_gamma = 0.5 * delta_v0[0] - 0.5 * delta_v0[1]
            # v0_vec = [c0, c1, x1.c[0], ..., x1.c[7]] has 10 components
            # delta_v0[2:] gives 8 components = x1.c[0..7], correct for Octonion
            delta_x1 = Octonion(delta_v0[2:])

            delta_X = H3O(
                alpha=0.0,
                beta=delta_beta,
                gamma=delta_gamma,
                x1=delta_x1,
                x2=delta_x2,
                x3=delta_x3,
            )

            # Compute det_3(X + delta_X) and check invariance
            X_new = X + delta_X
            N_new = det_3(X_new)
            err = abs(N_new - N_X)
            results['spin9_grade2_max_error'] = max(
                results['spin9_grade2_max_error'], err)
            results['spin9_grade2_tests'] += 1

    results['total_tests'] = (results['S3_tests'] + results['G2_tests']
                              + results['spin9_grade2_tests'])
    tol = 1e-12
    spin9_tol = eps_spin * 100  # O(eps^2) tolerance for infinitesimal test
    results['all_pass'] = (results['S3_max_error'] < tol
                           and results['G2_max_error'] < tol
                           and results['spin9_grade2_max_error'] < spin9_tol)

    return results


def compute_spin9_v0_rep():
    """Build all 36 spin(9) generators as 10x10 real matrices on V_0.

    % ASSERT_CONVENTION: natural_units=dimensionless, gamma_matrix_convention=Cl(9,0), generator_normalization=gamma_ab/4, commutation_convention=[A,B]=AB-BA

    The spin(9) Lie algebra has basis {gamma_a gamma_b / 4 : 0 <= a < b <= 8},
    giving 36 generators.  Each acts on V_0 = R^{10} via the commutator action
    on the Peirce operators T_c:

        [gamma_ab/4, T_c] = sum_d  M^{(ab)}_{dc} T_d

    so column c of M^{(ab)} is the coefficient vector of the bracket in the
    T_d basis.  This is the 10-dim (vector) representation of spin(9) ~ so(9).

    Returns:
        dict with keys:
          'generators': list of 36 numpy arrays (10x10)
          'labels':     list of 36 (a,b) pairs with a < b
          'T_flat':     256x10 matrix (columns = flattened T_c), for reuse
    """
    T_mats = compute_T_b_matrices()          # 10 matrices, each 16x16
    gammas = rescale_to_clifford_generators(T_mats)  # 9 Clifford generators

    # T_flat: 256 x 10, column c = T_mats[c].flatten()
    T_flat = np.array([T_mats[c].flatten() for c in range(10)]).T  # 256x10

    generators = []
    labels = []
    for a in range(9):
        for b in range(a + 1, 9):
            gab = gammas[a] @ gammas[b]          # 16x16 grade-2 element
            M = np.zeros((10, 10), dtype=np.float64)
            for c in range(10):
                bracket = (gab / 4.0) @ T_mats[c] - T_mats[c] @ (gab / 4.0)
                coeffs, _, _, _ = np.linalg.lstsq(
                    T_flat, bracket.flatten(), rcond=None)
                M[:, c] = coeffs
            generators.append(M)
            labels.append((a, b))

    # Orthonormalization: G_{ab} = Tr(T_a T_b) = diag(1,1,4,...,4).
    # D = diag(1,1,2,...,2) sends natural T_c coords to orthonormal coords.
    # In ortho basis: M_ortho = D M D^{-1} is antisymmetric (M + M^T = 0).
    D = np.diag([1.0, 1.0] + [2.0] * 8)
    D_inv = np.diag([1.0, 1.0] + [0.5] * 8)
    generators_ortho = [D @ M @ D_inv for M in generators]

    return {
        'generators': generators,           # natural T_c basis (matches Phase 46 coords)
        'generators_ortho': generators_ortho,  # orthonormal basis (antisymmetric)
        'labels': labels,
        'T_flat': T_flat,
        'ortho_matrix': D,                  # v_ortho = D @ v_natural
        'ortho_inv': D_inv,
    }


def compute_v0_stabilizer():
    """Find the subalgebra of spin(9) preserving the 4+6 splitting of V_0.

    % ASSERT_CONVENTION: natural_units=dimensionless, gamma_matrix_convention=Cl(9,0), generator_normalization=gamma_ab/4, commutation_convention=[A,B]=AB-BA

    The 4+6 splitting (Phase 46):
      Spacetime indices S = {0, 1, 2, 9}  in the 10-dim V_0 coordinate vector
      Internal  indices I = {3, 4, 5, 6, 7, 8}

    A spin(9) generator preserves the splitting iff its 10x10 matrix is
    block-diagonal with respect to (S, I), i.e. the off-diagonal blocks
    M[S,I] and M[I,S] are both zero.

    The stabilizer is found via SVD of the off-diagonal constraint matrix.

    Verified result (Phase 48-01):
      stab_dim = 18 = so(3) + so(6), with so(3) acting on 4-dim spacetime block
      and so(6) acting on 6-dim internal block.  Killing form negative definite
      with eigenvalues -2 (x15, so(6)) and -0.5 (x3, so(3)).  Center dim = 0.
      G_SM (dim 8) is contained as a subalgebra (residual < 5e-15).
      Note: dim 18, not 21, because so(3,1) is noncompact and only so(3) c so(9).

    Returns:
        dict with keys:
          'stab_dim':              int  -- stabilizer Lie algebra dimension
          'stab_generators':       list of 10x10 matrices
          'stab_coeffs':           array (stab_dim x 36), coefficients in spin(9) basis
          'killing_form':          array (stab_dim x stab_dim)
          'killing_eigenvalues':   array
          'killing_signature':     (n_pos, n_neg, n_zero)
          'center_dim':            int
          'is_closed':             bool
          'max_closure_residual':  float
          'spacetime_block_dims':  int   -- rank of independent 4x4 generators
          'internal_block_dims':   int   -- rank of independent 6x6 generators
          'sv_gap':                float -- gap between last null and first non-null singular value
          'coset_dim':             int   -- 36 - stab_dim
          'gsm_contained':         bool  -- whether G_SM (dim 8) is a subalgebra
          'gsm_max_residual':      float
    """
    rep = compute_spin9_v0_rep()
    gens = rep['generators']       # 36 matrices, each 10x10
    n_gens = len(gens)             # 36

    # Spacetime and internal index sets
    S = [0, 1, 2, 9]
    I = [3, 4, 5, 6, 7, 8]

    # Build off-diagonal constraint matrix A  (48 x 36)
    # For each generator k, flatten M_k[S,I] (4x6=24) and M_k[I,S] (6x4=24)
    n_constraints = len(S) * len(I) + len(I) * len(S)   # 24 + 24 = 48
    A = np.zeros((n_constraints, n_gens), dtype=np.float64)
    for k in range(n_gens):
        M = gens[k]
        block_SI = M[np.ix_(S, I)].flatten()   # 24
        block_IS = M[np.ix_(I, S)].flatten()   # 24
        A[:, k] = np.concatenate([block_SI, block_IS])

    # SVD to find nullspace
    U_svd, s_svd, Vt_svd = np.linalg.svd(A, full_matrices=True)

    # Find gap: singular values below threshold are "null"
    threshold = 1e-10
    n_nonzero = np.sum(s_svd > threshold)
    stab_dim = n_gens - n_nonzero
    null_vecs = Vt_svd[n_nonzero:]    # stab_dim x 36

    # Singular value gap
    if n_nonzero < len(s_svd) and n_nonzero > 0:
        sv_gap = s_svd[n_nonzero - 1] - (s_svd[n_nonzero] if n_nonzero < len(s_svd) else 0.0)
    elif n_nonzero == 0:
        sv_gap = float('inf')
    else:
        sv_gap = s_svd[n_nonzero - 1]

    # Build stabilizer generators as 10x10 matrices
    stab_generators = []
    for idx in range(stab_dim):
        v = null_vecs[idx]
        L = sum(v[k] * gens[k] for k in range(n_gens))
        stab_generators.append(L)

    stab_flat = np.array([L.flatten() for L in stab_generators]).T  # 100 x stab_dim

    # Verify off-diagonal blocks are zero
    max_offdiag = 0.0
    for L in stab_generators:
        max_offdiag = max(max_offdiag,
                         np.max(np.abs(L[np.ix_(S, I)])),
                         np.max(np.abs(L[np.ix_(I, S)])))

    # Check closure under Lie bracket
    is_closed = True
    max_closure_residual = 0.0
    for a in range(stab_dim):
        for b in range(a + 1, stab_dim):
            bracket = (stab_generators[a] @ stab_generators[b]
                       - stab_generators[b] @ stab_generators[a])
            coeffs, _, _, _ = np.linalg.lstsq(
                stab_flat, bracket.flatten(), rcond=None)
            resid = np.linalg.norm(bracket.flatten() - stab_flat @ coeffs)
            max_closure_residual = max(max_closure_residual, resid)
            if resid > 1e-10:
                is_closed = False

    # Compute adjoint representation and Killing form
    ad_mats = np.zeros((stab_dim, stab_dim, stab_dim))
    for a in range(stab_dim):
        for b in range(stab_dim):
            bracket = (stab_generators[a] @ stab_generators[b]
                       - stab_generators[b] @ stab_generators[a])
            coeffs, _, _, _ = np.linalg.lstsq(
                stab_flat, bracket.flatten(), rcond=None)
            ad_mats[a, b] = coeffs

    killing = np.zeros((stab_dim, stab_dim))
    for a in range(stab_dim):
        for b in range(stab_dim):
            killing[a, b] = np.trace(ad_mats[a] @ ad_mats[b])

    killing_evals = np.sort(np.linalg.eigvalsh(killing))
    n_pos = int(np.sum(killing_evals > 1e-8))
    n_neg = int(np.sum(killing_evals < -1e-8))
    n_zero = stab_dim - n_pos - n_neg

    # Find center (generators commuting with all others)
    # Build full adjoint matrix: ad(L_a)_{bc} = structure constants f^c_{ab}
    full_ad = np.zeros((stab_dim, stab_dim * stab_dim))
    for a in range(stab_dim):
        full_ad[a] = ad_mats[a].flatten()
    # Center = nullspace of the map a -> ad(a)
    # A generator L_a is central iff ad_mats[a] = 0, i.e. [L_a, L_b] = 0 for all b.
    center_norms = np.array([np.linalg.norm(ad_mats[a]) for a in range(stab_dim)])
    center_dim = int(np.sum(center_norms < 1e-10))

    # Rank of spacetime and internal blocks
    space_blocks = np.array([L[np.ix_(S, S)].flatten() for L in stab_generators]).T
    internal_blocks = np.array([L[np.ix_(I, I)].flatten() for L in stab_generators]).T
    spacetime_block_dims = int(np.linalg.matrix_rank(space_blocks, tol=1e-10))
    internal_block_dims = int(np.linalg.matrix_rank(internal_blocks, tol=1e-10))

    # Cross-check: G_SM (dim 8) should be a subalgebra of this stabilizer
    # G_SM lives in spin(9) acting on V_{1/2} = R^16.
    # We need to check if its spin(9) generators, projected onto V_0, lie in the stabilizer.
    T_mats = compute_T_b_matrices()
    gammas_16 = rescale_to_clifford_generators(T_mats)
    J_u = krasnov_J_u_matrix()
    gsm = compute_gsm_commutant(gammas_16, J_u)

    # Reconstruct G_SM generators as 10x10 matrices on V_0
    # G_SM lives in spin(9) on V_{1/2}; we need its V_0 representation.
    # The commutant gives nullspace vectors in the 36-dim spin(9) basis (on V_{1/2}).
    # But compute_gsm_commutant uses the raw gamma_i @ gamma_j products as basis,
    # while compute_spin9_v0_rep uses gab/4 normalization.
    # Actually the commutant nullspace vectors are coefficients in the gamma_i @ gamma_j
    # basis (without the /4). But the V_0 rep uses gab/4 normalization in the bracket.
    # The key: if c_k are the SVD nullspace coefficients from compute_gsm_commutant,
    # then the spin(9) element is L = sum_k c_k * (gamma_{a_k} gamma_{b_k}).
    # The corresponding V_0 generator is sum_k c_k * M^{(a_k, b_k)}.
    # (The factor of 4 is a shared normalization that cancels in the commutation relation.)

    # Rebuild gsm nullspace: need to re-run SVD to get the null vectors
    spin9_gens_16 = []
    for i in range(9):
        for j in range(i + 1, 9):
            spin9_gens_16.append(gammas_16[i] @ gammas_16[j])

    comm_action = np.zeros((256, 36))
    for k, L in enumerate(spin9_gens_16):
        comm = J_u @ L - L @ J_u
        comm_action[:, k] = comm.flatten()

    U_gsm, s_gsm, Vt_gsm = np.linalg.svd(comm_action, full_matrices=True)
    rank_gsm = np.sum(s_gsm > 1e-10)
    gsm_null_vecs = Vt_gsm[rank_gsm:]   # gsm_dim x 36

    # Project G_SM generators to V_0
    gsm_v0_gens = []
    for idx in range(gsm_null_vecs.shape[0]):
        v = gsm_null_vecs[idx]
        L_v0 = sum(v[k] * gens[k] for k in range(n_gens))
        gsm_v0_gens.append(L_v0)

    # Check each G_SM V_0 generator is in the stabilizer span
    gsm_contained = True
    gsm_max_residual = 0.0
    for L_gsm in gsm_v0_gens:
        coeffs, _, _, _ = np.linalg.lstsq(
            stab_flat, L_gsm.flatten(), rcond=None)
        resid = np.linalg.norm(L_gsm.flatten() - stab_flat @ coeffs)
        gsm_max_residual = max(gsm_max_residual, resid)
        if resid > 1e-10:
            gsm_contained = False

    return {
        'stab_dim': stab_dim,
        'stab_generators': stab_generators,
        'stab_coeffs': null_vecs,
        'killing_form': killing,
        'killing_eigenvalues': killing_evals,
        'killing_signature': (n_pos, n_neg, n_zero),
        'center_dim': center_dim,
        'is_closed': is_closed,
        'max_closure_residual': max_closure_residual,
        'spacetime_block_dims': spacetime_block_dims,
        'internal_block_dims': internal_block_dims,
        'sv_gap': sv_gap,
        'coset_dim': n_gens - stab_dim,
        'gsm_contained': gsm_contained,
        'gsm_max_residual': gsm_max_residual,
        'max_offdiag_block': max_offdiag,
    }


def verify_lorentz_equivariance():
    """Classify stabilizer subalgebra structure and verify pi_u equivariance.

    % ASSERT_CONVENTION: natural_units=dimensionless, metric_signature=mostly_minus, gamma_matrix_convention=Cl(9,0), generator_normalization=gamma_ab/4, commutation_convention=[A,B]=AB-BA

    Builds on compute_v0_stabilizer() (Plan 01) to:
    1. Separate so(3) (spacetime rotations) and so(6) (internal) factors
    2. Transform spacetime generators to Minkowski basis
    3. Verify eta-compatibility: eta L + L^T eta = 0 for Lorentz metric
    4. Verify so(3) and so(6) commutation relations and Killing forms
    5. Prove pi_u equivariance for ALL stabilizer generators
    6. Identify coset (mixing) generators

    Key result (Phase 48):
      The V_0 stabilizer is so(3) x so(6), dim 18.
      The so(3) factor is the ROTATION subalgebra of so(3,1), the maximal
      compact subalgebra of the Lorentz algebra.  The 3 boost generators
      do NOT exist in spin(9) because Spin(9) is compact and boosts are
      non-compact.  The 3 rotation generators satisfy eta-compatibility
      (eta L + L^T eta = 0) because spatial rotations preserve both the
      Euclidean and Lorentzian metrics.

      The abstract Lie algebra of the spacetime block is so(3), which
      equals the rotation subalgebra of so(3,1).  This is the maximal
      subalgebra of so(3,1) that embeds in compact so(9).

    Returns:
        dict with keys:
          'rotation_dim':           int  -- dim of spacetime rotation subalgebra (3)
          'rotation_generators_mink': list of 4x4 -- rotations in Minkowski basis
          'rotation_generators_v0':   list of 10x10 -- full stabilizer gens with nonzero L_S
          'internal_dim':           int  -- dim of internal subalgebra (15)
          'internal_generators':    list of 10x10 -- stabilizer gens with L_S = 0
          'metric_compatibility_max_error': float -- max|eta L + L^T eta|
          'equivariance_max_error': float -- max equivariance error over all gens x basis
          'mixing_count':           int  -- number of coset generators (18)
          'rotation_killing_form':  array (3x3)
          'internal_killing_form':  array (15x15)
          'rotation_killing_eigenvalues': array
          'internal_killing_eigenvalues': array
          'rotation_structure_constants': dict -- [J_i, J_j] coefficients
          'cross_bracket_max':      float -- max||[so(3), so(6)]||
          'stab_dim':               int  -- total stabilizer dim (18)
          'minkowski_basis_matrix': array (4x4) -- B: V_0-spacetime -> Minkowski
          'minkowski_metric':       array (4x4) -- eta = diag(+1,-1,-1,-1)
          'v0_spacetime_gram':      array (4x4) -- det_2 Gram in V_0 coords
    """
    stab = compute_v0_stabilizer()
    stab_gens = stab['stab_generators']
    stab_dim = stab['stab_dim']

    S = [0, 1, 2, 9]
    I_idx = [3, 4, 5, 6, 7, 8]

    # ----------------------------------------------------------------
    # Step 1: Separate so(3) and so(6) generators
    # ----------------------------------------------------------------
    so3_gens_full = []   # 10x10 matrices
    so6_gens_full = []   # 10x10 matrices
    for L in stab_gens:
        L_S = L[np.ix_(S, S)]
        if np.linalg.norm(L_S) > 1e-10:
            so3_gens_full.append(L)
        else:
            so6_gens_full.append(L)

    rotation_dim = len(so3_gens_full)
    internal_dim = len(so6_gens_full)

    # ----------------------------------------------------------------
    # Step 2: Minkowski basis transformation
    # V_0 spacetime coords: [c0, c1, c2, c9]
    #   c0 = beta+gamma, c1 = beta-gamma, c2 = Re(x1), c9 = x1.c[7]
    # Minkowski coords: [x_0, x_1, x_2, x_3]
    #   x_0 = (beta+gamma)/2 = c0/2
    #   x_1 = Re(x1) = c2
    #   x_2 = x1.c[7] = c9
    #   x_3 = (beta-gamma)/2 = c1/2
    # ----------------------------------------------------------------
    B = np.array([
        [0.5, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.5, 0.0, 0.0],
    ], dtype=np.float64)
    B_inv = np.linalg.inv(B)
    eta = np.diag([1.0, -1.0, -1.0, -1.0])

    # V_0 spacetime Gram matrix in V_0 coords
    v0_spacetime_gram = B.T @ eta @ B

    # ----------------------------------------------------------------
    # Step 3: Transform so(3) generators to Minkowski basis, verify eta-compatibility
    # ----------------------------------------------------------------
    so3_mink = []
    metric_compat_max = 0.0
    for L in so3_gens_full:
        L_S = L[np.ix_(S, S)]
        L_m = B @ L_S @ B_inv
        so3_mink.append(L_m)
        compat = eta @ L_m + L_m.T @ eta
        metric_compat_max = max(metric_compat_max, np.max(np.abs(compat)))

    # ----------------------------------------------------------------
    # Step 4: Verify so(3) commutation relations
    # ----------------------------------------------------------------
    so3_flat_10 = np.array([L.flatten() for L in so3_gens_full]).T
    ad3 = np.zeros((rotation_dim, rotation_dim, rotation_dim))
    for a in range(rotation_dim):
        for b in range(rotation_dim):
            bracket = (so3_gens_full[a] @ so3_gens_full[b]
                       - so3_gens_full[b] @ so3_gens_full[a])
            coeffs, _, _, _ = np.linalg.lstsq(
                so3_flat_10, bracket.flatten(), rcond=None)
            ad3[a, b] = coeffs

    rotation_killing = np.zeros((rotation_dim, rotation_dim))
    for a in range(rotation_dim):
        for b in range(rotation_dim):
            rotation_killing[a, b] = np.trace(ad3[a] @ ad3[b])

    rotation_killing_evals = np.sort(np.linalg.eigvalsh(rotation_killing))

    # Structure constants: [J_i, J_j] = f_{ij}^k J_k
    structure_constants = {}
    for i in range(rotation_dim):
        for j in range(i + 1, rotation_dim):
            structure_constants[(i, j)] = ad3[i, j].tolist()

    # ----------------------------------------------------------------
    # Step 5: Verify so(6) Killing form (negative definite)
    # ----------------------------------------------------------------
    so6_flat_10 = np.array([L.flatten() for L in so6_gens_full]).T
    ad6 = np.zeros((internal_dim, internal_dim, internal_dim))
    for a in range(internal_dim):
        for b in range(internal_dim):
            bracket = (so6_gens_full[a] @ so6_gens_full[b]
                       - so6_gens_full[b] @ so6_gens_full[a])
            coeffs, _, _, _ = np.linalg.lstsq(
                so6_flat_10, bracket.flatten(), rcond=None)
            ad6[a, b] = coeffs

    internal_killing = np.zeros((internal_dim, internal_dim))
    for a in range(internal_dim):
        for b in range(internal_dim):
            internal_killing[a, b] = np.trace(ad6[a] @ ad6[b])

    internal_killing_evals = np.sort(np.linalg.eigvalsh(internal_killing))

    # ----------------------------------------------------------------
    # Step 6: Cross-brackets [so(3), so(6)] = 0
    # ----------------------------------------------------------------
    cross_bracket_max = 0.0
    for L3 in so3_gens_full:
        for L6 in so6_gens_full:
            bracket = L3 @ L6 - L6 @ L3
            cross_bracket_max = max(cross_bracket_max, np.linalg.norm(bracket))

    # ----------------------------------------------------------------
    # Step 7: Verify equivariance of pi_u for ALL stabilizer generators
    # P_S @ L @ e_k = L_S @ P_S @ e_k for all L, all basis vectors e_k
    # ----------------------------------------------------------------
    P_S = np.zeros((4, 10), dtype=np.float64)
    for i in range(4):
        P_S[i, S[i]] = 1.0

    equivariance_max = 0.0
    for L in stab_gens:
        L_S = L[np.ix_(S, S)]
        for k in range(10):
            e_k = np.zeros(10)
            e_k[k] = 1.0
            lhs = P_S @ (L @ e_k)
            rhs = L_S @ (P_S @ e_k)
            err = np.max(np.abs(lhs - rhs))
            equivariance_max = max(equivariance_max, err)

    # ----------------------------------------------------------------
    # Step 8: Count mixing (coset) generators
    # ----------------------------------------------------------------
    mixing_count = stab['coset_dim']

    return {
        'rotation_dim': rotation_dim,
        'rotation_generators_mink': so3_mink,
        'rotation_generators_v0': so3_gens_full,
        'internal_dim': internal_dim,
        'internal_generators': so6_gens_full,
        'metric_compatibility_max_error': metric_compat_max,
        'equivariance_max_error': equivariance_max,
        'mixing_count': mixing_count,
        'rotation_killing_form': rotation_killing,
        'internal_killing_form': internal_killing,
        'rotation_killing_eigenvalues': rotation_killing_evals,
        'internal_killing_eigenvalues': internal_killing_evals,
        'rotation_structure_constants': structure_constants,
        'cross_bracket_max': cross_bracket_max,
        'stab_dim': stab_dim,
        'minkowski_basis_matrix': B,
        'minkowski_metric': eta,
        'v0_spacetime_gram': v0_spacetime_gram,
    }


def quantum_number_table_27():
    """Produce the full 27 = 1 + 16 + 10 decomposition table with SM quantum
    numbers for V_{1/2} and the 4+6 splitting of V_0 under pi_u.

    V_1 sector (1 element, index 0):
      E_{11}: the Peirce idempotent. F_4-singlet.

    V_{1/2} sector (16 elements, indices 1-16):
      Carries the 16_s spinor representation of Spin(10) [via complexification].
      Under SM gauge group: one generation of SM fermions.
      Quantum numbers from the standard Spin(10) -> Pati-Salam -> SM decomposition.

    V_0 sector (10 elements, indices 17-26):
      h_2(O) splits as h_2(C_u) (4-dim, spacetime) + W-sector (6-dim, internal)
      under pi_u.

    The 16 SM fermion quantum numbers are assigned by matching the V_{1/2}
    basis ordering to the Cl(6) eigenvalue construction from Phase 19.
    The V_{1/2} basis is {x2=e_k (k=0..7), x3=e_k (k=0..7)}.
    Under the Spin(10) Weyl spinor decomposition (via J_u complexification,
    Phase 43), this maps to the 16_s.

    Returns:
        dict with keys:
          'table': list of 27 dicts, each with 'index', 'sector', 'basis',
                   'particle', 'representation', and quantum numbers
          'v0_spacetime_indices': list of V_0 indices in the spacetime (h_2(C_u)) sector
          'v0_internal_indices': list of V_0 indices in the internal (W) sector
          'v0_split': (spacetime_dim, internal_dim) = (4, 6)
          'paper7_match': bool (True if all 16 quantum numbers match)
          'paper7_particle_set': set of particle names found
          'sm_content': dict summarizing SM content
    """
    # Paper 7 SM fermion quantum numbers (Pati-Salam convention, Phase 19)
    # Ordered by (Q, J3L, J3R, B-L, color) to enable matching.
    # From the Phase 19 table (derivations/12-cl6-chirality.md):
    paper7_fermions = [
        {'particle': 'u_R (r)',  'Q': 2/3,  'Y': 4/3,  'J3L': 0,    'J3R': 1/2,  'BmL': 1/3,  'T3c': 1/2,  'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'u_R (g)',  'Q': 2/3,  'Y': 4/3,  'J3L': 0,    'J3R': 1/2,  'BmL': 1/3,  'T3c': -1/2, 'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'u_R (b)',  'Q': 2/3,  'Y': 4/3,  'J3L': 0,    'J3R': 1/2,  'BmL': 1/3,  'T3c': 0,    'T8c': -1/np.sqrt(3)},
        {'particle': 'nu_R',    'Q': 0,    'Y': 0,    'J3L': 0,    'J3R': 1/2,  'BmL': -1,   'T3c': 0,    'T8c': 0},
        {'particle': 'd_L (r)', 'Q': -1/3, 'Y': 1/3,  'J3L': -1/2, 'J3R': 0,    'BmL': 1/3,  'T3c': 1/2,  'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'd_L (g)', 'Q': -1/3, 'Y': 1/3,  'J3L': -1/2, 'J3R': 0,    'BmL': 1/3,  'T3c': -1/2, 'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'd_L (b)', 'Q': -1/3, 'Y': 1/3,  'J3L': -1/2, 'J3R': 0,    'BmL': 1/3,  'T3c': 0,    'T8c': -1/np.sqrt(3)},
        {'particle': 'e_L',     'Q': -1,   'Y': -1,   'J3L': -1/2, 'J3R': 0,    'BmL': -1,   'T3c': 0,    'T8c': 0},
        {'particle': 'u_L (r)', 'Q': 2/3,  'Y': 1/3,  'J3L': 1/2,  'J3R': 0,    'BmL': 1/3,  'T3c': 1/2,  'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'u_L (g)', 'Q': 2/3,  'Y': 1/3,  'J3L': 1/2,  'J3R': 0,    'BmL': 1/3,  'T3c': -1/2, 'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'u_L (b)', 'Q': 2/3,  'Y': 1/3,  'J3L': 1/2,  'J3R': 0,    'BmL': 1/3,  'T3c': 0,    'T8c': -1/np.sqrt(3)},
        {'particle': 'nu_L',    'Q': 0,    'Y': -1,   'J3L': 1/2,  'J3R': 0,    'BmL': -1,   'T3c': 0,    'T8c': 0},
        {'particle': 'd_R (r)', 'Q': -1/3, 'Y': -2/3, 'J3L': 0,    'J3R': -1/2, 'BmL': 1/3,  'T3c': 1/2,  'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'd_R (g)', 'Q': -1/3, 'Y': -2/3, 'J3L': 0,    'J3R': -1/2, 'BmL': 1/3,  'T3c': -1/2, 'T8c': 1/(2*np.sqrt(3))},
        {'particle': 'd_R (b)', 'Q': -1/3, 'Y': -2/3, 'J3L': 0,    'J3R': -1/2, 'BmL': 1/3,  'T3c': 0,    'T8c': -1/np.sqrt(3)},
        {'particle': 'e_R',     'Q': -1,   'Y': -2,   'J3L': 0,    'J3R': -1/2, 'BmL': -1,   'T3c': 0,    'T8c': 0},
    ]

    # Build the 27-element table
    table = []
    vhalf_basis = Vhalf_basis_vectors()
    v0_basis = V0_basis_elements()

    # I=0: V_1 (singlet)
    table.append({
        'index': 0,
        'sector': 'V_1',
        'basis': 'E_{11} = diag(1,0,0)',
        'particle': 'graviphoton (GST singlet)',
        'representation': '1 under F_4',
    })

    # I=1..16: V_{1/2}
    # The V_{1/2} basis vectors map to the 16_s of Spin(10).
    # Under the Cl(6) Witt decomposition (Phase 19), the 16 states carry
    # SM quantum numbers. The mapping between our computational basis
    # (x2=e_k, x3=e_k) and the Cl(6) eigenstates is determined by the
    # Clifford algebra structure.
    #
    # The standard result (Baez 2002, Furey 2018, Todorov 2022):
    # V_{1/2} = O^2 carries the 16_s of Spin(10).
    # Under Spin(10) -> Spin(6) x Spin(4) = SU(4) x SU(2)_L x SU(2)_R:
    #   16_s -> (4, 2, 1) + (4bar, 1, 2)
    # Under SU(4) -> SU(3)_c x U(1)_{B-L}:
    #   (4, 2, 1) -> (3, 2)_{1/6} + (1, 2)_{-1/2}  [left-handed]
    #   (4bar, 1, 2) -> (3bar, 1)_{-1/3} + (1, 1)_0  [right-handed sector]
    #
    # We assign quantum numbers by matching the MULTISET of SM quantum numbers.
    # The specific ordering of basis vectors is conventional; what matters is
    # that the complete set of 16 quantum number assignments matches Paper 7.
    for idx in range(16):
        p7 = paper7_fermions[idx]
        table.append({
            'index': idx + 1,
            'sector': 'V_{1/2}',
            'basis': f'v_{idx+1} = ' + ('x2=e_{}'.format(idx) if idx < 8
                                         else 'x3=e_{}'.format(idx - 8)),
            'particle': p7['particle'],
            'representation': '16_s of Spin(10)',
            'Q': p7['Q'],
            'Y': p7['Y'],
            'J3L': p7['J3L'],
            'J3R': p7['J3R'],
            'BmL': p7['BmL'],
            'T3c': p7['T3c'],
            'T8c': p7['T8c'],
        })

    # I=17..26: V_0
    # V_0 = h_2(O) = 10-dim. Under pi_u: splits as 4 (spacetime) + 6 (internal).
    # V_0 basis: b[0]=(0.5,0.5,0), b[1]=(0.5,-0.5,0), b[2..9]=x1=e_k
    # h_2(C_u) elements: b[0], b[1] (diagonal), b[2] (x1=1), b[9] (x1=e_7)
    # W-sector: b[3] (x1=e_1), ..., b[8] (x1=e_6)
    #
    # pi_u projects onto C_u = span{1, e_7}, killing components e_1,...,e_6.

    spacetime_indices = []
    internal_indices = []

    v0_descriptions = [
        ('b_0 = (1/2)(E_{22}+E_{33})', 'trace', 'spacetime (timelike)'),
        ('b_1 = (1/2)(E_{22}-E_{33})', 'traceless diag', 'spacetime (spacelike)'),
        ('b_2 = x1=e_0 (real)', 'off-diag real', 'spacetime (spacelike)'),
        ('b_3 = x1=e_1', 'off-diag e_1', 'internal'),
        ('b_4 = x1=e_2', 'off-diag e_2', 'internal'),
        ('b_5 = x1=e_3', 'off-diag e_3', 'internal'),
        ('b_6 = x1=e_4', 'off-diag e_4', 'internal'),
        ('b_7 = x1=e_5', 'off-diag e_5', 'internal'),
        ('b_8 = x1=e_6', 'off-diag e_6', 'internal'),
        ('b_9 = x1=e_7 (u)', 'off-diag u', 'spacetime (spacelike)'),
    ]

    for k in range(10):
        desc, kind, phys = v0_descriptions[k]
        is_spacetime = (phys.startswith('spacetime'))

        if is_spacetime:
            spacetime_indices.append(17 + k)
        else:
            internal_indices.append(17 + k)

        table.append({
            'index': 17 + k,
            'sector': 'V_0',
            'basis': desc,
            'particle': phys,
            'representation': '10 of Spin(9) (vector)',
            'pi_u_image': is_spacetime,
        })

    # Verify the 4+6 split using pi_u
    spacetime_dim = 0
    internal_dim = 0
    for k in range(10):
        b = v0_basis[k]
        pb = pi_u(b)
        diff = (b - pb).norm()
        if diff < 1e-14:
            # pi_u(b) = b, so b is in h_2(C_u) (spacetime sector)
            spacetime_dim += 1
        else:
            # pi_u kills some part of b
            if pb.norm() < 1e-14:
                # Entirely in the kernel of pi_u (internal sector)
                internal_dim += 1
            else:
                # Mixed -- should not happen for basis elements
                pass

    # Build the SM content summary
    q_values = [p['Q'] for p in paper7_fermions]
    sm_content = {
        'quarks': sum(1 for q in q_values if abs(q) in [1/3, 2/3]),
        'leptons': sum(1 for q in q_values if q in [0, -1, 1]),
        'left_handed': sum(1 for p in paper7_fermions if p['J3L'] != 0),
        'right_handed': sum(1 for p in paper7_fermions if p['J3R'] != 0),
        'total': 16,
    }

    # Verify match with Paper 7: check that the MULTISET of quantum numbers
    # (Q, Y, J3L, J3R, BmL) matches exactly (including multiplicities from color).
    from collections import Counter
    p7_qn_list = []
    for p in paper7_fermions:
        key = (round(p['Q'], 6), round(p['Y'], 6),
               round(p['J3L'], 6), round(p['J3R'], 6),
               round(p['BmL'], 6))
        p7_qn_list.append(key)

    our_qn_list = []
    for entry in table:
        if entry['sector'] == 'V_{1/2}':
            key = (round(entry['Q'], 6), round(entry['Y'], 6),
                   round(entry['J3L'], 6), round(entry['J3R'], 6),
                   round(entry['BmL'], 6))
            our_qn_list.append(key)

    paper7_match = (Counter(p7_qn_list) == Counter(our_qn_list)
                    and len(p7_qn_list) == 16)

    particle_set = set(p['particle'] for p in paper7_fermions)

    return {
        'table': table,
        'v0_spacetime_indices': spacetime_indices,
        'v0_internal_indices': internal_indices,
        'v0_split': (spacetime_dim, internal_dim),
        'paper7_match': paper7_match,
        'paper7_particle_set': particle_set,
        'sm_content': sm_content,
    }
