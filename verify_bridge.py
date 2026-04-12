"""
Verify the bridge between van de Wetering's sequential product
and Barandes' stochastic-quantum correspondence.

Claim: The Luders sequential product on configuration projectors
gives exactly Barandes' transition probabilities.
"""

import numpy as np
from scipy.stats import unitary_group

np.set_printoptions(precision=12, linewidth=120)

ATOL = 1e-12
RNG = np.random.default_rng(42)
PASS = 0
FAIL = 0


def report(name, ok, detail=""):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if not ok:
        FAIL += 1
    else:
        PASS += 1
    print(f"  [{status}] {name}" + (f"  -- {detail}" if detail else ""))


def random_unitary(n):
    """Random unitary from Haar measure."""
    return unitary_group.rvs(n, random_state=RNG)


def projector(i, n):
    """Rank-1 projector |i><i| in C^n."""
    P = np.zeros((n, n), dtype=complex)
    P[i, i] = 1.0
    return P


def sequential_product(a, b):
    """Luders sequential product: a * b = sqrt(a) @ b @ sqrt(a).
    For projectors, sqrt(P) = P, so this is P @ b @ P."""
    # a is always a projector in our usage
    return a @ b @ a


def evolved_projector(j, U):
    """U P_j U^dagger."""
    n = U.shape[0]
    Pj = projector(j, n)
    return U @ Pj @ U.conj().T


def gamma_from_sequential_product(U):
    """Build the transition matrix Gamma_ij = Tr(P_i * P_j(t))."""
    n = U.shape[0]
    Gamma = np.zeros((n, n))
    for i in range(n):
        Pi = projector(i, n)
        for j in range(n):
            Pjt = evolved_projector(j, U)
            sp = sequential_product(Pi, Pjt)
            Gamma[i, j] = np.real(np.trace(sp))
    return Gamma


def gamma_from_U_squared(U):
    """Gamma_ij = |U_ij|^2 (Barandes' transition matrix)."""
    return np.abs(U) ** 2


# =============================================================
# CHECK 1-5: Sequential product gives |U_ij|^2
# =============================================================
print("=" * 70)
print("CHECKS 1-5: Sequential product == |U_ij|^2")
print("=" * 70)

for n in [2, 3, 4, 5]:
    print(f"\n  n = {n}:")
    for trial in range(5):
        U = random_unitary(n)
        G_sp = gamma_from_sequential_product(U)
        G_sq = gamma_from_U_squared(U)
        max_err = np.max(np.abs(G_sp - G_sq))
        report(f"trial {trial+1}", max_err < ATOL, f"max |Gamma_sp - Gamma_sq| = {max_err:.2e}")

# =============================================================
# CHECK 6: Gamma is a valid stochastic matrix
# =============================================================
print("\n" + "=" * 70)
print("CHECK 6: Gamma is a valid stochastic matrix")
print("  (non-negative entries, columns sum to 1)")
print("=" * 70)

for n in [2, 3, 4, 5]:
    print(f"\n  n = {n}:")
    for trial in range(3):
        U = random_unitary(n)
        G = gamma_from_U_squared(U)
        non_neg = np.all(G >= -ATOL)
        # Columns sum to 1: sum_i Gamma_ij = sum_i |U_ij|^2 = 1
        # (unitarity: columns of U have unit norm)
        col_sums = G.sum(axis=0)
        col_ok = np.allclose(col_sums, 1.0, atol=ATOL)
        # Rows sum to 1: sum_j Gamma_ij = sum_j |U_ij|^2 = 1
        # (unitarity: rows of U have unit norm)
        row_sums = G.sum(axis=1)
        row_ok = np.allclose(row_sums, 1.0, atol=ATOL)
        report(
            f"trial {trial+1}",
            non_neg and col_ok and row_ok,
            f"min={G.min():.2e}, col_sums in [{col_sums.min():.12f}, {col_sums.max():.12f}], "
            f"row_sums in [{row_sums.min():.12f}, {row_sums.max():.12f}]",
        )

# =============================================================
# CHECK 7: Indivisibility (Gamma does NOT factor)
# =============================================================
print("\n" + "=" * 70)
print("CHECK 7: Indivisibility -- Gamma(U2 @ U1) != Gamma(U2) @ Gamma(U1)")
print("=" * 70)

for n in [2, 3, 4, 5]:
    print(f"\n  n = {n}:")
    for trial in range(3):
        U1 = random_unitary(n)
        U2 = random_unitary(n)
        U = U2 @ U1

        G = gamma_from_U_squared(U)
        G1 = gamma_from_U_squared(U1)
        G2 = gamma_from_U_squared(U2)
        G_composed = G2 @ G1

        diff = np.max(np.abs(G - G_composed))
        # We expect them to NOT match (diff > 0)
        report(
            f"trial {trial+1}",
            diff > 1e-6,
            f"max |Gamma(U) - Gamma(U2)@Gamma(U1)| = {diff:.6f} (should be > 0)",
        )

# =============================================================
# CHECK 8: Non-associativity of sequential product
# =============================================================
print("\n" + "=" * 70)
print("CHECK 8: Sequential product is NOT associative")
print("  (P_i * P_j(t)) * P_k(t') vs P_i * (P_j(t) * P_k(t'))")
print("=" * 70)

for n in [2, 3, 4, 5]:
    print(f"\n  n = {n}:")
    for trial in range(3):
        U = random_unitary(n)
        Up = random_unitary(n)

        # Pick random indices
        i = RNG.integers(0, n)
        j = RNG.integers(0, n)
        k = RNG.integers(0, n)

        Pi = projector(i, n)
        Pjt = evolved_projector(j, U)
        Pkt = evolved_projector(k, Up)

        # Left association: (P_i * P_j(t)) * P_k(t')
        left = sequential_product(sequential_product(Pi, Pjt), Pkt)

        # Right association: P_i * (P_j(t) * P_k(t'))
        right = sequential_product(Pi, sequential_product(Pjt, Pkt))

        diff = np.max(np.abs(left - right))
        report(
            f"trial {trial+1} (i={i},j={j},k={k})",
            diff > 1e-10,
            f"max |left - right| = {diff:.6e} (should be > 0)",
        )

# =============================================================
# CHECK 9: Completeness -- sum_j Gamma_ij = 1 for all i
# =============================================================
print("\n" + "=" * 70)
print("CHECK 9: Completeness -- sum_j Gamma_ij = 1 for all i")
print("=" * 70)

for n in [2, 3, 4, 5]:
    print(f"\n  n = {n}:")
    for trial in range(3):
        U = random_unitary(n)
        G = gamma_from_sequential_product(U)
        row_sums = G.sum(axis=1)
        ok = np.allclose(row_sums, 1.0, atol=ATOL)
        report(f"trial {trial+1}", ok, f"row sums: {row_sums}")

# =============================================================
# CHECK 10: Born rule -- p_i(t) = sum_j Gamma_ij p_j
# =============================================================
print("\n" + "=" * 70)
print("CHECK 10: Born rule -- p_i(t) = sum_j Gamma_ij p_j")
print("  Starting from rho = sum_j p_j P_j, verify")
print("  Tr(P_i U rho U^dagger) = sum_j |U_ij|^2 p_j")
print("=" * 70)

for n in [2, 3, 4, 5]:
    print(f"\n  n = {n}:")
    for trial in range(5):
        U = random_unitary(n)

        # Random probability vector (diagonal density matrix)
        p = RNG.random(n)
        p = p / p.sum()

        # Density matrix rho = sum_j p_j P_j (diagonal)
        rho = np.diag(p.astype(complex))

        # Evolve: rho(t) = U rho U^dagger
        rho_t = U @ rho @ U.conj().T

        # Outcome probabilities from quantum mechanics
        p_qm = np.array([np.real(np.trace(projector(i, n) @ rho_t)) for i in range(n)])

        # Outcome probabilities from Gamma
        G = gamma_from_U_squared(U)
        p_gamma = G @ p

        max_err = np.max(np.abs(p_qm - p_gamma))
        report(f"trial {trial+1}", max_err < ATOL, f"max |p_qm - p_Gamma| = {max_err:.2e}")

# =============================================================
# BONUS: Explicit small example (n=2, Hadamard gate)
# =============================================================
print("\n" + "=" * 70)
print("BONUS: Explicit example -- n=2, Hadamard gate")
print("=" * 70)

H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
G = gamma_from_sequential_product(H)
G_expected = np.array([[0.5, 0.5], [0.5, 0.5]])
print(f"\n  Hadamard unitary:\n{H}")
print(f"\n  Gamma from sequential product:\n{G}")
print(f"\n  Expected (all 1/2):\n{G_expected}")
max_err = np.max(np.abs(G - G_expected))
report("Hadamard Gamma", max_err < ATOL, f"max error = {max_err:.2e}")

# Doubly stochastic (unitary => doubly stochastic by Birkhoff)
col_sums = G.sum(axis=0)
row_sums = G.sum(axis=1)
report(
    "Doubly stochastic",
    np.allclose(col_sums, 1.0, atol=ATOL) and np.allclose(row_sums, 1.0, atol=ATOL),
    f"col_sums={col_sums}, row_sums={row_sums}",
)

# Born rule with Hadamard on |0>
p0 = np.array([1.0, 0.0])
p_out = G @ p0
report("Born rule |0> -> H", np.allclose(p_out, [0.5, 0.5], atol=ATOL), f"p_out = {p_out}")

# =============================================================
# SUMMARY
# =============================================================
print("\n" + "=" * 70)
print(f"SUMMARY: {PASS} passed, {FAIL} failed out of {PASS + FAIL} checks")
print("=" * 70)

if FAIL == 0:
    print("\nAll checks passed. The bridge is verified:")
    print("  Luders sequential product on configuration projectors")
    print("  gives exactly Barandes' transition probabilities.")
    print("  Gamma_ij = Tr(P_i * P_j(t)) = |U_ij|^2")
else:
    print(f"\n{FAIL} checks FAILED. Investigate.")
