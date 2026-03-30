# ASSERT_CONVENTION: natural_units=natural, metric_signature=riemannian,
#   jordan_product=(1/2)(ab+ba),
#   clifford_normalization={T_a,T_b}=(1/2)delta_{ab}I,
#   coupling_convention=J_gt_0_antiferro,
#   v_half_basis=(x2_0..x2_7,x3_0..x3_7)
#
# Phase 38, Plan 01: 2-site effective Hamiltonian H_eff from Peirce
# multiplication operators. Constructs H_2 = J * sum_{a=1}^{9} T_a (x) T_a
# on V_{1/2} (x) V_{1/2} = R^256, diagonalizes, verifies Spin(9) symmetry,
# determines ferro/antiferro character.
#
# DEVIATION [Rule 4]: Raw T_b matrices from compute_T_b_matrices() have
# non-uniform normalization: T_b[1] (traceless diagonal) satisfies
# {T_b[1],T_b[1]} = (1/8)*I while T_b[2..9] satisfy {T_a,T_a} = (1/2)*I.
# To get a Spin(9)-invariant Hamiltonian we rescale via
# rescale_to_clifford_generators() -> gamma_a with {gamma_a,gamma_b} = 2*delta*I
# then define T_a = (1/2)*gamma_a giving uniform {T_a,T_b} = (1/2)*delta*I.
#
# Reproducibility: numpy 2.4.2, Python 3.14.2, macOS Darwin 24.6.0
# No random seeds needed (fully deterministic computation).

import numpy as np
from octonion_algebra import compute_T_b_matrices, rescale_to_clifford_generators


def get_traceless_generators():
    """Return 9 uniformly-normalized traceless generators satisfying
    {T_a, T_b} = (1/2)*delta_{ab}*I_16 for all a,b in {0,...,8}.

    These are T_a = (1/2)*gamma_a where gamma_a are the Cl(9,0) generators
    from rescale_to_clifford_generators() with {gamma_a,gamma_b} = 2*delta*I.

    Returns:
        List of 9 numpy arrays, each 16x16 real symmetric.
    """
    all_Tb = compute_T_b_matrices()
    # Verify T_b[0] = (1/4)*I_16 (trace element)
    T_b1 = all_Tb[0]
    expected = 0.25 * np.eye(16)
    err = np.linalg.norm(T_b1 - expected, 'fro')
    if err > 1e-14:
        raise ValueError(
            f"T_b1 is not (1/4)*I_16: Frobenius error = {err:.2e}"
        )
    # Get uniformly normalized Clifford generators
    gammas = rescale_to_clifford_generators(all_Tb)
    # T_a = (1/2)*gamma_a gives {T_a, T_b} = (1/2)*delta_{ab}*I
    return [0.5 * g for g in gammas]


def verify_single_site_casimir(T_matrices):
    """Verify C_1 = sum_{a=0}^{8} T_a^2 = (9/4)*I_16.

    From {T_a, T_a} = (1/2)*I, each T_a^2 = (1/4)*I, so C_1 = 9*(1/4)*I.

    Returns:
        Frobenius norm of (C_1 - (9/4)*I_16).
    """
    C1 = sum(T @ T for T in T_matrices)
    expected = (9.0 / 4.0) * np.eye(16)
    return np.linalg.norm(C1 - expected, 'fro')


def construct_2site_hamiltonian(T_matrices, J=1.0):
    """Construct H_2 = J * sum_{a=0}^{8} kron(T_a, T_a) on R^256.

    Parameters:
        T_matrices: list of 9 traceless 16x16 real symmetric matrices
                    with {T_a, T_b} = (1/2)*delta_{ab}*I.
        J: coupling constant (J > 0 = antiferromagnetic).

    Returns:
        256x256 numpy array (real symmetric).
    """
    dim = 256
    H = np.zeros((dim, dim), dtype=np.float64)
    for T_a in T_matrices:
        H += np.kron(T_a, T_a)
    H *= J
    return H


def compute_spin9_generators(T_matrices):
    """Compute the 36 Spin(9) generators G_{ab} = [T_a, T_b] for a < b.

    Parameters:
        T_matrices: list of 9 traceless 16x16 matrices.

    Returns:
        List of 36 tuples ((a, b), G_ab) where G_ab is 16x16.
    """
    generators = []
    n = len(T_matrices)
    for a in range(n):
        for b in range(a + 1, n):
            G = T_matrices[a] @ T_matrices[b] - T_matrices[b] @ T_matrices[a]
            generators.append(((a, b), G))
    return generators


def verify_spin9_commutation(H, T_matrices):
    """Verify [H_2, G_{ab}^{total}] = 0 for all 36 Spin(9) generators.

    G_{ab}^{total} = kron(G_{ab}, I_16) + kron(I_16, G_{ab}).

    Returns:
        max Frobenius norm across all 36 commutators, and list of all norms.
    """
    generators = compute_spin9_generators(T_matrices)
    I16 = np.eye(16)
    norms = []
    for (a, b), G_ab in generators:
        G_total = np.kron(G_ab, I16) + np.kron(I16, G_ab)
        comm = H @ G_total - G_total @ H
        norms.append(np.linalg.norm(comm, 'fro'))
    return max(norms), norms


def diagonalize_2site(H):
    """Diagonalize H_2 using eigh (real symmetric).

    Returns:
        eigenvalues (sorted, length 256), eigenvectors (256x256, columns).
    """
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    return eigenvalues, eigenvectors


def analyze_spectrum(eigenvalues, tol=1e-10):
    """Group eigenvalues by value and count multiplicities.

    Returns:
        List of (eigenvalue, multiplicity) tuples, sorted by eigenvalue.
    """
    levels = []
    i = 0
    n = len(eigenvalues)
    while i < n:
        val = eigenvalues[i]
        count = 1
        while i + count < n and abs(eigenvalues[i + count] - val) < tol:
            count += 1
        levels.append((val, count))
        i += count
    return levels


def construct_swap_operator(dim_site=16):
    """Construct the SWAP operator P on R^{dim^2} that permutes two sites.

    P|v1 (x) v2> = |v2 (x) v1>.

    Returns:
        (dim_site^2 x dim_site^2) numpy array.
    """
    dim = dim_site * dim_site
    P = np.zeros((dim, dim), dtype=np.float64)
    for i in range(dim_site):
        for j in range(dim_site):
            row = j * dim_site + i
            col = i * dim_site + j
            P[row, col] = 1.0
    return P


def determine_magnetic_character(eigenvectors, ground_indices, dim_site=16):
    """Determine if ground state is in symmetric or antisymmetric sector.

    The SWAP operator P has eigenvalue +1 (symmetric, dim 136) and
    -1 (antisymmetric, dim 120).

    Parameters:
        eigenvectors: 256x256 array, columns are eigenvectors.
        ground_indices: indices of ground state eigenvectors.

    Returns:
        dict with 'sector', 'swap_expectation_values', 'verdict'.
    """
    P = construct_swap_operator(dim_site)
    swap_vals = []
    for idx in ground_indices:
        v = eigenvectors[:, idx]
        swap_val = v @ P @ v
        swap_vals.append(swap_val)

    avg_swap = np.mean(swap_vals)
    if abs(avg_swap - 1.0) < 1e-8:
        sector = 'symmetric'
        verdict = 'ferromagnetic'
    elif abs(avg_swap + 1.0) < 1e-8:
        sector = 'antisymmetric'
        verdict = 'antiferromagnetic'
    else:
        sector = 'mixed'
        verdict = 'undetermined'

    return {
        'sector': sector,
        'verdict': verdict,
        'swap_expectation_values': swap_vals,
    }


def print_spectrum_summary(eigenvalues, eigenvectors, T_matrices, J=1.0):
    """Print full spectrum summary with Spin(9) analysis.

    Returns the summary dict for programmatic use.
    """
    levels = analyze_spectrum(eigenvalues)
    total_states = sum(m for _, m in levels)

    ground_energy = levels[0][0]
    ground_mult = levels[0][1]
    ground_indices = list(range(ground_mult))

    if len(levels) > 1:
        gap = levels[1][0] - levels[0][0]
    else:
        gap = 0.0

    mag = determine_magnetic_character(eigenvectors, ground_indices)

    P = construct_swap_operator(16)
    level_info = []
    idx = 0
    for energy, mult in levels:
        sym_count = 0
        antisym_count = 0
        for k in range(mult):
            v = eigenvectors[:, idx + k]
            sv = v @ P @ v
            if abs(sv - 1.0) < 1e-8:
                sym_count += 1
            elif abs(sv + 1.0) < 1e-8:
                antisym_count += 1
        if sym_count == mult:
            sector = 'sym'
        elif antisym_count == mult:
            sector = 'antisym'
        else:
            sector = f'mixed({sym_count}s+{antisym_count}a)'
        level_info.append({
            'energy': energy,
            'multiplicity': mult,
            'sector': sector,
        })
        idx += mult

    print("=" * 60)
    print("2-SITE SPECTRUM SUMMARY")
    print("=" * 60)
    print(f"Total states: {total_states}")
    print(f"Distinct energy levels: {len(levels)}")
    print(f"Coupling J = {J}")
    print()
    print(f"{'Level':>5} {'Energy/J':>12} {'Mult':>6} {'Sector':>12}")
    print("-" * 40)
    for i, info in enumerate(level_info):
        print(f"{i:>5} {info['energy']/J:>12.6f} {info['multiplicity']:>6} {info['sector']:>12}")
    print()
    print(f"Ground state energy: {ground_energy/J:.6f} J")
    print(f"Ground state multiplicity: {ground_mult}")
    print(f"Ground state sector: {mag['sector']}")
    print(f"Energy gap: {gap/J:.6f} J")
    print(f"Magnetic character: {mag['verdict']}")
    print("=" * 60)

    return {
        'levels': level_info,
        'ground_energy': ground_energy,
        'ground_multiplicity': ground_mult,
        'gap': gap,
        'magnetic_character': mag,
        'total_states': total_states,
    }


def run_all_checks():
    """Run the full computation and all verification checks.

    Returns dict with all results and check outcomes.
    """
    results = {}

    # 1. Get uniformly-normalized traceless generators
    T_matrices = get_traceless_generators()
    results['n_generators'] = len(T_matrices)
    print(f"Loaded {len(T_matrices)} traceless generators "
          f"(uniformly normalized: {{T_a,T_b}} = (1/2)*delta*I)")

    # 2. Verify anticommutator normalization
    I16 = np.eye(16)
    for a in range(9):
        anti = T_matrices[a] @ T_matrices[a] + T_matrices[a] @ T_matrices[a]
        err = np.linalg.norm(anti - 0.5 * I16, 'fro')
        if err > 1e-14:
            raise ValueError(
                f"{{T_{a}, T_{a}}} != (1/2)*I: error = {err:.2e}"
            )
    for a in range(9):
        for b in range(a + 1, 9):
            anti = T_matrices[a] @ T_matrices[b] + T_matrices[b] @ T_matrices[a]
            err = np.linalg.norm(anti, 'fro')
            if err > 1e-14:
                raise ValueError(
                    f"{{T_{a}, T_{b}}} != 0: norm = {err:.2e}"
                )
    print("Anticommutator verification: PASSED (all 45 checks)")

    # 3. Verify single-site Casimir
    casimir_err = verify_single_site_casimir(T_matrices)
    results['casimir_error'] = casimir_err
    print(f"Single-site Casimir error: {casimir_err:.2e}")
    assert casimir_err < 1e-14, f"Casimir check FAILED: {casimir_err:.2e}"

    # 4. Construct H_2
    H = construct_2site_hamiltonian(T_matrices, J=1.0)
    results['H_shape'] = H.shape
    print(f"H_2 shape: {H.shape}")

    # 5. Verify real symmetric
    sym_err = np.linalg.norm(H - H.T, 'fro')
    results['symmetry_error'] = sym_err
    print(f"Symmetry error (H - H^T): {sym_err:.2e}")
    assert sym_err < 1e-14, f"Symmetry check FAILED: {sym_err:.2e}"

    # 6. Verify trace zero
    tr = np.trace(H)
    results['trace'] = tr
    print(f"Tr(H_2) = {tr:.2e}")
    assert abs(tr) < 1e-12, f"Trace check FAILED: {tr:.2e}"

    # 7. Verify Spin(9) commutation
    max_comm, all_comm = verify_spin9_commutation(H, T_matrices)
    results['max_commutator_norm'] = max_comm
    print(f"Max Spin(9) commutator norm: {max_comm:.2e}")
    assert max_comm < 1e-12, f"Spin(9) check FAILED: {max_comm:.2e}"

    # 8. Diagonalize
    eigenvalues, eigenvectors = diagonalize_2site(H)
    results['n_eigenvalues'] = len(eigenvalues)
    results['eigenvalue_sum'] = np.sum(eigenvalues)
    print(f"Eigenvalue count: {len(eigenvalues)}")
    print(f"Sum of eigenvalues: {np.sum(eigenvalues):.2e}")
    assert len(eigenvalues) == 256
    assert abs(np.sum(eigenvalues)) < 1e-10, \
        f"Eigenvalue sum check FAILED: {np.sum(eigenvalues):.2e}"

    # 9. Analyze spectrum
    levels = analyze_spectrum(eigenvalues)
    results['levels'] = levels
    results['n_levels'] = len(levels)
    total_mult = sum(m for _, m in levels)
    results['total_multiplicity'] = total_mult
    print(f"Distinct levels: {len(levels)}")
    print(f"Total multiplicity: {total_mult}")
    assert total_mult == 256

    # 10. Print full summary
    summary = print_spectrum_summary(eigenvalues, eigenvectors, T_matrices)
    results['summary'] = summary

    # 11. J=0 limit check
    H0 = construct_2site_hamiltonian(T_matrices, J=0.0)
    assert np.linalg.norm(H0, 'fro') < 1e-14, "J=0 limit check FAILED"
    print("J=0 limit check: PASSED")

    results['all_checks_passed'] = True
    return results


if __name__ == '__main__':
    import sys
    sys.path.insert(0, '/Users/ehrlich/scratch/get-physics-done/code')
    results = run_all_checks()
