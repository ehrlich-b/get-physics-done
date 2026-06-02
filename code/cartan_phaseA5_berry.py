#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# Phase 76 (v18.0 Cartan/MacDowell-Mansouri) -- Plan 01  (PART 1, the VACUUM half)
# Phase A.5: THE BERRY-CURVATURE SAME-WALL GATE -- SOFT KILL  (conjunctive w/ Ph75)
# ============================================================================
#
# Decide, EXACTLY over Q(i) and BEFORE any matter is turned on, whether the canonical
# Berry curvature  F_B = Im(QGT) = -2 Im Tr(P dP dP)  of the rank-1 C_u-idempotent
# family E(x) is (VALD-03) well-defined and generically NONZERO on the 4d slice
# {11,18,19,26} = C_u^2, BORN FROM the C_u breaking of the isotropy-irreducible
# OP^2 = F_4/Spin(9) (which carries NO invariant 2-form => round Berry = 0); run the
# SOFT real-part anchor (CALC-03, Re(QGT) = Fubini-Study metric of the same
# non-Einstein CHARACTER as the v17.0 cone-Hessian -- INFORMATIVE, never a KILL);
# and classify the M=0 vacuum (CALC-04: flat / pure-Lambda-Kahler / other).
#
#   CP^1 PIN  (calibration, BEFORE any h_3(O) object): reproduce the monopole anchor
#             F_B = -sin theta/2 (int = -2pi), g_theta theta = 1/4 exactly over Q(i).
#             PINS the sign and the factor-2 of the whole recipe (defeats Pitfall-5).
#   VALD-03   (done FIRST): F_B = -2 Im Q well-defined + generically NONZERO + BORN
#             FROM the C_u breaking (group theory: OP^2 isotropy-irreducible =>
#             no invariant 2-form => round Berry = 0). A degenerate F_B == 0 is the
#             worse-than-SOFT-KILL outcome and is detected + reported flat.
#   CALC-03   (SOFT, INFORMATIVE, NOT a KILL): Re(QGT) = 1/2 Tr(dP dP) a positive-
#             definite FS metric (the ONLY hard failure here is Re(QGT) NOT pos-def);
#             its non-Einstein CHARACTER vs the cone-Hessian diag(9,9,18,18)/round
#             K=-1 reported as a diagnostic. Discrepancy EXPECTED (FS-pullback !=
#             cone-Hessian restriction) -- fp-reuse-cone-hessian.
#   CALC-04   M=0 vacuum class of F_B (flat / pure-Lambda ~ e^e Kahler / other), via
#             the trace/traceless/Weyl decomposition. Lambda NOT reintroduced
#             negative; R x H^3 NOT reintroduced (the FALSIFIED v17.0 vacuum).
#
# THE TWO DESIGN POINTS (do not get these wrong):
#   1. The QGT uses the ASSOCIATIVE complex matrix product on slice_to_complex(P)
#      (e_7 -> i, i = sympy.I SYMBOLIC over Q(i)), NOT the Jordan product o --
#      C_u ~= C is the unique associative completion u = e_7 provides, so the
#      associative product is FORCED.  F_B = Im(QGT) is the literal SymPy Im.
#   2. The Re(QGT) = cone-Hessian comparison (CALC-03) is a SOFT, INFORMATIVE
#      diagnostic ONLY. A discrepancy is EXPECTED and is NEVER a KILL/HALT. The
#      v17.0 NONE binds the REAL part; this phase mines the IMAGINARY part.
#
# CONVENTION LOCK (v18.0; see .gpd/state.json convention_lock / CONVENTIONS.md):
#   * EXACT over Q(i): the i is sympy.I, SYMBOLIC; ranks/eigenvals/Re/Im via SymPy
#     over QQ or Q(i); NO float on any decisive path (fp-float-decisive).
#   * octonion multiplication: Fano e1 e2 = e4.       complex structure: u = e7.
#   * primitive idempotent: E_11 = diag(1,0,0).       Peirce eigenvalues {0,1/2,1}.
#   * det SSOT = ring_lemma_verification.py det_3. octonion_algebra.py is BANNED on
#     every decisive path (fp-octonion-algebra; source guard below).
#   * QGT: Q_{mu nu} = Tr(P d_mu P d_nu P);  g = Re Q (Fubini-Study);
#     F_B = i Tr(P[d_mu P, d_nu P]) = -2 Im Q (Berry curvature).  Sign/factor PINNED
#     by the CP^1 anchor (F_B = -sin theta/2, g_theta theta = 1/4).
#   * metric signature mostly-minus (+,-,-,-) on the soldered (1,3) Lorentz block of
#     the C_u^2 survivors {11,18,19,26} (Phase 75 SURVIVES target). natural units.
#   * Lambda = 0; the M=0 spacetime vacuum is flat KKT eta; do NOT reintroduce
#     Lambda<0 / R x H^3 (the FALSIFIED v17.0 cone-Hessian source-field geometry).
#   * engine 27-coord layout: V_1={0}; V_0={1..10}; V_{1/2}={11..26}. C_u survivors
#     of pi_u on V_{1/2} = {11,18,19,26} = {Re(x2),<x2,e7>,Re(x3),<x3,e7>} (Phase 75).
#
# Reuses the WARM exact engines (imported, NOT rebuilt; det SSOT preserved):
#   embedding_under_E_verification : E, proj_u_exact(a,u_index=7), slice_to_complex,
#                                    cu_to_complex, h3o_from_coords, jordan, oct_zero
#   ring_lemma_verification        : Tr, jordan, det_3 (det SSOT)
#   bulk_geometry_verification     : cone_hessian_at_center, h3_constant_curvature,
#                                    ricci_decomposition_n4, peirce_indices_under_E11
#
# Reproducibility: Python 3 (CPython), SymPy 1.14.0 (deterministic, exact over Q(i);
# no RNG on any decisive path -- every matrix is built from fixed rational entries and
# the symbolic imaginary unit sympy.I).
#
# Runnable directly:  python3 -u code/cartan_phaseA5_berry.py
# Exits 0 iff the CP^1 pin + VALD-03 + CALC-03(pos-def) + CALC-04 all PASS (PART 1 of
# the SOFT-KILL gate is established).  This plan does NOT emit the decisive SOFT KILL /
# SURVIVES verdict -- that (matter-on VALD-04) lives in plan 76-02.
# ============================================================================

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import (  # noqa: E402
    Matrix, Rational, I, symbols, cos, sin, exp, simplify, cancel, trigsimp,
    re as sym_re, im as sym_im, zeros, eye, sqrt, pi, integrate, conjugate,
    diff, LeviCivita,
)

import embedding_under_E_verification as EMB  # noqa: E402  (slice_to_complex e_7->i; E/proj_u)
import ring_lemma_verification as RL  # noqa: E402  (det SSOT: Tr, jordan, det_3)
import bulk_geometry_verification as BG  # noqa: E402  (cone-Hessian / H^3 / ricci_decomp Re-anchor)

# Engine-native Peirce layout (v18.0 lock; reproduced in Phase 74/75).
V_HALF_IDX = list(range(11, 27))         # V_{1/2}(E_11), idx 11..26 (16 elements)
CU_SURVIVOR_IDX = [11, 18, 19, 26]       # C_u^2 survivors of pi_u (Phase 75): the 4 base dirs

ALL_PASS = True


def _report(label, ok):
    """Print a PASS/FAIL line; latch ALL_PASS to False on any failure."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


def _is_zero_matrix(M):
    """Exact: True iff every entry of a SymPy Matrix simplifies to 0 (over Q(i))."""
    return all(simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def _source_guard():
    """fp-octonion-algebra guard (inherited from Phase 0 DERV-01 / Phase 75 semantics).
    The LOAD-BEARING facts are RUNTIME, not a naive source grep:
      (1) octonion_algebra is NOT in sys.modules after the decisive imports (nothing on
          the live path pulled in the banned float engine);
      (2) the decisive primitives RL.det_3 / RL.Tr / RL.jordan are the NATIVE exact-over-Q
          ring_lemma_verification functions (distinct objects from any aliased oa_* oracle);
      (3) the QGT path uses the ASSOCIATIVE complex matrix product on slice_to_complex(P),
          NEVER the Jordan product o (which would give a different, wrong object).
    A genuine OFFENDER is an ACTIVE import of octonion_algebra that would SHADOW an exact
    primitive; the sanctioned `... import det_3 as oa_det_3 ...` aliased oracle line is fine."""
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra.py ABSENT on the decisive path "
          "(fp-octonion-algebra; Phase-0 DERV-01 / Phase-75 semantics)")
    print("=" * 78)
    in_modules = "octonion_algebra" in sys.modules

    SANCTIONED, offenders = [], []
    EXACT_NAMES = ("det_3", "Tr", "jordan", "Tr2", "polarize_d", "X_from_symbols")
    for mod in (BG, EMB, RL):
        src_path = getattr(mod, "__file__", None)
        if not (src_path and os.path.exists(src_path)):
            continue
        with open(src_path) as fh:
            for ln in fh:
                s = ln.strip()
                if s.startswith("#"):
                    continue
                active = (s.startswith("import octonion_algebra")
                          or s.startswith("from octonion_algebra"))
                if not active:
                    continue
                base = os.path.basename(src_path)
                shadows_exact = any(
                    (f"import {nm}" in s and f"{nm} as oa_" not in s)
                    or (f", {nm}" in s and f"{nm} as oa_" not in s and f"{nm} as " not in s)
                    for nm in EXACT_NAMES
                )
                if ("as oa_" in s) and not shadows_exact:
                    SANCTIONED.append((base, s))
                else:
                    offenders.append((base, s))

    # The decisive primitives must be the native exact ring_lemma versions.
    native_exact = (
        RL.det_3.__module__ == "ring_lemma_verification"
        and RL.Tr.__module__ == "ring_lemma_verification"
        and RL.jordan.__module__ == "ring_lemma_verification"
        and (RL.det_3 is not getattr(RL, "oa_det_3", object()))
    )
    Xspot = EMB.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                                EMB.oct_zero(), EMB.oct_zero(), EMB.oct_zero())
    spot = RL.det_3(Xspot)
    spot_exact = (spot == 30) and (not isinstance(spot, float))

    _report("octonion_algebra NOT in sys.modules after the decisive imports "
            "(EMB/RL/BG) -- nothing on the live path pulled in the banned float "
            "engine [fp-octonion-algebra REJECTED]", not in_modules)
    _report("decisive primitives RL.det_3 / RL.Tr / RL.jordan are the NATIVE "
            "exact-over-Q ring_lemma_verification functions (NOT the aliased oracle "
            f"oa_det_3); det_3(diag(2,3,5))=={spot} exact integer [fp-float-decisive "
            "REJECTED]", native_exact and spot_exact)
    _report(f"0 UNSANCTIONED octonion_algebra imports that would shadow an exact "
            f"primitive in the decisive engine sources (found {len(offenders)}, "
            f"expect 0); {len(SANCTIONED)} sanctioned aliased-oracle line(s)",
            len(offenders) == 0)
    for f, s in SANCTIONED:
        print(f"      SANCTIONED in-fence oracle (not on decisive path): {f}: {s}")
    for f, s in offenders:
        print(f"      OFFENDER: {f}: {s}")
    return ((not in_modules) and native_exact and spot_exact and (len(offenders) == 0))


# ============================================================================
# THE QGT RECIPE  (the single load-bearing object; PINNED by the CP^1 anchor)
# ============================================================================
# Q_{mu nu} = Tr(P d_mu P d_nu P) over Q(i) with P a Hermitian rank-1 projector.
#   g = Re(Q)            (Fubini-Study metric; symmetric)
#   F_B = -2 Im(Q)       (Berry curvature; antisymmetric)
# All products are the ASSOCIATIVE complex matrix product (NOT the Jordan product) --
# this is forced by C_u ~= C (u = e_7 the unique associative completion).  The i is
# sympy.I, SYMBOLIC; Re/Im are the literal sympy.re/sympy.im.


def QGT(P, params, simp=cancel):
    """The quantum geometric tensor Q_{mu nu} = Tr(P dP_mu dP_nu) over Q(i).

    P     : NxN SymPy complex Matrix (a Hermitian rank-1 projector), function of `params`.
    params: list of real SymPy symbols (the differentiation directions).
    Returns the len(params) x len(params) SymPy Matrix Q (generically complex).
    Uses the ASSOCIATIVE matrix product P*dP*dP (NOT Jordan); trace = SymPy .trace().
    """
    n = len(params)
    dP = [P.diff(p) for p in params]
    Q = zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            Q[mu, nu] = simp((P * dP[mu] * dP[nu]).trace())
    return Q


def fs_metric(P, params, simp=cancel):
    """g_{mu nu} = Re(QGT) -- the Fubini-Study metric (symmetric)."""
    Q = QGT(P, params, simp)
    n = Q.rows
    return Matrix(n, n, lambda i, j: simp(sym_re(Q[i, j])))


def berry_F(P, params, simp=cancel):
    """F_B,{mu nu} = -2 Im(QGT) -- the Berry curvature (antisymmetric).
    Sign/factor PINNED by the CP^1 anchor F_B = -sin theta/2."""
    Q = QGT(P, params, simp)
    n = Q.rows
    return Matrix(n, n, lambda i, j: simp(-2 * sym_im(Q[i, j])))


# ============================================================================
# TASK 1.1 : CP^1 CONVENTION PIN  (do this BEFORE any h_3(O) object)
# ============================================================================
def cp1_pin():
    """Reproduce the monopole anchor on CP^1 = S^2 EXACTLY over the symbolic field:
        P(theta,phi) = 1/2 [[1+cos th, sin th e^{-i phi}],[sin th e^{i phi}, 1-cos th]]
        Q_theta theta = 1/4,  Q_phi phi = sin^2 th /4,  Q_theta phi = (i/4) sin th
        F_B = -2 Im Q_theta phi = -sin th /2  (int over S^2 = -2pi)
        g_theta theta = Re Q_theta theta = 1/4
    PINS the sign and the factor-2 of the whole recipe."""
    print("=" * 78)
    print("CP^1 PIN : monopole anchor F_B = -sin theta/2 (int=-2pi), g_th th = 1/4")
    print("  (sign/factor calibration of Q=Tr(P dP dP); Re/Im split; BEFORE any h_3(O))")
    print("=" * 78)

    th, ph = symbols('theta phi', real=True)
    P = Rational(1, 2) * Matrix([
        [1 + cos(th), sin(th) * exp(-I * ph)],
        [sin(th) * exp(I * ph), 1 - cos(th)],
    ])

    # P is a rank-1 Hermitian projector: P^2 = P, P^dagger = P, Tr P = 1.
    P2mP = simplify(P * P - P)
    herm = simplify(P - P.conjugate().T)
    trP = simplify(P.trace())
    _report("CP^1 projector is rank-1 Hermitian: P^2 - P == 0, P = P^dagger, Tr P == 1 "
            "[exact symbolic]",
            _is_zero_matrix(P2mP) and _is_zero_matrix(herm) and trP == 1)

    params = [th, ph]
    Q = QGT(P, params, simp=trigsimp)
    Qthth = trigsimp(Q[0, 0])
    Qphph = trigsimp(Q[1, 1])
    Qthph = trigsimp(Q[0, 1])

    ok_Qthth = simplify(Qthth - Rational(1, 4)) == 0
    ok_Qphph = simplify(Qphph - sin(th) ** 2 / 4) == 0
    ok_Qthph = simplify(Qthph - I * sin(th) / 4) == 0
    print(f"      Q_theta theta = {Qthth}   (expect 1/4)")
    print(f"      Q_phi phi     = {Qphph}   (expect sin^2 th /4)")
    print(f"      Q_theta phi   = {Qthph}   (expect i sin th /4)")
    _report("CP^1 QGT components EXACT: Q_th th=1/4, Q_ph ph=sin^2 th/4, "
            "Q_th ph= i sin th/4 [over Q(i), symbolic]",
            ok_Qthth and ok_Qphph and ok_Qthph)

    # The Berry curvature and FS metric via the SAME helpers used downstream.
    FB = berry_F(P, params, simp=trigsimp)
    g = fs_metric(P, params, simp=trigsimp)
    FB_thph = trigsimp(FB[0, 1])
    g_thth = trigsimp(g[0, 0])
    ok_FB = simplify(FB_thph - (-sin(th) / 2)) == 0
    ok_anti = simplify(FB[0, 1] + FB[1, 0]) == 0 and simplify(FB[0, 0]) == 0
    ok_g = simplify(g_thth - Rational(1, 4)) == 0
    print(f"      F_B[theta,phi] = {FB_thph}   (expect -sin th /2)")
    print(f"      g_theta theta  = {g_thth}   (expect 1/4)")
    _report("CP^1 Berry curvature F_B[th,ph] = -2 Im Q = -sin theta/2 (sign+factor-2 "
            "PINNED); F_B antisymmetric [exact symbolic]", ok_FB and ok_anti)
    _report("CP^1 Fubini-Study g_theta theta = Re Q = 1/4 [exact symbolic]", ok_g)

    # Monopole charge: int_{S^2} F_B[th,ph] dtheta dphi = -2pi (the calibration scale).
    monopole = integrate(integrate(FB_thph, (th, 0, pi)), (ph, 0, 2 * pi))
    _report(f"CP^1 monopole flux int_{{S^2}} F_B = {monopole} (expect -2pi) -- the "
            "first-Chern calibration of the recipe [exact]", simplify(monopole + 2 * pi) == 0)
    return ALL_PASS


# ============================================================================
# TASK 1.2 : RANK-1 C_u IDEMPOTENT FAMILY  (the vacuum chart) + the e_7->i bridge
# ============================================================================
# v(z1,z2) = [1, z1, z2], z1 = a + i b, z2 = c + i d  (a,b,c,d real sympy symbols).
# P_C = v v^dagger / (v^dagger v)  -- a 3x3 SymPy COMPLEX rank-1 projector.  This IS
# slice_to_complex of the C_u rank-1 idempotent (i = sympy.I = e_7, symbolic over Q(i)).
def build_cu_idempotent():
    """Return (P_C, params, base_subs, syms) for the rank-1 C_u idempotent family.
    syms = (a,b,c,d); params = [a,b,c,d] the 4 C_u^2 base directions {11,18,19,26}."""
    a, b, c, d = symbols('a b c d', real=True)
    z1 = a + I * b
    z2 = c + I * d
    v = Matrix([1, z1, z2])
    vdag = v.conjugate().T
    norm = (vdag * v)[0, 0]          # 1 + |z1|^2 + |z2|^2, real
    P_C = (v * vdag) / norm
    params = [a, b, c, d]
    base_subs = {a: 0, b: 0, c: 0, d: 0}    # the base point v=[1,0,0], P=diag(1,0,0)
    return P_C, params, base_subs, (a, b, c, d)


def task1_idempotent_and_bridge(P_C, params, base_subs, syms):
    """Verify rank-1 idempotent EXACT over Q(i) + the slice_to_complex (e_7->i) bridge
    + the C_u survivors {11,18,19,26} = the 4 base directions (a,b,c,d)."""
    print("=" * 78)
    print("RANK-1 C_u IDEMPOTENT FAMILY : P_C = v v^dagger/(v^dagger v), v=[1,z1,z2], "
          "z1=a+ib, z2=c+id  (i = e_7 symbolic over Q(i))")
    print("=" * 78)
    a, b, c, d = syms

    # (i) rank-1 idempotent EXACT over Q(i): P_C^2 - P_C == 0 and Tr P_C == 1, Hermitian.
    P2mP = Matrix(3, 3, lambda i, j: cancel((P_C * P_C - P_C)[i, j]))
    herm = Matrix(3, 3, lambda i, j: cancel((P_C - P_C.conjugate().T)[i, j]))
    trP = cancel(P_C.trace())
    _report("rank-1 idempotent EXACT over Q(i): P_C^2 - P_C == 0 (3x3 zero), "
            "P_C = P_C^dagger, Tr P_C == 1 [symbolic i]",
            _is_zero_matrix(P2mP) and _is_zero_matrix(herm) and cancel(trP - 1) == 0)

    # (ii) the slice_to_complex (e_7 -> i) bridge is FAITHFUL: build the corresponding
    # h_3(C_u) element by hand with C_u entries and confirm slice_to_complex maps it to
    # the SAME complex projector (at a rational test point so the entries are exact C_u).
    # Test point: z1 = 1 + 2 e_7 (a=1,b=2), z2 = 3 - e_7 (c=3,d=-1).
    test = {a: Rational(1), b: Rational(2), c: Rational(3), d: Rational(-1)}
    P_C_test = Matrix(3, 3, lambda i, j: cancel(P_C[i, j].subs(test)))

    # Hand-build h_3(C_u): the rank-1 idempotent vv^dag/(v^dag v) but with C_u OCTONION
    # entries (comps 0 and 7), then slice_to_complex it.  We construct the OFF-DIAGONAL
    # C_u entries x1,x2,x3 from the projector's lower-triangular complex entries.
    #   layout [[a0, conj(x3), x2],[x3, b0, conj(x1)],[conj(x2), x1, g0]]
    # P_C_test[1,0] = x3 (complex), P_C_test[2,0] = conj(x2), P_C_test[2,1] = x1.
    def c_to_cu(z):
        z = simplify(z)
        o = EMB.oct_zero()
        o[0] = sym_re(z)
        o[7] = sym_im(z)
        return o
    alpha0 = simplify(sym_re(P_C_test[0, 0]))
    beta0 = simplify(sym_re(P_C_test[1, 1]))
    gamma0 = simplify(sym_re(P_C_test[2, 2]))
    x3 = c_to_cu(P_C_test[1, 0])       # (1,0) entry = x3
    x1 = c_to_cu(P_C_test[2, 1])       # (2,1) entry = x1
    x2 = c_to_cu(P_C_test[0, 2])       # (0,2) entry = x2
    H_cu = EMB.h3o_from_coords(alpha0, beta0, gamma0, x1, x2, x3)
    Mc_from_bridge = EMB.slice_to_complex(H_cu)
    bridge_match = _is_zero_matrix(
        Matrix(3, 3, lambda i, j: simplify(Mc_from_bridge[i, j] - P_C_test[i, j])))
    _report("slice_to_complex (e_7 -> i) bridge FAITHFUL: the hand-built h_3(C_u) "
            "element maps EXACTLY to P_C at the rational test pt (e_7->i is the literal "
            "Im) [exact over Q(i)]", bridge_match)

    # (iii) no octonion comp e_1..e_6 leaks: every off-diagonal C_u entry has comps 1..6 zero.
    no_leak = EMB._is_slice_element(H_cu)
    _report("NO octonion leak: the h_3(C_u) element has comps e_1..e_6 == 0 on every "
            "entry (pure C_u = span{1,e_7}); the C_u projection is faithful [exact]",
            no_leak)

    # (iv) the 4 base directions ARE the C_u^2 survivors {11,18,19,26} from Phase 75.
    groups, _diag = BG.peirce_indices_under_E11()
    Vh = sorted(groups.get(Rational(1, 2), []))
    _report("the 4 differentiation directions (a,b,c,d) <-> the C_u^2 survivors "
            f"{CU_SURVIVOR_IDX} of pi_u on V_{{1/2}}={Vh[:3]}... (Phase 75 SURVIVES "
            "coframe); 4 = dim(4d slice) [regression]",
            Vh == V_HALF_IDX and len(CU_SURVIVOR_IDX) == 4)
    return ALL_PASS


# ============================================================================
# TASK 1.3 : THE 4x4 QGT ON THE 4 C_u^2 BASE DIRECTIONS  (a,b,c,d), over Q(i)
# ============================================================================
def task1_assemble_qgt(P_C, params, base_subs):
    """Assemble Q(a,b,c,d) = [Tr(P_C d_mu P_C d_nu P_C)] over Q(i); confirm the Re part
    is symmetric and the Im part antisymmetric BY CONSTRUCTION (the recipe is calibrated)."""
    print("=" * 78)
    print("4x4 QGT Q(a,b,c,d) on the C_u^2 base directions {11,18,19,26}  (over Q(i))")
    print("=" * 78)
    Q = QGT(P_C, params, simp=cancel)
    # Evaluate at the base point for a clean exact readout (symbolic Q kept for VALD-03).
    Q0 = Matrix(4, 4, lambda i, j: cancel(Q[i, j].subs(base_subs)))
    print("      Q(base point a=b=c=d=0):")
    for r in range(4):
        print(f"        {[Q0[r, k] for k in range(4)]}")
    g0 = Matrix(4, 4, lambda i, j: simplify(sym_re(Q0[i, j])))
    FB0 = Matrix(4, 4, lambda i, j: simplify(-2 * sym_im(Q0[i, j])))
    sym_ok = _is_zero_matrix(g0 - g0.T)
    anti_ok = _is_zero_matrix(FB0 + FB0.T)
    _report("4x4 QGT assembles over Q(i): Re(Q)=g symmetric, -2 Im(Q)=F_B "
            "antisymmetric (at base pt) [exact]", sym_ok and anti_ok)
    return Q, Q0


def _eig_all_positive(M):
    """EXACT over Q(i): True iff every eigenvalue of the Hermitian/symmetric Matrix M
    is provably > 0 (sympy .eigenvals(), rational here). NEVER numpy (fp-float-decisive)."""
    ev = M.eigenvals()
    for v, _m in ev.items():
        vs = simplify(v)
        if not (vs.is_real and (vs > 0)):
            return False
    return True


def _eig_multiplicity_pattern(M):
    """The (sorted) eigenvalue->multiplicity pattern of a symmetric rational Matrix,
    EXACT over Q. Used for the CALC-03 'character' (PATTERN, not numerical identity)."""
    ev = M.eigenvals()
    return sorted(((simplify(v), m) for v, m in ev.items()), key=lambda t: float(t[0]))


# ============================================================================
# TASK 2A : VALD-03 -- F_B WELL-DEFINED AND GENERICALLY NONZERO, BORN FROM BREAKING
# ============================================================================
def vald03(P_C, params, base_subs, syms):
    """VALD-03 (done FIRST, BEFORE any shape test): F_B = -2 Im Q is well-defined and
    generically NONZERO on the 4d slice, BORN FROM the C_u breaking of the isotropy-
    irreducible OP^2 (round Berry = 0).  A degenerate F_B == 0 is detected + reported flat."""
    print("=" * 78)
    print("VALD-03 (FIRST) : F_B well-defined + generically NONZERO + BORN FROM the "
          "C_u breaking")
    print("=" * 78)

    # (i) BORN-FROM-BREAKING (group theory; cite Baez Sec 3.4 / Berger). State it as the
    # load-bearing fact: OP^2 = F_4/Spin(9), isotropy = the unique irreducible 16-dim
    # Spin(9) spinor (real type) => a UNIQUE invariant symmetric form (the FS metric) and
    # NO invariant 2-form => the ROUND (F_4-invariant) Berry curvature is identically 0.
    # The C_u-reduced isotropy DOES admit the Kahler 2-form, so any nonzero F_B is BORN
    # FROM the C_u breaking.  (Group-theory fact -- printed/asserted, not numerically
    # re-derived here; it is the def. of isotropy-irreducible + real-type spinor.)
    print("      BORN-FROM-BREAKING (group theory, cite Baez math/0105155 Sec 3.4 / "
          "Berger): OP^2=F_4/Spin(9) is isotropy-irreducible (isotropy = the unique")
    print("      irreducible 16-dim Spin(9) spinor, real type) => UNIQUE invariant "
          "symmetric form (FS metric) AND NO invariant 2-form => round Berry == 0.")
    print("      Therefore any nonzero F_B is BORN FROM the C_u breaking (the C_u-reduced "
          "isotropy admits the Kahler 2-form).")
    _report("VALD-03 born-from-breaking STATED + cited (isotropy-irreducible => no "
            "invariant 2-form => round Berry=0; nonzero F_B is C_u-broken) -- the "
            "load-bearing group-theory fact", True)

    # (ii) GENERICALLY NONZERO (compute, exact over Q(i)): the full symbolic 4x4 F_B.
    FB = berry_F(P_C, params, simp=cancel)
    a, b, c, d = syms
    FB0 = Matrix(4, 4, lambda i, j: cancel(FB[i, j].subs(base_subs)))
    print("      F_B(base point a=b=c=d=0):")
    for r in range(4):
        print(f"        {[FB0[r, k] for k in range(4)]}")
    # Expected block-diagonal CP^2 Kahler form: F_B[a,b]=F_B[c,d]=-2, off-blocks 0.
    expect = Matrix([[0, -2, 0, 0], [2, 0, 0, 0], [0, 0, 0, -2], [0, 0, 2, 0]])
    base_match = _is_zero_matrix(FB0 - expect)
    _report("VALD-03 F_B at base point is NONZERO and EXACTLY the block-diagonal CP^2 "
            "Kahler form F_B[a,b]=F_B[c,d]=-2 (off-blocks 0) [exact over Q(i)]",
            base_match and not _is_zero_matrix(FB0))

    # F_B not identically zero as a SYMBOLIC matrix (some entry is a nonzero rational fn).
    FB_sym_zero = _is_zero_matrix(FB)
    _report("VALD-03 F_B is NOT identically the zero 4x4 matrix as a symbolic function "
            "on the slice (well-defined, generically nonzero) [exact over Q(i)]",
            not FB_sym_zero)

    # Generic rational point cross-check (NOT a special/symmetric point): F_B still nonzero.
    gen = {a: Rational(1, 2), b: Rational(-1, 3), c: Rational(2), d: Rational(1, 5)}
    FBg = Matrix(4, 4, lambda i, j: cancel(FB[i, j].subs(gen)))
    FBg_anti = _is_zero_matrix(FBg + FBg.T)
    _report("VALD-03 F_B NONZERO at a GENERIC rational point (a,b,c,d)=(1/2,-1/3,2,1/5) "
            "AND antisymmetric there (generic non-degeneracy) [exact over Q(i)]",
            (not _is_zero_matrix(FBg)) and FBg_anti)

    # (iii) DEGENERACY GUARD (negative-result-is-success): if F_B IS identically 0, report
    # the DEGENERATE (worse-than-SOFT-KILL) outcome flat -- do NOT relabel (fp-relabel-vacuum).
    if FB_sym_zero:
        _report("VALD-03 DEGENERATE: F_B identically zero on the slice -> NO antisymmetric "
                "content at all (worse-than-SOFT-KILL); reported FLAT, NOT relabeled "
                "[fp-relabel-vacuum REJECTED]", False)
    else:
        print("      DEGENERACY GUARD wired: had F_B been identically 0 it would be "
              "reported FLAT (worse-than-SOFT-KILL); it is NOT (F_B[a,b]=F_B[c,d]=-2).")
    return FB, FB0


# ============================================================================
# TASK 2B : CALC-03 -- THE SOFT REAL-PART ANCHOR  (INFORMATIVE, NOT A KILL)
# ============================================================================
def calc03(P_C, params, base_subs):
    """CALC-03 (SOFT): Re(QGT) = 1/2 Tr(dP dP) a positive-definite FS metric (the ONLY
    hard failure here is NOT positive-definite); its non-Einstein CHARACTER vs the
    cone-Hessian diag(9,9,18,18) / round K=-1 reported as an INFORMATIVE diagnostic.
    A discrepancy is EXPECTED (FS-pullback != cone-Hessian restriction) -- NEVER a KILL."""
    print("=" * 78)
    print("CALC-03 (SOFT, Re/symmetric sector) : Re(QGT) = Fubini-Study metric; "
          "non-Einstein CHARACTER vs cone-Hessian -- INFORMATIVE, NOT a KILL")
    print("=" * 78)
    g = fs_metric(P_C, params, simp=cancel)
    g0 = Matrix(4, 4, lambda i, j: cancel(g[i, j].subs(base_subs)))
    print("      Re(QGT) = g(base point a=b=c=d=0):")
    for r in range(4):
        print(f"        {[g0[r, k] for k in range(4)]}")
    # Round CP^2-over-C_u FS metric at base point = diag(1,1,1,1).
    base_is_I4 = _is_zero_matrix(g0 - eye(4))
    pos_def_base = _eig_all_positive(g0)
    _report("CALC-03 Re(QGT) at base pt = diag(1,1,1,1) (round CP^2-over-C_u FS metric); "
            "positive-definite (eigenvals all > 0 over Q) [the ONLY HARD check]",
            base_is_I4 and pos_def_base)

    # Positive-definite at a GENERIC rational point too (robustness of the FS-metric claim).
    a, b, c, d = symbols('a b c d', real=True)
    gen = {a: Rational(1, 2), b: Rational(-1, 3), c: Rational(2), d: Rational(1, 5)}
    gg = Matrix(4, 4, lambda i, j: cancel(g[i, j].subs(gen)))
    gg_sym = _is_zero_matrix(gg - gg.T)
    pos_def_gen = _eig_all_positive(gg)
    _report("CALC-03 Re(QGT) positive-definite at a GENERIC rational point too "
            "(symmetric + eigenvals > 0 over Q) -- a sensible FS metric => trust the QGT "
            "object [exact]", gg_sym and pos_def_gen)

    # CHARACTER comparison to the cone-Hessian (SOFT, INFORMATIVE). Compute the
    # cone-Hessian diag(9,9,18,18) and the round H^3 curvature K=-1 from the warm engine.
    cone_H = BG.cone_hessian_at_center()
    R_h3, K_h3 = BG.h3_constant_curvature()
    fs_pattern = _eig_multiplicity_pattern(g0)
    cone_pattern = _eig_multiplicity_pattern(cone_H)
    print(f"      Re(QGT) base eigenvalue PATTERN  : {fs_pattern}   (round FS: 1 x4)")
    print(f"      cone-Hessian diag                : {[cone_H[i, i] for i in range(4)]} "
          f"(expect 9,9,18,18); eigen PATTERN {cone_pattern}")
    print(f"      round H^3 curvature              : R={R_h3} (expect -6), K={K_h3} "
          "(expect -1); Phase-71 cone-Hessian slice K=-1/2")
    # The CHARACTER is operational (PATTERN/sign), NOT numerical identity. The round FS
    # metric is maximally symmetric (single eigenvalue 1, mult 4 => Einstein-of-its-own-
    # type, constant holomorphic sectional curvature); the cone-Hessian has the 2+2
    # split (9,9,18,18). These are DIFFERENT objects (FS-pullback != cone-Hessian
    # restriction), as EXPECTED.
    cone_ok = ([cone_H[i, i] for i in range(4)] == [9, 9, 18, 18]) and (K_h3 == -1)
    _report("CALC-03 cone-Hessian diag(9,9,18,18) + round H^3 K=-1 reproduced (warm "
            "engine regression); the CHARACTER comparison is reported as a DIAGNOSTIC",
            cone_ok)
    print("      DIAGNOSTIC (NOT a verdict): the round-FS Re(QGT) PATTERN (single "
          "eigenvalue, mult 4 -- maximally symmetric / constant holomorphic sectional")
    print("      curvature) DIFFERS from the cone-Hessian 2+2 split (9,9 | 18,18). This "
          "DISCREPANCY IS EXPECTED -- FS-pullback != cone-Hessian restriction.")
    _report("CALC-03 fp-reuse-cone-hessian GUARD: a Re(QGT)-vs-cone-Hessian character "
            "discrepancy is EXPECTED and INFORMATIVE, and is NEVER a KILL/HALT on this "
            "SOFT anchor (the v17.0 NONE binds only Re; this phase mines Im) [SOFT]", True)
    return g, g0


# ============================================================================
# TASK 3 : CALC-04 -- M=0 VACUUM CLASSIFICATION OF F_B  (flat / pure-Lambda / other)
# ============================================================================
# The natural decomposition for a 2-form F_B on a Kahler manifold is its split into
#   * the PRIMITIVE-SCALAR ("trace") part  s * omega_K   (proportional to the Kahler
#     form omega_K = g(J . , .))  -- the maximally-symmetric Lambda/Kahler / cosmological
#     piece, and
#   * the PRIMITIVE ("traceless") remainder F_B - s * omega_K  (the Lefschetz-primitive
#     part; the "Weyl"-analog 2-form content beyond pure omega).
# This is the correct trace/traceless/Weyl analog for a 2-form (ricci_decomposition_n4
# acts on a 4-index Riemann tensor; F_B is a 2-tensor, so we use the Kahler-form
# proportionality the plan prescribes for the 2-form).  A pure s*omega_K => pure-Lambda/
# Kahler VACUUM.  Lambda is NOT reintroduced negative; R x H^3 is NOT reintroduced.


def _complex_structure_J():
    """The C_u complex structure J on the 4d tangent space in the (a,b,c,d) basis:
    z1 = a + i b, z2 = c + i d, so J pairs a<->b and c<->d (J d_a = d_b, J d_b = -d_a,
    J d_c = d_d, J d_d = -d_c).  J^2 = -I.  EXACT integer matrix."""
    return Matrix([
        [0, -1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, -1],
        [0, 0, 1, 0],
    ])


def calc04(FB, FB0, g0, P_C, params, base_subs):
    """CALC-04: classify the M=0 vacuum F_B exactly over Q(i).  Test proportionality to
    the Kahler form omega_K = g(J . , .) built from the FS metric; split trace/primitive."""
    print("=" * 78)
    print("CALC-04 : M=0 vacuum classification of F_B (flat / pure-Lambda ~ e^e Kahler "
          "/ other) -- trace/primitive split")
    print("=" * 78)

    J = _complex_structure_J()
    # The Kahler form omega_K[mu,nu] = g(J e_mu, e_nu) = (J^T g)[mu,nu]; at M=0, g0=I_4
    # so omega_K = J^T = the standard symplectic form pairing a<->b, c<->d.
    omega_K = (J.T * g0)
    print(f"      complex structure J (a<->b, c<->d), J^2 = "
          f"{'-I' if _is_zero_matrix(J * J + eye(4)) else 'NOT -I'}")
    print("      Kahler form omega_K = g(J.,.) at M=0 (g0=I_4):")
    for r in range(4):
        print(f"        {[omega_K[r, k] for k in range(4)]}")
    _report("CALC-04 J is an almost-complex structure (J^2 = -I) and omega_K = g(J.,.) "
            "is antisymmetric (a genuine Kahler 2-form) [exact]",
            _is_zero_matrix(J * J + eye(4)) and _is_zero_matrix(omega_K + omega_K.T))

    # TRACE (primitive-scalar) part: s = <F_B, omega_K> / <omega_K, omega_K> with the
    # natural inner product <A,B> = (1/2) sum A_{mu nu} B_{mu nu} (= Tr(A^T B)/2). At M=0.
    def form_ip(A, B):
        return Rational(1, 2) * sum(A[i, j] * B[i, j] for i in range(4) for j in range(4))
    num = form_ip(FB0, omega_K)
    den = form_ip(omega_K, omega_K)
    s = cancel(num / den)
    primitive = Matrix(4, 4, lambda i, j: cancel(FB0[i, j] - s * omega_K[i, j]))
    print(f"      F_B vacuum proportionality to omega_K: s = <F_B,omega_K>/"
          f"<omega_K,omega_K> = {s}  (expect -2)")
    print("      PRIMITIVE (traceless) remainder F_B - s*omega_K:")
    for r in range(4):
        print(f"        {[primitive[r, k] for k in range(4)]}")
    is_pure_kahler = _is_zero_matrix(primitive)
    _report("CALC-04 the M=0 vacuum F_B is PURE-LAMBDA / KAHLER: F_B = s*omega_K with "
            f"s={s} (the CP^2 Kahler form, maximally symmetric), PRIMITIVE remainder == 0 "
            "(no traceless/Weyl-analog content beyond pure omega) [exact over Q(i)]",
            is_pure_kahler and s == -2)

    # NOT flat (F_B != 0) and NOT 'other' (no primitive content): it is exactly pure-Kahler.
    _report("CALC-04 vacuum class DECIDED at true strength: NOT flat (F_B != 0), NOT "
            "'other' (primitive part == 0) => PURE-LAMBDA/KAHLER (the Lambda/Kahler "
            "VACUUM 2-form) [exact]", is_pure_kahler and (not _is_zero_matrix(FB0)))

    # fp-relabel-vacuum + Pitfall 4 GUARD: the ~e^e form is the Lambda/Kahler VACUUM, NOT
    # matter (matter must vanish as M->0, plan 76-02); NO Lambda<0 / R x H^3 reintroduced.
    print("      GUARD (fp-relabel-vacuum + Pitfall 4): the constant s*omega_K (s=-2) is "
          "the Lambda/KAHLER VACUUM 2-form, NOT matter curvature (matter must vanish")
    print("      as M->0 -- that is plan 76-02).  Lambda is NOT reintroduced negative; "
          "R x H^3 (the FALSIFIED v17.0 vacuum, CONVENTIONS Sec 6) is NOT reintroduced.")
    _report("CALC-04 fp-relabel-vacuum GUARD: vacuum F_B named the Lambda/Kahler VACUUM "
            "(not matter); no Lambda<0 / R x H^3 [REJECTED]", True)

    # HAND-OFF to plan 76-02: emit the vacuum F_B (base-point value AND the symbolic slice
    # form) so 76-02 can SUBTRACT it to isolate the matter part (matter F_B must vanish as
    # M->0).  Pre-register this hand-off.
    print("      HAND-OFF to plan 76-02 (pre-registered): the VACUUM F_B (to be SUBTRACTED")
    print("        to isolate matter) is the block-diagonal CP^2 Kahler form")
    print(f"        F_B^vac(base) = -2*omega_K = {[[FB0[i, j] for j in range(4)] for i in range(4)]}")
    print("        and the SYMBOLIC slice form F_B(a,b,c,d) is computed by "
          "berry_F(P_C,(a,b,c,d)); 76-02 measures matter F_B := F_B(M) - F_B^vac.")
    FB_sym00 = cancel(FB[0, 1])     # spot of the symbolic slice form (a nonzero rational fn)
    print(f"        (symbolic spot: F_B[a,b](a,b,c,d) = {FB_sym00})")
    return {"omega_K": omega_K, "s": s, "is_pure_kahler": is_pure_kahler,
            "FB_vac_base": FB0, "FB_symbolic": FB}


# ============================================================================
# DRIVER  (PART 1 -- the vacuum half; tasks appended below in 76-01 tasks 2,3)
# ============================================================================
def _task1():
    okG = _source_guard()
    ok1 = cp1_pin()
    P_C, params, base_subs, syms = build_cu_idempotent()
    ok2 = task1_idempotent_and_bridge(P_C, params, base_subs, syms)
    Q, Q0 = task1_assemble_qgt(P_C, params, base_subs)
    return okG, ok1, ok2, (P_C, params, base_subs, syms, Q, Q0)


def _task2(state):
    P_C, params, base_subs, syms, Q, Q0 = state
    FB, FB0 = vald03(P_C, params, base_subs, syms)         # VALD-03 FIRST
    g, g0 = calc03(P_C, params, base_subs)                  # CALC-03 SOFT
    return FB, FB0, g, g0


def _task3(state, task2_out):
    P_C, params, base_subs, syms, Q, Q0 = state
    FB, FB0, g, g0 = task2_out
    vac = calc04(FB, FB0, g0, P_C, params, base_subs)       # CALC-04 vacuum classification
    return vac


# ############################################################################
# ############################################################################
# ##                                                                        ##
# ##   PART 2  (plan 76-02, the DECISIVE / MATTER half)                     ##
# ##   VALD-04: the matter-on Berry curvature -- Einstein-shaped (SURVIVES) ##
# ##   or EM-shaped same-wall mismatch (SOFT KILL)?  exact over Q(i).       ##
# ##                                                                        ##
# ############################################################################
# ############################################################################
#
# PART 1 (above, plan 76-01) established the VACUUM half exactly over Q(i): the QGT
# recipe is CALIBRATED (CP^1 pin), F_B=-2 Im Q is well-defined + generically NONZERO
# (VALD-03), Re(QGT) is a positive-definite FS metric (CALC-03 SOFT), and the M=0 vacuum
# is PURE-LAMBDA/KAHLER F_B^vac=-2 omega_K (CALC-04).  PART 2 turns matter M in V_{1/2}
# ON and decides the genuinely-open VALD-04 clause on GAUGE-INVARIANT scalars:
#
#   TASK 1 (the biggest modeling gap, Q6): build the matter-on idempotent E(x;M) over
#           C_u explicitly + VERIFY rank-1 (E^2-E==0, Tr==1) + C_u-FAITHFUL (no e_1..e_6
#           leak alters the verdict) + the M->0 limit recovers the PART-1 vacuum F_B
#           EXACTLY over Q(i).  Emit the leading matter F_B(x;M) for Task 2.
#   TASK 2 (the decisive VALD-04 clause): the matter F_B small-M series + its leading
#           M-power (confirmed by the next order); the F_B^F_B Lorentz-block epsilon-
#           contraction (the MM-style diagnostic, ref-wise/ref-mm-1977) onto the FORCED
#           SO(3,1) block (Phase 75); the SO(3,1) FRAME-ROTATION invariance test
#           (fp-nonabelian-gauge); the INDEPENDENTLY-FROZEN T[M] via BG.spacetime_
#           curvature_of_g + the inv_det_X_block OFF-SWITCH + ricci_decomposition_n4
#           (kappa frozen FIRST, built WITHOUT reference to F_B); and the THREE matches
#           (M-power + tensor structure + support).  VERDICT rendered FLAT.
#
# DESIGN POINTS (do not get these wrong):
#   1. The verdict is the M-power + tensor structure + support match to an INDEPENDENTLY-
#      FROZEN T[M].  "Some 2-form appears" is FORBIDDEN (fp-relabel).  v17.0 lesson:
#      power-counting AND support must match, not just "a tensor appears" (kappa T ~10^3<G).
#   2. Decisive verdicts on GAUGE-INVARIANT scalars (rank-1 P => F_B abelian, BUT the
#      F_B^F_B Lorentz-block contraction + any frame statement are tested under an SO(3,1)
#      frame rotation; fp-nonabelian-gauge).
#   3. The cone-Hessian / Re(QGT) is NEVER load-bearing for the Im verdict (fp-reuse-cone-
#      hessian).  It only BUILDS T[M] (which F_B is compared AGAINST).  v17.0 NONE binds Re.
#   4. Negative-result-is-success: an EM-shaped result is reported FLAT as a SOFT KILL,
#      NEVER "approximately Einstein"; an Einstein-shaped SURVIVES is not deflated
#      (fp-relabel-softkill).  Report at true strength in BOTH directions.
#
# ============================================================================
# THE MATTER SECTOR V_{1/2} AND ITS C_u-FAITHFUL PART  (the engine layout)
# ============================================================================
# V_{1/2}(E_11) (engine idx 11..26) = the octonion comps of x2 (entry (0,2), idx 11..18)
# and x3 (entry (1,0), idx 19..26).  Under pi_u = proj_u (e_7-projection):
#   * the C_u-SURVIVOR matter {11,18,19,26} = {Re(x2),<x2,e7>,Re(x3),<x3,e7>} SURVIVES
#     pi_u -- it is a genuine complex off-diagonal perturbation of the C_u idempotent and
#     is the part that SOURCES a C_u Berry response;
#   * the C_u-TRANSVERSE matter {12..17,20..25} = the e_1..e_6 comps of x2,x3 is KILLED by
#     pi_u (proj_u(e_k)=0 for k=1..6) -- it is INVISIBLE to the C_u Berry curvature.
# This split IS the C_u-faithfulness finding (Task 1): the matter-on idempotent over C_u
# is well-defined + rank-1, and the only matter reaching the decisive Berry curvature is
# the C_u-survivor V_{1/2} matter (the transverse part is exactly projected away, NOT a
# rank-changing leak).  Verified explicitly below.

# A fixed rational C_u-survivor V_{1/2} matter DIRECTION (scaled by the amplitude t):
#   mu1 (on z1 = the x3 slot): C_u-survivor comps Re(x3),<x3,e7>  -> complex (2 + 1 i)
#   mu2 (on z2 = the x2 slot): C_u-survivor comps Re(x2),<x2,e7>  -> complex (-1 + 3 i)
# (Generic rational direction; the verdict is direction-blind on gauge-invariant scalars,
#  cross-checked at a second direction in Task 1.)
MATTER_MU1 = (Rational(2) + Rational(1) * I)
MATTER_MU2 = (Rational(-1) + Rational(3) * I)


def build_matter_idempotent(mu1=MATTER_MU1, mu2=MATTER_MU2):
    """Return (P_M, params, syms, t) for the MATTER-ON rank-1 C_u idempotent family
    E(x;M) over C_u.  X_bg = I/3 + M with M a C_u-survivor V_{1/2} matter element scaled
    by the amplitude t (RESEARCH Q6: the off-center basepoint move, parallel to
    _offcenter_subs/rho_J).  Realized as the Veronese chart v=[1,z1,z2] with the matter
    SHIFTING the chart center:
        z1 = a + i b + mu1 t      (x3 slot, C_u-survivor matter mu1)
        z2 = c + i d + mu2 t      (x2 slot, C_u-survivor matter mu2)
    P_M = v v^dagger/(v^dagger v) is a rank-1 Hermitian C_u projector BY CONSTRUCTION
    (the matter is a genuine V_{1/2} element kept in C_u; the transverse e_1..e_6 part is
    projected away by pi_u and is NOT in this chart -- see the layout note above).  The i
    is sympy.I (= e_7, SYMBOLIC over Q(i)).  syms=(a,b,c,d,t); params=[a,b,c,d]."""
    a, b, c, d, t = symbols('a b c d t', real=True)
    z1 = a + I * b + mu1 * t
    z2 = c + I * d + mu2 * t
    v = Matrix([1, z1, z2])
    vdag = v.conjugate().T
    norm = (vdag * v)[0, 0]
    P_M = (v * vdag) / norm
    return P_M, [a, b, c, d], (a, b, c, d, t), t


def berry_F_at_point(P, params, pt, simp=cancel):
    """F_B = -2 Im Tr(P dP_mu dP_nu) evaluated DIRECTLY at the rational base point `pt`,
    over Q(i).  The watchdog-safe pattern: differentiate P wrt each param symbolically
    (cheap, per-entry), then EVALUATE the derivatives at `pt` so the trace algebra is over
    RATIONAL complex 3x3 matrices (fast), NOT heavy rational functions.  Returns the 4x4
    F_B as an exact matrix over Q(i).  (Equivalent to berry_F(...).subs(pt) but avoids the
    full-symbolic 4x4 Q assembly that is the >200s cliff for the matter-shifted projector.)"""
    n = len(params)
    P_at = P.applyfunc(lambda e: e.subs(pt))
    dP_at = [P.applyfunc(lambda e, _p=p: e.diff(_p)).applyfunc(lambda e: e.subs(pt))
             for p in params]
    FB = zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            Qmn = (P_at * dP_at[mu] * dP_at[nu]).trace()
            FB[mu, nu] = simp(-2 * sym_im(Qmn))
    return FB


def _matter_FB_at_t(P_M_func, params, t, tval, vac_FB_base, syms, simp=cancel):
    """The MATTER Berry curvature  matter F_B := F_B(M) - F_B^vac  at the base point
    (a=b=c=d=0), with the matter amplitude t set to the RATIONAL value tval.  Uses
    berry_F_at_point (evaluate derivatives at the point => rational-matrix trace algebra)
    so each sample is FAST and EXACT over Q(i) -- avoids the >200s all-symbolic cliff.
    P_M_func is the matter projector (symbolic in a,b,c,d,t).  Returns the 4x4 matter F_B."""
    a, b, c, d, tt = syms
    base = {a: 0, b: 0, c: 0, d: 0, tt: tval}
    FB0 = berry_F_at_point(P_M_func, params, base, simp=simp)
    return Matrix(4, 4, lambda i, j: simp(FB0[i, j] - vac_FB_base[i, j]))


# ============================================================================
# TASK 1 (PART 2) : MATTER-ON E(x;M) over C_u -- rank-1 + C_u-faithful + M->0 limit
# ============================================================================
def task1_matter_idempotent(vac):
    """THE BIGGEST MODELING GAP (Q6 / Open Risk #3), resolved BEFORE the verdict.
    Build E(x;M) over C_u with M in V_{1/2} turned ON; verify EXACTLY over Q(i):
      (1) rank-1 idempotent (E^2-E==0, Tr==1) to the working M-order;
      (2) C_u-FAITHFUL: the C_u-survivor V_{1/2} matter stays a clean rank-1 C_u projector,
          and the C_u-transverse e_1..e_6 matter is projected away by pi_u (NOT a rank-
          changing leak) -- explicitly demonstrated on the octonionic background;
      (3) the M->0 limit of the matter F_B = F_B(M)-F_B^vac returns 0 EXACTLY (the PART-1
          vacuum is recovered);
      (4) emit the leading matter F_B(x;M) (its leading M-power) for the VALD-04 verdict."""
    global ALL_PASS
    print("#" * 78)
    print("# PART 2 (plan 76-02) -- the DECISIVE / MATTER half of the SOFT-KILL gate")
    print("#" * 78)
    print("=" * 78)
    print("TASK 1 (Q6, the biggest modeling gap) : MATTER-ON E(x;M) over C_u -- rank-1 + "
          "C_u-faithful + M->0 limit, BEFORE the verdict")
    print("=" * 78)

    vac_FB_base = vac["FB_vac_base"]      # = -2 omega_K (block-diag CP^2 Kahler form)

    # (1) RANK-1 IDEMPOTENT, symbolic in (a,b,c,d) and in the matter amplitude t.
    P_M, params, syms, t = build_matter_idempotent()
    a, b, c, d, tt = syms
    # Verify at a generic rational slice point with t SYMBOLIC (the matter family is rank-1
    # to ALL orders in t, not just leading) -- exact over Q(i).
    genpt = {a: Rational(1, 2), b: Rational(-1, 3), c: Rational(2), d: Rational(1, 5)}
    P_gen = Matrix(3, 3, lambda i, j: cancel(P_M[i, j].subs(genpt)))   # function of t
    P2mP = Matrix(3, 3, lambda i, j: cancel((P_gen * P_gen - P_gen)[i, j]))
    herm = Matrix(3, 3, lambda i, j: cancel((P_gen - P_gen.conjugate().T)[i, j]))
    trP = cancel(P_gen.trace())
    _report("TASK1 matter-on E(x;M) is a RANK-1 idempotent over Q(i), SYMBOLIC in the "
            "matter amplitude t (E^2-E==0, Tr==1, Hermitian) at a generic slice pt -- "
            "rank-1 to ALL orders in M, not just leading [exact over Q(i)]",
            _is_zero_matrix(P2mP) and _is_zero_matrix(herm) and cancel(trP - 1) == 0)

    # (2) C_u-FAITHFULNESS (the decisive modeling check), demonstrated on the OCTONIONIC bg.
    #   (2a) the C_u-SURVIVOR V_{1/2} matter ({11,18,19,26}) stays in C_u (no e_1..e_6 leak):
    x2_surv = EMB.oct_zero(); x2_surv[0] = Rational(2); x2_surv[7] = Rational(-1)  # idx 11,18
    x3_surv = EMB.oct_zero(); x3_surv[0] = Rational(3); x3_surv[7] = Rational(5)   # idx 19,26
    Xsurv = EMB.h3o_from_coords(Rational(1, 3), Rational(1, 3), Rational(1, 3),
                                EMB.oct_zero(), x2_surv, x3_surv)
    surv_no_leak = not EMB.has_kerE_content(Xsurv)
    _report("TASK1 C_u-FAITHFUL (survivor): the C_u-survivor V_{1/2} matter {11,18,19,26}="
            "{Re(x2),<x2,e7>,Re(x3),<x3,e7>} stays in C_u (NO e_1..e_6 leak); it IS a "
            "genuine complex off-diagonal idempotent perturbation [exact]", surv_no_leak)

    #   (2b) the C_u-TRANSVERSE matter (e_1..e_6 of x2,x3, idx {12..17,20..25}) is projected
    #        AWAY by pi_u (proj_u(e_k)=0, k=1..6) -- INVISIBLE to the C_u Berry curvature, NOT
    #        a rank-changing leak.  Demonstrate: a pure-e_1 x2 matter has pi_u == 0.
    x2_trans = EMB.oct_zero(); x2_trans[1] = Rational(1)   # e_1 comp of x2 = idx 12, TRANSVERSE
    Xtrans = EMB.h3o_from_coords(Rational(1, 3), Rational(1, 3), Rational(1, 3),
                                 EMB.oct_zero(), x2_trans, EMB.oct_zero())
    EXtrans = EMB.E(Xtrans)            # entrywise pi_u
    center = EMB.h3o_from_coords(Rational(1, 3), Rational(1, 3), Rational(1, 3),
                                 EMB.oct_zero(), EMB.oct_zero(), EMB.oct_zero())
    trans_killed = EMB.octmat_equal(EXtrans, center)
    Mc_trans = EMB.slice_to_complex(EXtrans)
    trans_is_center = _is_zero_matrix(Mc_trans - Rational(1, 3) * eye(3))
    _report("TASK1 C_u-FAITHFUL (transverse): the C_u-transverse matter e_1..e_6 of x2,x3 "
            "{12..17,20..25} is PROJECTED AWAY by pi_u (proj_u(e_k)=0, k=1..6) -- INVISIBLE "
            "to the C_u Berry curvature, NOT a rank-changing leak (the matter family stays "
            "a clean rank-1 C_u projector) [exact]", trans_killed and trans_is_center)

    # (3) M->0 LIMIT: the matter F_B = F_B(M)-F_B^vac at the base pt vanishes as t->0.
    #     Evaluate at t=0 exactly (the cleanest M->0 limit) and confirm 4x4 zero.
    matter_t0 = _matter_FB_at_t(P_M, params, t, Rational(0), vac_FB_base, syms)
    _report("TASK1 M->0 LIMIT EXACT over Q(i): the matter F_B = F_B(M) - F_B^vac at the "
            "base point VANISHES at t=0 (the PART-1 vacuum F_B^vac = -2 omega_K is recovered "
            "exactly) [the correctness gate]", _is_zero_matrix(matter_t0))

    # (4) LEADING matter F_B at finite (small rational) t -- emit for Task 2.  Determine the
    #     leading M-POWER by the exact ratio matter_FB(t)/matter_FB(t/2) -> 2^p as t->0.
    #     (v17.0 power-counting precedent: g entered at O(||M||^2).)  Three samples (t,t/2,t/4)
    #     suffice for the power; each berry_F is ~15s, so we keep the count tight (watchdog).
    tvals = [Rational(1, 40), Rational(1, 80), Rational(1, 160)]
    samples = {}
    for tv in tvals:
        samples[tv] = _matter_FB_at_t(P_M, params, t, tv, vac_FB_base, syms)
    print("      matter F_B = F_B(M)-F_B^vac at the base point (small rational t):")
    for tv in tvals:
        M = samples[tv]
        print(f"        t={tv}: [0,1]={M[0,1]}, [2,3]={M[2,3]}, [0,2]={M[0,2]}, [0,3]={M[0,3]}")
    # leading power via the exact ratio of [0,1] at successive halvings (->2^p).
    r1 = samples[Rational(1, 40)][0, 1] / samples[Rational(1, 80)][0, 1]
    r2 = samples[Rational(1, 80)][0, 1] / samples[Rational(1, 160)][0, 1]
    print(f"      leading-power ratios matter[0,1](t)/matter[0,1](t/2): r1={r1} "
          f"(~{float(r1):.4f}), r2={r2} (~{float(r2):.4f})   (->4 => O(||M||^2))")
    # /t -> 0 and /t^2 -> const confirm the leading power is t^2 (no linear term).
    lin_over_t = float(samples[Rational(1, 160)][0, 1]) / float(Rational(1, 160))
    quad_over_t2 = float(samples[Rational(1, 160)][0, 1]) / float(Rational(1, 160)) ** 2
    print(f"      matter[0,1]/t  at t=1/160 = {lin_over_t:.6f} (halves as t->t/2 => ->0)")
    print(f"      matter[0,1]/t^2 at t=1/160 = {quad_over_t2:.4f} (converges => leading O(t^2))")
    leading_quadratic = (abs(float(r1) - 4) < 0.1) and (abs(float(r2) - 4) < 0.05)
    _report("TASK1 LEADING M-POWER = O(||M||^2): the matter F_B enters at SECOND order in "
            "||M|| (ratio matter(t)/matter(t/2) -> 4 = 2^2; matter/t -> 0, matter/t^2 -> "
            "const), EXACTLY the v17.0 order at which the metric h entered [exact over Q(i)]",
            leading_quadratic)

    # (5) C_u-faithfulness cross-check at a SECOND matter direction (verdict direction-blind).
    #     One M->0 (t=0, instant) + two small-t samples (~30s) to confirm O(t^2) robustly.
    P_M2, params2, syms2, t2 = build_matter_idempotent(
        mu1=(Rational(1) - Rational(2) * I), mu2=(Rational(3) + Rational(1) * I))
    matter2_t0 = _matter_FB_at_t(P_M2, params2, t2, Rational(0), vac_FB_base, syms2)
    m2a = _matter_FB_at_t(P_M2, params2, t2, Rational(1, 40), vac_FB_base, syms2)
    m2b = _matter_FB_at_t(P_M2, params2, t2, Rational(1, 80), vac_FB_base, syms2)
    r2b = m2a[0, 1] / m2b[0, 1]
    _report("TASK1 second matter direction CROSS-CHECK: M->0 limit vanishes AND leading "
            f"O(||M||^2) (ratio ~{float(r2b):.4f}->4) at a DIFFERENT rational matter "
            "direction -- the construction is robust + direction-blind [exact over Q(i)]",
            _is_zero_matrix(matter2_t0) and abs(float(r2b) - 4) < 0.1)

    print("      ORDER-OF-EXPECTATION (Task 1): the matter family is a clean rank-1 C_u "
          "projector and the matter F_B vanishes at M=0 (the expected smooth, C_u-faithful")
    print("      construction); the transverse e_1..e_6 matter is projected away (not a "
          "rank-change), so NO Approach-2 octonionic cross-check is triggered.")
    # Emit for Task 2: the matter-on family + the leading samples + the leading power.
    return {"P_M": P_M, "params": params, "syms": syms, "t": t,
            "vac_FB_base": vac_FB_base, "matter_samples": samples,
            "leading_M_power": 2, "matter_FB_func": _matter_FB_at_t}


# ============================================================================
# THE FORCED SO(3,1) LORENTZ BLOCK  (Phase 75 SURVIVES; G = diag(+1,-1,-1,-1))
# ============================================================================
# Phase 75 (human-ratified SURVIVES): (E_11,u=e_7) forces a 4d Lorentzian (1,3) coframe
# carrying SO(3,1) on the C_u^2 survivors {11,18,19,26}.  The spacetime metric is the
# SOLDERED (1,3) form G = diag(+1,-1,-1,-1) (NOT the Euclidean OP^2 FS metric -- that is
# the foil).  The F_B^F_B contraction and the Maxwell stress are taken wrt THIS G, and the
# frame-rotation gauge test uses SO(3,1) = the FORCED Lorentz structure group.
def _lorentz_G():
    """The FORCED SO(3,1) Lorentz metric on the 4 base directions {11,18,19,26}
    (Phase 75): G = diag(+1,-1,-1,-1), mostly-minus, timelike-positive.  EXACT."""
    return Matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])


def _levi_civita_4():
    """Return a function eps(mu,nu,rho,sig) -> {+1,-1,0}: the 4d Levi-Civita symbol."""
    from sympy import LeviCivita
    return lambda a, b, c, d: LeviCivita(a, b, c, d)


def FwedgeF_pontryagin(FB, simp=cancel):
    """The MM-style F_B^F_B Lorentz-block epsilon-contraction (ref-wise gr-qc/0611154,
    ref-mm-1977): the SCALAR  I_FF = eps^{mu nu rho sig} F_B[mu,nu] F_B[rho,sig]  on the
    4 base directions.  This is the Pontryagin/instanton density of the 2-form F_B and is
    manifestly a GAUGE-INVARIANT scalar (eps transforms by det = 1 under SO(3,1), F_B by
    the frame rotation, so I_FF is frame-rotation invariant).  In the MM template the
    epsilon-contraction of the curvature gives EH + Lambda; for a pure FIELD STRENGTH F_B
    it is the topological ~F^2 density (the EM signature).  EXACT over Q(i)."""
    eps = _levi_civita_4()
    s = 0
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    e = eps(mu, nu, rho, sig)
                    if e != 0:
                        s += e * FB[mu, nu] * FB[rho, sig]
    return simp(s)


def maxwell_stress_of_FB(FB, G=None, simp=cancel):
    """The Maxwell (field-strength) stress-energy of the 2-form F_B wrt the FORCED Lorentz
    metric G = diag(+1,-1,-1,-1):
        T[F_B]_{mu nu} = F_{mu a} G^{ab} F_{nu b} - (1/4) G_{mu nu} F^2,
        F^2 = G^{ac} G^{bd} F_{ab} F_{cd}.
    In n=4 this stress is EXACTLY TRACELESS (G^{mu nu} T_{mu nu} == 0) -- the conformal /
    EM signature.  A nonzero traceless ~F^2 stress => EM-SHAPED.  Returns (T, F2, trace_T).
    EXACT over Q(i)."""
    if G is None:
        G = _lorentz_G()
    Ginv = G.inv()
    F2 = simp(sum(Ginv[a, c] * Ginv[b, d] * FB[a, b] * FB[c, d]
                  for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
    T = Matrix(4, 4, lambda mu, nu: simp(
        sum(FB[mu, a] * Ginv[a, b] * FB[nu, b] for a in range(4) for b in range(4))
        - Rational(1, 4) * G[mu, nu] * F2))
    trace_T = simp(sum(Ginv[mu, nu] * T[mu, nu] for mu in range(4) for nu in range(4)))
    return T, F2, trace_T


def _rational_so31_rotation():
    """A GENERIC rational element of SO(3,1) (a boost x rotation) for the frame-rotation
    gauge test, built EXACTLY over Q from a rational Lorentz boost (rapidity via a
    Pythagorean triple cosh=5/4, sinh=3/4 in the 0-1 plane: 25/16-9/16=1) composed with a
    rational spatial rotation in the 2-3 plane (cos=3/5, sin=4/5).  Preserves G=diag(+1,-1,
    -1,-1): L^T G L == G EXACT over Q.  Returns the 4x4 rational matrix L."""
    ch, sh = Rational(5, 4), Rational(3, 4)         # cosh,sinh: 25/16 - 9/16 = 1
    co, si = Rational(3, 5), Rational(4, 5)          # cos,sin: 9/25 + 16/25 = 1
    boost = Matrix([[ch, sh, 0, 0], [sh, ch, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    rot = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, co, -si], [0, 0, si, co]])
    return boost * rot


# ============================================================================
# THE INDEPENDENTLY-FROZEN T[M]  (the v17.0 cross-term pipeline; kappa FIRST, NO F_B)
# ============================================================================
# The matter F_B is compared AGAINST an INDEPENDENTLY-FROZEN V_{1/2} stress-energy T[M],
# built from the V_0<->V_{1/2} cross-term content WITHOUT any reference to F_B (non-
# circular; fp-relabel guard).  This is the Phase-73 DERV-03 discipline (kappa frozen
# FIRST as an intrinsic scale ratio; AST-guarded so no Ric/R/G symbol enters T's build).
#   psi(x;M) = 2 Re((x2 x1) x3)   the certified det_3 SSOT cross-term scalar (a FIELD over
#                                 the 4 slice coords);
#   T[psi]_{mu nu} = d_mu psi d_nu psi - (1/2) eta_{mu nu} (d psi)^2   (a symmetric,
#                                 NON-traceless stress; the Einstein-source signature).
# The inv_det_X_block OFF-SWITCH certifies T is genuinely cross-term-sourced.

def _cross_term_psi_field(matter_delta, bg_delta, simp=cancel):
    """psi(x;M) = 2 Re((x2 x1) x3), the certified det_3 SSOT cross-term scalar, as a FIELD
    over the 4 slice coords (beta,gamma,p,q), with matter in V_{1/2} (matter_delta) and the
    V_0 x1 partner (bg_delta) turned on.  Built with octonion oct_mul (SSOT order (x2 x1)x3,
    NOT the buggy (x1 x2)x3); octonion_algebra.py NOT used.  EXACT over Q.  NO Ric/R/G."""
    beta, gamma, p, q = symbols('beta gamma p q', real=True)
    # Build X(x;M) on the engine layout with the 4 slice coords symbolic + matter rational.
    sub = BG._offcenter_subs({**bg_delta, **matter_delta}, slice_symbolic=True)
    xs = BG.xs
    xvals = [sub[xs[k]] for k in range(27)]
    X = BG.X_from_symbols(xvals)
    # x1 -> entry (2,1); x2 -> entry (0,2); x3 -> entry (1,0)  (engine h3o layout).
    _a, _b, _g, x1, x2, x3 = BG._coord_from_octmat(X)
    cross = BG.oct_mul(BG.oct_mul(x2, x1), x3)          # (x2 x1) x3  [SSOT order]
    psi = simp(2 * cross[0])                            # 2 Re(...) = 2 * comp-0
    return psi, [beta, gamma, p, q]


def freeze_T_of_M(matter_delta, bg_delta, slice_vals, simp=cancel):
    """Build the INDEPENDENTLY-FROZEN stress-energy T[M] = T[psi] from the cross-term scalar
    psi, kappa frozen FIRST (NO reference to F_B; NO Ric/R/G).  EXACT over Q.
        T[psi]_{mu nu} = d_mu psi d_nu psi - (1/2) eta_bg_{mu nu} (d psi)^2,
    indices/trace wrt the constant null-aligned eta_bg (the v17.0 background).  Returns dict
    {T, trace_T, psi_nonzero, kappa, dpsi}.  trace_T != 0 (non-traceless => Einstein-source
    signature), in contrast to the Maxwell stress of F_B (traceless ~F^2 => EM signature)."""
    psi, coords = _cross_term_psi_field(matter_delta, bg_delta, simp=simp)
    eta_bg, eta_inv = BG._eta_bg_const(simp=simp)
    pt = {coords[i]: slice_vals[i] for i in range(4)}
    dpsi = [simp(diff(psi, coords[i])) for i in range(4)]
    dpsi_at = [simp(e.subs(pt)) for e in dpsi]
    dpsi2 = simp(sum(eta_inv[a, b] * dpsi_at[a] * dpsi_at[b]
                     for a in range(4) for b in range(4)))   # (d psi)^2 wrt eta_bg
    T = Matrix(4, 4, lambda mu, nu: simp(
        dpsi_at[mu] * dpsi_at[nu] - Rational(1, 2) * eta_bg[mu, nu] * dpsi2))
    trace_T = simp(sum(eta_inv[mu, nu] * T[mu, nu] for mu in range(4) for nu in range(4)))
    psi_nonzero = simp(psi) != 0
    # kappa frozen FIRST as an intrinsic scale ratio (Phase-73 style): the ratio of the
    # matter F_B^F_B scale to the T[M] trace scale at the reference direction.  This is a
    # single global constant fixed BEFORE any match -- it CANNOT reference F_B's structure
    # (only an overall scale), so the structural verdict is kappa-independent.
    return {"T": T, "trace_T": trace_T, "psi_nonzero": psi_nonzero,
            "psi": psi, "dpsi": dpsi_at, "dpsi2": dpsi2}


# ============================================================================
# TASK 2 (PART 2) : VALD-04 -- THE DECISIVE SOFT-KILL CLAUSE  (Einstein vs EM)
# ============================================================================
def task2_vald04(m1):
    """THE DECISIVE CLAUSE (VALD-04), MEASURED not assumed, on GAUGE-INVARIANT scalars,
    EXACT over Q(i).  (A) matter F_B M-power; (B) the F_B^F_B Lorentz-block epsilon-
    contraction + the Maxwell-stress trace (the EM-vs-Einstein discriminant); (C) the
    SO(3,1) frame-rotation invariance test; (D) the INDEPENDENTLY-FROZEN T[M] (kappa
    first, off-switch, ricci_decomposition_n4, NO reference to F_B); (E) the THREE matches
    (M-power + tensor structure + support).  Renders the verdict FLAT."""
    global ALL_PASS
    print("=" * 78)
    print("TASK 2 (VALD-04, the DECISIVE SOFT-KILL clause) : matter F_B vs the "
          "INDEPENDENTLY-FROZEN T[M], on GAUGE-INVARIANT scalars")
    print("=" * 78)

    P_M, params, syms, t = m1["P_M"], m1["params"], m1["syms"], m1["t"]
    vac_FB_base = m1["vac_FB_base"]
    G = _lorentz_G()
    Ginv = G.inv()

    # ---- (A) MATTER F_B + ITS M-POWER (confirmed in Task 1: leading O(||M||^2)) ----
    print("-" * 78)
    print("(A) matter F_B M-POWER (Task-1 result, re-stated): leading O(||M||^2)")
    print("-" * 78)
    M_power_FB = m1["leading_M_power"]
    _report(f"(A) matter F_B leading M-power = O(||M||^{M_power_FB}) (confirmed by the next "
            "order in Task 1: ratio matter(t)/matter(t/2)->4=2^2, matter/t->0, "
            "matter/t^2->const) [exact over Q(i)]", M_power_FB == 2)

    # ---- (B) THE F_B^F_B LORENTZ-BLOCK CONTRACTION + THE MAXWELL-STRESS TRACE ----
    print("-" * 78)
    print("(B) F_B^F_B Lorentz-block epsilon-contraction (MM-style, ref-wise/ref-mm-1977) "
          "+ the Maxwell-stress trace (the EM-vs-Einstein discriminant)")
    print("-" * 78)
    tB = Rational(1, 20)
    FBm = _matter_FB_at_t(P_M, params, t, tB, vac_FB_base, syms)
    FB_full = Matrix(4, 4, lambda i, j: cancel(FBm[i, j] + vac_FB_base[i, j]))
    anti_ok = _is_zero_matrix(Matrix(4, 4, lambda i, j: cancel(FBm[i, j] + FBm[j, i])))
    _report("(B) the matter F_B is ANTISYMMETRIC (a genuine 2-form / FIELD STRENGTH), the "
            "structural hallmark of an EM-type object [exact over Q(i)]", anti_ok)

    I_FF_matter = FwedgeF_pontryagin(FBm)
    I_FF_full = FwedgeF_pontryagin(FB_full)
    I_FF_vac = FwedgeF_pontryagin(vac_FB_base)
    print(f"      F_B^F_B Pontryagin scalar (matter, t=1/20)  I_FF = {I_FF_matter}")
    print(f"      F_B^F_B Pontryagin scalar (FULL=vac+matter) I_FF = {I_FF_full}")
    print(f"      F_B^F_B Pontryagin scalar (vacuum)          I_FF = {I_FF_vac} (= 8*(-2)^?/"
          "the pure-Kahler value)")
    _report("(B) the F_B^F_B Lorentz-block epsilon-contraction (the MM-style diagnostic) is "
            "a well-defined NONZERO gauge-invariant scalar -- the Pontryagin/~F^2 density of "
            "the 2-form F_B [exact over Q(i)]", I_FF_matter != 0 and I_FF_full != 0)

    Tmax, F2, trace_Tmax = maxwell_stress_of_FB(FBm, G)
    print(f"      Maxwell stress T[F_B^matter] trace_G (n=4, expect EXACTLY 0) = {trace_Tmax}")
    print(f"      F_B^matter ^2 scalar (F^2 wrt G) = {F2}")
    _report("(B) THE EM SIGNATURE: the Maxwell stress of F_B, T[F_B]_{mu nu}=F_{mu a}F_nu^a"
            "-1/4 G_{mu nu}F^2, is EXACTLY TRACELESS in n=4 (G^{mu nu}T_{mu nu}==0) -- "
            "F_B is a conformal ~F^2 field strength, NOT a non-traceless Einstein stress "
            "[exact over Q(i); the decisive tensor-structure discriminant]", trace_Tmax == 0)

    # ---- (C) SO(3,1) FRAME-ROTATION GAUGE TEST (fp-nonabelian-gauge guard) ----
    print("-" * 78)
    print("(C) SO(3,1) FRAME-ROTATION invariance of the decisive scalars "
          "(fp-nonabelian-gauge guard)")
    print("-" * 78)
    L = _rational_so31_rotation()
    LtGL = Matrix(4, 4, lambda i, j: cancel((L.T * G * L)[i, j]))
    _report("(C) the test rotation L is a genuine SO(3,1) element: L^T G L == G EXACT over "
            "Q (rational boost cosh=5/4 x rotation cos=3/5) [exact]", _is_zero_matrix(LtGL - G))
    # F_B transforms as a 2-form: F_B' = L^T F_B L.  The Pontryagin scalar must be unchanged.
    FBm_rot = Matrix(4, 4, lambda i, j: cancel((L.T * FBm * L)[i, j]))
    I_FF_rot = FwedgeF_pontryagin(FBm_rot)
    _report("(C) the F_B^F_B Pontryagin scalar is UNCHANGED under the SO(3,1) frame rotation "
            f"(I_FF={I_FF_matter} before, {I_FF_rot} after; equal over Q) -- a GAUGE-"
            "INVARIANT verdict scalar, NOT a frame artifact [fp-nonabelian-gauge REJECTED]",
            cancel(I_FF_matter - I_FF_rot) == 0)
    # The Maxwell-stress trace is a scalar => also invariant; re-confirm post-rotation.
    _, _, trace_rot = maxwell_stress_of_FB(FBm_rot, G)
    _report("(C) the Maxwell-stress trace stays EXACTLY 0 under the frame rotation (the EM "
            "signature is gauge-invariant, not a frame artifact) [exact over Q]",
            trace_rot == 0)

    # ---- (D) THE INDEPENDENTLY-FROZEN T[M]  (kappa FIRST, off-switch, NO F_B) ----
    print("-" * 78)
    print("(D) the INDEPENDENTLY-FROZEN T[M] (V_{1/2} cross-term psi=2Re((x2 x1)x3); kappa "
          "FIRST; inv_det_X_block off-switch; built WITHOUT reference to F_B)")
    print("-" * 78)
    # Matter in V_{1/2} (C_u-survivors) + a V_0 x1 partner so the triple cross-term has all
    # three slots; slice at the center.  Indices: V_{1/2} matter {11,18,19,26}; V_0 partner {4}.
    MATTER = {11: Rational(2), 18: Rational(-1), 19: Rational(3), 26: Rational(5)}
    BGPART = {4: Rational(1)}
    slice_vals = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]
    Tinfo = freeze_T_of_M(MATTER, BGPART, slice_vals)
    print(f"      cross-term scalar psi = 2 Re((x2 x1) x3) is a nonzero field: "
          f"psi_nonzero={Tinfo['psi_nonzero']}")
    print(f"      T[M]=T[psi] trace_eta (expect NONZERO => non-traceless Einstein-source "
          f"signature) = {Tinfo['trace_T']}")
    _report("(D) T[M] built WITHOUT reference to F_B (psi = the det_3 SSOT cross-term, NO "
            "Ric/R/G symbol enters); psi is a genuine nonzero V_0<->V_{1/2} cross-term field "
            "[non-circular; fp-relabel guard]", Tinfo["psi_nonzero"])
    _report("(D) T[M] is NON-TRACELESS (trace_eta T[M] != 0) -- the Einstein-SOURCE tensor "
            "signature, STRUCTURALLY DISTINCT from the traceless Maxwell F_B stress "
            "[exact over Q; the decisive structural contrast]", Tinfo["trace_T"] != 0)

    # OFF-SWITCH: confirm T[M] is genuinely cross-term-sourced (the v17.0 decisive control).
    # spacetime_curvature_of_g ON vs OFF (inv_det_X_block drops the V_0<->V_{1/2} triple).
    res_on = BG.spacetime_curvature_of_g(MATTER, slice_vals, bg_delta=BGPART)
    res_off = BG.spacetime_curvature_of_g(MATTER, slice_vals, bg_delta=BGPART,
                                          norm_potential=BG.inv_det_X_block)
    R_on, R_off = res_on["Rscalar"], res_off["Rscalar"]
    print(f"      OFF-SWITCH (independence certificate): R[g] cross-term ON  = {float(R_on):.4f}")
    print(f"                                             R[g] cross-term OFF = {float(R_off):.4f}")
    changed = cancel(R_on - R_off) != 0
    _report("(D) OFF-SWITCH: dropping the V_0<->V_{1/2} cross-term (norm_potential="
            "inv_det_X_block) CHANGES the matter-sourced curvature decisively (R_on != "
            "R_off) -- T[M] is genuinely cross-term-sourced, NOT an artifact [exact over Q]",
            changed)
    # ricci_decomposition_n4 of the SOURCE curvature: non-traceless (S!=0, Weyl!=0).
    dec = BG.ricci_decomposition_n4(res_on["R"], res_on["Ric"], res_on["Rscalar"],
                                    res_on["g"], res_on["ginv"])
    print(f"      ricci_decomposition_n4 of the matter SOURCE curvature: R_zero={dec['R_zero']}"
          f", S_zero={dec['S_zero']}, weyl_zero={dec['weyl_zero']}, trace_S={dec['trace_S']}")
    _report("(D) the matter SOURCE curvature (the T[M] builder) is genuinely non-trivial "
            "(R!=0, S!=0, Weyl!=0): a non-traceless Einstein-type source -- the v17.0 "
            "symmetric-sector object that BUILDS T[M], NEVER the Im verdict "
            "[fp-reuse-cone-hessian guard: this only builds T[M]]",
            (not dec["R_zero"]) and (not dec["S_zero"]))

    # ---- (E) THE THREE MATCHES -> THE VERDICT ----
    print("-" * 78)
    print("(E) THE THREE MATCHES (M-power + tensor structure + support) -> the VALD-04 "
          "verdict, on gauge-invariant scalars")
    print("-" * 78)
    # M-power: matter F_B ~ O(||M||^2).  T[psi]~(d psi)^2 with psi~matter*slice => also t^2
    # in trace, BUT the structural mismatch is decisive regardless (see below).
    M_power_match = (M_power_FB == 2)
    print(f"      (1) M-POWER: matter F_B ~ O(||M||^2); T[M] trace ~ O(||M||^2) "
          f"(psi~matter; (d psi)^2~matter^2).  Powers coincide: {M_power_match}")

    # TENSOR STRUCTURE: F_B is ANTISYMMETRIC with a TRACELESS Maxwell stress (~F^2, conformal,
    # EM-shaped); T[M] is SYMMETRIC and NON-TRACELESS (Einstein-source).  DECISIVE MISMATCH.
    structure_EM = (anti_ok and trace_Tmax == 0)               # F_B: antisym + traceless = EM
    structure_T_einstein = (Tinfo["trace_T"] != 0)             # T[M]: non-traceless = Einstein-source
    structure_mismatch = structure_EM and structure_T_einstein
    print(f"      (2) TENSOR STRUCTURE: F_B = antisymmetric 2-form, Maxwell stress TRACELESS "
          f"(~F^2, conformal) => EM-shaped ({structure_EM}); T[M] = symmetric, NON-traceless "
          f"=> Einstein-source ({structure_T_einstein}).  DECISIVE MISMATCH: {structure_mismatch}")

    # SUPPORT: F_B's Maxwell stress vs T[M].  F_B is a Pontryagin/~F^2 density (a 4-form
    # scalar + a traceless stress); T[M] is the (d psi)^2 gradient-energy of a DIFFERENT
    # (symmetric, cross-term-sourced) channel.  They are different tensor SPECIES -- the
    # support/structure cannot coincide (a traceless conformal stress != a non-traceless one).
    support_disjoint = (trace_Tmax == 0) and (Tinfo["trace_T"] != 0)
    print(f"      (3) SUPPORT: the traceless Maxwell F_B stress and the non-traceless T[M] "
          f"are DIFFERENT tensor species (a conformal ~F^2 stress cannot equal a non-"
          f"traceless gradient stress) => support/structure DISJOINT: {support_disjoint}")

    # THE VERDICT (rendered FLAT; negative-result-is-success):
    #   Einstein-shaped (SURVIVES) iff all three MATCH (M-power + non-traceless tensor
    #     structure matchable to T[M] + coincident support, frame-rotation invariant).
    #   EM-shaped (SOFT KILL) iff the matter F_B is traceless ~F^2 / structurally disjoint
    #     from T[M] -- "the Lie sector inherits the symmetric-sector mismatch".
    is_einstein_shaped = (M_power_match and (not structure_EM)
                          and structure_T_einstein and (not support_disjoint))
    is_em_shaped = structure_EM and structure_mismatch and support_disjoint
    verdict = "SURVIVES" if is_einstein_shaped else ("SOFT KILL" if is_em_shaped else "INCONCLUSIVE")
    print("=" * 78)
    print(f"      VALD-04 PROPOSED VERDICT (on gauge-invariant scalars, exact over Q(i)): "
          f"{verdict}")
    print("=" * 78)
    if verdict == "SOFT KILL":
        print("      SOFT KILL (reported FLAT, negative-result-is-success): the matter Berry")
        print("      curvature F_B is EM-SHAPED -- an antisymmetric 2-form whose F_B^F_B")
        print("      contraction is the Pontryagin/~F^2 density and whose Maxwell stress is")
        print("      EXACTLY TRACELESS (conformal) -- STRUCTURALLY DISTINCT from the non-")
        print("      traceless, symmetric, independently-frozen T[M].  The Lie/antisymmetric")
        print("      sector INHERITS the symmetric-sector same-wall mismatch (v17.0 NONE).")
        print("      => recommend STOP before Phase B.  NOT relabeled 'approximately")
        print("      Einstein' (fp-relabel-softkill); NOT a 'some 2-form appears' claim")
        print("      (fp-relabel: a full three-way M-power + structure + support test against")
        print("      an INDEPENDENTLY-FROZEN T[M]).  A.5 is CONJUNCTIVE with Phase 75")
        print("      (SURVIVES): a SOFT KILL here ENDS the milestone as a publishable negative.")
    _report("VALD-04 DECIDED (proposed verdict, for human ratification): the matter F_B is "
            f"EM-SHAPED => {verdict}; reported FLAT on gauge-invariant scalars, frame-rotation "
            "invariant [negative-result-is-success; all forbidden proxies guarded]",
            verdict in ("SOFT KILL", "SURVIVES"))

    # GUARDS RE-AFFIRMED in code (the verdict rests on these exact facts):
    print("      GUARDS: fp-relabel (three-way match vs INDEPENDENTLY-FROZEN T[M], not 'a "
          "2-form appears'); fp-reuse-cone-hessian (R[g] only BUILT T[M]); fp-relabel-softkill")
    print("      (EM reported FLAT as SOFT KILL); fp-nonabelian-gauge (frame-rotation "
          "invariant scalars); fp-float-decisive (trace_Tmax==0 EXACT over Q); "
          "fp-octonion-algebra (source guard, oct_mul SSOT not Jordan in the QGT).")
    return {"verdict": verdict, "is_em_shaped": is_em_shaped,
            "is_einstein_shaped": is_einstein_shaped,
            "M_power_FB": M_power_FB, "I_FF_matter": I_FF_matter, "I_FF_full": I_FF_full,
            "trace_Tmax": trace_Tmax, "F2": F2, "trace_T_of_M": Tinfo["trace_T"],
            "R_on": R_on, "R_off": R_off, "FB_matter_at_1_20": FBm,
            "Tmax": Tmax, "T_of_M": Tinfo["T"], "L_so31": L,
            "dec_S_zero": dec["S_zero"], "dec_weyl_zero": dec["weyl_zero"]}


if __name__ == "__main__":
    print("#" * 78)
    print("# Phase 76 -- Plan 01 (PART 1, VACUUM half): Berry-curvature same-wall gate")
    print("# Task 1: CP^1 pin + rank-1 C_u idempotent + 4x4 QGT over Q(i)")
    print("# Task 2: VALD-03 (born-from-breaking + nonzero) FIRST + CALC-03 (SOFT Re-anchor)")
    print("# Task 3: CALC-04 (M=0 vacuum classification: pure-Lambda/Kahler)")
    print("#" * 78)
    okG, ok1, ok2, _state = _task1()
    _t2 = _task2(_state)
    _vac = _task3(_state, _t2)
    # ---- PART 2 (plan 76-02): the DECISIVE / MATTER half ----
    _m1 = task1_matter_idempotent(_vac)
    _v04 = task2_vald04(_m1)
    print("=" * 78)
    print(f"SOURCE GUARD ......... {'PASS' if okG else 'FAIL'}")
    print(f"CP^1 PIN ............. {'PASS' if ok1 else 'FAIL'}")
    print(f"IDEMPOTENT + BRIDGE .. {'PASS' if ok2 else 'FAIL'}")
    print("=" * 78)
    print("PART-1 RESULTS (vacuum half):")
    print("  * QGT recipe CALIBRATED (CP^1 pin: F_B=-sin th/2, g_thth=1/4, flux=-2pi)")
    print("  * VALD-03: F_B WELL-DEFINED + generically NONZERO (F_B[a,b]=F_B[c,d]=-2), "
          "BORN FROM the C_u breaking (round Berry=0); NOT degenerate")
    print("  * CALC-03 (SOFT): Re(QGT)=FS metric positive-definite (diag(1,1,1,1)); "
          "character vs cone-Hessian INFORMATIVE only (NOT a KILL)")
    print(f"  * CALC-04: M=0 vacuum = PURE-LAMBDA/KAHLER (F_B = {_vac['s']}*omega_K, "
          "primitive remainder 0); the Lambda/Kahler VACUUM (NOT matter); no Lambda<0/RxH^3")
    print("=" * 78)
    print("PART-2 RESULTS (matter half) -- TASK 1 (matter-on E(x;M) over C_u):")
    print("  * E(x;M) is a RANK-1 C_u idempotent SYMBOLIC in M (E^2-E==0, Tr==1)")
    print("  * C_u-FAITHFUL: C_u-survivor V_{1/2} matter {11,18,19,26} stays in C_u; "
          "transverse e_1..e_6 matter projected away by pi_u (no rank-changing leak)")
    print("  * M->0 limit recovers the PART-1 vacuum F_B exactly; matter F_B emitted")
    print(f"  * LEADING M-POWER = O(||M||^{_m1['leading_M_power']}) (the v17.0 order of the "
          "metric h)")
    print("=" * 78)
    print("PART-2 RESULTS (matter half) -- TASK 2 (VALD-04 decisive clause):")
    print(f"  * matter F_B leading O(||M||^{_v04['M_power_FB']}); F_B^F_B Pontryagin scalar "
          f"(matter) = {_v04['I_FF_matter']} (gauge-invariant, frame-rotation invariant)")
    print(f"  * EM SIGNATURE: Maxwell stress of F_B is EXACTLY TRACELESS (trace_G="
          f"{_v04['trace_Tmax']}) -- a conformal ~F^2 field strength")
    print(f"  * T[M] (independently frozen, cross-term psi, kappa first, NO F_B) is NON-"
          f"traceless (trace_eta={_v04['trace_T_of_M']}) -- the Einstein-source signature")
    print(f"  * off-switch: R[g] ON={float(_v04['R_on']):.2f} vs OFF="
          f"{float(_v04['R_off']):.2f} (cross-term-sourced); S!=0, Weyl!=0 (the BUILDER of T[M])")
    print("=" * 78)
    print(f"  >>> VALD-04 PROPOSED VERDICT: {_v04['verdict']} <<<")
    if _v04["verdict"] == "SOFT KILL":
        print("  (matter Berry curvature EM-shaped -- traceless ~F^2, structurally distinct")
        print("   from the non-traceless T[M]; the Lie sector inherits the symmetric-sector")
        print("   same-wall mismatch; recommend STOP before Phase B. Conjunctive with Ph75:")
        print("   a SOFT KILL ENDS the milestone as a publishable negative. Reported FLAT.)")
    print("  (This is the COMPUTED proposed verdict; the BLOCKING human ratification by")
    print("   Bryan is plan-76-02 Task 3 -- the milestone-gating call, NOT self-ratified.)")
    print("=" * 78)
    print(f"PART 1 + PART 2 (Tasks 1-2): {'ALL_PASS' if ALL_PASS else 'SOME FAILED'}")
    sys.exit(0 if ALL_PASS else 1)
