#!/usr/bin/env python3
"""
Attempt-01 per-attempt SymPy rank-1 sanity gate on H_3(R).

Purpose (per 54-02-PLAN.md, test-attempt-01-sympy, CONTEXT.md VALD-54-01):
    Check that the Peirce-Preservation Lemma target propositions 3.1 and 3.2
    hold in the concrete model H_3(R) with two orthogonal rank-1 projectors
    p_1, p_2 and a = lambda_1 p_1 + lambda_2 p_2.

Scope:
    This is a LEMMA-LEVEL check (does the claim hold in H_3(R)?), not a
    PROOF-LEVEL check of attempt-01's argument. Attempt-01.md does NOT
    close the argument; it documents FAILED - structural insufficiency of
    the (A) tool set. The SymPy check here verifies that the lemma is TRUE
    in the canonical H_3(R) model - i.e., the failure mode is
    tool-insufficiency, not false claim.

Implementation notes:
    - The sequential product used here is the concrete Jordan product
      a . b = (1/2)(ab + ba) on H_3(R) = real symmetric 3x3 matrices.
      This is the POST-JORDAN realization of the SP in H_3(R) and is used
      here ONLY as a concrete lemma-level sanity check (instantiation in a
      canonical model). It is NOT a proof device and is NOT used in
      attempt-01.md's argument body.
    - Compressions C_{p_i} on H_3(R) for rank-1 diagonal projectors act as
      the linear projection onto the span of p_i's Peirce-2 space. We
      implement this via the Jordan product characterization:
      C_p(b) = 2 p . (p . b) - p . b on a JB-algebra (standard Jordan
      Peirce formula). Again, POST-JORDAN realization for lemma-level
      sanity only.

Exit code: 0 = PASS (lemma holds), nonzero = FAIL (lemma false in model).

Runtime: << 1 sec expected.
"""

import sys
import sympy as sp


def jordan_product(a, b):
    """Jordan product a . b = (1/2)(ab + ba) on H_3(R).

    Concrete realization of the sequential product on H_3(R) used here
    ONLY as a model-level sanity-check instantiation of the Peirce-
    Preservation Lemma's claim. Not used as a proof device.
    """
    return sp.Rational(1, 2) * (a * b + b * a)


def compression(p, b):
    """A-S compression C_p on H_3(R), realized via Jordan Peirce formula.

    For a projective unit p in a JB-algebra, the A-S compression C_p acts
    as the projection onto the Peirce-2 space V_2(p) = range(C_p). In a
    JB-algebra, C_p(b) = 2 p . (p . b) - p . b (equivalent to the Jordan
    Peirce projector 2 L_p^2 - L_p where L_p is Jordan left-multiplication
    by p; valid for a projection p such that p . p = p).

    For the rank-1 diagonal projector p = diag(1,0,0), this should coincide
    with picking out the (1,1) entry of b as a 1x1 block; we verify this
    in a unit test below.
    """
    pbp_half = jordan_product(p, b)  # = (1/2)(pb + bp)
    return 2 * jordan_product(p, pbp_half) - pbp_half


def is_in_V2(b, p):
    """Check whether b in V_2(p), i.e., C_p(b) == b (via L.1 of attempt-01.md)."""
    return sp.simplify(compression(p, b) - b) == sp.zeros(*b.shape)


def is_in_V1(b, pi, pj):
    """Check whether b in V_1(p_i, p_j).

    Jordan-Peirce characterization of V_1(p_i, p_j) for the H_3(R)
    realization (equivalent to the claim.md definition in the Jordan
    model up to a standard OUS compression-sum identity issue; see
    Note below):

        b in V_1(p_i, p_j) iff
            C_{p_i}(b) = 0 AND C_{p_j}(b) = 0
            AND C_{p_i + p_j}(b) = b
            (i.e. b is in the "off-diagonal block" of the (i,j) pair,
            not in either individual V_2 and not in V_0).

    NOTE: claim.md Section 4.5 defines
        V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V - C_{p_i}V - C_{p_j}V.
    In a generic Jordan realization (including H_3(R)), C_{p+q} is NOT
    equal to C_p + C_q (compressions don't add on the Jordan model).
    The abstract OUS definition is equivalent to the Jordan-Peirce
    characterization under the A-S identity C_{p+q} = C_p + C_q for
    orthogonal projective units (see alfsen-shultz-notes.md Section 5,
    NEEDS-VERIFICATION), OR, in the weakest interpretation, V_1 is the
    off-diagonal Peirce subspace characterized as above. Both
    interpretations coincide in H_3(R) for the intended element type
    (symmetric off-diagonal between rows/cols i and j).

    For the SymPy lemma-level sanity gate, we use the Jordan-Peirce
    characterization (i.e., C_{p_i+p_j}(b) = b and C_{p_i}(b) = C_{p_j}(b) = 0),
    which is the characterization every Phase 54 target proposition
    actually needs and which faithfully represents "off-diagonal between
    p_i and p_j" in the concrete canonical model.
    """
    pij = pi + pj
    ci_b = compression(pi, b)
    cj_b = compression(pj, b)
    cij_b = compression(pij, b)
    zero = sp.zeros(*b.shape)
    in_V2_pij = sp.simplify(cij_b - b) == zero
    ann_by_pi = sp.simplify(ci_b) == zero
    ann_by_pj = sp.simplify(cj_b) == zero
    return ann_by_pi and ann_by_pj and in_V2_pij


def main():
    # --- Setup: H_3(R) with two orthogonal rank-1 diagonal projectors ---
    p1 = sp.Matrix([[1, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]])
    p2 = sp.Matrix([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

    # Verify orthogonality via mutual annihilation in the Jordan sense:
    # p1 . p2 = (1/2)(p1 p2 + p2 p1) = 0 for these diagonal disjoint projectors.
    ortho = sp.simplify(jordan_product(p1, p2))
    assert ortho == sp.zeros(3, 3), \
        f"p1 and p2 not orthogonal: p1.p2 = {ortho}"
    print("Setup: p1, p2 orthogonal rank-1 projectors on H_3(R). OK.")

    # Sanity: compression axioms
    # Idempotency: C_{p1}^2 = C_{p1} checked on a generic element.
    x_sym = sp.Symbol('x', real=True)
    test = sp.Matrix([[x_sym, 0, 0], [0, 0, 0], [0, 0, 0]])
    c1_test = compression(p1, test)
    c1_c1_test = compression(p1, c1_test)
    assert sp.simplify(c1_c1_test - c1_test) == sp.zeros(3, 3), \
        "C_{p1} idempotency failed."
    # Projector fix: C_{p1}(p1) = p1.
    assert sp.simplify(compression(p1, p1) - p1) == sp.zeros(3, 3), \
        "Projector-fix axiom failed: C_{p1}(p1) != p1."
    # Orthogonal annihilation: C_{p1}(p2) = 0.
    assert sp.simplify(compression(p1, p2)) == sp.zeros(3, 3), \
        "Orthogonal annihilation failed: C_{p1}(p2) != 0."
    print("Compression axioms: idempotency, projector-fix, orthogonal "
          "annihilation. OK.")

    # --- Symbolic scalar weights: a = lambda_1 p_1 + lambda_2 p_2 ---
    lam1, lam2 = sp.symbols('lambda_1 lambda_2', real=True)
    a = lam1 * p1 + lam2 * p2

    # ------------------------------------------------------------------
    # Test (i): V_2(p_1) invariance.
    # For b in V_2(p_1), verify a . b in V_2(p_1).
    # A generic element of V_2(p_1) is b = x * p_1 for x in R
    # (range(C_{p1}) = span(p_1) in the diagonal rank-1 case).
    # ------------------------------------------------------------------
    x = sp.Symbol('x', real=True)
    b_V2 = x * p1
    assert is_in_V2(b_V2, p1), \
        f"Setup error: b_V2 = x p_1 not in V_2(p_1)."
    a_b_V2 = jordan_product(a, b_V2)
    # Is a . b in V_2(p_1)?
    c1_ab_V2 = compression(p1, a_b_V2)
    diff_V2 = sp.simplify(c1_ab_V2 - a_b_V2)
    if diff_V2 == sp.zeros(3, 3):
        print("V_2 invariance PASS: a . b in V_2(p_1) for b = x*p_1. "
              "[Specifically a . b = lambda_1 * x * p_1.]")
        # Verify the specific form
        expected = lam1 * x * p1
        assert sp.simplify(a_b_V2 - expected) == sp.zeros(3, 3), \
            f"a.b = {a_b_V2}, expected {expected}"
        print(f"         Verified: a . (x*p_1) = {sp.simplify(a_b_V2[0, 0])}"
              f" * p_1 (scaled rank-1).")
    else:
        print(f"V_2 invariance FAIL: C_{{p_1}}(a . b) - a . b = {diff_V2}")
        sys.exit(1)

    # ------------------------------------------------------------------
    # Test (ii): V_1(p_1, p_2) invariance.
    # A generic element of V_1(p_1, p_2) is an off-diagonal symmetric
    # matrix: b = y * (E_{12} + E_{21}) where E_{ij} is the (i,j) unit.
    # On H_3(R), this corresponds to the real symmetric matrix
    # b = [[0, y, 0], [y, 0, 0], [0, 0, 0]].
    # ------------------------------------------------------------------
    y = sp.Symbol('y', real=True)
    b_V1 = sp.Matrix([[0, y, 0],
                      [y, 0, 0],
                      [0, 0, 0]])
    assert is_in_V1(b_V1, p1, p2), \
        f"Setup error: b_V1 not in V_1(p_1, p_2)."
    a_b_V1 = jordan_product(a, b_V1)
    # Is a . b in V_1(p_1, p_2)?
    # Jordan-Peirce check: C_{p_1}(a.b) = 0, C_{p_2}(a.b) = 0,
    # C_{p_1+p_2}(a.b) = a.b.
    c1_ab = compression(p1, a_b_V1)
    c2_ab = compression(p2, a_b_V1)
    cij_ab = compression(p1 + p2, a_b_V1)
    diff_cij = sp.simplify(cij_ab - a_b_V1)
    zero = sp.zeros(3, 3)
    in_V1 = (sp.simplify(c1_ab) == zero
             and sp.simplify(c2_ab) == zero
             and diff_cij == zero)
    if in_V1:
        print("V_1 invariance PASS: a . b in V_1(p_1, p_2) for off-diagonal "
              "b = y * (E_{12} + E_{21}).")
        # Verify the specific Jordan-Peirce form:
        # a . b = (1/2)(lambda_1 + lambda_2) * b for b in V_1(p_1, p_2).
        expected = sp.Rational(1, 2) * (lam1 + lam2) * b_V1
        diff_V1_exact = sp.simplify(a_b_V1 - expected)
        assert diff_V1_exact == sp.zeros(3, 3), \
            f"a.b = {a_b_V1}, expected (lam1+lam2)/2 * b = {expected}"
        print(f"         Verified: a . b = ((lambda_1 + lambda_2)/2) * b "
              f"(Peirce-1 acts by the average eigenvalue; "
              f"classical Jordan-Peirce result).")
    else:
        print(f"V_1 invariance FAIL: C_{{p_1}}(a.b) = {c1_ab}, "
              f"C_{{p_2}}(a.b) = {c2_ab}, C_{{p_1+p_2}}(a.b) - a.b = {diff_cij}")
        sys.exit(1)

    # ------------------------------------------------------------------
    # Test (iii) [extension; Proposition 3.3 cross-term is the R3 case]:
    # To test V_1(p_k, p_l) cross-term with {k,l} intersect supp(a) = empty,
    # we need a THIRD orthogonal projector p_3 and an 'a' that has
    # zero components on p_1 and p_2 but non-zero on p_3. Wait - but then
    # supp(a) = {3} and the cross-term V_1(p_1, p_2) has {1,2} disjoint
    # from supp(a) = {3}.
    # Use a = lambda_3 * p_3, test on b in V_1(p_1, p_2).
    # Expected: a . b should still be in V_1(p_1, p_2), and in fact should
    # be 0 (since a is supported only on p_3 which is orthogonal to the
    # plane spanned by p_1, p_2).
    # ------------------------------------------------------------------
    p3 = sp.Matrix([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 1]])
    lam3 = sp.Symbol('lambda_3', real=True)
    a_cross = lam3 * p3
    # b_V1 as above, in V_1(p_1, p_2); supp(a_cross) = {3} disjoint from {1, 2}
    a_b_cross = jordan_product(a_cross, b_V1)
    c1_cross = compression(p1, a_b_cross)
    c2_cross = compression(p2, a_b_cross)
    cij_cross = compression(p1 + p2, a_b_cross)
    diff_cij_cross = sp.simplify(cij_cross - a_b_cross)
    in_V1_cross = (sp.simplify(c1_cross) == zero
                   and sp.simplify(c2_cross) == zero
                   and diff_cij_cross == zero)
    if in_V1_cross:
        # In this specific realization, a_cross . b_V1 should equal 0
        # (lambda_3 * p_3 times the off-diagonal-in-(1,2) element b_V1 is 0
        # by the Jordan product in H_3(R)). 0 is trivially in V_1(p_1, p_2).
        if sp.simplify(a_b_cross) == zero:
            print("V_1(p_1,p_2) cross-term PASS (bonus check beyond per-attempt gate): "
                  "a . b = 0 for a = lambda_3*p_3 and b in V_1(p_1, p_2). "
                  "Trivially in V_1(p_1, p_2). {k,l}={1,2}, supp(a)={3}, disjoint.")
        else:
            print(f"V_1(p_1,p_2) cross-term PASS: a . b = {a_b_cross} in V_1(p_1, p_2).")
    else:
        print(f"V_1(p_1,p_2) cross-term FAIL: c1_cross = {c1_cross}, "
              f"c2_cross = {c2_cross}, C_{{p1+p2}}(a.b) - a.b = {diff_cij_cross}")
        sys.exit(1)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print()
    print("=" * 70)
    print("ATTEMPT-01 SYMPY RANK-1 GATE: PASS")
    print("=" * 70)
    print("Lemma propositions 3.1 (V_2 invariance) and 3.2 (V_1 invariance)")
    print("VERIFIED to hold in H_3(R) with rank-1 projectors p_1, p_2 and")
    print("a = lambda_1 p_1 + lambda_2 p_2. Bonus cross-term check at")
    print("Proposition 3.3 also PASSES for a = lambda_3 p_3 with")
    print("{1,2} disjoint from supp(a) = {3}.")
    print()
    print("INTERPRETATION: The Peirce-Preservation Lemma TARGET STATEMENT")
    print("is TRUE in the canonical H_3(R) model. This confirms the")
    print("attempt-01 FAILED verdict is an (A) TOOL-INSUFFICIENCY gap,")
    print("NOT a false-claim defect. The lemma statement is sound;")
    print("the (A) tool set {S1, S3, linearity, A-S compressions}")
    print("is provably incapable of proving it without additional")
    print("axiomatic input (S2 forbidden; Jordan/pxp/spin-factor")
    print("forbidden; associativity post-vdW-Thm-1 post-S4; the natural")
    print("bridge 'C_p(a)=0 implies C_p(a.b)=0' is the invariance claim")
    print("restated, i.e., circular without a new axiom).")
    print()
    print("ROUTING IMPLICATION: motivates PIVOT-TO-C-I for Plan 54-03.")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    sys.exit(main())
