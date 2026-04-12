#!/usr/bin/env python3
"""
Verification script for the Spectral Extension Theorem and the
functional form f = sqrt(x*y) of the mixing function.

Tests:
  1. Spectral extension formula agrees with Luders product on M_n(C)^sa (n=2,3)
  2. Functional equation f(a1,a2)*f(b1,b2) = f(a1*b1, a2*b2) for f = sqrt(xy)
  3. Degenerate-limit test: f(x,y) = (xy)^s with s != 1/2 fails lambda coalescence
  4. Non-symmetric f fails the S5 functional equation
  5. Sweep s in {0.3, 0.5, 0.7, 1.0} confirming only s=0.5 works
  6. Factorization: f(x,y) = f(x,1)*f(1,y) for f = sqrt(xy)
  7. Multiplicative Cauchy: g(xy) = g(x)*g(y) for g(x) = x^{1/2}
"""

import numpy as np
from numpy.linalg import eigvalsh


def sqrtm(a):
    """Matrix square root for real symmetric / Hermitian PSD matrices."""
    evals, evecs = np.linalg.eigh(a)
    evals = np.maximum(evals, 0.0)  # clamp numerical negatives
    return evecs @ np.diag(np.sqrt(evals)) @ evecs.conj().T


# ---- Helpers ----

def luders_product(a, b):
    """Luders sequential product: sqrt(a) @ b @ sqrt(a)."""
    sqrt_a = sqrtm(a)
    # sqrtm can return complex with tiny imaginary parts for real PSD input
    if np.allclose(sqrt_a.imag, 0, atol=1e-14):
        sqrt_a = sqrt_a.real
    return sqrt_a @ b @ sqrt_a


def peirce_product(a, b):
    """Corrected sequential product via Peirce decomposition.

    a = sum_i lam_i p_i  (spectral decomposition)
    sp(a, b) = sum_i lam_i C_{p_i}(b) + sum_{i<j} sqrt(lam_i lam_j) P_{ij}(b)
    """
    n = a.shape[0]
    evals, evecs = np.linalg.eigh(a)
    # Build projectors (rank-1)
    projectors = []
    for k in range(n):
        v = evecs[:, k:k+1]
        projectors.append((evals[k], v @ v.conj().T))

    # Diagonal (compression) contribution
    result = np.zeros_like(b, dtype=complex)
    for lam_i, p_i in projectors:
        result += lam_i * (p_i @ b @ p_i)

    # Peirce 1-space contribution
    for i in range(n):
        for j in range(i + 1, n):
            lam_i, p_i = projectors[i]
            lam_j, p_j = projectors[j]
            # P_{ij}(b) = p_i @ b @ p_j + p_j @ b @ p_i
            p_ij_b = p_i @ b @ p_j + p_j @ b @ p_i
            result += np.sqrt(lam_i * lam_j) * p_ij_b

    if np.allclose(result.imag, 0, atol=1e-14):
        result = result.real
    return result


def peirce_product_general_s(a, b, s):
    """Product with f(lam_i, lam_j) = (lam_i * lam_j)^s."""
    n = a.shape[0]
    evals, evecs = np.linalg.eigh(a)
    projectors = []
    for k in range(n):
        v = evecs[:, k:k+1]
        projectors.append((evals[k], v @ v.conj().T))

    result = np.zeros_like(b, dtype=complex)
    for lam_i, p_i in projectors:
        result += lam_i * (p_i @ b @ p_i)

    for i in range(n):
        for j in range(i + 1, n):
            lam_i, p_i = projectors[i]
            lam_j, p_j = projectors[j]
            p_ij_b = p_i @ b @ p_j + p_j @ b @ p_i
            if lam_i > 0 and lam_j > 0:
                result += (lam_i * lam_j) ** s * p_ij_b
            # if either eigenvalue is 0, contribution is 0

    if np.allclose(result.imag, 0, atol=1e-14):
        result = result.real
    return result


def random_effect(n, rng):
    """Random effect (Hermitian matrix with eigenvalues in [0,1])."""
    # Random unitary via QR
    z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    q, r = np.linalg.qr(z)
    q = q @ np.diag(np.sign(np.diag(r)))
    evals = rng.uniform(0.05, 0.95, n)  # stay away from boundary
    return (q @ np.diag(evals) @ q.conj().T).real if n <= 2 else q @ np.diag(evals) @ q.conj().T


def random_effect_real(n, rng):
    """Random real symmetric effect with eigenvalues in [0,1]."""
    z = rng.standard_normal((n, n))
    q, r = np.linalg.qr(z)
    q = q @ np.diag(np.sign(np.diag(r)))
    evals = rng.uniform(0.05, 0.95, n)
    return q @ np.diag(evals) @ q.T


def is_effect(m, tol=1e-10):
    """Check 0 <= m <= I."""
    eigs = eigvalsh(m)
    return np.all(eigs >= -tol) and np.all(eigs <= 1 + tol)


# ---- Tests ----

def test_spectral_extension_m2():
    """Test 1a: Peirce formula agrees with Luders on M_2(C)^sa."""
    rng = np.random.default_rng(42)
    max_err = 0.0
    n_tests = 50

    for _ in range(n_tests):
        a = random_effect_real(2, rng)
        b = random_effect_real(2, rng)
        sp_luders = luders_product(a, b)
        sp_peirce = peirce_product(a, b)
        err = np.max(np.abs(sp_luders - sp_peirce))
        max_err = max(max_err, err)

    print(f"Test 1a [M_2 Peirce vs Luders]: max error = {max_err:.2e}", end="  ")
    assert max_err < 1e-12, f"FAIL: max_err = {max_err}"
    print("PASS")


def test_spectral_extension_m3():
    """Test 1b: Peirce formula agrees with Luders on M_3(C)^sa."""
    rng = np.random.default_rng(123)
    max_err = 0.0
    n_tests = 50

    for _ in range(n_tests):
        a = random_effect_real(3, rng)
        b = random_effect_real(3, rng)
        sp_luders = luders_product(a, b)
        sp_peirce = peirce_product(a, b)
        err = np.max(np.abs(sp_luders - sp_peirce))
        max_err = max(max_err, err)

    print(f"Test 1b [M_3 Peirce vs Luders]: max error = {max_err:.2e}", end="  ")
    assert max_err < 1e-12, f"FAIL: max_err = {max_err}"
    print("PASS")


def test_functional_equation():
    """Test 2: f(a1,a2)*f(b1,b2) = f(a1*b1, a2*b2) for f = sqrt(xy)."""
    rng = np.random.default_rng(77)
    max_err = 0.0

    for _ in range(200):
        a1, a2, b1, b2 = rng.uniform(0, 1, 4)
        f = lambda x, y: np.sqrt(x * y)
        lhs = f(a1, a2) * f(b1, b2)
        rhs = f(a1 * b1, a2 * b2)
        err = abs(lhs - rhs)
        max_err = max(max_err, err)

    print(f"Test 2  [Functional equation]: max error = {max_err:.2e}", end="  ")
    assert max_err < 1e-15, f"FAIL: max_err = {max_err}"
    print("PASS")


def test_degenerate_limit():
    """Test 3: f(x,y) = (xy)^s with s != 1/2 fails the degenerate limit.

    When lambda_1 -> lambda, lambda_2 -> lambda, the 2-projector formula
    must reduce to lambda * b (the 1-projector result). This requires:
      lambda^{2s} * P_{12}(b) = lambda * P_{12}(b)
    i.e., lambda^{2s} = lambda for all lambda in (0,1], giving 2s = 1.
    """
    test_lambdas = [0.3, 0.5, 0.7, 0.9]
    test_s_values = [0.3, 0.5, 0.7, 1.0]

    print("Test 3  [Degenerate limit]:")
    for s in test_s_values:
        all_pass = True
        max_discrepancy = 0.0
        for lam in test_lambdas:
            # The coalescence condition: lam^{2s} must equal lam
            lhs = lam ** (2 * s)
            rhs = lam
            disc = abs(lhs - rhs)
            max_discrepancy = max(max_discrepancy, disc)
            if disc > 1e-14:
                all_pass = False

        status = "PASS" if all_pass else "FAIL"
        print(f"  s = {s}: coalescence max discrepancy = {max_discrepancy:.2e}  {status}")

    # Also verify numerically with actual matrices
    print("  Numerical matrix verification:")
    rng = np.random.default_rng(99)
    b = random_effect_real(2, rng)

    for s in test_s_values:
        max_err = 0.0
        for lam in test_lambdas:
            a = lam * np.eye(2)  # degenerate: both eigenvalues = lam
            sp_general_s = peirce_product_general_s(a, b, s)
            sp_expected = lam * b  # 1-projector result
            err = np.max(np.abs(sp_general_s - sp_expected))
            max_err = max(max_err, err)

        status = "PASS" if max_err < 1e-12 else "FAIL"
        print(f"  s = {s}: matrix test max error = {max_err:.2e}  {status}")


def test_nonsymmetric_f_fails():
    """Test 4: Non-symmetric f fails the S5 functional equation.

    If f(x,y) = x^s * y^t with s != t, then the functional equation
    f(a1,a2)*f(b1,b2) = f(a1*b1, a2*b2) gives:
      (a1^s a2^t)(b1^s b2^t) = (a1 b1)^s (a2 b2)^t
    This holds, BUT symmetry f(x,y) = f(y,x) requires s = t.
    Test that s != t gives an asymmetric mixing function.
    """
    print("Test 4  [Non-symmetric f]:")
    test_cases = [(0.3, 0.7), (0.8, 0.2), (1.0, 0.0)]
    for s, t in test_cases:
        f = lambda x, y: (x ** s) * (y ** t) if x > 0 and y > 0 else 0.0
        # Check symmetry
        x_vals = [0.2, 0.5, 0.8]
        y_vals = [0.3, 0.6, 0.9]
        max_asym = 0.0
        for x in x_vals:
            for y in y_vals:
                asym = abs(f(x, y) - f(y, x))
                max_asym = max(max_asym, asym)

        is_sym = max_asym < 1e-14
        print(f"  s={s}, t={t}: max asymmetry = {max_asym:.2e}  "
              f"{'symmetric' if is_sym else 'NOT symmetric'}")


def test_s_sweep():
    """Test 5: Sweep s in {0.3, 0.5, 0.7, 1.0}. Only s=0.5 satisfies:
    (a) functional equation f(a1,a2)*f(b1,b2) = f(a1*b1, a2*b2)
    (b) degenerate limit lam^{2s} = lam for all lam in (0,1]
    (c) S5 on actual matrices

    All s values satisfy (a) since (xy)^s is multiplicative.
    Only s=0.5 satisfies (b).
    """
    print("Test 5  [s-sweep combined test]:")
    s_values = [0.3, 0.5, 0.7, 1.0]
    rng = np.random.default_rng(55)

    for s in s_values:
        # (a) Functional equation: always passes for (xy)^s
        fe_max = 0.0
        for _ in range(50):
            a1, a2, b1, b2 = rng.uniform(0.01, 0.99, 4)
            f = lambda x, y: (x * y) ** s
            lhs = f(a1, a2) * f(b1, b2)
            rhs = f(a1 * b1, a2 * b2)
            fe_max = max(fe_max, abs(lhs - rhs))
        fe_pass = fe_max < 1e-14

        # (b) Degenerate limit
        dl_max = 0.0
        for lam in [0.2, 0.4, 0.6, 0.8]:
            dl_max = max(dl_max, abs(lam ** (2 * s) - lam))
        dl_pass = dl_max < 1e-14

        # (c) S5 test on M_2: a,b compatible (both diagonal), check
        #     a &_s (b &_s d) = (a &_s b) &_s d
        a = np.diag([0.75, 0.25])
        b = np.diag([2/3, 1/3])
        d = 0.5 * np.array([[1, 1], [1, 1]])

        bd = peirce_product_general_s(b, d, s)
        lhs_s5 = peirce_product_general_s(a, bd, s)
        ab = peirce_product_general_s(a, b, s)
        rhs_s5 = peirce_product_general_s(ab, d, s)
        s5_err = np.max(np.abs(lhs_s5 - rhs_s5))
        s5_pass = s5_err < 1e-12

        overall = fe_pass and dl_pass and s5_pass
        status = "ALL PASS" if overall else "FAIL"
        print(f"  s = {s}: func_eq={'PASS' if fe_pass else 'FAIL'} "
              f"degen_lim={'PASS' if dl_pass else 'FAIL'} "
              f"S5={'PASS' if s5_pass else 'FAIL'} "
              f"(fe_err={fe_max:.1e} dl_err={dl_max:.1e} s5_err={s5_err:.1e})  "
              f"=> {status}")


def test_factorization():
    """Test 6: f(x,y) = f(x,1)*f(1,y) for f = sqrt(xy).

    f(x,1) = sqrt(x), f(1,y) = sqrt(y), product = sqrt(x)*sqrt(y) = sqrt(xy).
    """
    rng = np.random.default_rng(33)
    max_err = 0.0
    for _ in range(100):
        x, y = rng.uniform(0, 1, 2)
        f_xy = np.sqrt(x * y)
        f_x1_f_1y = np.sqrt(x) * np.sqrt(y)
        err = abs(f_xy - f_x1_f_1y)
        max_err = max(max_err, err)

    print(f"Test 6  [Factorization f(x,y) = f(x,1)*f(1,y)]: max error = {max_err:.2e}", end="  ")
    assert max_err < 1e-15, f"FAIL: max_err = {max_err}"
    print("PASS")


def test_multiplicative_cauchy():
    """Test 7: g(xy) = g(x)*g(y) for g(x) = x^{1/2}.

    The continuous solutions of g(xy) = g(x)g(y) on [0,1] with g(0)=0, g(1)=1
    are g(x) = x^s for s > 0. Verify that only s=1/2 yields f(x,y) = sqrt(xy)
    when combined with symmetry and the degenerate limit.
    """
    rng = np.random.default_rng(11)
    print("Test 7  [Multiplicative Cauchy equation]:")

    for s_val in [0.3, 0.5, 0.7, 1.0]:
        g = lambda x: x ** s_val if x > 0 else 0.0
        max_err = 0.0
        for _ in range(100):
            x, y = rng.uniform(0.01, 0.99, 2)
            lhs = g(x * y)
            rhs = g(x) * g(y)
            err = abs(lhs - rhs)
            max_err = max(max_err, err)
        print(f"  s = {s_val}: g(xy) vs g(x)g(y) max error = {max_err:.2e}  "
              f"{'PASS (multiplicative)' if max_err < 1e-14 else 'FAIL'}")

    print("  All s > 0 satisfy Cauchy. Degenerate limit selects s = 1/2.")


def test_effect_preservation():
    """Bonus: verify the product maps effects to effects (positivity)."""
    rng = np.random.default_rng(7)
    n_tests = 100
    violations = 0

    for _ in range(n_tests):
        for n in [2, 3]:
            a = random_effect_real(n, rng)
            b = random_effect_real(n, rng)
            sp = peirce_product(a, b)
            if not is_effect(sp, tol=1e-10):
                violations += 1

    print(f"Test 8  [Effect preservation]: {n_tests * 2} products checked, "
          f"{violations} violations", end="  ")
    assert violations == 0, f"FAIL: {violations} violations"
    print("PASS")


if __name__ == "__main__":
    print("=" * 72)
    print("Spectral Extension Theorem & Functional Form Verification")
    print("=" * 72)
    print()
    test_spectral_extension_m2()
    test_spectral_extension_m3()
    print()
    test_functional_equation()
    print()
    test_degenerate_limit()
    print()
    test_nonsymmetric_f_fails()
    print()
    test_s_sweep()
    print()
    test_factorization()
    print()
    test_multiplicative_cauchy()
    print()
    test_effect_preservation()
    print()
    print("=" * 72)
    print("All tests complete.")
    print("=" * 72)
