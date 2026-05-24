"""
Ambient E-Transport Test Harness  --  VALD-62-01  (TDD RED phase)
==================================================================
Phase: 62-coherent-embedding-under-e-the-hard-part, Plan: 02

ASSERT-BASED harness (NO pytest -- pytest is NOT installed in the executor venv;
sympy/numpy only). Runnable directly:

    python tests/test_embedding_under_E.py

It imports the check functions from code/embedding_under_E_verification.py and
asserts on their (exact-SymPy) results, mirroring the _report / ALL_PASS /
sys.exit pattern of code/slice_clause_iii_verification.py (NOT the pytest style
of tests/test_slice_clause_iii.py). It is RED (import / AttributeError) until
plan 62-02 Task 2 implements code/embedding_under_E_verification.py.

# ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na
# Pure-algebra: Jordan product a o b = (1/2)(ab+ba); sequential product a&b = sqrt(a) b sqrt(a)
#   (CFC principal branch); EXACT symbolic/rational/surd arithmetic (SymPy), NEVER float64
#   on the decisive path; octonion Fano e_1 e_2 = e_4; complex structure u = e_7;
#   slice A = h_3(C_u) ~ M_3(C)^sa.

THE DECISIVE OBJECT (this whole plan turns on it):
    R := E( sqrt(X) Y sqrt(X) )  -  sqrt(EX) (EY) sqrt(EX)
for GENERIC ambient X (PSD), Y in h_3(O), with sqrt(X) computed IN THE AMBIENT
(non-associative h_3(O)), and the relevant associator EXACTLY nonzero
(non-associativity load-bearing). EXACT R == 0 => coherent transport (P);
EXACT R != 0 => ambient-transport obstruction (O, the EXPECTED outcome).

The slice-internal sqrt(a) b sqrt(a) (a,b in A) is the documented TRIVIAL CONTROL
(closed associative subalgebra; leakage 0; associator 0) -- NOT the decisive test.

HONEST verdict: this harness does NOT hardcode R==0 (force P) or R!=0 (force O).
It asserts internal consistency (R.equals(zeros) <=> is_zero_exact), cross-route
agreement (direct residual vs Peirce/grade-component), and the self-checks
(E-properties, ambient sqrt, associator-nonzero on the DECISIVE data) -- so it
PASSES for whichever verdict the true exact computation yields.

Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0. Deterministic
(no random seeds; all test elements hardcoded with exact rational/surd entries).
"""

import os
import sys

# Import the (Task-2) verification module from code/.
_HERE = os.path.dirname(os.path.abspath(__file__))
_CODE = os.path.join(os.path.dirname(_HERE), "code")
if _CODE not in sys.path:
    sys.path.insert(0, _CODE)

from sympy import zeros, eye, Rational, sqrt  # noqa: E402

import embedding_under_E_verification as V  # noqa: E402  (RED until Task 2)


# ---- assert-based accumulator (mirrors slice_clause_iii_verification._report) ----
ALL_PASS = True


def _report(label, ok):
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok:
        ALL_PASS = False
    return ok


def _is_zero_octmat(M):
    """True iff a 3x3 matrix of OctSym is EXACTLY the zero octonionic matrix."""
    return V.octmat_is_zero(M)


# ============================================================
# (A) E conditional-expectation properties (exact)
# ============================================================

def check_A_E_properties():
    print("\n=== (A) E conditional-expectation properties (exact) ===")

    I3 = V.h3o_identity()
    # (a) unital: E(I_3) == I_3
    _report("E unital: E(I_3) == I_3 (exact)",
            V.octmat_equal(V.E(I3), I3))

    # (b) idempotent: E(E(X)) == E(X) for a GENERIC ambient X with nonzero e_1..e_6
    Xgen = V.generic_ambient_element("idem")
    _report("E idempotent: E(E(X)) == E(X) for generic ambient X (exact)",
            V.octmat_equal(V.E(V.E(Xgen)), V.E(Xgen)))
    # the generic X must genuinely have e_1..e_6 content (else idempotency is vacuous)
    _report("idempotency test element has nonzero e_1..e_6 (non-vacuous)",
            V.has_kerE_content(Xgen))

    # (c) E|_A = id on a SLICE element (off-diagonals in C_u = span{1,e_7})
    a = V.generic_slice_element("Eid")
    _report("E|_A = id: E(a) == a for a in slice A = h_3(C_u) (exact)",
            V.octmat_equal(V.E(a), a))

    # (d) E is the entrywise proj_u: zeroes octonion comps 1..6 of x1,x2,x3, keeps 0,7
    _report("E entrywise proj_u: E(X) off-diagonals have zero e_1..e_6, keep e_0,e_7",
            V.E_is_entrywise_proj_u(Xgen))

    # (e) positivity spot-check: a PSD slice effect maps to a PSD element (exact eigenvalues >= 0)
    _report("E positive (spot): PSD slice element -> E(.) PSD (exact eigenvalues >= 0)",
            V.E_positive_spotcheck())

    # (f) E is NOT a Jordan morphism on the AMBIENT: E(X o X) != (EX) o (EX) (exact nonzero)
    is_morphism, diff_nonzero = V.E_jordan_morphism_on_ambient_check(Xgen)
    _report("E is NOT a Jordan morphism on the ambient: E(X o X) != (EX) o (EX) "
            "(exact nonzero difference) -- this is what makes transport non-trivial",
            (not is_morphism) and diff_nonzero)

    # dimension bookkeeping
    dr, dk = V.dim_range_E(), V.dim_ker_E()
    _report(f"dim(range E)=9, dim(ker E)=18, 27=9+18 (got {dr}+{dk})",
            dr == 9 and dk == 18 and dr + dk == 27)


# ============================================================
# (B) Ambient square root (exact, non-associative)
# ============================================================

def check_B_ambient_sqrt():
    print("\n=== (B) Ambient square root (exact, non-associative) ===")

    # exact-square trick: X = C^2 with C an ambient element (exact entries), sqrt(X)=C.
    # register_square(C) computes X = C*C (ambient octonionic product) AND records the
    # known principal PSD root C, so sqrt_ambient(X) returns it.
    C = V.generic_ambient_psd_root("C")   # the ambient "C" (single-direction off-diags)
    X = V.register_square(C)               # X = C*C (ambient), root C registered
    sqrtX = V.sqrt_ambient(X)

    # self-check: sqrt_ambient(X)^2 == X EXACTLY in the ambient octonionic product
    _report("ambient sqrt self-check: h3o_matmul(sqrt_X, sqrt_X) == X (exact, octonionic)",
            V.octmat_equal(V.h3o_matmul(sqrtX, sqrtX), X))

    # sqrt_ambient must use the AMBIENT product, not a slice-only complex sqrt:
    # confirm X genuinely lives outside the slice (has e_1..e_6 content) so the sqrt is ambient.
    _report("ambient sqrt operates on a genuinely ambient X (nonzero e_1..e_6 content)",
            V.has_kerE_content(X))


# ============================================================
# (C) Non-associativity exerciser (mandatory, on the DECISIVE data)
# ============================================================

def check_C_nonassociativity_load_bearing():
    print("\n=== (C) Non-associativity exerciser (on the DECISIVE data) ===")

    # The associator (X*Y)*Z - X*(Y*Z) must be EXACTLY nonzero for the relevant
    # ambient triple built from the DECISIVE test data X,Y (NOT unrelated matrices).
    nonzero, _assoc = V.decisive_associator_nonzero()
    _report("associator (X*Y)*Z - X*(Y*Z) EXACTLY nonzero on the DECISIVE triple "
            "(non-associativity load-bearing; (xy)z != x(yz) genuinely engaged)",
            nonzero)

    # the decisive X,Y are GENERIC ambient (NOT slice-confined)
    _report("decisive X,Y are generic ambient (nonzero e_1..e_6), NOT slice-confined",
            V.decisive_data_is_ambient())


# ============================================================
# (D) THE DECISIVE AMBIENT-TRANSPORT residual (exact)
# ============================================================

def check_D_decisive_residual():
    print("\n=== (D) THE DECISIVE AMBIENT-TRANSPORT residual (exact) ===")

    pairs = V.decisive_test_pairs()   # >= 2 generic (X,Y)
    _report(f">= 2 generic decisive (X,Y) pairs provided (got {len(pairs)})",
            len(pairs) >= 2)

    verdicts = []
    for idx, (X, Y) in enumerate(pairs):
        # associator-nonzero precheck on THIS (X,Y) so the residual is a genuine
        # non-associative test (the associator and the residual on the SAME X,Y).
        assoc_nonzero, _ = V.associator_nonzero_for_pair(X, Y)
        _report(f"  pair {idx}: associator nonzero on the SAME X,Y (load-bearing)",
                assoc_nonzero)

        R, is_zero_exact = V.compute_ambient_transport_residual(X, Y)

        # HONEST consistency (NOT rigged toward P or O):
        #   is_zero_exact is a BOOLEAN consistent with R: R is the zero octmat <=> is_zero_exact.
        r_is_zero = _is_zero_octmat(R)
        _report(f"  pair {idx}: is_zero_exact is consistent with R "
                f"(R==0 <=> is_zero_exact); is_zero_exact={is_zero_exact}",
                (r_is_zero == bool(is_zero_exact)))
        verdicts.append(bool(is_zero_exact))

    # Verdict step: P (all True) or O (any False) -- recorded, NOT asserted to a value.
    verdict = "P (COHERENT TRANSPORT)" if all(verdicts) else "O (AMBIENT-TRANSPORT OBSTRUCTION)"
    print(f"      >>> DECISIVE VERDICT (direct residual route): {verdict}")
    print(f"          per-pair is_zero_exact = {verdicts}")
    # No assert on the value of `verdict`: both P and O are valid scientific outcomes.


# ============================================================
# (E) Slice-internal TRIVIAL control (exact)
# ============================================================

def check_E_slice_internal_control():
    print("\n=== (E) Slice-internal TRIVIAL control (exact) -- NOT the decisive test ===")

    leakage_zero, assoc_zero = V.slice_internal_control()
    _report("CONTROL: slice-internal sqrt(a) b sqrt(a) stays in A "
            "(E(.) == ., leakage EXACTLY 0) for a,b in A",
            leakage_zero)
    _report("CONTROL: slice-internal triple associator EXACTLY 0 "
            "(A is a closed associative subalgebra)",
            assoc_zero)
    print("      (This is the documented TRIVIAL control; the decisive test is (D).)")


# ============================================================
# (F) Independent Peirce/grade cross-check (exact)
# ============================================================

def check_F_peirce_crosscheck():
    print("\n=== (F) Independent Peirce/grade cross-check (exact) ===")

    pairs = V.decisive_test_pairs()
    for idx, (X, Y) in enumerate(pairs):
        # direct verdict
        _R, is_zero_direct = V.compute_ambient_transport_residual(X, Y)
        # independent Peirce/grade-component verdict (decompose defect into C_u vs e_1..e_6
        # / Peirce grades V_0/V_{1/2}/V_1 at E_11); RAISES internally on a split decision.
        is_zero_peirce = V.peirce_grade_residual_is_zero(X, Y)
        _report(f"  pair {idx}: Peirce/grade route AGREES with direct residual "
                f"(both {'zero' if is_zero_direct else 'nonzero'})",
                bool(is_zero_peirce) == bool(is_zero_direct))


# ============================================================
# (G) No-pytest / runnable check
# ============================================================

def check_G_no_pytest():
    print("\n=== (G) No-pytest / runnable check ===")

    code_path = os.path.join(_CODE, "embedding_under_E_verification.py")
    test_path = os.path.abspath(__file__)
    # Build the forbidden needle from parts so this very source file does not
    # literally contain it (avoids a false self-trip on the search line).
    needle = "import" + " " + "pytest"
    no_pytest = True
    for p in (code_path, test_path):
        with open(p, "r") as f:
            src = f.read()
        if needle in src:
            no_pytest = False
    _report("no pytest import in code/embedding_under_E_verification.py "
            "or tests/test_embedding_under_E.py (assert-based harness)",
            no_pytest)


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 70)
    print("VALD-62-01: AMBIENT E-TRANSPORT residual on the NON-ASSOCIATIVE h_3(O)")
    print("            R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX), generic X,Y")
    print("            (slice-internal case = TRIVIAL control; EXACT arithmetic)")
    print("=" * 70)

    check_A_E_properties()
    check_B_ambient_sqrt()
    check_C_nonassociativity_load_bearing()
    check_D_decisive_residual()
    check_E_slice_internal_control()
    check_F_peirce_crosscheck()
    check_G_no_pytest()

    print("\n" + "=" * 70)
    if ALL_PASS:
        print("OVERALL: ALL SELF-CHECKS PASS")
        print("  (The decisive P/O verdict is printed above; BOTH are valid outcomes.")
        print("   The harness asserts CONSISTENCY + non-associativity load-bearing,")
        print("   NOT a forced verdict. See code/embedding_under_E_verification.py main()")
        print("   for the verdict and its characterization.)")
    else:
        print("OVERALL: SOME SELF-CHECKS FAILED")
        print("  A failure here is a self-check/consistency failure (sqrt^2 != X,")
        print("  E not idempotent, routes disagree, associator zero on decisive data),")
        print("  NOT merely an O verdict. Resolve before reading the verdict.")
    print("=" * 70)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
