# Tests for Phase 38, Plan 01: 2-site effective Hamiltonian H_eff.
#
# Covers: Hermiticity, trace, Casimir, Spin(9) commutation, eigenvalue
# structure, degeneracy, ferro/antiferro determination, SWAP decomposition,
# J=0 limit, and Casimir cross-check for all 5 Spin(9) irreps.

import sys
sys.path.insert(0, '/Users/ehrlich/scratch/get-physics-done/code')

import numpy as np
import pytest
from effective_hamiltonian import (
    get_traceless_generators,
    verify_single_site_casimir,
    construct_2site_hamiltonian,
    compute_spin9_generators,
    verify_spin9_commutation,
    diagonalize_2site,
    analyze_spectrum,
    construct_swap_operator,
    determine_magnetic_character,
    print_spectrum_summary,
)


@pytest.fixture(scope='module')
def T_matrices():
    return get_traceless_generators()


@pytest.fixture(scope='module')
def H2(T_matrices):
    return construct_2site_hamiltonian(T_matrices, J=1.0)


@pytest.fixture(scope='module')
def spectrum(H2):
    eigenvalues, eigenvectors = diagonalize_2site(H2)
    return eigenvalues, eigenvectors


def test_hermiticity(H2):
    """H_2 must be real symmetric: norm(H - H^T) < 1e-14."""
    err = np.linalg.norm(H2 - H2.T, 'fro')
    assert err < 1e-14, f"H_2 not symmetric: {err:.2e}"


def test_trace_zero(H2):
    """Tr(H_2) = 0 since all T_a are traceless."""
    tr = np.trace(H2)
    assert abs(tr) < 1e-12, f"Tr(H_2) = {tr:.2e}, expected 0"


def test_single_site_casimir(T_matrices):
    """sum_{a=0}^{8} T_a^2 = (9/4)*I_16."""
    err = verify_single_site_casimir(T_matrices)
    assert err < 1e-14, f"Casimir error: {err:.2e}"


def test_anticommutator_normalization(T_matrices):
    """{T_a, T_b} = (1/2)*delta_{ab}*I_16 for all a,b."""
    I16 = np.eye(16)
    for a in range(9):
        anti = T_matrices[a] @ T_matrices[a] + T_matrices[a] @ T_matrices[a]
        err = np.linalg.norm(anti - 0.5 * I16, 'fro')
        assert err < 1e-14, f"{{T_{a},T_{a}}} error: {err:.2e}"
    for a in range(9):
        for b in range(a + 1, 9):
            anti = T_matrices[a] @ T_matrices[b] + T_matrices[b] @ T_matrices[a]
            err = np.linalg.norm(anti, 'fro')
            assert err < 1e-14, f"{{T_{a},T_{b}}} error: {err:.2e}"


def test_spin9_commutation(H2, T_matrices):
    """[H_2, G_{ab}^total] = 0 for all 36 Spin(9) generators."""
    max_norm, all_norms = verify_spin9_commutation(H2, T_matrices)
    assert max_norm < 1e-12, f"Max commutator norm: {max_norm:.2e}"
    assert len(all_norms) == 36


def test_eigenvalue_count(spectrum):
    """Exactly 256 eigenvalues."""
    eigenvalues, _ = spectrum
    assert len(eigenvalues) == 256


def test_eigenvalue_sum(spectrum):
    """Sum of eigenvalues = 0 (trace zero)."""
    eigenvalues, _ = spectrum
    s = np.sum(eigenvalues)
    assert abs(s) < 1e-10, f"Sum = {s:.2e}"


def test_degeneracy_total(spectrum):
    """Multiplicities sum to 256."""
    eigenvalues, _ = spectrum
    levels = analyze_spectrum(eigenvalues)
    total = sum(m for _, m in levels)
    assert total == 256


def test_degeneracy_structure(spectrum):
    """Multiplicities match Lambda^k(V_9) dimensions: 1, 9, 36, 84, 126."""
    eigenvalues, _ = spectrum
    levels = analyze_spectrum(eigenvalues)
    mults = sorted([m for _, m in levels])
    expected = sorted([1, 9, 36, 84, 126])
    assert mults == expected, f"Mults {mults} != expected {expected}"


def test_j_zero_limit(T_matrices):
    """J=0 gives all eigenvalues = 0."""
    H0 = construct_2site_hamiltonian(T_matrices, J=0.0)
    assert np.linalg.norm(H0, 'fro') < 1e-14


def test_swap_eigenvalues():
    """SWAP has eigenvalues +1 (dim 136) and -1 (dim 120)."""
    P = construct_swap_operator(16)
    evals = np.linalg.eigvalsh(P)
    n_pos = np.sum(np.abs(evals - 1.0) < 1e-10)
    n_neg = np.sum(np.abs(evals + 1.0) < 1e-10)
    assert n_pos == 136, f"Symmetric sector: {n_pos}"
    assert n_neg == 120, f"Antisymmetric sector: {n_neg}"


def test_ground_state_sector(spectrum):
    """Ground state sector is unambiguously identified."""
    eigenvalues, eigenvectors = spectrum
    levels = analyze_spectrum(eigenvalues)
    ground_mult = levels[0][1]
    ground_indices = list(range(ground_mult))
    mag = determine_magnetic_character(eigenvectors, ground_indices)
    assert mag['sector'] in ('symmetric', 'antisymmetric'), \
        f"Undetermined sector: {mag['sector']}"


def test_symmetric_antisymmetric_partition(spectrum):
    """sym + antisym = 136 + 120 = 256."""
    eigenvalues, eigenvectors = spectrum
    levels = analyze_spectrum(eigenvalues)
    P = construct_swap_operator(16)
    total_sym = 0
    total_antisym = 0
    idx = 0
    for _, mult in levels:
        for k in range(mult):
            v = eigenvectors[:, idx + k]
            sv = v @ P @ v
            if abs(sv - 1.0) < 1e-8:
                total_sym += 1
            elif abs(sv + 1.0) < 1e-8:
                total_antisym += 1
        idx += mult
    assert total_sym == 136, f"Symmetric: {total_sym}"
    assert total_antisym == 120, f"Antisymmetric: {total_antisym}"


def test_casimir_crosscheck(spectrum, T_matrices):
    """Computed eigenvalues match Casimir prediction for each irrep.

    E_R = J * (1/2) * (c_total(R) - 9/2) where c_total(R) is the
    eigenvalue of C_total = sum (T_a^(1) + T_a^(2))^2 on irrep R.
    """
    eigenvalues, _ = spectrum
    levels = analyze_spectrum(eigenvalues)
    I16 = np.eye(16)

    # Compute C_total
    C_total = np.zeros((256, 256))
    for T_a in T_matrices:
        Ta_total = np.kron(T_a, I16) + np.kron(I16, T_a)
        C_total += Ta_total @ Ta_total

    # C_total eigenvalues
    c_evals = np.linalg.eigvalsh(C_total)
    c_levels = analyze_spectrum(c_evals)

    # Map: E_R = (c_total - 9/2) / 2
    for c_val, c_mult in c_levels:
        E_pred = (c_val - 4.5) / 2.0
        found = False
        for e_val, e_mult in levels:
            if abs(e_val - E_pred) < 1e-10 and e_mult == c_mult:
                found = True
                break
        assert found, f"Casimir c_total={c_val:.2f} (mult {c_mult}) " \
                       f"predicts E={E_pred:.4f} but not found in spectrum"


def test_energy_gap(spectrum):
    """Energy gap is positive (non-degenerate ground state sector)."""
    eigenvalues, _ = spectrum
    levels = analyze_spectrum(eigenvalues)
    assert len(levels) >= 2, "Only one energy level"
    gap = levels[1][0] - levels[0][0]
    assert gap > 0, f"Non-positive gap: {gap}"


def test_eigenvalue_scale(spectrum):
    """All eigenvalues are O(J) = O(1)."""
    eigenvalues, _ = spectrum
    assert np.max(np.abs(eigenvalues)) < 10.0, \
        f"Eigenvalues not O(J): max = {np.max(np.abs(eigenvalues))}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
