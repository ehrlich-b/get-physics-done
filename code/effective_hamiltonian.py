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


def identify_spin9_irreps(levels):
    """Identify which Lambda^k(V_9) irrep each energy level belongs to.

    For Spin(9), S_9 x S_9 = sum_{k=0}^{4} Lambda^k(V_9) with dims
    C(9,k) = 1, 9, 36, 84, 126. The Casimir relation
    E_R = J/2 * (c_total(R) - 9/2) determines the mapping.

    Returns:
        dict mapping multiplicity to Lambda^k label.
    """
    from math import comb
    lambda_dims = {comb(9, k): k for k in range(5)}
    irrep_map = {}
    for energy, mult in levels:
        if mult in lambda_dims:
            irrep_map[mult] = f"Lambda^{lambda_dims[mult]}(V_9)"
        else:
            irrep_map[mult] = f"unknown(dim={mult})"
    return irrep_map


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
    irrep_map = identify_spin9_irreps(levels)

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
        c_total = 2 * energy / J + 9.0 / 2.0
        level_info.append({
            'energy': energy,
            'multiplicity': mult,
            'sector': sector,
            'irrep': irrep_map.get(mult, '?'),
            'c_total': c_total,
        })
        idx += mult

    print("=" * 60)
    print("2-SITE SPECTRUM SUMMARY")
    print("=" * 60)
    print(f"Total states: {total_states}")
    print(f"Distinct energy levels: {len(levels)}")
    print(f"Coupling J = {J}")
    print(f"Decomposition: S_9 x S_9 = Lambda^0 + Lambda^1 + Lambda^2 "
          f"+ Lambda^3 + Lambda^4")
    print()
    print(f"{'Level':>5} {'Energy/J':>10} {'Mult':>5} {'Sector':>9} "
          f"{'c_total':>8} {'Irrep':>16}")
    print("-" * 60)
    for i, info in enumerate(level_info):
        print(f"{i:>5} {info['energy']/J:>10.4f} {info['multiplicity']:>5} "
              f"{info['sector']:>9} {info['c_total']:>8.2f} "
              f"{info['irrep']:>16}")
    print()
    print(f"Ground state: E = {ground_energy/J:.4f} J, mult = {ground_mult}, "
          f"irrep = {irrep_map.get(ground_mult, '?')}")
    print(f"Ground state sector: {mag['sector']}")
    print(f"Energy gap: Delta = {gap/J:.4f} J")
    print(f"Magnetic character: {mag['verdict'].upper()}")
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


def test_f4_beyond_spin9(H_2, T_matrices):
    """Test whether H_2 commutes with F_4 generators beyond Spin(9).

    Uses Krasnov's J_u matrix (grade-3 element of Cl(9,0), outside spin(9))
    as a representative of the 16 extra F_4 generators.

    The algebraic argument:
    - F_4 = Aut(h_3(O)) has dim 52
    - Spin(9) = Stab(E_11) in F_4 has dim 36
    - The 16 extra generators of F_4/Spin(9) mix V_0 with V_{1/2}
    - J_u is antisymmetric, satisfies J_u^2 = -I, and is NOT in spin(9)
      (it lives at Cl(9,0) grade 3, while spin(9) = grade 2)
    - If [H_2, J_u^{total}] != 0, then H_2 breaks F_4 down to Spin(9)

    Parameters:
        H_2: 256x256 numpy array (2-site Hamiltonian)
        T_matrices: list of 9 traceless 16x16 generators

    Returns:
        dict with:
          'j_u': 16x16 J_u matrix
          'j_u_antisymmetric': bool
          'j_u_squared_minus_id': bool
          'j_u_in_spin9': bool
          'j_u_spin9_residual': float
          'commutator_norm': float
          'commutator_relative': float
          'stabilizer': str
          'stabilizer_dim': int
    """
    from octonion_algebra import krasnov_J_u_matrix

    J_u = krasnov_J_u_matrix()
    I16 = np.eye(16)

    # Verify J_u properties
    j_u_antisym = np.allclose(J_u, -J_u.T, atol=1e-14)
    j_u_sq = np.allclose(J_u @ J_u, -I16, atol=1e-14)

    # Check J_u is NOT in spin(9)
    generators = compute_spin9_generators(T_matrices)
    spin9_basis = np.array([G.flatten() for (_, G) in generators]).T
    J_u_flat = J_u.flatten()
    coeffs, _, _, _ = np.linalg.lstsq(spin9_basis, J_u_flat, rcond=None)
    spin9_residual = np.linalg.norm(J_u_flat - spin9_basis @ coeffs)
    j_u_in_spin9 = spin9_residual < 1e-10

    # Compute [H_2, J_u^{total}]
    J_u_total = np.kron(J_u, I16) + np.kron(I16, J_u)
    comm = H_2 @ J_u_total - J_u_total @ H_2
    comm_norm = np.linalg.norm(comm, 'fro')
    h_norm = np.linalg.norm(H_2, 'fro')
    comm_relative = comm_norm / h_norm if h_norm > 0 else 0.0

    if comm_norm > 1e-10:
        stabilizer = 'Spin(9)'
        stabilizer_dim = 36
    else:
        stabilizer = 'unknown (>= Spin(9))'
        stabilizer_dim = -1

    return {
        'j_u': J_u,
        'j_u_antisymmetric': j_u_antisym,
        'j_u_squared_minus_id': j_u_sq,
        'j_u_in_spin9': j_u_in_spin9,
        'j_u_spin9_residual': spin9_residual,
        'commutator_norm': comm_norm,
        'commutator_relative': comm_relative,
        'stabilizer': stabilizer,
        'stabilizer_dim': stabilizer_dim,
    }


def frame_stabilizer_analysis(eigenvalues, eigenvectors, T_matrices):
    """Full frame stabilizer analysis combining algebraic and spectral methods.

    Approach A (algebraic): The projection V_0 -> V_{1/2} that defines T_b
    is Spin(9)-invariant but NOT F_4-invariant (F_4 mixes V_0 with V_{1/2}).
    Therefore H_eff = sum T_a^(1) T_a^(2) is Spin(9)-invariant, not F_4.

    Approach B (computational): Direct commutator test with J_u (grade-3
    Clifford element outside spin(9)).

    Approach C (spectral): Check whether 2-site spectrum degeneracies
    match Spin(9) irreps exclusively, or combine into F_4 irreps.

    Parameters:
        eigenvalues: 256-length sorted array
        eigenvectors: 256x256 array
        T_matrices: list of 9 traceless generators

    Returns:
        dict with full analysis results.
    """
    from effective_hamiltonian import analyze_spectrum

    H_2 = construct_2site_hamiltonian(T_matrices, J=1.0)

    # Approach B: J_u commutator
    f4_test = test_f4_beyond_spin9(H_2, T_matrices)

    # Approach C: spectrum analysis
    levels = analyze_spectrum(eigenvalues)
    from math import comb
    spin9_dims = {comb(9, k) for k in range(5)}
    all_match_spin9 = all(m in spin9_dims for _, m in levels)

    # Check if any pair of multiplicities sums to an F_4 irrep dim
    f4_low_dims = {1, 26, 52, 273, 324, 1053, 1274, 2652, 4096}
    mults = [m for _, m in levels]
    f4_enhancement = False
    for i in range(len(mults)):
        for j in range(i + 1, len(mults)):
            if mults[i] + mults[j] in f4_low_dims:
                f4_enhancement = True

    # Approach A: algebraic argument summary
    algebraic_argument = (
        "V_0 = h_2(O) under Spin(9) decomposes as 1 + 9 (trace + vector). "
        "Under full F_4, V_0 is NOT an invariant subspace (F_4 mixes "
        "V_0 with V_{1/2} via the 16 generators of OP^2). The projection "
        "Pi_{1/2}: h_3(O) -> V_{1/2} that defines T_b operators is "
        "Spin(9)-covariant but NOT F_4-covariant. Therefore H_eff = "
        "sum T_a^(i) T_a^(j), which uses only V_0-projected operators, "
        "has Spin(9) symmetry but NOT full F_4 symmetry."
    )

    return {
        'algebraic_argument': algebraic_argument,
        'f4_commutator_test': f4_test,
        'spectrum_all_spin9': all_match_spin9,
        'spectrum_f4_enhancement': f4_enhancement,
        'stabilizer': f4_test['stabilizer'],
        'stabilizer_dim': f4_test['stabilizer_dim'],
        'ssb_pattern': 'F_4 -> Spin(9)' if f4_test['stabilizer'] == 'Spin(9)' else 'undetermined',
        'target_space': 'F_4/Spin(9) = OP^2 (dim 16)' if f4_test['stabilizer'] == 'Spin(9)' else 'undetermined',
        'goldstone_count': 52 - 36 if f4_test['stabilizer'] == 'Spin(9)' else -1,
    }


if __name__ == '__main__':
    import sys
    sys.path.insert(0, '/Users/ehrlich/scratch/get-physics-done/code')
    results = run_all_checks()

    # Run frame stabilizer analysis
    T_matrices = get_traceless_generators()
    H = construct_2site_hamiltonian(T_matrices, J=1.0)
    eigenvalues, eigenvectors = diagonalize_2site(H)
    fs = frame_stabilizer_analysis(eigenvalues, eigenvectors, T_matrices)
    print()
    print("=" * 60)
    print("FRAME STABILIZER ANALYSIS")
    print("=" * 60)
    print(f"Stabilizer: {fs['stabilizer']} (dim {fs['stabilizer_dim']})")
    print(f"SSB pattern: {fs['ssb_pattern']}")
    print(f"Target space: {fs['target_space']}")
    print(f"Goldstone modes: {fs['goldstone_count']}")
    print(f"J_u commutator norm: {fs['f4_commutator_test']['commutator_norm']:.4f}")
    print(f"J_u in spin(9): {fs['f4_commutator_test']['j_u_in_spin9']}")
    print(f"All multiplicities match Spin(9): {fs['spectrum_all_spin9']}")
    print(f"F_4 enhancement possible: {fs['spectrum_f4_enhancement']}")
    print()
    print("Algebraic argument:")
    print(fs['algebraic_argument'])
