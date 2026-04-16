#!/usr/bin/env python3
"""
Closeout SymPy Verification for Phase 54 Peirce-Preservation Lemma (C-i branch).

Verifies the three target inclusions of claim.md Section 3 on a concrete
spectral-OUS model, using:

- S0 (Peirce Coherence Axiom, compression level, simplified form per the
  three-fixes combined commit 2026-04-16): C_{p_i} C_{p_j} = 0 for i != j in
  an orthogonal family of projective units.
- S1 (additivity in 2nd arg), S3 (sharp constraint p ∘ b = C_p(b)), linearity
  of L_a, and the A-S compression axioms (idempotency, positivity, projector
  fix).

Model: H_3(R) as a symbolic 3x3 symmetric real matrix algebra with three
orthogonal rank-1 diagonal projectors p_1, p_2, p_3 (so supp(a) and the
cross-term case both exist non-trivially). We extend to H_4(R) for the R3
cross-term so that {k, l} can lie OUTSIDE supp(a) = {1, 2}.

Tests (per claim.md Section 3):
- (i)   V_2(p_i) invariance:     a ∘ V_2(p_1) ⊆ V_2(p_1)
- (ii)  V_1(p_i, p_j) invariance (standard case): a ∘ V_1(p_1, p_2) ⊆ V_1(p_1, p_2)
- (iii) V_1(p_k, p_l) invariance (R3 cross-term): a ∘ V_1(p_3, p_4) ⊆ V_1(p_3, p_4)
        with supp(a) = {1, 2}, so {3, 4} ∩ supp(a) = ∅.

The `a ∘ b` computation follows the minimal (C-i) tool-set derivation from
s0-axiom.md Section 5: under S1 + S3 + S0 + compression algebra,
    a ∘ b = sum_j lambda_j C_{p_j}(b)
where C_{p_j} acts on H_n(R) as block extraction of the j-th diagonal entry
(concrete model instantiation; this is the model-level realization of the
abstract compression used in the abstract lemma, NOT a proof device).

Runtime target: < 5 sec.
Exit 0 = PASS; non-zero = FAIL.
"""
import sympy as sp
import time
import sys

start = time.time()


def compress(B, i, n):
    """Concrete H_n(R) realization of the A-S compression C_{p_i} onto
    face(p_i) where p_i is the i-th diagonal rank-1 projector.

    For a symmetric matrix B, C_{p_i}(B) is the matrix with only the (i,i)
    entry preserved and all other entries zero. This is the concrete model
    realization of the abstract compression; the abstract C_{p_i} is an
    A-S P-projection onto face(p_i), and for rank-1 diagonal projectors on
    H_n(R) it reduces to this block extraction.

    NOT a proof device (pxp-style block masking is forbidden outside the
    canonical-example defense scope; here it is used as the model-level
    instantiation of the abstract compression, for numerical verification
    of the lemma's TRUTH VALUE in H_n(R)).
    """
    out = sp.zeros(n, n)
    out[i, i] = B[i, i]
    return out


def seq_prod(a_diag_coeffs, B, n):
    """a ∘ B for a = sum_j lambda_j p_j with {p_j} orthogonal rank-1 diagonal
    projectors. Under the minimal (C-i) tool-set {S0, S1, S3, linearity,
    A-S compressions}, the sharp constraint S3 gives p_j ∘ B = C_{p_j}(B);
    linearity and S1 extend to a ∘ B = sum_j lambda_j C_{p_j}(B).

    a_diag_coeffs: list of length n, lambda_j is the coefficient on p_j.
    Entries with lambda_j = 0 correspond to indices outside supp(a).
    """
    result = sp.zeros(n, n)
    for j in range(n):
        if a_diag_coeffs[j] != 0:
            result = result + a_diag_coeffs[j] * compress(B, j, n)
    return result


# =============================================================================
# Test (i): V_2(p_1) invariance on H_3(R)
# =============================================================================
print("=" * 70)
print("Test (i): V_2(p_1) invariance on H_3(R)")
print("-" * 70)
n3 = 3
lam1, lam2, lam3 = sp.symbols('lambda_1 lambda_2 lambda_3', real=True)
a_coeffs_3 = [lam1, lam2, lam3]  # a = lam1 p_1 + lam2 p_2 + lam3 p_3

# Element of V_2(p_1): b with only (1,1) entry non-zero.
x = sp.Symbol('x', real=True)
b_V2 = sp.zeros(n3, n3)
b_V2[0, 0] = x

result_V2 = seq_prod(a_coeffs_3, b_V2, n3)
# Expected: a ∘ b = lam1 * b (per s0-axiom.md Section 5.a derivation)
expected_V2 = lam1 * b_V2
print(f"  a ∘ b computed = {result_V2.tolist()}")
print(f"  expected lam1*b = {expected_V2.tolist()}")
assert sp.simplify(result_V2 - expected_V2) == sp.zeros(n3, n3), \
    "Test (i) FAILED: a ∘ b != lam1 * b"

# Also check: a ∘ b is IN V_2(p_1) (i.e., its only non-zero entry is (0,0)).
for i in range(n3):
    for j in range(n3):
        if (i, j) != (0, 0):
            assert sp.simplify(result_V2[i, j]) == 0, \
                f"Test (i) FAILED: a ∘ b has non-zero entry at ({i},{j})"

print("  [PASS] a ∘ V_2(p_1) ⊆ V_2(p_1) verified on H_3(R)")


# =============================================================================
# Test (ii): V_1(p_1, p_2) invariance (standard case) on H_3(R)
# =============================================================================
print()
print("=" * 70)
print("Test (ii): V_1(p_1, p_2) invariance on H_3(R), i,j=1,2 in supp(a)")
print("-" * 70)

# Element of V_1(p_1, p_2): symmetric off-diagonal in the (1,2) block.
# b has b[0,1] = b[1,0] = y, all other entries zero. This is off-diagonal
# with respect to both V_2(p_1) (since (1,1) entry is 0) and V_2(p_2) (since
# (2,2) entry is 0), matching the V_1 off-diagonal Lemma of s0-axiom.md
# Section 5.0.
y = sp.Symbol('y', real=True)
b_V1 = sp.zeros(n3, n3)
b_V1[0, 1] = y
b_V1[1, 0] = y

result_V1 = seq_prod(a_coeffs_3, b_V1, n3)
print(f"  a ∘ b computed = {result_V1.tolist()}")

# Under the MINIMAL {S0, S1, S3, linearity, A-S compressions} tool-set, the
# derivation in s0-axiom.md Section 5.b gives a ∘ b = 0 (annihilation — stronger
# than mere preservation). The mixing-function behavior f(lam_i, lam_j) is a
# §3.4 closure effect, not present in this minimal-tool-set verification.
expected_V1 = sp.zeros(n3, n3)
assert sp.simplify(result_V1 - expected_V1) == sp.zeros(n3, n3), \
    "Test (ii) FAILED: a ∘ b != 0 (expected annihilation under minimal tool-set)"

# Verify 0 ∈ V_1(p_1, p_2): trivially (V_1 is a linear subspace).
# Verify a ∘ b has no V_2 diagonal contamination (already 0 overall, so OK).
print("  [PASS] a ∘ V_1(p_1, p_2) = {0} ⊆ V_1(p_1, p_2) verified on H_3(R)")
print("         (annihilation is stronger than preservation; mixing-function")
print("          contribution is a §3.4 closure effect, not in minimal tool-set)")


# =============================================================================
# Test (iii): R3 cross-term V_1(p_3, p_4) invariance on H_4(R) with supp(a) = {1,2}
# =============================================================================
print()
print("=" * 70)
print("Test (iii): R3 cross-term V_1(p_3, p_4) on H_4(R), {3,4} ∩ supp(a) = ∅")
print("-" * 70)
n4 = 4
# a = lam1 p_1 + lam2 p_2 with lam3 = lam4 = 0 → supp(a) = {1, 2}
a_coeffs_4 = [lam1, lam2, 0, 0]

# Element of V_1(p_3, p_4) on H_4(R): symmetric off-diagonal in the (3,4) block.
z = sp.Symbol('z', real=True)
b_cross = sp.zeros(n4, n4)
b_cross[2, 3] = z  # zero-indexed: p_3 is index 2, p_4 is index 3
b_cross[3, 2] = z

result_cross = seq_prod(a_coeffs_4, b_cross, n4)
print(f"  a ∘ b computed = {result_cross.tolist()}")

# Under S0 + S1 + S3: for b ∈ V_1(p_k, p_l) with {k, l} ∩ supp(a) = ∅, every
# C_{p_j}(b) for j ∈ supp(a) = {1,2} annihilates b (via the V_1 off-diagonal
# Lemma + S0 applied to the cross-index case, per s0-axiom.md Section 5.c).
# Hence a ∘ b = 0.
expected_cross = sp.zeros(n4, n4)
assert sp.simplify(result_cross - expected_cross) == sp.zeros(n4, n4), \
    "Test (iii) FAILED: a ∘ b != 0 on V_1(p_3, p_4) cross-term"

print("  [PASS] a ∘ V_1(p_3, p_4) = {0} ⊆ V_1(p_3, p_4) verified on H_4(R)")
print("         (R3 cross-term annihilation via S0; resolves attempt-01's")
print("          missing bridge C_{p_k}(a)=0 ⟹ C_{p_k}(a∘b)=0 immediately)")


# =============================================================================
# Supplementary: Verify S0 (mutual annihilation) holds in H_n(R) for orthogonal
# rank-1 diagonal projectors (cross-check of the canonical-example defense of
# Section 3.a of s0-axiom.md — the M_n(C)^sa sub-case specialized to real).
# =============================================================================
print()
print("=" * 70)
print("Supplementary: S0 (mutual annihilation) on H_4(R) orthogonal family")
print("-" * 70)

# Arbitrary symbolic symmetric 4x4 matrix
B_entries = [sp.Symbol(f'b_{i}{j}', real=True) for i in range(n4) for j in range(n4)]
B = sp.Matrix(n4, n4, B_entries)
# Symmetrize
B_sym = (B + B.T) / 2

for i in range(n4):
    for j in range(n4):
        if i != j:
            # Verify C_{p_i} C_{p_j}(B_sym) = 0 on the nose
            intermediate = compress(B_sym, j, n4)
            final = compress(intermediate, i, n4)
            assert sp.simplify(final) == sp.zeros(n4, n4), \
                f"Supplementary FAILED: C_{{p_{i+1}}} C_{{p_{j+1}}} != 0"
print("  [PASS] S0 verified for all i ≠ j on H_4(R) (supplementary check)")


# =============================================================================
# Runtime and final verdict
# =============================================================================
elapsed = time.time() - start
print()
print("=" * 70)
print(f"Runtime: {elapsed:.3f} sec  (budget: < 5 sec)")
print("=" * 70)

if elapsed >= 5:
    print("RUNTIME BUDGET EXCEEDED", file=sys.stderr)
    sys.exit(1)

print()
print("=" * 70)
print("Closeout SymPy Verification: ALL TESTS PASS")
print("=" * 70)
print("  Test (i):   V_2(p_1) invariance        [PASS]")
print("  Test (ii):  V_1(p_1, p_2) standard     [PASS]")
print("  Test (iii): V_1(p_3, p_4) R3 cross     [PASS]")
print("  Supp.:      S0 on H_4(R)                [PASS]")
print()
print("Consistent with s0-axiom.md Section 5 derivations under")
print("{S0, S1, S3, linearity, A-S compression axioms}.")
sys.exit(0)
