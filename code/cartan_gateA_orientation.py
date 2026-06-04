#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# v19.0 (Orientation-forcing) -- GATE A : the cheap kill (run BEFORE any ceremony)
# ============================================================================
#
# THE QUESTION (the one forced data class Phase 78 left on the table).
# v18.0/Phase 78 returned `fp-imported-action` because the SYMMETRIC data
# (Tr(X o Y), det_3) cannot build the ANTISYMMETRIC orientation eps (clause C2):
# eps was reachable only as the orientation-ambiguous metric volume form
# sqrt|det eta| eps, whose SIGN is a by-hand choice. This milestone tests the one
# forced ANTISYMMETRIC datum Phase 78 never used as an orientation: the complex
# structure u = e_7 (J^2 = -1), which canonically orients a COMPLEX manifold.
#
# GATE A (decide EXACTLY over Q, ~minutes; KILL the route here or greenlight B/C/D):
#   (A1) Construct the endomorphism J on the 4d SPACETIME slice tangent space
#        h_2(C_u) ~= R^{3,1} (engine coords {1,2,3,10}) induced by u = e_7 via the
#        SAME pi_u mechanism (entrywise C_u action). Decide:
#          - J^2 = -1 on the 4d slice (a genuine almost-complex structure)?
#          - J compatible with the soldered (1,3) eta (J in so(3,1) / eta-Hermitian)?
#   (A2) Is the induced orientation FORCED / sign-definite:
#          omega_K(.,.) = eta(J.,.),  omega_K ^ omega_K = c * vol, sign(c) fixed by u?
#
#   KILL CONDITION (report `fp-no-intrinsic-orientation`, STOP, NO further phases):
#     J^2 != -1 on the slice, OR J incompatible with eta, OR the orientation sign is
#     NOT fixed by u. Then u supplies nothing the symmetric data didn't, and the
#     antisymmetric-data route is dead (Phase-78 clause C2 SURVIVES).
#
# NEW fp TRIPWIRE (v19.0 addition): `fp-imported-orientation` -- the orientation must
# come from u INTRINSICALLY. If J^2 = -1 on the slice is achieved only by ADDING a
# pairing (e.g. beta <-> gamma) that is NOT the action of u, that pairing is an IMPORT
# under audit, exactly as the MM action was in Phase 78. This driver SHOWS what u does,
# it does not assume it.
#
# CONVENTION LOCK (inherit v18.0 verbatim; CONVENTIONS.md / state.json convention_lock):
#   * EXACT over Q (sympy QQ); NO float / numpy on any decisive path (fp-float-decisive).
#     u = e_7 is a REAL octonion basis unit: the C_u complex structure is realized over Q
#     directly (the e_7 axis IS the imaginary direction; no Q(i) needed here).
#   * octonion Fano e_1 e_2 = e_4; complex structure u = e_7; E_11 = diag(1,0,0).
#   * det SSOT = ring_lemma_verification.py det_3; octonion_algebra.py BANNED (source guard).
#   * metric signature mostly-minus (+,-,-,-) on the h_2(C_u) det_2 slice (timelike-positive),
#     eta = diag(+1,-1,-1,-1); the bulk OP^2 trace form is Euclidean (4,0) (the Phase-75 FOIL).
#   * engine 27-coords [alpha 0; beta 1; gamma 2; x1 3..10; x2 11..18; x3 19..26]:
#     V_1={0}; V_0={1..10}; V_{1/2}={11..26}. Spacetime slice h_2(C_u) = {1,2,3,10}
#     = {beta, gamma, p=Re(x1), q=<x1,e7>}; Minkowski x0=(b+g)/2, x1=p, x2=q, x3=(b-g)/2.
#     V_{1/2} C_u survivors {11,18,19,26} = {Re(x2),<x2,e7>,Re(x3),<x3,e7>} = C_u^2 (the
#     Euclidean (4,0) coframe-value FOIL).
#
# Reuses the WARM exact-Q engines (imported, NOT rebuilt; det SSOT preserved):
#   embedding_under_E_verification : oct_mul, oct_zero, oct_conj, proj_u_exact, h3o_from_coords,
#                                    h3o_matmul, E   (the literal Phase-46 pi_u)
#   ring_lemma_verification        : Tr, jordan (det SSOT trace form)
#   bulk_geometry_verification     : _flat27, _standard_basis_27 (27-coord layout)
#
# Runnable directly:  python3 -u code/cartan_gateA_orientation.py
# Exits 0 iff Gate A SURVIVES (u forces a sign-definite orientation on the (1,3) slice);
# nonzero => KILL `fp-no-intrinsic-orientation` (negative-result-is-success; STOP).
# ============================================================================

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import Matrix, Rational, eye, zeros, simplify  # noqa: E402

import embedding_under_E_verification as EMB  # noqa: E402  (oct_mul, proj_u, E = pi_u)
import ring_lemma_verification as RL          # noqa: E402  (det SSOT: Tr, jordan)
import bulk_geometry_verification as BG       # noqa: E402  (27-coord layout, _flat27)

# ----- Peirce / slice layout (v18.0 lock; reproduced in Phase 74/75) ---------
V_HALF_IDX = list(range(11, 27))          # V_{1/2}(E_11): idx 11..26 (16)
CU4_IDX = [1, 2, 3, 10]                   # spacetime slice h_2(C_u): beta,gamma,p,q
CU_SURVIVOR_IDX = [11, 18, 19, 26]        # V_{1/2} C_u^2 foil: Re(x2),<x2,e7>,Re(x3),<x3,e7>
ETA_MINK = Matrix.diag(1, -1, -1, -1)     # mostly-minus (1,3); order (x0,x1,x2,x3)
# raw {beta,gamma,p,q} -> Minkowski {x0,x1,x2,x3}: x0=(b+g)/2, x1=p, x2=q, x3=(b-g)/2
RAW_TO_MINK = Matrix([[Rational(1, 2), Rational(1, 2), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1],
                      [Rational(1, 2), Rational(-1, 2), 0, 0]])

ALL_PASS = True
SURVIVES = True   # latched False by any KILL clause (A1 / A2)


def _report(label, ok, kill=False):
    global ALL_PASS, SURVIVES
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
        if kill:
            SURVIVES = False
    return ok


def _signature(M):
    """(n_pos, n_neg, n_zero) of a symmetric rational Matrix, EXACT over Q."""
    ev = M.eigenvals()
    return (sum(m for v, m in ev.items() if v > 0),
            sum(m for v, m in ev.items() if v < 0),
            sum(m for v, m in ev.items() if v == 0))


def _pfaffian4(O):
    """Pfaffian of a 4x4 antisymmetric matrix; (omega ^ omega) = 2 Pf(O) vol.
    Pf = O_01 O_23 - O_02 O_13 + O_03 O_12."""
    return O[0, 1] * O[2, 3] - O[0, 2] * O[1, 3] + O[0, 3] * O[1, 2]


# ============================================================================
# SOURCE GUARD : octonion_algebra absent; decisive primitives exact over Q.
# ============================================================================
def source_guard():
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra.py ABSENT; exact over Q (fp-octonion-algebra,")
    print("               fp-float-decisive)")
    print("=" * 78)
    in_modules = "octonion_algebra" in sys.modules
    numpy_here = "numpy" in sys.modules
    # det SSOT spot check (exact integer, not float).
    Xspot = EMB.h3o_from_coords(2, 3, 5, EMB.oct_zero(), EMB.oct_zero(), EMB.oct_zero())
    spot = RL.det_3(Xspot)
    spot_exact = (spot == 30) and (not isinstance(spot, float))
    # u = e_7 is a genuine complex structure on O: u*u = -1, u*1 = u (exact via oct_mul).
    u = EMB.oct_zero(); u[7] = Rational(1)
    one = EMB.oct_zero(); one[0] = Rational(1)
    uu = EMB.oct_mul(u, u)
    u1 = EMB.oct_mul(u, one)
    uu_is_minus1 = (uu[0] == -1 and all(uu[k] == 0 for k in range(1, 8)))
    u1_is_u = (u1[7] == 1 and u1[0] == 0 and all(u1[k] == 0 for k in (1, 2, 3, 4, 5, 6)))
    _report("octonion_algebra NOT in sys.modules; numpy NOT on the decisive path "
            "[fp-octonion-algebra / fp-float-decisive REJECTED]",
            (not in_modules) and (not numpy_here))
    _report(f"det SSOT exact: RL.det_3(diag(2,3,5)) == {spot} (exact integer, not float)",
            spot_exact)
    _report("u = e_7 is a complex structure on O (EXACT via Fano oct_mul): "
            f"u*u == -1 ({uu_is_minus1}), u*1 == u ({u1_is_u}) -- u^2=-1 confirmed",
            uu_is_minus1 and u1_is_u)
    return (not in_modules) and (not numpy_here) and spot_exact and uu_is_minus1 and u1_is_u


# ============================================================================
# Construct J on the 4d slice from u = e_7 via the literal entrywise C_u action.
# ============================================================================
def _u():
    u = EMB.oct_zero(); u[7] = Rational(1); return u


def _slice_elt(beta, gamma, p, q):
    """h_3(O) spacetime-slice element: alpha=0, off-diag x1 = p + q e_7 in C_u,
    x2 = x3 = 0. (Engine layout: V_0 = lower-right 2x2 {beta,gamma,x1}.)"""
    x1 = EMB.oct_zero(); x1[0] = p; x1[7] = q
    return EMB.h3o_from_coords(0, beta, gamma, x1, EMB.oct_zero(), EMB.oct_zero())


def _Lu_entrywise(X):
    """Left-multiply EVERY octonion entry of the 3x3 matrix X by u = e_7. This is
    the literal 'act by the complex structure u' on the algebra. On the real
    diagonal (a real scalar r) it returns u*r = r e_7 -- which is NOT a Hermitian
    diagonal (it has no comp-0): u carries the diagonal OUT of h_3(O)."""
    u = _u()
    return [[EMB.oct_mul(u, X[i][j]) for j in range(3)] for i in range(3)]


def _slice_coords(X):
    """Read an octonion 3x3 matrix back into the 4 slice coords (beta,gamma,p,q):
    beta = Re X[1][1], gamma = Re X[2][2], p = Re(x1)=Re X[2][1], q = <x1,e7> = X[2][1][7].
    Only the slice-valued (Hermitian, C_u) part is read; a pure-e_7 diagonal reads 0
    (it has no slice coordinate -- this is FORCED, not a discretionary projection)."""
    return [X[1][1][0], X[2][2][0], X[2][1][0], X[2][1][7]]


def build_J_slice():
    """J (4x4 over Q) on the slice {beta,gamma,p,q}, column k = slice-coords of
    L_u(basis_k). Returns (J_raw, J_mink, diag_images)."""
    basis = {"beta": _slice_elt(1, 0, 0, 0), "gamma": _slice_elt(0, 1, 0, 0),
             "p": _slice_elt(0, 0, 1, 0), "q": _slice_elt(0, 0, 0, 1)}
    cols, diag_images = [], {}
    for name in ("beta", "gamma", "p", "q"):
        Y = _Lu_entrywise(basis[name])
        cols.append(_slice_coords(Y))
        # record the (1,1),(2,2) diagonal images fully to expose the non-Hermitian leak
        diag_images[name] = (Y[1][1], Y[2][2])
    J_raw = Matrix(4, 4, lambda i, j: cols[j][i])      # column j = image of basis_j
    J_mink = RAW_TO_MINK * J_raw * RAW_TO_MINK.inv()
    return J_raw, J_mink, diag_images


# ============================================================================
# A1 : does u induce J^2 = -1 on the 4d (1,3) slice, eta-compatible?
# ============================================================================
def gateA1():
    print("=" * 78)
    print("A1 : J induced by u=e_7 on the 4d (1,3) SPACETIME slice -- J^2=-1 & eta-compat?")
    print("=" * 78)
    J_raw, J_mink, diag_images = build_J_slice()
    print(f"      J on slice (raw {{beta,gamma,p,q}}) =\n        {J_raw.tolist()}")
    print(f"      J on slice (Minkowski {{x0,x1,x2,x3}}) =\n        {J_mink.tolist()}")

    # --- the honest leak: u maps the real diagonal OUT of h_3(O) (pure e_7) --------
    db = diag_images["beta"][0]   # L_u(D_beta) at (1,1) = u*1 = e_7
    leak_ok = (db[0] == 0 and db[7] == 1)
    print(f"      u * (beta diagonal) = {db}  (= e_7: comp0=0, comp7=1 -> NON-Hermitian "
          "diagonal, leaves h_3(O))")
    _report("DIAGONAL LEAK: u*(real diagonal) = r e_7 has NO comp-0 -- u carries the "
            "{beta,gamma} (= the {x0,x3} timelike Minkowski plane) OUT of the Hermitian "
            "algebra; there is NO u-action on the slice diagonal [exact Q]", leak_ok)

    # --- J^2 on the slice (the decisive clause) ------------------------------------
    J2 = simplify(J_raw * J_raw)
    is_minus_I = (J2 == -eye(4))
    rankJ = J_raw.rank()
    J2_mink = simplify(J_mink * J_mink)
    print(f"      J^2 (raw) =\n        {J2.tolist()}   (expect NOT -I if u fails)")
    print(f"      J^2 (Minkowski) = diag {[J2_mink[i, i] for i in range(4)]}  "
          f"(order x0,x1,x2,x3); rank(J) = {rankJ}")
    _report("A1 VERDICT (J^2 = -1 on the 4d slice?): J^2 == -I_4 over Q "
            f"[KILL clause A1 if NOT].  Result: J^2 {'==' if is_minus_I else '!='} -I_4",
            is_minus_I, kill=True)

    # Where DOES J^2 = -1 hold? -> the {x1,x2} purely-SPATIAL plane only.
    spatial_block = (J2_mink[1, 1] == -1 and J2_mink[2, 2] == -1)
    frozen_block = (J2_mink[0, 0] == 0 and J2_mink[3, 3] == 0)
    print(f"      J^2 = -1 on the {{x1,x2}} purely-spatial plane: {spatial_block}; "
          f"J = 0 on the {{x0,x3}} timelike plane: {frozen_block}")
    _report("STRUCTURE OF THE FAILURE: u complexifies ONLY the {x1,x2} off-diagonal "
            "purely-SPATIAL plane (eta=(-,-)); the {x0,x3} plane (containing the "
            "TIMELIKE x0) is u-frozen (rank(J)=2). Complexifying it would rotate time "
            "into space -- which a spatial octonion unit e_7 cannot do [exact Q]",
            spatial_block and frozen_block and rankJ == 2)

    # eta-compatibility of the (rank-2) constructed J: it IS eta-skew (an so(2) in
    # so(3,1)), but that is NOT a complex structure (J^2 != -I). Report honestly.
    eta_skew = simplify(J_mink.T * ETA_MINK + ETA_MINK * J_mink) == zeros(4, 4)
    _report("eta-COMPATIBILITY (diagnostic): the constructed (rank-2) J IS eta-skew "
            "(J^T eta + eta J = 0, an so(2) spatial-rotation generator in so(3,1)) -- "
            "but eta-skew + J^2=-I would force eta J-Hermitian (parity cross-check "
            "below), so an eta-compatible COMPLEX structure cannot coexist with (1,3)",
            eta_skew)
    return is_minus_I


# ============================================================================
# A1' : parity cross-check -- (1,3) admits NO eta-compatible complex structure.
# ============================================================================
def gateA1_parity():
    print("=" * 78)
    print("A1' : parity obstruction -- a (1,3) metric admits NO eta-Hermitian J^2=-1")
    print("=" * 78)
    # If J^2 = -I and J in so(3,1) (J^T eta + eta J = 0), then eta(JX,JY)=eta(X,Y):
    #   eta(JX,JY) = X^T J^T eta J Y = X^T (-eta J) J Y = -X^T eta J^2 Y = X^T eta Y.
    # So eta is J-Hermitian; every J-invariant 2-plane {v,Jv} has eta|plane=diag(a,a)
    # => signature contributes an EVEN count of +. (1,3) has ONE + (ODD) -> impossible.
    # Demonstrate the implication concretely on eta = diag(+1,-1,-1,-1):
    pos, neg, zer = _signature(ETA_MINK)
    odd_plus = (pos % 2 == 1)
    print(f"      eta signature (n_+, n_-, n_0) = ({pos},{neg},{zer}); n_+ is "
          f"{'ODD' if odd_plus else 'EVEN'}")
    _report("PARITY OBSTRUCTION: an eta-Hermitian complex structure forces an EVEN "
            "number of + eigenvalues (each {v,Jv} plane contributes diag(a,a)); the "
            "(1,3) slice has n_+ = 1 (ODD) => NO eta-compatible J with J^2=-1 exists, "
            "for ANY construction (not just u's) -- a structural, u-independent reason "
            "[exact Q]", odd_plus)
    return odd_plus


# ============================================================================
# A1'' : triangulation -- u DOES orient the Euclidean (4,0) V_{1/2} FOIL.
# ============================================================================
def gateA_foil():
    print("=" * 78)
    print("A1'' : triangulation -- on the V_{1/2} C_u^2 coframe FOIL {11,18,19,26}")
    print("        (Euclidean (4,0)), u DOES give J^2=-1 -- but that is the WRONG space")
    print("=" * 78)
    # Build J on the C_u^2 value space: x2's C_u {11,18} and x3's C_u {19,26}, each a
    # genuine complex line, u acts as the standard J on each. Construct via oct_mul.
    # x2 line: comp0 (idx11) and comp7 (idx18); x3 line: comp0 (idx19), comp7 (idx26).
    u = _u()
    def cu_line_J():
        # u * (1) = e_7 ; u * (e_7) = -1  => (Re,e7) -> (-e7coeff, Re): [[0,-1],[1,0]]
        one = EMB.oct_zero(); one[0] = Rational(1)
        e7 = EMB.oct_zero(); e7[7] = Rational(1)
        c1 = EMB.oct_mul(u, one)   # = e_7      -> (Re',e7') = (0, 1)
        c2 = EMB.oct_mul(u, e7)    # = -1       -> (Re',e7') = (-1, 0)
        return Matrix([[c1[0], c2[0]], [c1[7], c2[7]]])
    Jline = cu_line_J()
    J_foil = zeros(4, 4)
    J_foil[0:2, 0:2] = Jline    # x2 C_u line {11,18}
    J_foil[2:4, 2:4] = Jline    # x3 C_u line {19,26}
    J2_foil = simplify(J_foil * J_foil)
    foil_minus_I = (J2_foil == -eye(4))
    print(f"      J on the foil =\n        {J_foil.tolist()};  J^2 == -I_4: {foil_minus_I}")
    _report("FOIL J^2 = -I_4: on the V_{1/2} C_u^2 = C^2 value space u IS a genuine "
            "complex structure (two C_u lines, u rotates each) [exact Q]", foil_minus_I)

    # Foil metric = bare trace Gram on the 4 survivor directions = diag(2,2,2,2)=(4,0).
    basis = BG._standard_basis_27()
    cof = [EMB.E(basis[k]) for k in CU_SURVIVOR_IDX]
    Gram = Matrix(4, 4, lambda i, j: RL.Tr(RL.jordan(cof[i], cof[j])))
    posf, negf, zerf = _signature(Gram)
    print(f"      foil metric (bare trace Gram) signature = ({posf},{negf},{zerf}) "
          f"(expect (4,0) Euclidean OP^2 Fubini-Study)")
    # Kahler form on the foil is NON-degenerate => forced orientation HERE.
    omega_foil = Gram * J_foil      # omega(X,Y) = g(JX,Y); g Euclidean here
    omega_foil = (omega_foil - omega_foil.T) * Rational(1, 2)   # antisymmetric part
    pf_foil = simplify(_pfaffian4(omega_foil))
    print(f"      Pf(omega_K) on the foil = {pf_foil} (nonzero -> omega^omega = "
          "2 Pf vol, orientation forced ON THE FOIL)")
    _report("FOIL ORIENTATION FORCED (but WRONG space): foil metric (4,0) Euclidean, "
            "Pf(omega_K) != 0 -> u forces an orientation on the EUCLIDEAN OP^2 "
            "coframe-value foil; this is NOT the (1,3) spacetime slice where "
            "eps_{abcd} R^{ab} e^c e^d lives [exact Q]",
            (posf, negf, zerf) == (4, 0, 0) and pf_foil != 0)
    return (posf, negf, zerf) == (4, 0, 0) and foil_minus_I


# ============================================================================
# A2 : is the orientation FORCED on the (1,3) slice? (omega_K ^ omega_K)
# ============================================================================
def gateA2():
    print("=" * 78)
    print("A2 : orientation on the (1,3) slice -- omega_K = eta(J.,.), omega_K ^ omega_K")
    print("=" * 78)
    J_raw, J_mink, _ = build_J_slice()
    # omega_K(X,Y) = eta(JX,Y) = (eta J)_{..}; antisymmetric part is the Kahler 2-form.
    omega = ETA_MINK * J_mink
    omega_anti = simplify((omega - omega.T) * Rational(1, 2))
    pf = simplify(_pfaffian4(omega_anti))
    rk = omega_anti.rank()
    print(f"      omega_K (antisymmetric part of eta J), Minkowski =\n        "
          f"{omega_anti.tolist()}")
    print(f"      rank(omega_K) = {rk} (expect 2 -- degenerate); Pf(omega_K) = {pf} "
          "(=> omega_K ^ omega_K = 2 Pf vol)")
    forced = (pf != 0)
    _report("A2 VERDICT (orientation forced on the (1,3) slice?): omega_K ^ omega_K = "
            f"2 Pf(omega_K) vol with Pf != 0 [KILL clause A2 if Pf == 0]. Result: Pf = "
            f"{pf} -> orientation {'FORCED' if forced else 'NOT forced'} by u",
            forced, kill=True)
    _report("ORIENTATION-AMBIGUITY UNREPAIRED: Pf(omega_K) = 0 (omega_K degenerate, "
            "rank 2) => u gives NO volume form on the (1,3) slice => the eps SIGN is "
            "STILL a by-hand choice, exactly Phase-78 clause C2. C2 SURVIVES.",
            pf == 0)
    return forced


def main():
    print("#" * 78)
    print("# v19.0 GATE A -- the cheap orientation kill (EXACT over Q; run before ceremony)")
    print("#   Does u=e_7 force a sign-definite orientation on the (1,3) spacetime slice?")
    print("#   SURVIVES => greenlight Gates B/C/D ;  KILL => fp-no-intrinsic-orientation.")
    print("#" * 78)

    okG = source_guard()
    a1 = gateA1()           # J^2 = -1 on the (1,3) slice?  (expect FAIL => KILL)
    par = gateA1_parity()   # structural: (1,3) admits no eta-compatible J at all
    foil = gateA_foil()     # triangulation: u orients the Euclidean (4,0) FOIL instead
    a2 = gateA2()           # orientation forced on the slice?  (expect FAIL => KILL)

    print("=" * 78)
    print(f"SOURCE GUARD ............................. {'PASS' if okG else 'FAIL'}")
    print(f"A1  J^2 = -1 on the (1,3) slice .......... {'PASS (J is ACS)' if a1 else 'FAIL => KILL'}")
    print(f"A1' (1,3) admits eta-compatible J (parity) {'n/a' if not par else 'NO (obstruction shown)'}")
    print(f"A1'' u orients Euclidean (4,0) FOIL ...... {'YES (wrong space)' if foil else '?'}")
    print(f"A2  orientation forced on the slice ...... {'PASS' if a2 else 'FAIL => KILL'}")
    print("-" * 78)
    if SURVIVES and a1 and a2 and okG:
        print("GATE A SURVIVES: u=e_7 forces a sign-definite orientation on the (1,3)")
        print("  slice. GREENLIGHT Gates B (does u repair C2) / C (V_{1/2} repairs C3) / D.")
        verdict = "SURVIVES"
    else:
        print("GATE A KILL => `fp-no-intrinsic-orientation`. u = e_7 complexifies ONLY")
        print("  the off-diagonal spatial C_u plane (and the Euclidean (4,0) V_{1/2} coframe")
        print("  FOIL), NOT the (1,3) spacetime slice's timelike {x0,x3} plane: J^2 != -1")
        print("  on the slice, the Kahler form is degenerate (Pf=0), and (1,3)'s odd time")
        print("  parity forbids ANY eta-compatible complex structure. The orientation eps")
        print("  is STILL not fixed by u -- Phase-78 clause C2 SURVIVES. The forced-")
        print("  antisymmetric-data route is DEAD at Gate A. Report FLAT; STOP; no further")
        print("  phases (negative-result-is-success).")
        verdict = "KILL: fp-no-intrinsic-orientation"
    print(f"GATE A VERDICT: {verdict}")
    print("=" * 78)
    return 0 if (SURVIVES and a1 and a2 and okG) else 1


if __name__ == "__main__":
    sys.exit(main())
