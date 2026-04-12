"""
Peirce coupling constants for h_3(K) Jordan algebras.

Computes direct (level-1) vs indirect (level-2) coupling of Peirce
subspaces to the observer idempotent E_{11}, for K = R, C, H, O.

The Jordan product is (X o Y) = (1/2)(XY + YX) where XY is formal
matrix multiplication using the division algebra multiplication.

For K = R, we use ordinary real matrix multiplication.
For K = C, H, O, we implement the algebra explicitly.
"""

import numpy as np
from itertools import product as iterproduct

np.set_printoptions(precision=10, suppress=True)

# ============================================================
# Part 0: Division algebra implementations
# ============================================================

class RealAlgebra:
    """K = R, d=1"""
    dim = 1
    name = "R"

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def conj(a):
        return a.copy()

    @staticmethod
    def norm_sq(a):
        return float(a[0]**2)

    @staticmethod
    def re(a):
        return float(a[0])

    @staticmethod
    def zero():
        return np.zeros(1)

    @staticmethod
    def one():
        return np.array([1.0])

    @staticmethod
    def basis(i):
        v = np.zeros(1)
        v[0] = 1.0
        return v


class ComplexAlgebra:
    """K = C, d=2"""
    dim = 2
    name = "C"

    @staticmethod
    def mul(a, b):
        # (a0 + a1*i)(b0 + b1*i) = (a0*b0 - a1*b1) + (a0*b1 + a1*b0)*i
        return np.array([a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]])

    @staticmethod
    def conj(a):
        return np.array([a[0], -a[1]])

    @staticmethod
    def norm_sq(a):
        return float(a[0]**2 + a[1]**2)

    @staticmethod
    def re(a):
        return float(a[0])

    @staticmethod
    def zero():
        return np.zeros(2)

    @staticmethod
    def one():
        return np.array([1.0, 0.0])

    @staticmethod
    def basis(i):
        v = np.zeros(2)
        v[i] = 1.0
        return v


class QuaternionAlgebra:
    """K = H, d=4. Basis: 1, i, j, k with ij=k, jk=i, ki=j."""
    dim = 4
    name = "H"

    @staticmethod
    def mul(a, b):
        # a = a0 + a1*i + a2*j + a3*k
        r = np.zeros(4)
        r[0] = a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
        r[1] = a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2]
        r[2] = a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1]
        r[3] = a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]
        return r

    @staticmethod
    def conj(a):
        return np.array([a[0], -a[1], -a[2], -a[3]])

    @staticmethod
    def norm_sq(a):
        return float(np.sum(a**2))

    @staticmethod
    def re(a):
        return float(a[0])

    @staticmethod
    def zero():
        return np.zeros(4)

    @staticmethod
    def one():
        v = np.zeros(4); v[0] = 1.0; return v

    @staticmethod
    def basis(i):
        v = np.zeros(4); v[i] = 1.0; return v


class OctonionAlgebra:
    """K = O, d=8. Fano-plane multiplication table."""
    dim = 8
    name = "O"

    # Multiplication table: e_i * e_j = sign * e_k
    # Using the standard Fano plane: (1,2,3), (1,4,5), (2,4,6), (2,5,7), (3,4,7), (1,6,7), (3,5,6)
    # e_0 = 1 (identity)
    # Triples (i,j,k) with e_i * e_j = e_k (and cyclic)
    _triples = [
        (1,2,4), (1,3,7), (1,5,6),
        (2,3,5), (2,6,7),
        (3,4,6),
        (4,5,7)
    ]

    @staticmethod
    def _build_table():
        """Build full multiplication table e_i * e_j -> (sign, index)"""
        table = {}
        # e_0 * e_i = e_i, e_i * e_0 = e_i
        for i in range(8):
            table[(0, i)] = (1, i)
            table[(i, 0)] = (1, i)
        # e_i * e_i = -1 for i >= 1
        for i in range(1, 8):
            table[(i, i)] = (-1, 0)
        # From triples
        for (a, b, c) in OctonionAlgebra._triples:
            # e_a * e_b = e_c
            table[(a, b)] = (1, c)
            table[(b, a)] = (-1, c)
            # e_b * e_c = e_a
            table[(b, c)] = (1, a)
            table[(c, b)] = (-1, a)
            # e_c * e_a = e_b
            table[(c, a)] = (1, b)
            table[(a, c)] = (-1, b)
        return table

    _table = None

    @classmethod
    def _get_table(cls):
        if cls._table is None:
            cls._table = cls._build_table()
        return cls._table

    @classmethod
    def mul(cls, a, b):
        table = cls._get_table()
        r = np.zeros(8)
        for i in range(8):
            if abs(a[i]) < 1e-15:
                continue
            for j in range(8):
                if abs(b[j]) < 1e-15:
                    continue
                sign, k = table[(i, j)]
                r[k] += sign * a[i] * b[j]
        return r

    @staticmethod
    def conj(a):
        r = np.zeros(8)
        r[0] = a[0]
        r[1:] = -a[1:]
        return r

    @staticmethod
    def norm_sq(a):
        return float(np.sum(a**2))

    @staticmethod
    def re(a):
        return float(a[0])

    @staticmethod
    def zero():
        return np.zeros(8)

    @staticmethod
    def one():
        v = np.zeros(8); v[0] = 1.0; return v

    @staticmethod
    def basis(i):
        v = np.zeros(8); v[i] = 1.0; return v


# ============================================================
# Part 1: Hermitian 3x3 matrix over K
# ============================================================

class H3Matrix:
    """
    3x3 Hermitian matrix over division algebra K.

    [[a,    x3*, x2*],
     [x3,   b,   x1*],
     [x2,   x1,  c  ]]

    where a, b, c are real and x1, x2, x3 are in K.

    Stored as: diag = [a, b, c], off = [x1, x2, x3] (each a K-vector)
    Convention: x1 is (2,3) entry, x2 is (1,3) entry, x3 is (1,2) entry
    """
    def __init__(self, K, diag, off):
        self.K = K
        self.diag = list(diag)  # [a, b, c] reals
        self.off = list(off)    # [x1, x2, x3] K-elements

    @classmethod
    def zero(cls, K):
        return cls(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), K.zero()])

    @classmethod
    def E(cls, K, i):
        """Diagonal idempotent E_{ii}"""
        d = [0.0, 0.0, 0.0]
        d[i] = 1.0
        return cls(K, d, [K.zero(), K.zero(), K.zero()])

    def trace(self):
        return sum(self.diag)

    def trace_inner(self, other):
        """Tr(self o other) = sum of products of corresponding components,
        weighted appropriately."""
        # For Hermitian matrices, Tr(A o B) = (1/2) Tr(AB + BA) = Tr(AB)
        # We compute Tr(AB) directly.
        # Tr(AB) = sum_i (AB)_{ii} = sum_i sum_j A_{ij} B_{ji}
        # For Hermitian: B_{ji} = conj(B_{ij})
        # Diagonal part: sum_i a_i * b_i
        K = self.K
        result = sum(self.diag[i] * other.diag[i] for i in range(3))
        # Off-diagonal part: 2 * Re(x_k * conj(y_k)) for each pair
        # Because A_{ij}B_{ji} + A_{ji}B_{ij} = x*conj(y) + conj(x)*y = 2*Re(x*conj(y))
        for k in range(3):
            prod = K.mul(self.off[k], K.conj(other.off[k]))
            result += 2.0 * K.re(prod)
        return result

    def norm_sq(self):
        """||X||^2 = Tr(X o X) = Tr(X^2)"""
        return self.trace_inner(self)

    def scale(self, s):
        K = self.K
        return H3Matrix(K, [s*d for d in self.diag], [s*x for x in self.off])

    def add(self, other):
        K = self.K
        return H3Matrix(K,
            [self.diag[i] + other.diag[i] for i in range(3)],
            [self.off[i] + other.off[i] for i in range(3)])

    def neg(self):
        return self.scale(-1.0)

    def jordan_product(self, other):
        """
        Compute self o other = (1/2)(self * other + other * self)
        using explicit matrix multiplication with K-multiplication.

        For 3x3 Hermitian matrices over K:
        self = [[a, x3*, x2*], [x3, b, x1*], [x2, x1, c]]

        We compute the full matrix product and symmetrize.
        """
        K = self.K

        # Extract components
        a1, b1, c1 = self.diag
        x1_1, x2_1, x3_1 = self.off  # x1=(2,3), x2=(1,3), x3=(1,2)

        a2, b2, c2 = other.diag
        x1_2, x2_2, x3_2 = other.off

        # Matrix product P = self * other
        # P_{11} = a1*a2 + x3_1* * x3_2 + x2_1* * x2_2
        # But we need to be careful: (i,j) entry of self is:
        # (1,1)=a1, (1,2)=x3_1*, (1,3)=x2_1*
        # (2,1)=x3_1, (2,2)=b1, (2,3)=x1_1*
        # (3,1)=x2_1, (3,2)=x1_1, (3,3)=c1

        # Let's define the full entries:
        # S[i][j] for self, O[i][j] for other
        # S[0][0] = a1 (real, treat as K element)
        # S[0][1] = conj(x3_1), S[0][2] = conj(x2_1)
        # S[1][0] = x3_1, S[1][1] = b1, S[1][2] = conj(x1_1)
        # S[2][0] = x2_1, S[2][1] = x1_1, S[2][2] = c1

        def to_K(r):
            """Convert real number to K element"""
            v = K.zero()
            v[0] = r
            return v

        S = [[to_K(a1), K.conj(x3_1), K.conj(x2_1)],
             [x3_1.copy(), to_K(b1), K.conj(x1_1)],
             [x2_1.copy(), x1_1.copy(), to_K(c1)]]

        O = [[to_K(a2), K.conj(x3_2), K.conj(x2_2)],
             [x3_2.copy(), to_K(b2), K.conj(x1_2)],
             [x2_2.copy(), x1_2.copy(), to_K(c2)]]

        # P = S * O, Q = O * S
        # (P + Q)/2 should be Hermitian

        P = [[K.zero() for _ in range(3)] for _ in range(3)]
        Q = [[K.zero() for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    P[i][j] = P[i][j] + K.mul(S[i][k], O[k][j])
                    Q[i][j] = Q[i][j] + K.mul(O[i][k], S[k][j])

        # Result = (P + Q) / 2
        R = [[0.5 * (P[i][j] + Q[i][j]) for j in range(3)] for i in range(3)]

        # Extract Hermitian components
        # Diagonal: real parts of R[i][i]
        new_diag = [K.re(R[i][i]) for i in range(3)]

        # Off-diagonal: R[2][1] = x1_new (the (3,2) = (2,3) lower entry)
        # Actually: (2,1) entry is x3 (lower-left of (1,2) block)
        # Let me re-check convention:
        # (2,3) lower entry = x1, (1,3) lower entry = x2, (1,2) lower entry = x3
        # In 0-indexed: (1,2) = x1, (0,2) = x2, (0,1) = x3
        # Lower entries: row > col
        # x1 is at (1,2) -> row=1, col=2 in 0-indexed, but it's the LOWER entry
        # Wait, in our convention: x1 is at position (2,3) in 1-indexed = (1,2) in 0-indexed
        # The LOWER triangle entry at (1,2) 0-indexed is at row=2, col=1... no.
        #
        # Let me re-read: the matrix is:
        # [[a,    x3*, x2*],    row 0
        #  [x3,   b,   x1*],    row 1
        #  [x2,   x1,  c  ]]    row 2
        #
        # So x1 is at (2,1) in 0-indexed (row 2, col 1)
        # x2 is at (2,0) in 0-indexed
        # x3 is at (1,0) in 0-indexed
        # And conjugates: x1* at (1,2), x2* at (0,2), x3* at (0,1)

        # From R (which is Hermitian up to numerics), extract the lower-triangle off-diags:
        x1_new = R[2][1].copy()  # (2,1) entry
        x2_new = R[2][0].copy()  # (2,0) entry
        x3_new = R[1][0].copy()  # (1,0) entry

        return H3Matrix(K, new_diag, [x1_new, x2_new, x3_new])

    def peirce_decompose(self, eidx=0):
        """
        Peirce decomposition relative to E_{eidx, eidx}.
        Returns (V1_component, V_half_component, V0_component).

        For E_{11} (eidx=0):
        V_1: only diagonal (eidx,eidx) entry
        V_{1/2}: off-diagonals involving row/col eidx
        V_0: the complementary 2x2 block
        """
        K = self.K

        if eidx == 0:
            # V_1: a * E_{11}
            v1 = H3Matrix(K, [self.diag[0], 0.0, 0.0],
                          [K.zero(), K.zero(), K.zero()])

            # V_{1/2}: x2 and x3 (off-diags involving row/col 0)
            v_half = H3Matrix(K, [0.0, 0.0, 0.0],
                              [K.zero(), self.off[1].copy(), self.off[2].copy()])

            # V_0: the (1,1), (2,2), (1,2) block = b, c, x1
            v0 = H3Matrix(K, [0.0, self.diag[1], self.diag[2]],
                          [self.off[0].copy(), K.zero(), K.zero()])

            return v1, v_half, v0
        else:
            raise NotImplementedError("Only eidx=0 implemented")

    def describe(self):
        K = self.K
        print(f"  diag = [{self.diag[0]:.6f}, {self.diag[1]:.6f}, {self.diag[2]:.6f}]")
        for i, name in enumerate(['x1', 'x2', 'x3']):
            print(f"  {name} = {self.off[i]}")

    def det(self):
        """
        Determinant of 3x3 Hermitian matrix over K.
        det = abc + 2*Re(x1*x2*x3) - a*|x1|^2 - b*|x2|^2 - c*|x3|^2

        Note: for octonions, x1*x2*x3 means (x1*x2)*x3 (left-to-right).
        The determinant is well-defined and real for h_3(O).
        """
        K = self.K
        a, b, c = self.diag
        x1, x2, x3 = self.off

        result = a * b * c
        # 2 * Re((x1 * x2) * x3)
        # But actually the standard formula uses specific ordering
        # det = abc + 2*Re(x1 x2 x3) - a*N(x1) - b*N(x2) - c*N(x3)
        # where x1 x2 x3 means multiply in that order
        prod = K.mul(K.mul(x1, x2), x3)
        result += 2.0 * K.re(prod)
        result -= a * K.norm_sq(x1)
        result -= b * K.norm_sq(x2)
        result -= c * K.norm_sq(x3)
        return result


def run_coupling_analysis(K):
    """Run the full Peirce coupling analysis for h_3(K)."""
    d = K.dim
    print(f"\n{'='*70}")
    print(f"  h_3({K.name}),  dim(K) = {d}")
    print(f"  dim(h_3) = 3 + 3*{d} = {3 + 3*d}")
    print(f"  V_1: dim 1,  V_{{1/2}}: dim 2*{d} = {2*d},  V_0: dim {1 + d} (= h_2({K.name}))")
    print(f"{'='*70}")

    # --------------------------------------------------------
    # Direct coupling: V_{1/2} o V_{1/2} -> V_1
    # --------------------------------------------------------
    print(f"\n--- Direct coupling (V_{{1/2}} o V_{{1/2}} -> V_1) ---")

    # Test with x2 direction (a unit octonion in position x2)
    for basis_idx in range(d):
        x2_val = K.basis(basis_idx)
        A = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_val, K.zero()])

        AoA = A.jordan_product(A)
        v1, v_half, v0 = AoA.peirce_decompose(0)

        if basis_idx == 0:
            print(f"\n  A = unit x2 (basis {basis_idx}), ||A||^2 = {A.norm_sq():.6f}")
            print(f"  A o A:")
            AoA.describe()
            print(f"  P_1(A o A) = {v1.diag[0]:.6f} * E_11")
            print(f"  P_0(A o A) diag[2] = {v0.diag[2]:.6f}")
            print(f"  Direct coupling k_direct = P_1 / ||A||^2 = {v1.diag[0] / A.norm_sq():.6f}")

    # Test with x3 direction
    x3_val = K.basis(0)
    B = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), x3_val])
    BoB = B.jordan_product(B)
    v1_B, _, _ = BoB.peirce_decompose(0)
    print(f"\n  B = unit x3 (basis 0), ||B||^2 = {B.norm_sq():.6f}")
    print(f"  P_1(B o B) = {v1_B.diag[0]:.6f} * E_11")
    print(f"  Direct coupling k_direct = {v1_B.diag[0] / B.norm_sq():.6f}")

    # General: random V_{1/2} element
    np.random.seed(42)
    x2_rand = np.random.randn(d)
    x3_rand = np.random.randn(d)
    x2_rand /= np.sqrt(np.sum(x2_rand**2))  # normalize components
    x3_rand /= np.sqrt(np.sum(x3_rand**2))

    R = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_rand, x3_rand])
    RoR = R.jordan_product(R)
    v1_R, _, _ = RoR.peirce_decompose(0)
    print(f"\n  Random V_{{1/2}} element, ||R||^2 = {R.norm_sq():.6f}")
    print(f"  P_1(R o R) = {v1_R.diag[0]:.6f} * E_11")
    print(f"  Direct coupling = P_1 / ||R||^2 = {v1_R.diag[0] / R.norm_sq():.6f}")

    # --------------------------------------------------------
    # Confirm V_0 decouples from V_1
    # --------------------------------------------------------
    print(f"\n--- V_0 decoupling check ---")
    x1_val = K.basis(0)
    C = H3Matrix(K, [0.0, 0.5, 0.5], [x1_val, K.zero(), K.zero()])
    E11 = H3Matrix.E(K, 0)
    CoE = C.jordan_product(E11)
    print(f"  C (V_0 element) o E_11:")
    CoE.describe()
    print(f"  ||C o E_11|| = {CoE.norm_sq():.10f}  (should be 0)")

    # --------------------------------------------------------
    # Indirect coupling: V_0 o V_{1/2} -> V_{1/2}, then -> V_1
    # --------------------------------------------------------
    print(f"\n--- Indirect coupling (V_0 -> V_{{1/2}} -> V_1) ---")

    # Step 1: c o a where c in V_0, a in V_{1/2}
    # Use unit x1 in V_0 and unit x2 in V_{1/2}

    results = []

    for c_type, c_mat in [
        ("x1=e_0", H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(0), K.zero(), K.zero()])),
        ("b=1,c=0", H3Matrix(K, [0.0, 1.0, 0.0], [K.zero(), K.zero(), K.zero()])),
        ("b=0,c=1", H3Matrix(K, [0.0, 0.0, 1.0], [K.zero(), K.zero(), K.zero()])),
    ]:
        for a_type, a_mat in [
            ("x2=e_0", H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.basis(0), K.zero()])),
            ("x3=e_0", H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), K.basis(0)])),
        ]:
            # w = c o a (should be in V_{1/2})
            w = c_mat.jordan_product(a_mat)
            _, w_half, _ = w.peirce_decompose(0)

            # Now w_half o a -> project to V_1
            wa = w_half.jordan_product(a_mat)
            v1_wa, _, _ = wa.peirce_decompose(0)

            coupling = v1_wa.diag[0]
            results.append((c_type, a_type, coupling, c_mat.norm_sq(), a_mat.norm_sq()))

            print(f"\n  c = ({c_type}), ||c||^2 = {c_mat.norm_sq():.4f}")
            print(f"  a = ({a_type}), ||a||^2 = {a_mat.norm_sq():.4f}")
            print(f"  w = c o a:")
            w.describe()
            print(f"  P_{{1/2}}(w):")
            w_half.describe()
            print(f"  P_1(w_half o a) = {coupling:.6f} * E_11")

    # --------------------------------------------------------
    # Systematic: average over random directions
    # --------------------------------------------------------
    print(f"\n--- Statistical analysis: random directions ---")

    N_samples = 1000
    np.random.seed(123)

    direct_couplings = []
    indirect_couplings = []

    for _ in range(N_samples):
        # Random unit V_{1/2} element
        x2_r = np.random.randn(d)
        x3_r = np.random.randn(d)
        a_rand = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_r, x3_r])
        norm_a = a_rand.norm_sq()
        if norm_a < 1e-10:
            continue
        # Normalize
        scale = 1.0 / np.sqrt(norm_a)
        a_rand = a_rand.scale(scale)

        # Direct: P_1(a o a) for unit a
        aoa = a_rand.jordan_product(a_rand)
        v1_d, _, _ = aoa.peirce_decompose(0)
        direct_couplings.append(v1_d.diag[0])

        # Random unit V_0 element
        b_r, c_r = np.random.randn(), np.random.randn()
        x1_r = np.random.randn(d)
        c_rand = H3Matrix(K, [0.0, b_r, c_r], [x1_r, K.zero(), K.zero()])
        norm_c = c_rand.norm_sq()
        if norm_c < 1e-10:
            continue
        scale_c = 1.0 / np.sqrt(norm_c)
        c_rand = c_rand.scale(scale_c)

        # Indirect: P_1((P_{1/2}(c o a)) o a) for unit c, unit a
        w = c_rand.jordan_product(a_rand)
        _, w_half, _ = w.peirce_decompose(0)
        wa = w_half.jordan_product(a_rand)
        v1_i, _, _ = wa.peirce_decompose(0)
        indirect_couplings.append(v1_i.diag[0])

    direct_arr = np.array(direct_couplings)
    indirect_arr = np.array(indirect_couplings)

    print(f"\n  Over {len(direct_arr)} random samples:")
    print(f"  Direct coupling P_1(a o a) for ||a||=1:")
    print(f"    mean = {np.mean(direct_arr):.6f}")
    print(f"    std  = {np.std(direct_arr):.6f}")
    print(f"    min  = {np.min(direct_arr):.6f}")
    print(f"    max  = {np.max(direct_arr):.6f}")

    print(f"\n  Indirect coupling P_1(P_{{1/2}}(c o a) o a) for ||a||=||c||=1:")
    print(f"    mean = {np.mean(indirect_arr):.6f}")
    print(f"    std  = {np.std(indirect_arr):.6f}")
    print(f"    min  = {np.min(indirect_arr):.6f}")
    print(f"    max  = {np.max(indirect_arr):.6f}")

    print(f"\n  |mean indirect| / mean direct = {abs(np.mean(indirect_arr)) / np.mean(direct_arr):.6f}")
    print(f"  RMS indirect / RMS direct = {np.sqrt(np.mean(indirect_arr**2)) / np.sqrt(np.mean(direct_arr**2)):.6f}")

    # --------------------------------------------------------
    # Determinant cubic coupling
    # --------------------------------------------------------
    print(f"\n--- Determinant cubic coupling ---")

    # det = abc + 2*Re(x1*x2*x3) - a*|x1|^2 - b*|x2|^2 - c*|x3|^2
    # The mixed cubic term: d^3(det)/(dx1 dx2 dx3) at identity directions
    # For unit e_0 in each slot:
    x1_u = K.basis(0)
    x2_u = K.basis(0)
    x3_u = K.basis(0)

    # Numerical derivative
    eps = 1e-5
    def det_at(t1, t2, t3):
        M = H3Matrix(K, [0.0, 0.0, 0.0], [t1 * x1_u, t2 * x2_u, t3 * x3_u])
        return M.det()

    # d^3 det / dt1 dt2 dt3 at (0,0,0)
    d3 = 0.0
    for s1, s2, s3 in iterproduct([1, -1], repeat=3):
        d3 += s1 * s2 * s3 * det_at(s1*eps, s2*eps, s3*eps)
    d3 /= (8 * eps**3)

    print(f"  d^3(det)/d(t1)d(t2)d(t3) at origin = {d3:.6f}")
    print(f"  (expected: 2.0 for aligned directions, from 2*Re(x1*x2*x3) term)")

    # With non-aligned directions
    if d > 1:
        x1_u2 = K.basis(1)
        def det_at2(t1, t2, t3):
            M = H3Matrix(K, [0.0, 0.0, 0.0], [t1 * x1_u2, t2 * x2_u, t3 * x3_u])
            return M.det()

        d3_2 = 0.0
        for s1, s2, s3 in iterproduct([1, -1], repeat=3):
            d3_2 += s1 * s2 * s3 * det_at2(s1*eps, s2*eps, s3*eps)
        d3_2 /= (8 * eps**3)

        print(f"  d^3(det)/d(t1)d(t2)d(t3) with x1=e_1, x2=x3=e_0 = {d3_2:.6f}")
        print(f"  (expected: 0.0 for orthogonal imaginary directions)")

    return direct_arr, indirect_arr


def compute_max_indirect_coupling(K):
    """
    Find the MAXIMUM indirect coupling over all unit a in V_{1/2} and unit c in V_0.

    The indirect coupling is: f(a, c) = P_1(P_{1/2}(c o a) o a)[E_11 coefficient]

    This is a degree-3 polynomial in a and degree-1 in c.
    For fixed a, it's linear in c, so the max over unit c is the operator norm.
    """
    d = K.dim
    print(f"\n--- Maximum indirect coupling for h_3({K.name}) ---")

    # For a more careful analysis, fix a = unit x2 direction
    # and vary c over all unit V_0 elements

    x2_val = K.basis(0)
    a_fixed = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_val, K.zero()])
    # ||a|| = sqrt(2) * |x2| = sqrt(2), normalize
    a_norm = np.sqrt(a_fixed.norm_sq())
    a_fixed = a_fixed.scale(1.0 / a_norm)

    print(f"\n  Fixed a = unit x2 direction (normalized), ||a||^2 = {a_fixed.norm_sq():.6f}")

    # Scan over V_0 basis elements
    # V_0 basis: E_{22}, E_{33}, and x1 basis vectors
    v0_basis = []
    v0_basis.append(("E_22", H3Matrix(K, [0.0, 1.0, 0.0], [K.zero(), K.zero(), K.zero()])))
    v0_basis.append(("E_33", H3Matrix(K, [0.0, 0.0, 1.0], [K.zero(), K.zero(), K.zero()])))
    for i in range(d):
        v0_basis.append((f"x1_e{i}", H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(i), K.zero(), K.zero()])))

    print(f"\n  Indirect coupling for each V_0 basis direction (with a = unit x2):")
    for name, c_mat in v0_basis:
        c_norm = np.sqrt(c_mat.norm_sq())
        c_unit = c_mat.scale(1.0 / c_norm)

        w = c_unit.jordan_product(a_fixed)
        _, w_half, _ = w.peirce_decompose(0)
        wa = w_half.jordan_product(a_fixed)
        v1_wa, _, _ = wa.peirce_decompose(0)

        print(f"    c = {name:8s} (||c||=1): P_1 = {v1_wa.diag[0]:+.6f}")

    # Now with a = unit x3 direction
    x3_val = K.basis(0)
    a_fixed2 = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), x3_val])
    a_norm2 = np.sqrt(a_fixed2.norm_sq())
    a_fixed2 = a_fixed2.scale(1.0 / a_norm2)

    print(f"\n  Fixed a = unit x3 direction (normalized), ||a||^2 = {a_fixed2.norm_sq():.6f}")
    print(f"\n  Indirect coupling for each V_0 basis direction (with a = unit x3):")
    for name, c_mat in v0_basis:
        c_norm = np.sqrt(c_mat.norm_sq())
        c_unit = c_mat.scale(1.0 / c_norm)

        w = c_unit.jordan_product(a_fixed2)
        _, w_half, _ = w.peirce_decompose(0)
        wa = w_half.jordan_product(a_fixed2)
        v1_wa, _, _ = wa.peirce_decompose(0)

        print(f"    c = {name:8s} (||c||=1): P_1 = {v1_wa.diag[0]:+.6f}")


def analytic_formulas():
    """
    Derive the coupling formulas analytically using the explicit matrix product.
    """
    print(f"\n{'='*70}")
    print(f"  ANALYTIC DERIVATION")
    print(f"{'='*70}")

    print("""
For h_3(K) with idempotent E_{11}:

DIRECT COUPLING:
  Take a in V_{1/2} with x2 component alpha, x3 component beta (both in K).

  a = [[0,      beta*, alpha*],
       [beta,   0,     0     ],
       [alpha,  0,     0     ]]

  ||a||^2 = Tr(a^2) = 2*(|alpha|^2 + |beta|^2)

  a o a = a^2 (since a is real-symmetric in matrix sense)

  (a^2)_{11} = |beta|^2 + |alpha|^2
  (a^2)_{22} = |beta|^2
  (a^2)_{33} = |alpha|^2
  (a^2)_{23} = conj(beta) * alpha    [x1 position]
  (a^2)_{13} = 0                      [x2 position]
  (a^2)_{12} = 0                      [x3 position]

  Wait - let me compute more carefully.

  Actually a^2:
  Row 0 of a: [0, beta*, alpha*]
  Col 0 of a: [0, beta, alpha]^T

  (a^2)_{00} = 0*0 + beta* * beta + alpha* * alpha = |beta|^2 + |alpha|^2

  Row 0, Col 1: [0, beta*, alpha*] . [beta*, 0, 0]^T = beta* * beta* + ...

  Hmm, the (i,j) entry of a*a is sum_k a_{ik} * a_{kj}.

  a_{01} = conj(beta), a_{02} = conj(alpha)
  a_{10} = beta, a_{11} = 0, a_{12} = 0  (for pure x3)
  a_{20} = alpha, a_{21} = 0, a_{22} = 0  (for pure x2)

  But wait - if BOTH x2 and x3 are nonzero, then:
  a_{12} = conj(x1) = 0 (no x1 component in V_{1/2})
  a_{21} = x1 = 0

  (a^2)_{00} = a_{00}*a_{00} + a_{01}*a_{10} + a_{02}*a_{20}
             = 0 + conj(beta)*beta + conj(alpha)*alpha
             = |beta|^2 + |alpha|^2

  (a^2)_{01} = a_{00}*a_{01} + a_{01}*a_{11} + a_{02}*a_{21}
             = 0 + 0 + 0 = 0

  (a^2)_{02} = a_{00}*a_{02} + a_{01}*a_{12} + a_{02}*a_{22}
             = 0 + 0 + 0 = 0

  (a^2)_{10} = a_{10}*a_{00} + a_{11}*a_{10} + a_{12}*a_{20}
             = 0 + 0 + 0 = 0

  (a^2)_{11} = a_{10}*a_{01} + a_{11}*a_{11} + a_{12}*a_{21}
             = beta*conj(beta) + 0 + 0 = |beta|^2

  (a^2)_{12} = a_{10}*a_{02} + a_{11}*a_{12} + a_{12}*a_{22}
             = beta*conj(alpha) + 0 + 0

  (a^2)_{21} = conj of (a^2)_{12} = alpha*conj(beta)

  (a^2)_{22} = a_{20}*a_{02} + a_{21}*a_{12} + a_{22}*a_{22}
             = alpha*conj(alpha) + 0 + 0 = |alpha|^2

  BUT: for octonions, a_{10}*a_{01} = beta * conj(beta) = |beta|^2 ✓
  And: a_{10}*a_{02} = beta * conj(alpha) (this IS in the x1 slot)

  So a^2 (without Jordan symmetrization, just matrix product a*a):
  [[|beta|^2+|alpha|^2,  0,                  0               ],
   [0,                   |beta|^2,           beta*conj(alpha) ],
   [0,                   alpha*conj(beta),   |alpha|^2        ]]

  This IS already Hermitian, so a o a = (a^2 + a^2)/2 = a^2.

  P_1(a o a) = (|alpha|^2 + |beta|^2) * E_{11}

  DIRECT COUPLING: k_direct = P_1(a o a) / ||a||^2
                             = (|alpha|^2 + |beta|^2) / (2*(|alpha|^2 + |beta|^2))
                             = 1/2

  This is UNIVERSAL (independent of K).

INDIRECT COUPLING:
  Take c in V_0 with components (0, b, c_diag, x1):
  c_mat = [[0, 0,        0       ],
           [0, b,        conj(x1)],
           [0, x1,       c_diag  ]]

  And a in V_{1/2} with only x2 = alpha (x3 = 0):
  a_mat = [[0, 0,      conj(alpha)],
           [0, 0,      0          ],
           [alpha, 0,  0          ]]

  Step 1: c_mat * a_mat:
  Row i of c_mat times col j of a_mat.

  (c*a)_{00} = 0, (c*a)_{01} = 0, (c*a)_{02} = 0
  (c*a)_{10} = 0, (c*a)_{11} = 0, (c*a)_{12} = conj(x1)*conj(alpha) + ...

  Hmm, let me just let the code handle this.
""")


def peirce_tower_analysis(K):
    """
    Analyze the TWO-LEVEL Peirce tower.

    Level 1: h_3(O) under E_{11}
      V_1 = span(E_{11})
      V_{1/2} = {x2, x3 directions}
      V_0 = h_2(O) = {b, c, x1}

    Level 2: Inside V_0 = h_2(O), take E_{22} as sub-idempotent
      V_0 decomposes under E_{22}:
        V_1^(2) = span(E_{22})  (the 'b' component)
        V_{1/2}^(2) = {x1 direction}  (dim d)
        V_0^(2) = span(E_{33})  (the 'c' component)

    The question: what is the effective coupling of V_0^(2) (= E_{33} direction)
    to the observer E_{11}?

    Path: E_{33} -> Jordan with x1 -> get something in V_{1/2}^(2)
          -> Jordan with x1 -> get to V_1^(2) = E_{22}
          -> Jordan with x2 or x3 -> get to V_{1/2} of level 1
          -> Jordan with x2 or x3 -> get to V_1 = E_{11}

    This is a FOURTH-ORDER process!
    """
    d = K.dim
    print(f"\n{'='*70}")
    print(f"  PEIRCE TOWER ANALYSIS for h_3({K.name})")
    print(f"{'='*70}")

    print(f"\n  Level 1: h_3({K.name}) under E_11")
    print(f"    V_1 = dim 1 (observer)")
    print(f"    V_{{1/2}} = dim {2*d} (x2, x3)")
    print(f"    V_0 = dim {d+2} (h_2({K.name}): b, c, x1)")

    print(f"\n  Level 2: h_2({K.name}) under E_22")
    print(f"    V_1^(2) = dim 1 (E_22)")
    print(f"    V_{{1/2}}^(2) = dim {d} (x1)")
    print(f"    V_0^(2) = dim 1 (E_33)")

    # ---- Direct coupling (1 Jordan product) ----
    # a in V_{1/2}, ||a|| = 1
    # P_1(a o a) = 1/2 (as derived above)
    print(f"\n  COUPLING CONSTANTS:")
    print(f"    Level 1 direct: k_1 = 1/2 (universal)")

    # ---- 2nd-order: V_0 element to V_1 via V_{1/2} ----
    # c in V_0, a in V_{1/2}, both unit
    # path: c o a -> P_{1/2} -> result o a -> P_1

    # Let's compute this systematically
    # Use a = x2 = e_0 (unit), c = various V_0 basis elements

    x2_unit = K.basis(0)
    a = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_unit, K.zero()])
    a_nsq = a.norm_sq()
    a = a.scale(1.0 / np.sqrt(a_nsq))

    print(f"\n  --- 2nd order coupling (V_0 -> V_1 via V_{{1/2}}) ---")
    print(f"  mediator a = unit x2")

    # c = E_{22} (unit norm, since Tr(E22^2)=1)
    c_E22 = H3Matrix(K, [0.0, 1.0, 0.0], [K.zero(), K.zero(), K.zero()])
    w = c_E22.jordan_product(a)
    _, w_half, _ = w.peirce_decompose(0)
    wa = w_half.jordan_product(a)
    v1, _, _ = wa.peirce_decompose(0)
    k2_E22 = v1.diag[0]
    print(f"    c = E_22: k_2 = {k2_E22:.6f}")

    # c = E_{33}
    c_E33 = H3Matrix(K, [0.0, 0.0, 1.0], [K.zero(), K.zero(), K.zero()])
    w = c_E33.jordan_product(a)
    _, w_half, _ = w.peirce_decompose(0)
    wa = w_half.jordan_product(a)
    v1, _, _ = wa.peirce_decompose(0)
    k2_E33 = v1.diag[0]
    print(f"    c = E_33: k_2 = {k2_E33:.6f}")

    # c = x1 = e_0
    c_x1 = H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(0), K.zero(), K.zero()])
    c_x1_nsq = c_x1.norm_sq()
    c_x1 = c_x1.scale(1.0 / np.sqrt(c_x1_nsq))
    w = c_x1.jordan_product(a)
    _, w_half, _ = w.peirce_decompose(0)
    wa = w_half.jordan_product(a)
    v1, _, _ = wa.peirce_decompose(0)
    k2_x1 = v1.diag[0]
    print(f"    c = unit x1: k_2 = {k2_x1:.6f}")

    # ---- 3rd order: cubic determinant coupling ----
    print(f"\n  --- 3rd order (cubic det coupling) ---")
    print(f"    From det = abc + 2*Re(x1*x2*x3) - a|x1|^2 - b|x2|^2 - c|x3|^2")
    print(f"    The trilinear coupling d^3(det)/dx1 dx2 dx3 = 2*Re(e_i * e_j * e_k)")
    print(f"    For aligned (all e_0): coefficient = 2")

    # ---- 4th order: V_0^(2) to V_1 through full tower ----
    print(f"\n  --- 4th order coupling (E_33 -> E_11 through full Peirce tower) ---")
    print(f"  Path: E_33 -> x1 mediator -> E_22 -> x2 mediator -> E_11")
    print(f"  This requires 4 Jordan products.")

    # E_33 in V_0: needs x1 to get to E_22, then x2 to get to E_11
    # But E_33 is already DIRECTLY in V_0 and we computed k2_E33 above.
    # That was the 2nd order coupling with x2 as mediator.
    #
    # The TOWER path is different:
    # Step 1: E_33 lives in V_0^(2) of h_2(O)
    # Step 2: E_33 o x1_mediator -> something in V_{1/2}^(2) (x1 space)
    # Step 3: result o x1_mediator -> something in V_1^(2) = E_22 space
    # Step 4: Now E_22-like thing is in V_0 of h_3. Need x2 to reach E_11.
    # Step 5: result o x2_mediator -> V_{1/2}
    # Step 6: result o x2_mediator -> V_1

    # But actually: E_33 o x1 is computed within h_2(O), giving result in x1 space
    # Then (x1 result) o x1 gives E_22 component
    # Then E_22 o x2 gives V_{1/2} of h_3
    # Then result o x2 gives V_1 of h_3

    # Let's do this step by step within h_3(O):

    # Mediators
    x1_med = H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(0), K.zero(), K.zero()])
    x1_med_nsq = x1_med.norm_sq()
    x1_med = x1_med.scale(1.0 / np.sqrt(x1_med_nsq))

    x2_med = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.basis(0), K.zero()])
    x2_med_nsq = x2_med.norm_sq()
    x2_med = x2_med.scale(1.0 / np.sqrt(x2_med_nsq))

    # Source: E_33
    source = H3Matrix(K, [0.0, 0.0, 1.0], [K.zero(), K.zero(), K.zero()])

    print(f"\n  Step 1: E_33 o x1_med (should give V_{{1/2}} of inner h_2)")
    step1 = source.jordan_product(x1_med)
    step1.describe()
    # Project: x1 component goes to V_{1/2}^(2), diagonal goes to V_1^(2) or V_0^(2)
    # In h_3 terms, the result should be in V_0 (since E_33 and x1 are both in V_0)
    v1_s1, vh_s1, v0_s1 = step1.peirce_decompose(0)
    print(f"  V_1 component: {v1_s1.diag[0]:.6f}")
    print(f"  V_{{1/2}} component norm: {vh_s1.norm_sq():.6f}")
    print(f"  V_0 component norm: {v0_s1.norm_sq():.6f}")

    print(f"\n  Step 2: (step1 projected to V_0) o x1_med -> should include E_22 component")
    step2 = v0_s1.jordan_product(x1_med)
    step2.describe()
    v1_s2, vh_s2, v0_s2 = step2.peirce_decompose(0)
    print(f"  V_1 component: {v1_s2.diag[0]:.6f}")
    print(f"  V_{{1/2}} component norm: {vh_s2.norm_sq():.6f}")
    print(f"  V_0 component norm: {v0_s2.norm_sq():.6f}")
    # The V_0 part should now have an E_22 component
    print(f"  V_0 diag: [{v0_s2.diag[0]:.6f}, {v0_s2.diag[1]:.6f}, {v0_s2.diag[2]:.6f}]")

    print(f"\n  Step 3: V_0 part (with E_22 content) o x2_med -> V_{{1/2}} of h_3")
    step3 = v0_s2.jordan_product(x2_med)
    step3.describe()
    v1_s3, vh_s3, v0_s3 = step3.peirce_decompose(0)
    print(f"  V_1 component: {v1_s3.diag[0]:.6f}")
    print(f"  V_{{1/2}} component norm: {vh_s3.norm_sq():.6f}")

    print(f"\n  Step 4: V_{{1/2}} part o x2_med -> V_1 of h_3 (OBSERVER)")
    step4 = vh_s3.jordan_product(x2_med)
    step4.describe()
    v1_s4, vh_s4, v0_s4 = step4.peirce_decompose(0)
    k4 = v1_s4.diag[0]
    print(f"  V_1 component (4th order coupling): {k4:.6f}")

    print(f"\n  SUMMARY for h_3({K.name}):")
    print(f"    Direct (1st order, V_{{1/2}} self-coupling):  k_1 = 0.5")
    print(f"    2nd order (V_0 via V_{{1/2}} mediator):       k_2(E_22) = {k2_E22:.6f}")
    print(f"    2nd order (V_0 via V_{{1/2}} mediator):       k_2(E_33) = {k2_E33:.6f}")
    print(f"    2nd order (V_0 via V_{{1/2}} mediator):       k_2(x1)   = {k2_x1:.6f}")
    print(f"    4th order (E_33 through full tower):          k_4 = {k4:.6f}")
    print(f"    Ratio k_1 / k_2(E_22) = {0.5 / abs(k2_E22) if abs(k2_E22) > 1e-10 else 'inf'}")
    print(f"    Ratio k_1 / k_2(E_33) = {0.5 / abs(k2_E33) if abs(k2_E33) > 1e-10 else 'inf'}")
    print(f"    Ratio k_1 / |k_4| = {0.5 / abs(k4) if abs(k4) > 1e-10 else 'inf'}")

    return {
        'k1': 0.5,
        'k2_E22': k2_E22,
        'k2_E33': k2_E33,
        'k2_x1': k2_x1,
        'k4': k4
    }


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("PEIRCE COUPLING CONSTANTS FOR EXCEPTIONAL JORDAN ALGEBRAS")
    print("=" * 70)

    # First verify octonion algebra
    print("\n--- Octonion algebra verification ---")
    O = OctonionAlgebra
    e = [O.basis(i) for i in range(8)]

    # Check e_i * e_i = -1 for i >= 1
    for i in range(1, 8):
        prod = O.mul(e[i], e[i])
        assert abs(prod[0] + 1.0) < 1e-10 and all(abs(prod[j]) < 1e-10 for j in range(1,8)), \
            f"e_{i}^2 != -1: {prod}"
    print("  e_i^2 = -1 for i=1..7: OK")

    # Check a few products
    # e_1 * e_2 should give some e_k
    p12 = O.mul(e[1], e[2])
    print(f"  e_1 * e_2 = {p12}")

    # Check norm multiplicativity: |ab|^2 = |a|^2 * |b|^2
    np.random.seed(99)
    a_test = np.random.randn(8)
    b_test = np.random.randn(8)
    ab = O.mul(a_test, b_test)
    lhs = O.norm_sq(ab)
    rhs = O.norm_sq(a_test) * O.norm_sq(b_test)
    print(f"  |a*b|^2 = {lhs:.6f}, |a|^2*|b|^2 = {rhs:.6f}, ratio = {lhs/rhs:.10f}")

    # Check non-associativity
    c_test = np.random.randn(8)
    lhs_assoc = O.mul(O.mul(a_test, b_test), c_test)
    rhs_assoc = O.mul(a_test, O.mul(b_test, c_test))
    diff = np.max(np.abs(lhs_assoc - rhs_assoc))
    print(f"  Non-associativity: max|(ab)c - a(bc)| = {diff:.6f} (should be nonzero)")

    # Check alternativity: (aa)b = a(ab) and (ab)b = a(bb)
    lhs_alt = O.mul(O.mul(a_test, a_test), b_test)
    rhs_alt = O.mul(a_test, O.mul(a_test, b_test))
    diff_alt = np.max(np.abs(lhs_alt - rhs_alt))
    print(f"  Alternativity (aa)b = a(ab): max diff = {diff_alt:.10f} (should be ~0)")

    # Verify Jordan product is commutative for h_3(O)
    print("\n--- Jordan product commutativity check ---")
    np.random.seed(77)
    X = H3Matrix(O, np.random.randn(3).tolist(),
                 [np.random.randn(8), np.random.randn(8), np.random.randn(8)])
    Y = H3Matrix(O, np.random.randn(3).tolist(),
                 [np.random.randn(8), np.random.randn(8), np.random.randn(8)])
    XoY = X.jordan_product(Y)
    YoX = Y.jordan_product(X)

    diff_diag = max(abs(XoY.diag[i] - YoX.diag[i]) for i in range(3))
    diff_off = max(np.max(np.abs(XoY.off[i] - YoX.off[i])) for i in range(3))
    print(f"  max|X o Y - Y o X| (diag) = {diff_diag:.10e}")
    print(f"  max|X o Y - Y o X| (off)  = {diff_off:.10e}")

    # Run for all four division algebras
    algebras = [RealAlgebra, ComplexAlgebra, QuaternionAlgebra, OctonionAlgebra]

    all_results = {}
    for K in algebras:
        d, i = run_coupling_analysis(K)
        all_results[K.name] = (d, i)

    # Detailed tower analysis
    tower_results = {}
    for K in algebras:
        tower_results[K.name] = peirce_tower_analysis(K)

    # Maximum indirect coupling
    for K in algebras:
        compute_max_indirect_coupling(K)

    # Final comparison table
    print(f"\n\n{'='*70}")
    print(f"  FINAL COMPARISON TABLE")
    print(f"{'='*70}")
    print(f"\n  {'Algebra':<10} {'k_1':>8} {'k_2(E22)':>10} {'k_2(E33)':>10} {'k_2(x1)':>10} {'k_4':>10} {'k1/|k4|':>10}")
    print(f"  {'-'*8:<10} {'-'*8:>8} {'-'*10:>10} {'-'*10:>10} {'-'*10:>10} {'-'*10:>10} {'-'*10:>10}")
    for K in algebras:
        r = tower_results[K.name]
        ratio = 0.5 / abs(r['k4']) if abs(r['k4']) > 1e-10 else float('inf')
        print(f"  h_3({K.name:1s})   {r['k1']:8.4f} {r['k2_E22']:10.6f} {r['k2_E33']:10.6f} {r['k2_x1']:10.6f} {r['k4']:10.6f} {ratio:10.4f}")

    # Dimension dependence
    print(f"\n  Note: dim(K) = R:1, C:2, H:4, O:8")
    print(f"  The coupling constants should reveal whether there is a")
    print(f"  d-dependent hierarchy from the Peirce tower structure.")
