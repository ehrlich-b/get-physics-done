# ASSERT_CONVENTION: natural_units=dimensionless, clifford_convention=euclidean_positive,
#   octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7,
#   witt_operators=a_j=(1/2)(gamma_{2j-1}+i*gamma_{2j}),
#   gamma_matrix_representation=32x32_tensor_product_pauli,
#   hypercharge=pati_salam_Y_equals_BminusL_plus_2I3R,
#   su2_construction=schwinger_boson_from_cl4_witt
#
# Phase 19, Plan 02: Explicit Cl(10)/Cl(6) matrix construction and SM quantum
# number verification.
# References: Todorov arXiv:2206.06912, Furey arXiv:1806.00612
#
# Reproducibility: numpy 2.4.2, scipy 1.17.1, Python 3.14.2, macOS Darwin 24.6.0
# No random seeds needed (deterministic linear algebra only).

import numpy as np
import pytest

# Tolerance for machine-precision checks
ATOL = 1e-14
ATOL_TRACE = 1e-10

# ---------------------------------------------------------------------------
# Pauli matrices (standard)
# ---------------------------------------------------------------------------
sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
I32 = np.eye(32, dtype=complex)


def kron_list(matrices):
    """Tensor product of a list of matrices."""
    result = matrices[0]
    for m in matrices[1:]:
        result = np.kron(result, m)
    return result


# ---------------------------------------------------------------------------
# Task 1: Cl(10) and Cl(6) construction
# ---------------------------------------------------------------------------

def build_cl10_generators():
    """
    Build 10 generators of Cl(10) as 32x32 complex matrices using the
    standard recursive tensor-product construction.

    Convention: {Gamma_A, Gamma_B} = 2 delta_{AB} I_32

    Construction for Cl(2n) with n=5:
      Gamma_{2k+1} = sigma_3^{x k} x sigma_1 x I^{x (4-k)}   (k=0..4)
      Gamma_{2k+2} = sigma_3^{x k} x sigma_2 x I^{x (4-k)}   (k=0..4)
    """
    generators = []
    for k in range(5):
        mats_odd = [sigma_3] * k + [sigma_1] + [I2] * (4 - k)
        generators.append(kron_list(mats_odd))
        mats_even = [sigma_3] * k + [sigma_2] + [I2] * (4 - k)
        generators.append(kron_list(mats_even))
    return generators


def build_cl6_generators(cl10_gens):
    """Extract the first 6 Cl(10) generators as Cl(6) generators."""
    return cl10_gens[:6]


def build_omega6(cl6_gens):
    """Compute omega_6 = gamma_1 @ gamma_2 @ ... @ gamma_6."""
    result = np.eye(32, dtype=complex)
    for g in cl6_gens:
        result = result @ g
    return result


def build_projector(omega6):
    """P = (1/2)(I - i*omega_6).

    Selects the omega_6 = +i eigenspace (odd Cl(6) particle number).
    This is a 16-dim subspace of the 32-dim Dirac spinor.
    """
    return 0.5 * (I32 - 1j * omega6)


def witt_creation_annihilation(cl6_gens):
    """
    Cl(6) Witt creation/annihilation operators:
      a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j})  for j = 1, 2, 3
      a_j^dag = (1/2)(gamma_{2j-1} - i*gamma_{2j})
    """
    a_ops = []
    a_dag_ops = []
    for j in range(3):
        g_odd = cl6_gens[2 * j]
        g_even = cl6_gens[2 * j + 1]
        a_ops.append(0.5 * (g_odd + 1j * g_even))
        a_dag_ops.append(0.5 * (g_odd - 1j * g_even))
    return a_ops, a_dag_ops


def cl4_witt_operators(cl10_gens):
    """
    Cl(4) Witt creation/annihilation operators from the external sector
    (Gamma_7, ..., Gamma_10):
      b_1 = (1/2)(Gamma_7 + i*Gamma_8)
      b_2 = (1/2)(Gamma_9 + i*Gamma_10)
    """
    G7, G8, G9, G10 = cl10_gens[6], cl10_gens[7], cl10_gens[8], cl10_gens[9]
    b1 = 0.5 * (G7 + 1j * G8)
    b1_dag = 0.5 * (G7 - 1j * G8)
    b2 = 0.5 * (G9 + 1j * G10)
    b2_dag = 0.5 * (G9 - 1j * G10)
    return b1, b1_dag, b2, b2_dag


def find_clifford_vacuum(a_ops):
    """
    Find the Clifford vacuum: intersection of ker(a_1), ker(a_2), ker(a_3).
    Returns an orthonormal basis for this space as columns of a matrix.
    """
    stacked = np.vstack(a_ops)
    U, S, Vh = np.linalg.svd(stacked)
    null_dim = np.sum(S < 1e-12)
    vacuum_basis = Vh[-null_dim:].conj().T
    return vacuum_basis, null_dim


# ---------------------------------------------------------------------------
# Task 2: SM quantum number operators and state construction
# ---------------------------------------------------------------------------

def build_sm_generators(cl10_gens, a_ops, a_dag_ops):
    """
    Build the Cartan generators for SU(3)_C x SU(2)_L x SU(2)_R x U(1)_{B-L}.

    SU(3) color Cartan (from Cl(6) number operators n_j = a_j^dag a_j):
      T3c = (1/2)(n_1 - n_2)
      T8c = (1/(2*sqrt(3)))(n_1 + n_2 - 2*n_3)

    SU(2)_L x SU(2)_R (Schwinger boson construction from Cl(4) Witt operators):
      b_k = (1/2)(Gamma_{2k+5} + i*Gamma_{2k+6})  for k = 1, 2
      m_k = b_k^dag b_k (number operators)
      J3L = (1/2)(m_1 + m_2 - I)   [SU(2)_L Cartan]
      J3R = (1/2)(m_1 - m_2)       [SU(2)_R Cartan]

    B-L (from total Cl(6) particle number N = n_1 + n_2 + n_3):
      B-L = 1 - (2/3)*N
      (N=1 quarks: B-L = +1/3, N=3 leptons: B-L = -1)

    Hypercharge (Gell-Mann-Nishijima for Pati-Salam):
      Y = (B-L) + 2*J3R

    Electric charge:
      Q = J3L + Y/2
    """
    # Cl(6) number operators
    n_ops = [a_dag_ops[j] @ a_ops[j] for j in range(3)]
    N_total = n_ops[0] + n_ops[1] + n_ops[2]

    # SU(3) color Cartan
    T3c = 0.5 * (n_ops[0] - n_ops[1])
    T8c = (1.0 / (2.0 * np.sqrt(3))) * (n_ops[0] + n_ops[1] - 2 * n_ops[2])

    # Cl(4) Witt operators
    b1, b1_dag, b2, b2_dag = cl4_witt_operators(cl10_gens)
    m1 = b1_dag @ b1
    m2 = b2_dag @ b2

    # SU(2)_L x SU(2)_R Cartan (Schwinger boson)
    J3L = 0.5 * (m1 + m2 - I32)
    J3R = 0.5 * (m1 - m2)

    # B-L
    B_minus_L = I32 - (2.0 / 3.0) * N_total

    # Hypercharge
    Y = B_minus_L + 2 * J3R

    # Electric charge
    Q = J3L + 0.5 * Y

    return {
        "n1": n_ops[0], "n2": n_ops[1], "n3": n_ops[2],
        "N_total": N_total,
        "T3c": T3c, "T8c": T8c,
        "J3L": J3L, "J3R": J3R,
        "m1": m1, "m2": m2,
        "B_minus_L": B_minus_L,
        "Y": Y, "Q": Q,
    }


def build_all_16_states(a_ops, a_dag_ops, cl10_gens):
    """
    Build all 16 SM states from the Clifford vacuum.

    The Cl(6) vacuum |0> (annihilated by a_1, a_2, a_3) is 4-dimensional
    in the 32-dim Dirac space, spanning the 4 states of the Cl(4) sector.

    The omega_6 projector P selects the omega_6 = +i eigenspace, which
    corresponds to ODD Cl(6) particle number (N = 1 or N = 3).

    For each of the 4 vacuum vectors:
      - 3 states a_j^dag |vac> (N=1, color triplet = quarks)
      - 1 state a_1^dag a_2^dag a_3^dag |vac> (N=3, color singlet = lepton)
    Total: 4 x 4 = 16 states, all in the P-projected subspace.
    """
    vac_basis, vac_dim = find_clifford_vacuum(a_ops)
    assert vac_dim == 4, f"Vacuum dimension {vac_dim} != 4"

    cl6_gens = build_cl6_generators(cl10_gens)
    omega6 = build_omega6(cl6_gens)
    P = build_projector(omega6)

    # Diagonalize the Cl(4) quantum numbers within the vacuum subspace
    # so that each vacuum vector is a simultaneous eigenstate of m1 and m2.
    b1, b1_dag, b2, b2_dag = cl4_witt_operators(cl10_gens)
    m1 = b1_dag @ b1
    m2 = b2_dag @ b2

    # Restrict m1, m2 to vacuum subspace and jointly diagonalize
    m1_vac = vac_basis.conj().T @ m1 @ vac_basis
    m2_vac = vac_basis.conj().T @ m2 @ vac_basis

    # Both should be simultaneously diagonalizable (they commute)
    # Diagonalize m1 first, then m2 within each eigenspace
    evals_m1, evecs_m1 = np.linalg.eigh(m1_vac)
    # Transform m2 into the m1 eigenbasis
    m2_in_m1 = evecs_m1.conj().T @ m2_vac @ evecs_m1
    evals_m2, evecs_m2 = np.linalg.eigh(m2_in_m1)
    # Combined eigenvectors
    combined_evecs = evecs_m1 @ evecs_m2
    # New vacuum basis with definite (m1, m2) quantum numbers
    vac_basis_diag = vac_basis @ combined_evecs

    states = []
    labels = []
    for v_idx in range(4):
        vac = vac_basis_diag[:, v_idx:v_idx + 1]
        m1_val = round((vac.conj().T @ m1 @ vac).item().real)
        m2_val = round((vac.conj().T @ m2 @ vac).item().real)

        # N=1 states: a_j^dag |vac>
        for j in range(3):
            state = a_dag_ops[j] @ vac
            ps = P @ state
            norm = np.linalg.norm(ps)
            if norm > 1e-10:
                states.append(ps / norm)
                labels.append({
                    "vac_idx": v_idx, "m1": m1_val, "m2": m2_val,
                    "excitation": f"a{j+1}dag", "N_cl6": 1,
                })

        # N=3 state: a_1^dag a_2^dag a_3^dag |vac>
        state = a_dag_ops[0] @ (a_dag_ops[1] @ (a_dag_ops[2] @ vac))
        ps = P @ state
        norm = np.linalg.norm(ps)
        if norm > 1e-10:
            states.append(ps / norm)
            labels.append({
                "vac_idx": v_idx, "m1": m1_val, "m2": m2_val,
                "excitation": "a1a2a3dag", "N_cl6": 3,
            })

    return states, labels


def compute_quantum_numbers(states, labels, generators):
    """For each state, compute quantum numbers as matrix eigenvalues."""
    cartan_keys = ["n1", "n2", "n3", "N_total", "T3c", "T8c",
                   "J3L", "J3R", "m1", "m2", "B_minus_L", "Y", "Q"]
    results = []
    for state, label in zip(states, labels):
        v = state.flatten()
        qn = dict(label)
        for key in cartan_keys:
            op = generators[key]
            val = (v.conj() @ op @ v).real / (v.conj() @ v).real
            qn[key] = val
            # Eigenstate residual
            residual = np.linalg.norm(op @ v - val * v) / np.linalg.norm(v)
            qn[f"{key}_res"] = residual
        results.append(qn)
    return results


def identify_particle(qn):
    """Identify the SM particle from quantum numbers."""
    Q = round(qn["Q"] * 3) / 3
    J3L = round(qn["J3L"] * 2) / 2
    J3R = round(qn["J3R"] * 2) / 2
    T3c = qn["T3c"]
    T8c = qn["T8c"]
    is_color = abs(T3c) > 0.01 or abs(T8c) > 0.01

    if abs(J3L) > 0.01:  # SU(2)_L doublet (left-handed)
        if is_color:
            return "u_L" if Q > 0 else "d_L"
        else:
            return "nu_L" if abs(Q) < 0.01 else "e_L"
    else:  # SU(2)_L singlet (right-handed)
        if is_color:
            return "u_R" if Q > 0 else "d_R"
        else:
            return "nu_R" if abs(Q) < 0.01 else "e_R"


# ---------------------------------------------------------------------------
# Task 1 Tests
# ---------------------------------------------------------------------------

class TestCl10Construction:
    """Verify Cl(10) anticommutation relations."""

    @pytest.fixture(scope="class")
    def cl10_gens(self):
        return build_cl10_generators()

    def test_cl10_anticommutation_all_55_pairs(self, cl10_gens):
        max_err = 0.0
        count = 0
        for A in range(10):
            for B in range(A, 10):
                anticomm = cl10_gens[A] @ cl10_gens[B] + cl10_gens[B] @ cl10_gens[A]
                expected = 2.0 * (1.0 if A == B else 0.0) * I32
                err = np.max(np.abs(anticomm - expected))
                max_err = max(max_err, err)
                count += 1
        assert count == 55
        assert max_err < ATOL, f"Max error: {max_err}"
        print(f"  Cl(10): 55/55 pairs, max error = {max_err:.2e}")


class TestCl6Construction:
    """Verify Cl(6) anticommutation relations."""

    @pytest.fixture(scope="class")
    def cl6_gens(self):
        return build_cl6_generators(build_cl10_generators())

    def test_cl6_anticommutation_all_21_pairs(self, cl6_gens):
        max_err = 0.0
        count = 0
        for i in range(6):
            for j in range(i, 6):
                anticomm = cl6_gens[i] @ cl6_gens[j] + cl6_gens[j] @ cl6_gens[i]
                expected = 2.0 * (1.0 if i == j else 0.0) * I32
                err = np.max(np.abs(anticomm - expected))
                max_err = max(max_err, err)
                count += 1
        assert count == 21
        assert max_err < ATOL, f"Max error: {max_err}"
        print(f"  Cl(6): 21/21 pairs, max error = {max_err:.2e}")


class TestOmega6Properties:
    """Verify volume form omega_6 properties."""

    @pytest.fixture(scope="class")
    def setup(self):
        cl10 = build_cl10_generators()
        cl6 = build_cl6_generators(cl10)
        omega6 = build_omega6(cl6)
        P = build_projector(omega6)
        return {"cl10": cl10, "cl6": cl6, "omega6": omega6, "P": P}

    def test_omega6_squared(self, setup):
        """omega_6^2 = -I_32."""
        err = np.max(np.abs(setup["omega6"] @ setup["omega6"] + I32))
        assert err < ATOL, f"omega_6^2 + I error: {err}"
        print(f"  omega_6^2 = -I_32, error = {err:.2e}")

    def test_projector_idempotent(self, setup):
        """P^2 = P."""
        P = setup["P"]
        err = np.max(np.abs(P @ P - P))
        assert err < ATOL, f"P^2 - P error: {err}"

    def test_projector_trace(self, setup):
        """trace(P) = 16."""
        tr = np.trace(setup["P"])
        assert abs(tr - 16.0) < ATOL_TRACE, f"|trace(P) - 16| = {abs(tr - 16)}"
        print(f"  trace(P) = {tr.real:.6f}")

    def test_projector_rank(self, setup):
        """rank(P) = 16."""
        P = setup["P"]
        evals = np.linalg.eigvalsh((P + P.conj().T) / 2)
        rank = np.sum(np.abs(evals) > 0.5)
        assert rank == 16, f"rank(P) = {rank}"

    def test_omega6_trace_zero(self, setup):
        """trace(omega_6) = 0."""
        tr = np.trace(setup["omega6"])
        assert abs(tr) < ATOL_TRACE

    def test_omega6_vs_gamma11(self, setup):
        """omega_6 != Gamma_11 but Gamma_11 = omega_6 @ omega_4_ext."""
        cl10 = setup["cl10"]
        omega6 = setup["omega6"]
        gamma11 = np.eye(32, dtype=complex)
        for g in cl10:
            gamma11 = gamma11 @ g
        diff = np.max(np.abs(omega6 - gamma11))
        assert diff > 0.1, "omega_6 and Gamma_11 should differ"
        omega4_ext = np.eye(32, dtype=complex)
        for g in cl10[6:]:
            omega4_ext = omega4_ext @ g
        err = np.max(np.abs(omega6 @ omega4_ext - gamma11))
        assert err < ATOL


class TestWittOperators:
    """Verify CAR for Cl(6) Witt operators."""

    @pytest.fixture(scope="class")
    def witt(self):
        cl6 = build_cl6_generators(build_cl10_generators())
        return witt_creation_annihilation(cl6)

    def test_car_a_adag(self, witt):
        """{a_i, a_j^dag} = delta_ij I_32 (9 relations)."""
        a_ops, a_dag_ops = witt
        max_err = 0.0
        for i in range(3):
            for j in range(3):
                anticomm = a_ops[i] @ a_dag_ops[j] + a_dag_ops[j] @ a_ops[i]
                expected = (1.0 if i == j else 0.0) * I32
                max_err = max(max_err, np.max(np.abs(anticomm - expected)))
        assert max_err < ATOL
        print(f"  {{a_i, a_j^dag}} = delta_ij: max error = {max_err:.2e}")

    def test_car_a_a(self, witt):
        """{a_i, a_j} = 0 (9 relations)."""
        a_ops, _ = witt
        max_err = 0.0
        for i in range(3):
            for j in range(3):
                max_err = max(max_err, np.max(np.abs(
                    a_ops[i] @ a_ops[j] + a_ops[j] @ a_ops[i])))
        assert max_err < ATOL

    def test_car_adag_adag(self, witt):
        """{a_i^dag, a_j^dag} = 0 (9 relations)."""
        _, a_dag_ops = witt
        max_err = 0.0
        for i in range(3):
            for j in range(3):
                max_err = max(max_err, np.max(np.abs(
                    a_dag_ops[i] @ a_dag_ops[j] + a_dag_ops[j] @ a_dag_ops[i])))
        assert max_err < ATOL


class TestCl4WittOperators:
    """Verify CAR for Cl(4) Witt operators and SU(2) algebra."""

    @pytest.fixture(scope="class")
    def setup(self):
        cl10 = build_cl10_generators()
        b1, b1d, b2, b2d = cl4_witt_operators(cl10)
        m1 = b1d @ b1
        m2 = b2d @ b2
        J3L = 0.5 * (m1 + m2 - I32)
        J3R = 0.5 * (m1 - m2)
        JLp = b1d @ b2d
        JLm = b2 @ b1
        JRp = b1d @ b2
        JRm = b2d @ b1
        return {"b1": b1, "b1d": b1d, "b2": b2, "b2d": b2d,
                "m1": m1, "m2": m2,
                "J3L": J3L, "J3R": J3R,
                "JLp": JLp, "JLm": JLm, "JRp": JRp, "JRm": JRm}

    def test_cl4_car(self, setup):
        """Verify CAR for b1, b2."""
        b1, b1d = setup["b1"], setup["b1d"]
        b2, b2d = setup["b2"], setup["b2d"]
        assert np.allclose(b1 @ b1d + b1d @ b1, I32, atol=ATOL)
        assert np.allclose(b2 @ b2d + b2d @ b2, I32, atol=ATOL)
        assert np.allclose(b1 @ b2 + b2 @ b1, 0, atol=ATOL)
        assert np.allclose(b1 @ b2d + b2d @ b1, 0, atol=ATOL)

    def test_su2_L_algebra(self, setup):
        """[J+_L, J-_L] = 2 J3_L etc."""
        J3L = setup["J3L"]
        JLp, JLm = setup["JLp"], setup["JLm"]
        assert np.allclose(JLp @ JLm - JLm @ JLp, 2 * J3L, atol=ATOL)
        assert np.allclose(J3L @ JLp - JLp @ J3L, JLp, atol=ATOL)
        assert np.allclose(J3L @ JLm - JLm @ J3L, -JLm, atol=ATOL)

    def test_su2_R_algebra(self, setup):
        """[J+_R, J-_R] = 2 J3_R etc."""
        J3R = setup["J3R"]
        JRp, JRm = setup["JRp"], setup["JRm"]
        assert np.allclose(JRp @ JRm - JRm @ JRp, 2 * J3R, atol=ATOL)
        assert np.allclose(J3R @ JRp - JRp @ J3R, JRp, atol=ATOL)
        assert np.allclose(J3R @ JRm - JRm @ J3R, -JRm, atol=ATOL)

    def test_su2_L_R_commute(self, setup):
        """SU(2)_L and SU(2)_R generators commute."""
        for Lop in [setup["J3L"], setup["JLp"], setup["JLm"]]:
            for Rop in [setup["J3R"], setup["JRp"], setup["JRm"]]:
                assert np.allclose(Lop @ Rop - Rop @ Lop, 0, atol=ATOL)

    def test_su2_commute_with_omega6(self, setup):
        """Both SU(2)s commute with omega_6."""
        cl10 = build_cl10_generators()
        omega6 = build_omega6(build_cl6_generators(cl10))
        for op in [setup["J3L"], setup["J3R"], setup["JLp"], setup["JRp"]]:
            assert np.allclose(op @ omega6 - omega6 @ op, 0, atol=ATOL)


class TestCliffordVacuum:
    """Find and verify the Clifford vacuum."""

    @pytest.fixture(scope="class")
    def setup(self):
        cl10 = build_cl10_generators()
        cl6 = build_cl6_generators(cl10)
        a_ops, a_dag_ops = witt_creation_annihilation(cl6)
        return {"a_ops": a_ops, "a_dag_ops": a_dag_ops, "cl10": cl10}

    def test_vacuum_dimension(self, setup):
        """Clifford vacuum should be 4-dimensional (32 / 2^3 = 4)."""
        vac_basis, null_dim = find_clifford_vacuum(setup["a_ops"])
        assert null_dim == 4, f"dim = {null_dim}"
        print(f"  Clifford vacuum dimension = {null_dim}")

    def test_vacuum_annihilated(self, setup):
        """a_j |vac> = 0 for all vacuum basis vectors."""
        vac_basis, _ = find_clifford_vacuum(setup["a_ops"])
        max_err = 0.0
        for j in range(3):
            max_err = max(max_err, np.max(np.abs(setup["a_ops"][j] @ vac_basis)))
        assert max_err < ATOL, f"Max |a_j|vac>| = {max_err}"


# ---------------------------------------------------------------------------
# Task 2 Tests: SM quantum numbers
# ---------------------------------------------------------------------------

class TestSMStates:
    """Verify all 16 SM states from Witt decomposition."""

    @pytest.fixture(scope="class")
    def setup(self):
        cl10 = build_cl10_generators()
        cl6 = build_cl6_generators(cl10)
        a_ops, a_dag_ops = witt_creation_annihilation(cl6)
        states, labels = build_all_16_states(a_ops, a_dag_ops, cl10)
        generators = build_sm_generators(cl10, a_ops, a_dag_ops)
        qn_list = compute_quantum_numbers(states, labels, generators)
        return {
            "states": states, "labels": labels,
            "generators": generators, "qn_list": qn_list,
            "cl10": cl10, "cl6": cl6,
        }

    def test_16_linearly_independent(self, setup):
        """16 linearly independent states."""
        states = setup["states"]
        assert len(states) == 16
        mat = np.hstack(states)
        rank = np.linalg.matrix_rank(mat, tol=1e-10)
        assert rank == 16
        print(f"  16 independent states (rank = {rank})")

    def test_states_in_P_subspace(self, setup):
        """All 16 states lie in the omega_6 projector subspace."""
        P = build_projector(build_omega6(setup["cl6"]))
        max_err = 0.0
        for s in setup["states"]:
            v = s.flatten()
            max_err = max(max_err, np.linalg.norm(P @ v - v) / np.linalg.norm(v))
        assert max_err < 1e-10

    def test_eigenstates_of_cartan(self, setup):
        """Each state is an eigenstate of all Cartan generators."""
        max_res = 0.0
        cartan_keys = ["n1", "n2", "n3", "J3L", "J3R", "T3c", "T8c", "Q"]
        for qn in setup["qn_list"]:
            for key in cartan_keys:
                max_res = max(max_res, qn[f"{key}_res"])
        assert max_res < 1e-10, f"Max residual: {max_res}"
        print(f"  Eigenstate residuals < {max_res:.2e}")

    def test_16_distinct_tuples(self, setup):
        """All 16 states have distinct quantum number tuples."""
        tuples = set()
        for qn in setup["qn_list"]:
            t = (
                round(qn["n1"]),
                round(qn["n2"]),
                round(qn["n3"]),
                round(qn["J3L"] * 2) / 2,
                round(qn["J3R"] * 2) / 2,
            )
            tuples.add(t)
        assert len(tuples) == 16

    def test_chirality_8_left_8_right(self, setup):
        """8 SU(2)_L doublets (J3L != 0) and 8 SU(2)_L singlets (J3L = 0)."""
        left = sum(1 for qn in setup["qn_list"] if abs(qn["J3L"]) > 0.01)
        right = sum(1 for qn in setup["qn_list"] if abs(qn["J3L"]) < 0.01)
        assert left == 8, f"Left-handed: {left}"
        assert right == 8, f"Right-handed: {right}"
        print(f"  8 left-handed + 8 right-handed")

    def test_color_4_singlets_12_triplets(self, setup):
        """4 color singlets (leptons) and 12 color triplets (quarks)."""
        singlets = 0
        for qn in setup["qn_list"]:
            if abs(qn["T3c"]) < 0.01 and abs(qn["T8c"]) < 0.01:
                singlets += 1
        assert singlets == 4, f"Singlets: {singlets}"
        assert 16 - singlets == 12
        print(f"  4 leptons + 12 quarks")

    def test_charge_distribution(self, setup):
        """Q = {-1: 2, -1/3: 6, 0: 2, +2/3: 6}."""
        from collections import Counter
        Qs = Counter(round(qn["Q"] * 3) / 3 for qn in setup["qn_list"])
        assert Qs[round(-1.0 * 3) / 3] == 2, f"Q=-1 count: {Qs.get(-1.0, 0)}"
        assert Qs[round(-1/3 * 3) / 3] == 6, f"Q=-1/3 count: {Qs.get(round(-1/3, 4), 0)}"
        assert Qs[round(0.0 * 3) / 3] == 2, f"Q=0 count: {Qs.get(0.0, 0)}"
        assert Qs[round(2/3 * 3) / 3] == 6, f"Q=+2/3 count: {Qs.get(round(2/3, 4), 0)}"
        print(f"  Q distribution: {dict(sorted(Qs.items()))}")

    def test_sm_particle_identification(self, setup):
        """All 16 states match known SM fermion names."""
        from collections import Counter
        names = Counter(identify_particle(qn) for qn in setup["qn_list"])
        expected = {"u_L": 3, "d_L": 3, "nu_L": 1, "e_L": 1,
                    "u_R": 3, "d_R": 3, "nu_R": 1, "e_R": 1}
        assert dict(names) == expected, f"Got: {dict(names)}"
        print(f"  SM identification: {dict(sorted(names.items()))}")

    def test_hypercharge_consistency(self, setup):
        """Y = (B-L) + 2*J3R for all states."""
        for qn in setup["qn_list"]:
            expected = qn["B_minus_L"] + 2 * qn["J3R"]
            assert abs(qn["Y"] - expected) < 1e-10

    def test_charge_formula(self, setup):
        """Q = J3L + Y/2 for all states."""
        for qn in setup["qn_list"]:
            expected = qn["J3L"] + qn["Y"] / 2
            assert abs(qn["Q"] - expected) < 1e-10

    def test_print_quantum_number_table(self, setup):
        """Print the complete quantum number table."""
        print("\n  " + "=" * 90)
        print("  SM Quantum Number Table (16 states, one generation, Pati-Salam convention)")
        print("  " + "=" * 90)
        print(f"  {'#':>2} {'Particle':>8} {'N':>2} {'J3L':>5} {'J3R':>5} "
              f"{'B-L':>5} {'Y':>6} {'Q':>6} {'T3c':>5} {'T8c':>7}")
        print("  " + "-" * 70)
        for i, qn in enumerate(setup["qn_list"]):
            name = identify_particle(qn)
            print(f"  {i+1:>2} {name:>8} "
                  f"{round(qn['N_total']):>2} "
                  f"{qn['J3L']:>5.1f} {qn['J3R']:>5.1f} "
                  f"{qn['B_minus_L']:>5.2f} "
                  f"{qn['Y']:>6.2f} {qn['Q']:>6.2f} "
                  f"{qn['T3c']:>5.2f} {qn['T8c']:>7.4f}")
        print("  " + "=" * 90)


# ---------------------------------------------------------------------------
# Entry point for standalone execution
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Cl(10)/Cl(6) Explicit Matrix Construction and SM Verification")
    print("=" * 70)

    cl10 = build_cl10_generators()
    cl6 = build_cl6_generators(cl10)
    omega6 = build_omega6(cl6)
    P = build_projector(omega6)
    a_ops, a_dag_ops = witt_creation_annihilation(cl6)
    gens = build_sm_generators(cl10, a_ops, a_dag_ops)
    states, labels = build_all_16_states(a_ops, a_dag_ops, cl10)
    qn_list = compute_quantum_numbers(states, labels, gens)

    print(f"\nStates: {len(states)}, rank: {np.linalg.matrix_rank(np.hstack(states), tol=1e-10)}")
    print(f"\n{'#':>2} {'Particle':>8} {'N':>2} {'J3L':>5} {'J3R':>5} "
          f"{'B-L':>5} {'Y':>6} {'Q':>6} {'T3c':>5} {'T8c':>7}")
    print("-" * 60)
    for i, qn in enumerate(qn_list):
        name = identify_particle(qn)
        print(f"{i+1:>2} {name:>8} "
              f"{round(qn['N_total']):>2} "
              f"{qn['J3L']:>5.1f} {qn['J3R']:>5.1f} "
              f"{qn['B_minus_L']:>5.2f} "
              f"{qn['Y']:>6.2f} {qn['Q']:>6.2f} "
              f"{qn['T3c']:>5.2f} {qn['T8c']:>7.4f}")
