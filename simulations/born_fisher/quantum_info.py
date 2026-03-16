"""
Quantum information utilities for the Born-Fisher-Experiential conjecture test.

Core functions: von Neumann entropy, partial trace, quantum mutual information,
experiential density, diagonal BM state constructor, bisection root-finder,
density matrix validator.

All entropies in nats (natural logarithm). All density matrices are numpy arrays.

ASSERT_CONVENTION: entropy_base=nats, von_neumann_entropy=S_vN(rho)=-Tr(rho ln rho), mutual_information=I(B;M)=S(B)+S(M)-S(BM), experiential_density=rho_Q=I*(1-I/S_B)
"""

import numpy as np


def von_neumann_entropy(rho, eps=1e-15):
    """Compute S_vN = -Tr(rho ln rho) via eigendecomposition.

    Parameters
    ----------
    rho : ndarray, shape (d, d)
        Density matrix (Hermitian, PSD, trace 1).
    eps : float
        Eigenvalue cutoff. Values below eps treated as 0.

    Returns
    -------
    float
        Von Neumann entropy in nats.
    """
    eigenvalues = np.linalg.eigh(rho)[0]
    # Filter: eigenvalues < eps -> 0. Convention: 0*ln(0) = 0.
    eigenvalues = eigenvalues[eigenvalues > eps]
    if len(eigenvalues) == 0:
        return 0.0
    return -np.sum(eigenvalues * np.log(eigenvalues))


def partial_trace(rho_bm, d_b, d_m, trace_over='M'):
    """Partial trace of bipartite density matrix.

    Parameters
    ----------
    rho_bm : ndarray, shape (d_b*d_m, d_b*d_m)
        Joint density matrix on B tensor M.
    d_b : int
        Dimension of subsystem B.
    d_m : int
        Dimension of subsystem M.
    trace_over : str, 'M' or 'B'
        Which subsystem to trace out.

    Returns
    -------
    ndarray
        Reduced density matrix.
    """
    # Reshape to (d_b, d_m, d_b, d_m)
    rho_reshaped = rho_bm.reshape(d_b, d_m, d_b, d_m)
    if trace_over == 'M':
        # Trace over M indices (axes 1 and 3)
        return np.trace(rho_reshaped, axis1=1, axis2=3)
    elif trace_over == 'B':
        # Trace over B indices (axes 0 and 2)
        return np.trace(rho_reshaped, axis1=0, axis2=2)
    else:
        raise ValueError(f"trace_over must be 'M' or 'B', got '{trace_over}'")


def quantum_mutual_information(rho_bm, d_b, d_m):
    """Compute I_vN(B;M) = S_vN(B) + S_vN(M) - S_vN(BM).

    Parameters
    ----------
    rho_bm : ndarray, shape (d_b*d_m, d_b*d_m)
        Joint density matrix.
    d_b : int
        Dimension of subsystem B.
    d_m : int
        Dimension of subsystem M.

    Returns
    -------
    float
        Quantum mutual information in nats.
    """
    rho_b = partial_trace(rho_bm, d_b, d_m, trace_over='M')
    rho_m = partial_trace(rho_bm, d_b, d_m, trace_over='B')
    s_b = von_neumann_entropy(rho_b)
    s_m = von_neumann_entropy(rho_m)
    s_bm = von_neumann_entropy(rho_bm)
    return s_b + s_m - s_bm


def experiential_density(rho_bm, d_b, d_m):
    """Compute rho_Q = I * (1 - I/S_B).

    Parameters
    ----------
    rho_bm : ndarray, shape (d_b*d_m, d_b*d_m)
        Joint density matrix.
    d_b : int
        Dimension of subsystem B.
    d_m : int
        Dimension of subsystem M.

    Returns
    -------
    tuple (rho_Q, I_vn, S_B, ratio)
        rho_Q : float, experiential density in nats
        I_vn : float, quantum mutual information
        S_B : float, von Neumann entropy of B
        ratio : float, I_vn / S_B (or 0.0 if S_B = 0)
    """
    rho_b = partial_trace(rho_bm, d_b, d_m, trace_over='M')
    rho_m = partial_trace(rho_bm, d_b, d_m, trace_over='B')
    s_b = von_neumann_entropy(rho_b)
    s_m = von_neumann_entropy(rho_m)
    s_bm = von_neumann_entropy(rho_bm)
    i_vn = s_b + s_m - s_bm

    if s_b < 1e-15:
        return (0.0, i_vn, s_b, 0.0)

    ratio = i_vn / s_b
    rho_q = i_vn * (1.0 - ratio)
    return (rho_q, i_vn, s_b, ratio)


def diagonal_bm_state(p, alpha, d=2):
    """Construct diagonal (p, alpha)-parametrized BM state.

    For d=2 (qubit):
        rho_BM = p * |0><0| (x) rho_M^(0) + (1-p) * |1><1| (x) rho_M^(1)
        where rho_M^(0) = diag(alpha, 1-alpha)
              rho_M^(1) = diag(1-alpha, alpha)

    For d=3 (qutrit):
        rho_BM = sum_k p_k * |k><k| (x) rho_M^(k)
        where p_k = p for k=0, (1-p)/(d-1) for k>0  (generalized)
        and rho_M^(k) has alpha on diagonal k, (1-alpha)/(d-1) elsewhere.
        Actually for the d=3 case with a single p parameter, we use:
        p_0 = p, p_1 = p_2 = (1-p)/2 for simplicity.

    Parameters
    ----------
    p : float
        Probability of body state |0>. For d=2: body probs are (p, 1-p).
        For d=3: body probs are (p, (1-p)/2, (1-p)/2).
    alpha : float
        Tracking accuracy. alpha=1 means perfect tracking; alpha=1/d means no tracking.
    d : int
        Hilbert space dimension of each subsystem (default 2).

    Returns
    -------
    ndarray, shape (d*d, d*d)
        Joint density matrix, diagonal in the pointer basis.
    """
    dim = d * d
    rho_bm = np.zeros((dim, dim))

    if d == 2:
        body_probs = np.array([p, 1.0 - p])
    elif d == 3:
        body_probs = np.array([p, (1.0 - p) / 2.0, (1.0 - p) / 2.0])
    else:
        # General d: p for state 0, (1-p)/(d-1) for rest
        body_probs = np.full(d, (1.0 - p) / (d - 1))
        body_probs[0] = p

    for k in range(d):
        # Construct rho_M^(k): alpha on diagonal k, (1-alpha)/(d-1) elsewhere
        rho_m_k = np.full(d, (1.0 - alpha) / (d - 1))
        rho_m_k[k] = alpha
        # |k><k| (x) rho_M^(k) contributes to the diagonal
        for j in range(d):
            idx = k * d + j  # index in joint space
            rho_bm[idx, idx] = body_probs[k] * rho_m_k[j]

    return rho_bm


def bisect_root(f, a, b, tol=1e-12, max_iter=100):
    """Simple bisection root-finder. Replaces scipy.optimize.brentq.

    Parameters
    ----------
    f : callable
        Function of one variable. f(a) and f(b) must have opposite signs.
    a, b : float
        Bracket endpoints.
    tol : float
        Tolerance for root.
    max_iter : int
        Maximum iterations.

    Returns
    -------
    float
        Root of f in [a, b] to within tol.

    Raises
    ------
    ValueError
        If f(a) and f(b) do not have opposite signs.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError(
            f"f(a)={fa:.6e} and f(b)={fb:.6e} have the same sign. "
            f"No root guaranteed in [{a}, {b}]."
        )
    if abs(fa) < tol:
        return a
    if abs(fb) < tol:
        return b

    for _ in range(max_iter):
        mid = (a + b) / 2.0
        fm = f(mid)
        if abs(fm) < tol or (b - a) / 2.0 < tol:
            return mid
        if fa * fm < 0:
            b = mid
            fb = fm
        else:
            a = mid
            fa = fm
    return (a + b) / 2.0


def validate_density_matrix(rho, label="", tol=1e-12):
    """Validate density matrix: Tr=1, Hermitian, PSD.

    Parameters
    ----------
    rho : ndarray
        Density matrix to validate.
    label : str
        Label for diagnostic messages.
    tol : float
        Tolerance for checks.

    Returns
    -------
    bool
        True if all checks pass.
    """
    passed = True
    prefix = f"[{label}] " if label else ""

    # Trace check
    tr = np.trace(rho)
    if abs(tr - 1.0) > tol:
        print(f"  {prefix}FAIL: Tr(rho) = {tr:.15e} (expected 1.0, delta={abs(tr-1.0):.2e})")
        passed = False

    # Hermiticity check
    herm_err = np.max(np.abs(rho - rho.conj().T))
    if herm_err > tol:
        print(f"  {prefix}FAIL: Hermiticity error = {herm_err:.2e}")
        passed = False

    # PSD check (eigenvalues >= -tol)
    eigenvalues = np.linalg.eigh(rho)[0]
    min_eig = np.min(eigenvalues)
    if min_eig < -tol:
        print(f"  {prefix}FAIL: Minimum eigenvalue = {min_eig:.2e} (negative)")
        passed = False

    return passed


# ===================================================================
# Validation suite
# ===================================================================

if __name__ == '__main__':
    print("=" * 65)
    print("Quantum Information Utilities -- Validation Suite")
    print("=" * 65)
    print()

    all_pass = True
    ln2 = np.log(2)
    ln3 = np.log(3)

    # (a) Tr and PSD: diagonal_bm_state(0.5, 0.75, d=2)
    print("(a) Trace and PSD check for diagonal_bm_state(0.5, 0.75, d=2):")
    rho_a = diagonal_bm_state(0.5, 0.75, d=2)
    ok_a = validate_density_matrix(rho_a, label="test_a")
    print(f"     Tr={np.trace(rho_a):.15e}, min_eig={np.min(np.linalg.eigh(rho_a)[0]):.2e}")
    print(f"     -> {'PASS' if ok_a else 'FAIL'}")
    all_pass = all_pass and ok_a
    print()

    # (b) Pure Bell state: I_vN = 2*ln(2)
    print("(b) Pure Bell state |Phi+> = (|00>+|11>)/sqrt(2):")
    psi_bell = np.array([1, 0, 0, 1]) / np.sqrt(2)
    rho_bell = np.outer(psi_bell, psi_bell)
    i_bell = quantum_mutual_information(rho_bell, 2, 2)
    expected_b = 2 * ln2
    err_b = abs(i_bell - expected_b)
    ok_b = err_b < 1e-12
    print(f"     I_vN = {i_bell:.15e}")
    print(f"     Expected = {expected_b:.15e}")
    print(f"     Error = {err_b:.2e}")
    print(f"     -> {'PASS' if ok_b else 'FAIL'}")
    all_pass = all_pass and ok_b
    print()

    # (c) Product state: I_vN = 0
    print("(c) Product state rho_B (x) rho_M:")
    rho_b_test = np.diag([0.7, 0.3])
    rho_m_test = np.diag([0.4, 0.6])
    rho_prod = np.kron(rho_b_test, rho_m_test)
    i_prod = quantum_mutual_information(rho_prod, 2, 2)
    ok_c = abs(i_prod) < 1e-12
    print(f"     I_vN = {i_prod:.15e}")
    print(f"     -> {'PASS' if ok_c else 'FAIL'}")
    all_pass = all_pass and ok_c
    print()

    # (d) S_vN(I/2) = ln(2)
    print("(d) S_vN(I/2) = ln(2):")
    rho_max2 = np.eye(2) / 2.0
    s_max2 = von_neumann_entropy(rho_max2)
    err_d = abs(s_max2 - ln2)
    ok_d = err_d < 1e-12
    print(f"     S_vN = {s_max2:.15e}")
    print(f"     Expected = {ln2:.15e}")
    print(f"     Error = {err_d:.2e}")
    print(f"     -> {'PASS' if ok_d else 'FAIL'}")
    all_pass = all_pass and ok_d
    print()

    # (e) S_vN(I/3) = ln(3)
    print("(e) S_vN(I/3) = ln(3):")
    rho_max3 = np.eye(3) / 3.0
    s_max3 = von_neumann_entropy(rho_max3)
    err_e = abs(s_max3 - ln3)
    ok_e = err_e < 1e-12
    print(f"     S_vN = {s_max3:.15e}")
    print(f"     Expected = {ln3:.15e}")
    print(f"     Error = {err_e:.2e}")
    print(f"     -> {'PASS' if ok_e else 'FAIL'}")
    all_pass = all_pass and ok_e
    print()

    # (f) Araki-Lieb bound for 10 random diagonal states
    print("(f) Araki-Lieb bound for 10 random diagonal states:")
    rng = np.random.RandomState(42)
    ok_f = True
    for trial in range(10):
        p_rand = rng.uniform(0.05, 0.95)
        alpha_rand = rng.uniform(0.55, 0.95)
        rho_rand = diagonal_bm_state(p_rand, alpha_rand, d=2)
        rho_b_r = partial_trace(rho_rand, 2, 2, trace_over='M')
        rho_m_r = partial_trace(rho_rand, 2, 2, trace_over='B')
        s_b_r = von_neumann_entropy(rho_b_r)
        s_m_r = von_neumann_entropy(rho_m_r)
        i_r = quantum_mutual_information(rho_rand, 2, 2)
        upper = 2 * min(s_b_r, s_m_r)
        if i_r < -1e-12 or i_r > upper + 1e-12:
            print(f"     Trial {trial}: FAIL. I={i_r:.6e}, bound=[0, {upper:.6e}]")
            ok_f = False
    if ok_f:
        print(f"     All 10 trials: 0 <= I_vN <= 2*min(S_B, S_M)")
    print(f"     -> {'PASS' if ok_f else 'FAIL'}")
    all_pass = all_pass and ok_f
    print()

    # (g) Symmetry: I_vN(p, alpha) = I_vN(1-p, alpha)
    print("(g) Symmetry I(p, alpha) = I(1-p, alpha):")
    ok_g = True
    test_ps = [0.1, 0.2, 0.3, 0.4, 0.5]
    test_alphas = [0.6, 0.75, 0.9]
    max_sym_err = 0.0
    for p_t in test_ps:
        for alpha_t in test_alphas:
            rho1 = diagonal_bm_state(p_t, alpha_t, d=2)
            rho2 = diagonal_bm_state(1.0 - p_t, alpha_t, d=2)
            i1 = quantum_mutual_information(rho1, 2, 2)
            i2 = quantum_mutual_information(rho2, 2, 2)
            sym_err = abs(i1 - i2)
            max_sym_err = max(max_sym_err, sym_err)
            if sym_err > 1e-12:
                ok_g = False
    print(f"     Max symmetry error across {len(test_ps)*len(test_alphas)} pairs: {max_sym_err:.2e}")
    print(f"     -> {'PASS' if ok_g else 'FAIL'}")
    all_pass = all_pass and ok_g
    print()

    # (h) Eigenvalue cutoff stability
    print("(h) Eigenvalue cutoff stability for near-pure state:")
    # Near-pure state: mostly |0>, tiny admixture of |1>
    lam = 1e-10
    rho_near_pure = np.diag([1.0 - lam, lam])
    s_15 = von_neumann_entropy(rho_near_pure, eps=1e-15)
    s_14 = von_neumann_entropy(rho_near_pure, eps=1e-14)
    s_13 = von_neumann_entropy(rho_near_pure, eps=1e-13)
    err_h = max(abs(s_15 - s_14), abs(s_14 - s_13), abs(s_15 - s_13))
    ok_h = err_h < 1e-13
    print(f"     S(eps=1e-15) = {s_15:.15e}")
    print(f"     S(eps=1e-14) = {s_14:.15e}")
    print(f"     S(eps=1e-13) = {s_13:.15e}")
    print(f"     Max difference = {err_h:.2e}")
    print(f"     -> {'PASS' if ok_h else 'FAIL'}")
    all_pass = all_pass and ok_h
    print()

    # (i) Perfect tracking: alpha=1 gives I_vN/S_vN = 1.0
    print("(i) Perfect tracking (alpha=1): I/S = 1.0:")
    ok_i = True
    for p_t in [0.2, 0.5, 0.8]:
        rho_perf = diagonal_bm_state(p_t, 1.0, d=2)
        _, i_val, s_val, ratio_val = experiential_density(rho_perf, 2, 2)
        if abs(ratio_val - 1.0) > 1e-12:
            print(f"     p={p_t}: FAIL. ratio = {ratio_val:.15e}")
            ok_i = False
        else:
            print(f"     p={p_t}: ratio = {ratio_val:.15e}")
    print(f"     -> {'PASS' if ok_i else 'FAIL'}")
    all_pass = all_pass and ok_i
    print()

    # (j) No tracking: alpha=0.5 (d=2) gives I_vN = 0
    print("(j) No tracking (alpha=0.5, d=2): I_vN = 0:")
    ok_j = True
    for p_t in [0.2, 0.5, 0.8]:
        rho_no = diagonal_bm_state(p_t, 0.5, d=2)
        i_no = quantum_mutual_information(rho_no, 2, 2)
        if abs(i_no) > 1e-12:
            print(f"     p={p_t}: FAIL. I_vN = {i_no:.15e}")
            ok_j = False
        else:
            print(f"     p={p_t}: I_vN = {i_no:.15e}")
    print(f"     -> {'PASS' if ok_j else 'FAIL'}")
    all_pass = all_pass and ok_j
    print()

    # === Additional verification: d=3 tests ===
    print("--- Additional: d=3 checks ---")
    print()

    # d=3 maximally mixed
    print("(+1) S_vN(I/3) from d=3 diagonal_bm_state at no-tracking alpha=1/3:")
    rho_d3_no = diagonal_bm_state(1.0 / 3.0, 1.0 / 3.0, d=3)
    ok_d3_dm = validate_density_matrix(rho_d3_no, label="d3_notrack")
    rho_b_d3 = partial_trace(rho_d3_no, 3, 3, trace_over='M')
    s_b_d3 = von_neumann_entropy(rho_b_d3)
    i_d3_no = quantum_mutual_information(rho_d3_no, 3, 3)
    print(f"     Tr check: {'PASS' if ok_d3_dm else 'FAIL'}")
    print(f"     S_B = {s_b_d3:.15e}, expected ln(3) = {ln3:.15e}, err = {abs(s_b_d3 - ln3):.2e}")
    print(f"     I_vN = {i_d3_no:.15e} (expected ~0 for no-tracking)")
    print()

    # d=3 perfect tracking
    print("(+2) d=3 perfect tracking alpha=1:")
    rho_d3_perf = diagonal_bm_state(0.5, 1.0, d=3)
    ok_d3_perf_dm = validate_density_matrix(rho_d3_perf, label="d3_perfect")
    _, i_d3_p, s_d3_p, ratio_d3_p = experiential_density(rho_d3_perf, 3, 3)
    print(f"     ratio = {ratio_d3_p:.15e} (expected 1.0, err = {abs(ratio_d3_p - 1.0):.2e})")
    print()

    # === Additional verification: bisect_root ===
    print("--- Additional: bisect_root test ---")
    root = bisect_root(lambda x: x - 0.5, 0.0, 1.0)
    err_root = abs(root - 0.5)
    ok_root = err_root < 1e-12
    print(f"     Root of f(x) = x - 0.5: {root:.15e}, error = {err_root:.2e}")
    print(f"     -> {'PASS' if ok_root else 'FAIL'}")
    print()

    # === Additional verification: non-PSD detection ===
    print("--- Additional: non-PSD detection ---")
    rho_bad = np.array([[1.5, 0], [0, -0.5]])
    ok_bad = validate_density_matrix(rho_bad, label="non-PSD")
    print(f"     Correctly detected invalid: {'PASS' if not ok_bad else 'FAIL'}")
    print()

    # === Summary ===
    print("=" * 65)
    if all_pass:
        print("ALL 10 SANITY CHECKS PASSED")
    else:
        print("SOME CHECKS FAILED -- see above")
    print("=" * 65)
