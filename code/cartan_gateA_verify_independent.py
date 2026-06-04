#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# v19.0 GATE A -- INDEPENDENT RATIFICATION of the verdict `fp-no-intrinsic-orientation`
# ============================================================================
#
# This is a BLOCKING ratification gate (gpd-verifier). It does NOT re-run the
# driver under audit (code/cartan_gateA_orientation.py). It re-derives the SAME
# kill by GENUINELY INDEPENDENT constructions / code paths, exact over Q, so that
# agreement is real cross-validation rather than a re-run:
#
#   (a) CONSTRUCTION-INDEPENDENT FACT.  A (1,3) Lorentzian 4-metric admits NO
#       eta-compatible almost-complex structure J (J^2 = -I_4 AND J in so(3,1)).
#       INDEPENDENT METHOD (different from the driver's parity prose): parametrize
#       a GENERAL so(3,1) element with 6 rational unknowns, impose J^2 + I_4 = 0,
#       and show the polynomial system is INCONSISTENT over R (sympy solve =>
#       EMPTY) AND exhibit an explicit sign-clash witness: the diagonal of J^2 is
#         J^2 = diag(a^2+b^2+c^2,  a^2-d^2-e^2,  b^2-d^2-f^2,  c^2-e^2-f^2),
#       so J^2[1,1]-J^2[0,0] = -(b^2+c^2+d^2+e^2) <= 0 can never be 0 unless
#       b=c=d=e=0, which then forces J^2[0,0]=a^2=-1: impossible over R.  Holds no
#       matter how J is built from u (it is a property of the (1,3) signature).
#
#   (b) u-SPECIFIC CONSTRUCTION (DIFFERENT route than the audited driver).  The
#       driver builds J by left-multiplying EVERY octonion entry of the 3x3 matrix
#       by u=e_7 (entrywise oct_mul) and reading slice coords.  HERE we instead use
#       the M_2(C_u) ~ M_2(C) representation of the spacetime slice h_2(C_u):
#         slice element  [[beta, conj(x1)],[x1, gamma]],  x1 = p + q e_7 in C_u,
#       map e_7 -> i, and act by the C_u imaginary unit i on the 2x2 COMPLEX matrix
#       (scalar mult by i*I_2), then project back onto the (real-diagonal,
#       C_u-off-diagonal) slice.  i*beta, i*gamma leave the real diagonal (the
#       "diagonal leak"); the off-diagonal x1 -> i*x1 rotates (p,q).  Result:
#       J^2 = diag(0,-1,-1,0) in Minkowski coords (rank 2), Kahler form degenerate
#       (Pfaffian = 0) => no volume form => Phase-78 clause C2 NOT repaired.
#       Triangulated with a RIGHT-mult M_2(C) variant and a from-scratch hand-rolled
#       octonion left-mult (NOT the driver); all three u-faithful routes agree.
#
#   (c) TRIANGULATION.  On the Euclidean (4,0) V_{1/2} C_u^2 FOIL {11,18,19,26},
#       u DOES give a genuine compatible J (J^2 = -I_4) and the Kahler Pfaffian is
#       NONzero (= 4) -- so u orients the INTERNAL/Euclidean OP^2 foil, the WRONG
#       space.
#
#   (d) SOURCE GUARD.  octonion_algebra.py NOT imported on the decisive path; no
#       numpy / no float on any decisive path; det SSOT exact (det_3(diag(2,3,5))
#       == 30 exact int); u*u = -1, u*1 = u via the Fano oct_mul.  All ranks /
#       eigenvalues via sympy over QQ.
#
# EXIT 0 iff the KILL is REPRODUCED (all of (a)-(d) hold with the kill structure);
# nonzero otherwise (=> do NOT ratify).
#
# Imports ONLY the warm exact-Q primitives (oct_mul / proj_u / E / Tr / jordan /
# det_3 / the 27-coord layout); builds J by a DIFFERENT route than the driver.
# ============================================================================

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import (Matrix, Rational, eye, zeros, simplify, symbols, I as symI,
                   re as sym_re, im as sym_im, solve, Eq, expand)  # noqa: E402

import embedding_under_E_verification as EMB  # noqa: E402  (oct_mul, proj_u, E, h3o_from_coords)
import ring_lemma_verification as RL          # noqa: E402  (det SSOT: Tr, jordan, det_3)
import bulk_geometry_verification as BG       # noqa: E402  (27-coord layout, _standard_basis_27)

# ----- slice layout (engine-native; bulk_geometry_verification Section 4) ----
# 27-coords [alpha 0; beta 1; gamma 2; x1 3..10; x2 11..18; x3 19..26].
# spacetime slice h_2(C_u) = {1,2,3,10} = {beta, gamma, p=Re(x1), q=<x1,e7>}.
# (CONVENTIONS.md still labels this {17,18,19,26} from the v17.0 Peirce naming;
#  the LIVE engine-native set is {1,2,3,10} -- used by the driver and the spec.
#  Documentation lag only; the index SET is unambiguous from the layout.)
CU4_IDX = [1, 2, 3, 10]                    # beta, gamma, p, q
CU_SURVIVOR_IDX = [11, 18, 19, 26]         # V_{1/2} C_u^2 foil: Re(x2),<x2,e7>,Re(x3),<x3,e7>
ETA_MINK = Matrix.diag(1, -1, -1, -1)      # mostly-minus (1,3); order (x0,x1,x2,x3)
# raw {beta,gamma,p,q} -> Minkowski {x0,x1,x2,x3}: x0=(b+g)/2, x1=p, x2=q, x3=(b-g)/2
RAW_TO_MINK = Matrix([[Rational(1, 2), Rational(1, 2), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1],
                      [Rational(1, 2), Rational(-1, 2), 0, 0]])

ALL_PASS = True
KILL_REPRODUCED = True   # latched False if any kill-structural clause fails to reproduce


def _report(label, ok, kill=False):
    global ALL_PASS, KILL_REPRODUCED
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
        if kill:
            KILL_REPRODUCED = False
    return ok


def _signature(M):
    """(n_pos, n_neg, n_zero) of a symmetric rational Matrix, EXACT over Q (sympy)."""
    ev = M.eigenvals()
    return (sum(m for v, m in ev.items() if v > 0),
            sum(m for v, m in ev.items() if v < 0),
            sum(m for v, m in ev.items() if v == 0))


def _pfaffian4(O):
    """Pfaffian of a 4x4 antisymmetric matrix; (omega ^ omega) = 2 Pf(O) vol.
    Pf = O_01 O_23 - O_02 O_13 + O_03 O_12."""
    return O[0, 1] * O[2, 3] - O[0, 2] * O[1, 3] + O[0, 3] * O[1, 2]


def _u_oct():
    u = EMB.oct_zero(); u[7] = Rational(1); return u


# ============================================================================
# (d) SOURCE GUARD  (run first; gates everything)
# ============================================================================
def source_guard():
    print("=" * 78)
    print("(d) SOURCE GUARD: octonion_algebra ABSENT; exact over Q; det SSOT; u^2=-1")
    print("=" * 78)
    in_modules = "octonion_algebra" in sys.modules
    numpy_here = "numpy" in sys.modules
    # det SSOT spot check (exact integer, not float).
    Xspot = EMB.h3o_from_coords(2, 3, 5, EMB.oct_zero(), EMB.oct_zero(), EMB.oct_zero())
    spot = RL.det_3(Xspot)
    spot_exact = (spot == 30) and (not isinstance(spot, float))
    # u = e_7 complex structure: u*u = -1, u*1 = u (exact via the Fano oct_mul).
    u = _u_oct()
    one = EMB.oct_zero(); one[0] = Rational(1)
    uu = EMB.oct_mul(u, u)
    u1 = EMB.oct_mul(u, one)
    uu_is_minus1 = (uu[0] == -1 and all(uu[k] == 0 for k in range(1, 8)))
    u1_is_u = (u1[7] == 1 and u1[0] == 0 and all(u1[k] == 0 for k in (1, 2, 3, 4, 5, 6)))
    _report("octonion_algebra NOT in sys.modules; numpy NOT on the decisive path",
            (not in_modules) and (not numpy_here))
    _report(f"det SSOT exact: RL.det_3(diag(2,3,5)) == {spot} (exact integer, not float)",
            spot_exact)
    _report(f"u = e_7 complex structure (EXACT Fano oct_mul): u*u == -1 ({uu_is_minus1}), "
            f"u*1 == u ({u1_is_u})", uu_is_minus1 and u1_is_u)
    # numpy purge note: bulk_geometry imports may transitively pull numpy; assert it
    # is NOT used on OUR decisive path by confirming all our matrices are sympy QQ.
    return (not in_modules) and (not numpy_here) and spot_exact and uu_is_minus1 and u1_is_u


# ============================================================================
# (a) CONSTRUCTION-INDEPENDENT FACT: (1,3) admits NO eta-compatible J (J^2=-I,
#     J in so(3,1)).  INDEPENDENT METHOD: solve the polynomial system over R.
# ============================================================================
def claim_a_no_eta_compatible_J():
    print("=" * 78)
    print("(a) (1,3) admits NO eta-compatible J: solve a GENERAL so(3,1) J, J^2=-I_4")
    print("    [method INDEPENDENT of the parity prose AND of u's construction]")
    print("=" * 78)
    # General element of so(3,1) for eta = diag(1,-1,-1,-1): J^T eta + eta J = 0
    # <=> eta J antisymmetric.  Parametrize eta*J = antisymmetric A (6 params), so
    # J = eta^{-1} A = eta A (eta^2 = I).  6 unknowns a..f over Q.
    a, b, c, d, e, f = symbols('a b c d e f', real=True)
    A = Matrix([[0,  a,  b,  c],
                [-a, 0,  d,  e],
                [-b, -d, 0,  f],
                [-c, -e, -f, 0]])           # general antisymmetric 4x4
    J = ETA_MINK * A                          # J in so(3,1): J = eta * (antisym)
    eta_skew_ok = (simplify(J.T * ETA_MINK + ETA_MINK * J) == zeros(4, 4))
    _report("parametrized J = eta * A (A antisymmetric) is eta-skew (J in so(3,1)) "
            "by construction [exact Q]", eta_skew_ok)

    J2 = expand(J * J)
    # Impose J^2 = -I_4: 16 polynomial equations.
    eqs = []
    for i in range(4):
        for j in range(4):
            target = Rational(-1) if i == j else Rational(0)
            eqs.append(Eq(expand(J2[i, j]), target))
    # Independent route 1: sympy solve over the reals -> must be EMPTY (no solution).
    sol = solve(eqs, [a, b, c, d, e, f], dict=True)
    real_sol = []
    for s in sol:
        ok_real = True
        for v in (a, b, c, d, e, f):
            val = s.get(v, None)
            if val is not None and simplify(sym_im(val)) != 0:
                ok_real = False
                break
        if ok_real:
            real_sol.append(s)
    no_real_solution = (len(real_sol) == 0)
    print(f"      sympy solve(J^2 = -I_4 | J in so(3,1)) real solutions: {len(real_sol)} "
          f"(total branches {len(sol)})")
    _report("NO real so(3,1) J satisfies J^2 = -I_4 (solution set EMPTY over R) "
            "[INDEPENDENT polynomial-system route]", no_real_solution)

    # Independent route 2: explicit sign-clash WITNESS from the diagonal of J^2.
    j00 = expand(J2[0, 0]); j11 = expand(J2[1, 1])
    j22 = expand(J2[2, 2]); j33 = expand(J2[3, 3])
    print(f"      J^2 diagonal = [{j00}, {j11}, {j22}, {j33}]")
    diff_11_00 = expand(j11 - j00)
    # J^2[0,0] = a^2+b^2+c^2 (>=0);  J^2[1,1]-J^2[0,0] = -(b^2+c^2+d^2+e^2) (<=0).
    # Both forced to -1 => their difference forced to 0 => b=c=d=e=0 => J^2[0,0]=a^2,
    # forced =-1 => a^2=-1, impossible over R.  Witness = the SOS sign clash.
    witness_sign_clash = (expand(j00 - (a**2 + b**2 + c**2)) == 0
                          and expand(diff_11_00 + (b**2 + c**2 + d**2 + e**2)) == 0)
    print(f"      WITNESS: J^2[0,0] = a^2+b^2+c^2 >= 0 forced to -1, while "
          f"J^2[1,1]-J^2[0,0] = {diff_11_00} <= 0 forced to 0")
    print("               => b=c=d=e=0 => J^2[0,0]=a^2 forced =-1 => impossible over R")
    _report("SOS sign-clash witness confirms the EMPTY solution set (timelike + vs "
            "spacelike - parity) [exact Q]", witness_sign_clash)
    witness_ok = (no_real_solution and eta_skew_ok and witness_sign_clash)
    _report("(a) VERDICT: a (1,3) metric admits NO eta-compatible complex structure "
            "(J^2=-I_4 & J in so(3,1)) -- CONSTRUCTION-INDEPENDENT, exact over Q",
            witness_ok, kill=True)
    return witness_ok


# ============================================================================
# (b) u-SPECIFIC J via the M_2(C_u) representation (DIFFERENT route than driver).
# ============================================================================
def _slice_to_2x2_complex(beta, gamma, p, q):
    """h_2(C_u) slice element as a 2x2 Hermitian COMPLEX matrix (e_7 -> i):
        [[beta,        p - q i],
         [p + q i,     gamma  ]]
    (off-diagonal x1 = p + q e_7; the (2,1) entry is x1, (1,2) is conj(x1))."""
    return Matrix([[beta, p - q * symI],
                   [p + q * symI, gamma]])


def _2x2_complex_to_slice(M):
    """Read a 2x2 complex matrix back into slice coords (beta,gamma,p,q):
        beta = Re M[0,0], gamma = Re M[1,1], p = Re M[1,0], q = Im M[1,0].
    Only the (real-diagonal, C_u-off-diagonal) slice part is read; an imaginary
    diagonal (e.g. i*beta) has NO real-diagonal coordinate and reads 0 -- this is
    the FORCED 'diagonal leak' (u carrying the diagonal OUT of the slice), NOT a
    discretionary projection."""
    return [simplify(sym_re(M[0, 0])), simplify(sym_re(M[1, 1])),
            simplify(sym_re(M[1, 0])), simplify(sym_im(M[1, 0]))]


def build_J_via_M2C(side="left"):
    """Build J on {beta,gamma,p,q} by acting on the 2x2 COMPLEX representation of
    h_2(C_u) with the C_u imaginary unit i.  side='left' => i*I_2 . M ; 'right'
    => M . i*I_2 ; 'offdiag_keepdiag' => multiply ONLY the off-diagonal complex
    entry by i and LEAVE the real diagonal as-is (this is NOT u's action -- it is
    the fp-imported-orientation contrast operator).  Column k = slice-coords of the
    action on basis_k.  A DIFFERENT code path than the driver's entrywise oct_mul."""
    iI = symI * eye(2)
    basis = {"beta": (1, 0, 0, 0), "gamma": (0, 1, 0, 0),
             "p": (0, 0, 1, 0), "q": (0, 0, 0, 1)}
    cols = []
    for name in ("beta", "gamma", "p", "q"):
        bb, gg, pp, qq = basis[name]
        M = _slice_to_2x2_complex(Rational(bb), Rational(gg), Rational(pp), Rational(qq))
        if side == "left":
            MM = iI * M
        elif side == "right":
            MM = M * iI
        elif side == "offdiag_keepdiag":
            MM = Matrix([[M[0, 0], symI * M[0, 1]],
                         [symI * M[1, 0], M[1, 1]]])
        else:
            raise ValueError(side)
        cols.append(_2x2_complex_to_slice(MM))
    J_raw = Matrix(4, 4, lambda i, j: cols[j][i])
    J_mink = RAW_TO_MINK * J_raw * RAW_TO_MINK.inv()
    return J_raw, J_mink


def build_J_via_handrolled_oct_leftmult():
    """A SECOND independent (non-driver) route in the octonion algebra, written from
    scratch HERE (NOT importing cartan_gateA_orientation): act on the lower-right
    2x2-block entries by LEFT octonion mult by u=e_7, read slice coords by hand.
    Triangulates against the M_2(C) route."""
    u = _u_oct()

    def oct_of(p, q):
        o = EMB.oct_zero(); o[0] = p; o[7] = q; return o

    cols = []
    for (bb, gg, pp, qq) in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]:
        beta_o = EMB.oct_zero(); beta_o[0] = Rational(bb)
        gamma_o = EMB.oct_zero(); gamma_o[0] = Rational(gg)
        x1_o = oct_of(Rational(pp), Rational(qq))
        # u * (diagonal real r) = r e_7 -> NO comp-0 -> contributes 0 to beta',gamma'
        ubeta = EMB.oct_mul(u, beta_o)
        ugamma = EMB.oct_mul(u, gamma_o)
        ux1 = EMB.oct_mul(u, x1_o)
        cols.append([ubeta[0], ugamma[0], ux1[0], ux1[7]])
    J_raw = Matrix(4, 4, lambda i, j: cols[j][i])
    J_mink = RAW_TO_MINK * J_raw * RAW_TO_MINK.inv()
    return J_raw, J_mink


def claim_b_u_specific():
    print("=" * 78)
    print("(b) u-induced J on the (1,3) slice via the M_2(C_u) representation "
          "[DIFFERENT route]")
    print("=" * 78)
    expected = Matrix.diag(0, -1, -1, 0)   # the expected J^2 (Minkowski) under the kill

    # Primary independent route: M_2(C), left scalar mult by i.
    J_raw_L, J_mink_L = build_J_via_M2C("left")
    print(f"      [M2C left]  J (raw {{beta,gamma,p,q}}) = {J_raw_L.tolist()}")
    print(f"      [M2C left]  J (Minkowski {{x0,x1,x2,x3}}) = {J_mink_L.tolist()}")

    J2_raw = simplify(J_raw_L * J_raw_L)
    J2_mink = simplify(J_mink_L * J_mink_L)
    rankJ = J_raw_L.rank()
    is_minus_I = (J2_raw == -eye(4))
    print(f"      [M2C left]  J^2 (Minkowski) = diag {[J2_mink[i, i] for i in range(4)]} "
          f"(order x0,x1,x2,x3); rank(J) = {rankJ}")
    _report("J^2 != -I_4 on the (1,3) slice (u is NOT an almost-complex structure "
            f"there) [exact Q].  J^2 {'==' if is_minus_I else '!='} -I_4",
            not is_minus_I, kill=True)

    j2_is_expected = (J2_mink == expected)
    print(f"      expected J^2 (Minkowski) = diag(0,-1,-1,0): match = {j2_is_expected}")
    spatial = (J2_mink[1, 1] == -1 and J2_mink[2, 2] == -1)
    frozen = (J2_mink[0, 0] == 0 and J2_mink[3, 3] == 0)
    _report("STRUCTURE: J^2 = diag(0,-1,-1,0) -- u complexifies ONLY the {x1,x2} "
            "purely-spatial plane; the {x0,x3} timelike/diagonal plane is FROZEN "
            "(rank J = 2) [exact Q]",
            j2_is_expected and spatial and frozen and rankJ == 2, kill=True)

    # diagonal-leak witness in the M_2(C) picture
    Mbeta = _slice_to_2x2_complex(Rational(1), 0, 0, 0)
    iMbeta = symI * eye(2) * Mbeta
    leak = _2x2_complex_to_slice(iMbeta)
    leak_ok = (leak == [0, 0, 0, 0])
    print(f"      i * (beta diagonal) reads slice-coords {leak} (= 0: i*beta has no "
          f"real-diagonal coordinate -> the timelike/diagonal plane has NO u-action)")
    _report("DIAGONAL LEAK (M2C route): u (=i) carries the real diagonal OUT of the "
            "slice; {x0,x3} timelike plane is u-frozen [exact Q]", leak_ok, kill=True)

    # eta-skewness of the constructed (rank-2) J (diagnostic; consistent with (a)).
    eta_skew = (simplify(J_mink_L.T * ETA_MINK + ETA_MINK * J_mink_L) == zeros(4, 4))
    _report("eta-COMPATIBILITY (diagnostic): the rank-2 J IS eta-skew (an so(2) "
            "spatial rotation in so(3,1)) -- but J^2 != -I, so NOT a complex "
            "structure; consistent with (a) [exact Q]", eta_skew)

    # --- TRIANGULATION: the three u-FAITHFUL routes must agree on the kill ---
    J_raw_R, J_mink_R = build_J_via_M2C("right")
    J_raw_H, J_mink_H = build_J_via_handrolled_oct_leftmult()
    J2_R = simplify(J_mink_R * J_mink_R)
    J2_H = simplify(J_mink_H * J_mink_H)
    agree_L = (J2_mink == expected)
    agree_R = (J2_R == expected)
    agree_H = (J2_H == expected)
    # the hand-rolled octonion J must EQUAL the M_2(C)-left J exactly (same operator)
    agree_H_raw = (simplify(J_raw_H) == simplify(J_raw_L))
    print(f"      triangulation J^2(Mink): left={'(0,-1,-1,0)' if agree_L else J2_mink.diagonal().tolist()}, "
          f"right={'(0,-1,-1,0)' if agree_R else J2_R.diagonal().tolist()}, "
          f"handrolled-oct={'(0,-1,-1,0)' if agree_H else J2_H.diagonal().tolist()} "
          f"(raw-J(handrolled) == raw-J(M2C-left): {agree_H_raw})")
    _report("TRIANGULATION: the THREE u-faithful routes (M_2(C)-left, M_2(C)-right, "
            "from-scratch octonion left-mult) ALL give J^2 = diag(0,-1,-1,0) (rank 2); "
            "hand-rolled octonion J == M_2(C)-left J exactly -- the kill is "
            "route-independent [exact Q]",
            agree_L and agree_R and agree_H and agree_H_raw, kill=True)

    # --- fp-imported-orientation GUARD: the only way to J^2=-I on the slice is to
    #     ADD a diagonal pairing that is NOT u's action.  The 'keep-diagonal' offdiag
    #     operator does exactly that -- and STILL fails J^2=-I -- so no u-intrinsic
    #     repair exists.
    J_raw_off, J_mink_off = build_J_via_M2C("offdiag_keepdiag")
    J2_off = simplify(J_mink_off * J_mink_off)
    off_is_acs = (J2_off == -eye(4))
    off_keeps_diag = (J_raw_off[0, 0] == 1 and J_raw_off[1, 1] == 1)
    print(f"      CONTRAST 'keep-diagonal' offdiag operator (NOT u: it keeps the real "
          f"diagonal): J^2(Mink) diag = {J2_off.diagonal().tolist()}, is -I_4: {off_is_acs}")
    _report("fp-imported-orientation GUARD: the 'keep-diagonal' operator is NOT u's "
            "action (it retains the diagonal, contradicting the leak) AND still fails "
            "J^2=-I_4 -- there is NO u-intrinsic repair of the kill [exact Q]",
            (not off_is_acs) and off_keeps_diag, kill=True)

    # --- A2: Kahler form omega_K = eta(J.,.) is DEGENERATE (Pf = 0) ---
    omega = ETA_MINK * J_mink_L
    omega_anti = simplify((omega - omega.T) * Rational(1, 2))
    pf = simplify(_pfaffian4(omega_anti))
    rk = omega_anti.rank()
    print(f"      omega_K (antisym part of eta J), Minkowski = {omega_anti.tolist()}")
    print(f"      rank(omega_K) = {rk};  Pf(omega_K) = {pf}  (omega^omega = 2 Pf vol)")
    _report("A2 KILL: omega_K is DEGENERATE (rank 2, Pf = 0) => omega_K ^ omega_K = 0 "
            "=> NO volume form from u on the (1,3) slice => Phase-78 clause C2 NOT "
            "repaired (orientation eps still by-hand) [exact Q]",
            pf == 0 and rk == 2, kill=True)
    return (not is_minus_I) and (pf == 0)


# ============================================================================
# (c) TRIANGULATION: u DOES orient the Euclidean (4,0) V_{1/2} C_u^2 FOIL.
# ============================================================================
def claim_c_foil():
    print("=" * 78)
    print("(c) TRIANGULATION: on the Euclidean (4,0) V_{1/2} C_u^2 FOIL {11,18,19,26}, "
          "u GIVES J^2=-I_4 (wrong space)")
    print("=" * 78)
    # Foil value space = two C_u lines (x2's {Re,e7} and x3's {Re,e7}); u acts as the
    # standard complex structure on EACH line.  Build via the M_2(C)/complex-line
    # route (e_7 -> i; multiply by i): on a single C_u line (Re,e7)=(s,t)<->s+ti,
    # i*(s+ti) = -t + s i -> (Re',e7') = (-t, s): the matrix [[0,-1],[1,0]].
    def cu_line_J_via_complex():
        cols = []
        for (s, t) in [(1, 0), (0, 1)]:   # basis (Re=1,e7=0) and (Re=0,e7=1)
            z = Rational(s) + Rational(t) * symI
            zz = symI * z
            cols.append([sym_re(zz), sym_im(zz)])
        return Matrix(2, 2, lambda i, j: cols[j][i])
    Jline = cu_line_J_via_complex()
    J_foil = zeros(4, 4)
    J_foil[0:2, 0:2] = Jline    # x2 C_u line {11,18}
    J_foil[2:4, 2:4] = Jline    # x3 C_u line {19,26}
    J2_foil = simplify(J_foil * J_foil)
    foil_minus_I = (J2_foil == -eye(4))
    print(f"      J on foil = {J_foil.tolist()};  J^2 == -I_4: {foil_minus_I}")
    _report("FOIL J^2 == -I_4: u IS a genuine complex structure on the V_{1/2} "
            "C_u^2 = C^2 value space [exact Q, M_2(C) route]", foil_minus_I, kill=True)

    # Foil metric = bare trace Gram on the 4 survivor directions (expect (4,0)).
    basis = BG._standard_basis_27()
    cof = [EMB.E(basis[k]) for k in CU_SURVIVOR_IDX]
    Gram = Matrix(4, 4, lambda i, j: RL.Tr(RL.jordan(cof[i], cof[j])))
    sig = _signature(Gram)
    print(f"      foil bare-trace Gram = {Gram.tolist()}")
    print(f"      foil metric signature (n+,n-,n0) = {sig} (expect (4,0) Euclidean)")
    # Kahler form on the foil is NON-degenerate (Pf != 0) => forced orientation HERE.
    omega_foil = Gram * J_foil
    omega_foil = simplify((omega_foil - omega_foil.T) * Rational(1, 2))
    pf_foil = simplify(_pfaffian4(omega_foil))
    print(f"      Pf(omega_K) on the foil = {pf_foil} (nonzero => orientation FORCED "
          f"on the foil)")
    _report("FOIL ORIENTATION FORCED but WRONG SPACE: foil metric (4,0) Euclidean, "
            "Pf(omega_K) != 0 => u orients the EUCLIDEAN OP^2 coframe-value foil, "
            "NOT the (1,3) spacetime slice [exact Q]",
            sig == (4, 0, 0) and pf_foil != 0, kill=True)
    return foil_minus_I and sig == (4, 0, 0) and pf_foil != 0


def main():
    print("#" * 78)
    print("# v19.0 GATE A -- INDEPENDENT RATIFICATION (does u orient the (1,3) slice?)")
    print("#   EXIT 0 iff the KILL `fp-no-intrinsic-orientation` is REPRODUCED by")
    print("#   genuinely independent constructions (NOT a re-run of the audited driver).")
    print("#" * 78)

    okG = source_guard()
    a_ok = claim_a_no_eta_compatible_J()
    b_ok = claim_b_u_specific()
    c_ok = claim_c_foil()

    print("=" * 78)
    print(f"(d) SOURCE GUARD .................................. {'PASS' if okG else 'FAIL'}")
    print(f"(a) (1,3) admits NO eta-compatible J (indep solve) {'PASS' if a_ok else 'FAIL'}")
    print(f"(b) u-J via M_2(C): J^2!=-I, Pf=0, kill structure  {'PASS' if b_ok else 'FAIL'}")
    print(f"(c) u orients the Euclidean (4,0) FOIL (wrong sp.) {'PASS' if c_ok else 'FAIL'}")
    print("-" * 78)
    reproduced = KILL_REPRODUCED and okG and a_ok and b_ok and c_ok and ALL_PASS
    if reproduced:
        print("VERDICT: KILL `fp-no-intrinsic-orientation` is INDEPENDENTLY REPRODUCED.")
        print("  u = e_7 complexifies ONLY the off-diagonal spatial {x1,x2} plane (and the")
        print("  Euclidean (4,0) V_{1/2} foil), NOT the (1,3) slice's timelike {x0,x3} plane:")
        print("  J^2 = diag(0,-1,-1,0) != -I_4 (rank 2), the Kahler form is degenerate")
        print("  (Pf=0, no volume form), and (1,3)'s odd time-parity forbids ANY")
        print("  eta-compatible complex structure.  Phase-78 clause C2 SURVIVES.")
        print("  RATIFY the GATE A KILL.")
    else:
        print("VERDICT: KILL NOT reproduced -- at least one of (a)-(d) failed.")
        print("  DO NOT ratify.  See the FAIL line(s) above.")
    print(f"GATE A INDEPENDENT VERDICT: {'KILL REPRODUCED' if reproduced else 'NOT REPRODUCED'}")
    print("=" * 78)
    return 0 if reproduced else 1


if __name__ == "__main__":
    sys.exit(main())
